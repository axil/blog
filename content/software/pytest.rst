Pytest vs standard django tests
###############################

:tags: pytest, django, python

By default both testing frameworks rely on transactions for test cases isolation.
But the details are different.

To see how django test framework works consider the following testcase:

.. code:: python

        from django.test import TestCase
        from django.contrib.auth.models import User

        def get_users():
            return repr(list(u.username for u in User.objects.all()))

        class UserTest(TestCase):
            def setUp(self):
                User.objects.create(username='a')
                print('setup: ' + get_users())

            def test1(self):
                User.objects.create(username='b')
                print('test1: ' + get_users())

            def test2(self):
                User.objects.create(username='c')
                print('test2: ' + get_users())

It prints ("pytest test.py")::

    setup: ['a']
    test1: ['a', 'b']
    setup: ['a']
    test2: ['a', 'c']

Which corresponds to the following transaction layout::

    start transaction -> setup -> test1 -> rollback ->
    start transaction -> setup -> test2 -> rollback


By default in pytest the same algorithm is used:

.. code:: python

    import pytest
    from django.contrib.auth.models import User

    def get_users():
        return repr(list(u.username for u in User.objects.all()))

    @pytest.fixture
    def first_user(db):
        User.objects.create(username='a')
        print('setup: ' + get_users())

    @pytest.mark.django_db
    def test1(first_user):
        User.objects.create(username='b')
        print('test1: ' + get_users())

    @pytest.mark.django_db
    def test2(first_user):
        User.objects.create(username='c')
        print('test2: ' + get_users())

    setup: ['a']
    test1: ['a', 'b']
    setup: ['a']
    test2: ['a', 'c']

Now consider a situation where the setup function takes a long time to run. In pytest it is possible
to do such a trick then:

.. code:: python

    import pytest
    from django.contrib.auth.models import User

    def get_users():
        return repr(list(u.username for u in User.objects.all()))

    @pytest.fixture(scope='module')
    def django_db_setup(django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
            User.objects.create(username='a')
            print('setup: ' + get_users())

    @pytest.mark.django_db
    def test1(first_user):
        User.objects.create(username='b')
        print('test1: ' + get_users())

    @pytest.mark.django_db
    def test2(first_user):
        User.objects.create(username='c')
        print('test2: ' + get_users())

which prints::

    setup: ['a']
    test1: ['a', 'b']
    test2: ['a', 'c']

So the transactions layout is like that::

    setup ->
    start transaction -> test1 -> rollback ->
    start transaction -> test2 -> rollback

It can be used with "--reuse-db" flag to save db creation time, but at a cost of losing isolation between executions of the setup function in the subsequent test runs. To avoid 'User a already exists' situation we can change "User.objects.create" to "User.objects.get_or_create", but it leaves the db in a dirty state.

To keep test database clean, manual deletion of all records created in setup function is necessary, but doing so is error-prone (you need to keep in mind that you should delete each record you create in setup). In pytest cleanup is supposed to be implemented in the same setup function using the generators technique:

.. code:: python

    import pytest
    from django.contrib.auth.models import User

    def get_users():
        return repr(list(u.username for u in User.objects.all()))

    @pytest.fixture(scope='module')
    def django_db_setup(django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
            User.objects.create(username='a')
            print('setup: ' + get_users())
        yield
        with django_db_blocker.unblock():
            User.objects.filter(username='a').delete()
            print('cleanup: ' + get_users())

    @pytest.mark.django_db
    def test1():
        User.objects.create(username='b')
        print('test1: ' + get_users())

    @pytest.mark.django_db
    def test2():
        User.objects.create(username='c')
        print('test2: ' + get_users())


    setup: ['a']
    test1: ['a', 'b']
    test2: ['a', 'c']
    cleanup: []

The technique shows how in pytest one can exclude the setup function from the transaction rollback mechanism so that the setup is only run once for the test suite which means lower testing time.  

There are other ways to get such an effect, but this one is most close to the "letter of the documentation".

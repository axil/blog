Pytest vs standard django tests
###############################

:tags: pytest, django, python

Standard django test system works like that. Consider the following testcase:

    from django.test import TestCase
    from django.contrib.auth.models import User

    class UserTest(TestCase):
        def setUp(self):
            User.objects.create(username='a')
            print('setup: ' + ', '.join(u.username for u in User.objects.all()))

        def test1(self):
            User.objects.create(username='b')
            print('test1: ' + ', '.join(u.username for u in User.objects.all()))

        def test2(self):
            User.objects.create(username='c')
            print('test2: ' + ', '.join(u.username for u in User.objects.all()))



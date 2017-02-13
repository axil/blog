git fast-forward
################

:tags: git, linux, windows, fast-forward
:date: 2016-11-07 20:03

I've written a python script named::

        git ff

which does what you would expect it to: it fast-forwards the current branch against its tracking branch
and shows all kind of relevant info if there's an error.

**Prerequisites:**

| python of any version (preferably 2.7.x or 3.5.x)

**Installation:**

1. Download the git-ff_ script.

2. Copy the script:

   | (linux) to any directory in your path on linux (eg ~/bin provided it is in the path)
   | (windows) to "C:\\Program Files\\Git\\libexec\\git-core" or "C:\\Program Files\\Git\\mingw64\\libexec\\git-core" (use your git installation path if it is different)

PS The script itself

.. code:: python

    #!/usr/bin/python
    # vim: filetype=python :

    from __future__ import print_function
    import re, os, sys

    def mystrip(a):
        return re.sub('refs/heads/', '', a)

    def call(a):
        return os.popen(a).read().strip()

    def get_id(branch):
        return call('git rev-parse %s' % branch)

    if len(sys.argv) > 2:
        print('usage: git ff [<remote>]')
        exit(1)
    branch = mystrip(call('git symbolic-ref HEAD'))    # git name-rev --name-only HEAD would also do
    if len(sys.argv) == 2:
        tracked = '/'.join((sys.argv[1], branch))
    else:
        remote = call('git config branch.%s.remote' % branch)
        if remote == '':
            print('branch not tracking and no remote given, aborting')
            exit(1)
        merge = call('git config branch.%s.merge' % branch)
        if remote=='.':
            tracked = merge
        else:
            tracked = '/'.join(( remote, mystrip(merge) ))
    base_id = call('git merge-base %s %s' % (branch, tracked))

    print(get_id(branch)[:7], branch, '(current)')
    print(get_id(tracked)[:7], tracked, '(tracked)')
    print(base_id[:7], '(base)')

    if base_id != get_id(branch):
        print('Cannot fast-forward')
        sys.exit(1)
    n = call('git rev-list %s..%s |wc -l' % (branch, tracked))
    if n=='0':
        print('Your branch is already up-to-date')
        sys.exit(0)
    print('Fast-forwarding %s revision(s)' % n)
    print(call('git merge %s' % tracked))


.. _git-ff : https://axil.github.io/git-ff

git others
##########

:tags: git, linux, windows, untracked
:date: 2017-02-13 14:37

I've written a git alias named::

        git others

which lists files unknown to git. What it actually does is::

        git ls-files --exclude-standard -o

It can be used to move unnecessary files to some trash folder::

        git others | xargs -I{} mv {} trash/

On windows it's slightly different::

        git others | xargs -I"{}" mv {} trash/

**Installation:**

        git config --global alias.others "ls-files --exclude-standard -o"

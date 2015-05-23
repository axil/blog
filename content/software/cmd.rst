Patching cmd.exe
##############################

:tags: cmd.exe, patching

When breaking execution of bat-file with ctrl-c it stops with a pretty useless 
"Terminate Batch job (Y/N)?" prompt.

It looks like the most universal way to suppress it is to patch cmd.exe.

Here's a python script that implements the process described here_:

.. _here: http://itsme.home.xs4all.nl/projects/misc/patching-cmdexe.html

.. code:: python

    f = open('cmd.exe', 'r+b')
    a = f.read()
    z = ''.join(chr(int(b, 16)) for b in '68 28 23 00 00 68 7B 23 00 00'.split())
    p = a.find(z)
    if p == -1 or a.find(z, p+len(z)) != -1:
        print 'patch doesn\'t fit or file already patched'
    else:
        if raw_input('chunk found at offset %#x, patch? (y/n) ' % p) == 'y':
            f.seek(p)
            f.write('\x90' * 0x1A)
            print 'patch successful'
        else:
            print 'patching cancelled'
    f.close()

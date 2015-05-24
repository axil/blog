Patching cmd.exe
##############################

:tags: cmd.exe, patch, assembler

Breaking the execution of a bat-file with ctrl-c makes it stop with a pretty useless\ [*]_ 
"Terminate Batch job (Y/N)?" prompt.

It looks like the most universal way to suppress it is to patch cmd.exe as described in `this blog`_.

.. _this blog: http://itsme.home.xs4all.nl/projects/misc/patching-cmdexe.html

In Windows 7 there're two cmd.exe: 32bit (for which the recipe above works) and 64bit (for which it doesn't). 
Here's the corresponding code for the 64bit version (search for the hex string "BA 7B 23 00 00" in cmd.exe):

.. code::

        .text:000000004AD1D07A loc_4AD1D07A:                           ; CODE XREF: sub_4AD032D8+D^j
        .text:000000004AD1D07A                 cmp     cs:qword_4AD2E1E8, 0
        .text:000000004AD1D082                 jz      short loc_4AD1D0C1

        ...... fill this with NOPS ( byte value 0x90 ):
        .text:000000004AD1D084                 mov     edx, 237Bh
        .text:000000004AD1D089                 xor     ecx, ecx
        .text:000000004AD1D08B                 lea     r8d, [rdx-53h]
        .text:000000004AD1D08F                 call    sub_4AD24DE0
        .text:000000004AD1D094                 cmp     eax, 1
        .text:000000004AD1D097                 jz      short loc_4AD1D0A4
        .text:000000004AD1D099                 call    sub_4AD0231C
        .text:000000004AD1D09E                 nop
        .text:000000004AD1D09F                 jmp     loc_4AD032EB
        .text:000000004AD1D0A4 ; ---------------------------------------------------------------------------
        ......

        .text:000000004AD1D0A4
        .text:000000004AD1D0A4 loc_4AD1D0A4:                           ; CODE XREF: sub_4AD032D8+19DBF^j
        .text:000000004AD1D0A4                 mov     rbx, cs:qword_4AD2E1E8
        .text:000000004AD1D0AB                 jmp     short loc_4AD1D0BC


And here's a `python script`_ that automates the process:

.. _python script: https://github.com/axil/patch-cmd

.. code:: python

        import shutil

        def patch(filename, chunk, replacement):
        f = open(filename, 'r+b')
        a = f.read()
        z = ''.join(chr(int(b, 16)) for b in chunk.split())
        p = a.find(z)
        if p == -1 or a.find(z, p+len(z)) != -1:
            print 'patch doesn\'t fit or file already patched'
        else:
            if raw_input('chunk found (offset %#x), patch? (Y/n) ' % p) != 'n':
                shutil.copy(filename, filename + '.bak')
                f.seek(p)
                f.write(replacement)
                print 'patch successful'
            else:
                print 'patching cancelled'
        f.close()

        patch('c:/windows/syswow64/cmd.exe', '68 28 23 00 00 68 7B 23 00 00', '\x90' * 0x1A)
        patch('c:/windows/system32/cmd.exe', 'BA 7B 23 00 00 33 C9', '\x90' * 0x20)

Be sure to assign the appropriate rights to the script so that it could overwrite the files. 

Backups are saved with '.bak' extension.

.. [*] Answering 'N' will make the .bat execution continue from the line, following the one that was interrupted by ctrl-c. I've never used it and can't think of a situation where I would.


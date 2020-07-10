Enabling "Ctrl-V" in Windows console using Autohotkey
#####################################################

:tags: cmd.exe, paste, tips
:date: 2015-07-31 12:00

Follow those three steps and `Ctrl-V` will work in cmd.exe *seamlessly*, even without restarting an already open console.

#. Install Autohotkey_

#. Create a file named "anything.ahk" with the following contents::

       #IfWinActive ahk_class ConsoleWindowClass
       
       #EscapeChar \

       ^V::
       StringReplace clipboard2, clipboard, \r\n, \n, All
       SendInput {Raw}%clipboard2%
       return

       #IfWinActive

#. run it

You can disable it:

* using the tray icon, *or (if you don't like the tray icon)*,
    
* add '#NoTrayIcon' to the top of the script and then disable by killing 'AutoHotkey.exe' process in the Task manager

Apply at startup using Start->Programs->Startup

PS Microsoft *suddenly* added_ the functionality in Windows 10.

.. _added : http://www.howtogeek.com/197749/how-to-power-up-the-windows-10-command-prompt-with-ctrlc-and-ctrlv/

----------

Sources: 

#. http://stackoverflow.com/questions/131955/keyboard-shortcut-to-paste-clipboard-content-into-command-prompt-window-win-xp

#. http://www.howtogeek.com/howto/25590/how-to-enable-ctrlv-for-pasting-in-the-windows-command-prompt/


.. _Autohotkey : http://www.autohotkey.com/



Enabling "Ctrl-V" in Windows console using Autohotkey
#####################################################

#. Install Autohotkey

#. Create a file named "anything.ahk" with the following contents::

       #IfWinActive ahk_class ConsoleWindowClass
       
       #EscapeChar \

       ^V::
       StringReplace clipboard2, clipboard, \r\n, \n, All
       SendInput {Raw}%clipboard2%
       return

       #IfWinActive

#. run it

PS Disable using the tray icon, or add '#NoTrayIcon' to the top of the script and disable by killing 
'AutoHotkey' process in the Task manager

PPS apply at startup using Start->Programs->Startup

----------

Sources: 

#. http://stackoverflow.com/questions/131955/keyboard-shortcut-to-paste-clipboard-content-into-command-prompt-window-win-xp

#. http://www.howtogeek.com/howto/25590/how-to-enable-ctrlv-for-pasting-in-the-windows-command-prompt/


.. _Autohotkey : http://www.autohotkey.com/



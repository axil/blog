How to install a python wheel with one doubleclick
##################################################

:tags: python, whl, install
:date: 2015-12-03 17:50


To be able to install wheel files with a simple doubleclick on them you can do one the following:

#. Run this command in cmd.exe under administrator privileges::

       assoc .whl=pythonwheel& ftype pythonwheel=cmd /c pip.exe install "%1" ^& pause

#. Alternatively, a similar line can be copied into a wheel.bat_ file and executed through 'Run as administrator'::

       assoc .whl=pythonwheel& ftype pythonwheel=cmd /c pip.exe install "%%1" ^& pause

#. or a slightly more verbose wheel-verbose.bat_::

        @assoc .whl=pythonwheel || echo Run me with administrator rights! && pause && exit 1
        @ftype pythonwheel=cmd /c pip.exe install "%%1" ^& pause || echo Installation error && pause && exit 1
        @echo Installation successfull & pause

PS pip.exe is assumed to be in the PATH.

PPS If you have both python2 and python3 installed and want to install into python3 by default, replace pip with pip3.

.. _wheel.bat : http://axil.github.io/wheel.bat
.. _wheel-verbose.bat : http://axil.github.io/wheel-verbose.bat

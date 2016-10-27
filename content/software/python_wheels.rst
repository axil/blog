How to install a python wheel with one doubleclick
##################################################

:tags: python, whl, install
:date: 2015-12-03 17:50


To be able to install wheel files with a simple doubleclick on them you can do one the following:

#. Run this command in cmd.exe under administrator privileges::

       assoc .whl=pythonwheel& ftype pythonwheel=cmd /c pip.exe install "%1" ^& pause

#. Alternatively, a similar line can be copied into a wheel.bat file and executed through 'Run as administrator'::

       assoc .whl=pythonwheel& ftype pythonwheel=cmd /c pip.exe install "%%1" ^& pause

PS pip.exe is assumed to be in the PATH.

PPS If you have both python2 and python3 installed and want to install into python3 by default, replace pip with pip3.


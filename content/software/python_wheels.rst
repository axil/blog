How to install a python wheel with one doubleclick
##################################################

:tags: python, whl, install
:date: 2015-12-03 17:50


To be able to install wheel files with a simple doubleclick on them you can do one the following:

#. Run those commands in command line under administrator privileges::

       assoc .whl=pythonwheel
       ftype pythonwheel=cmd /c pip.exe install "%1" & pause

#. Alternatively, they can be copied into a wheel.bat file and executed with 'Run as administrator' checkbox in the properties.

PS pip.exe is assumed to be in the PATH.


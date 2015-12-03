How to install python wheel with one doubleclick
################################################

:tags: python, wheel, whl, install
:date: 2015-12-03 17:50


To be able to install wheel files with a simple doubleclick on them you can do one the following:

1) Run two commands in command line under administrator privileges:
assoc .whl=pythonwheel
ftype pythonwheel=cmd /c "pip.exe install %1 & pause"

2) Alternatively, they can be copied into a wheel.bat file and executed with 'Run as administrator' checkbox in the properties.

PS pip.exe is assumed to be in the PATH.


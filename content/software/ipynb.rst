How to open .ipynb file with one doubleclick
############################################

:tags: python, ipynb, jupyter, notebook
:date: 2017-01-11 11:36


To be able to open .ipynb jupyter notebook files with a simple doubleclick on them you can do one the following:

#. Run this command in cmd.exe under administrator privileges::

       assoc .whl=jupyter& ftype jupyter=cmd.exe /c jupyter-notebook "%1"

#. Alternatively, a slightly different line can be copied into a assoc_ipynb.bat_ file and executed through 'Run as administrator'::

       assoc .whl=jupyter& ftype jupyter=cmd /c jupyter-notebook "%%1"

PS jupyter-notebook.exe is assumed to be in the PATH.

.. _assoc_ipynb.bat : http://axil.github.io/assoc_ipynb.bat

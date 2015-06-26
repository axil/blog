Fix Alt-Tab in Labview
======================

In all Windows applications `Alt`\ +\ `Tab` switches to the most recently used window.

In Labview it switches to the most recently used *LabView* window.

This means that to get back to the browser window if you have just alt-tabbed to LabView
it will take about 2n-1 strokes of `Alt`\ +\ `Tab` where n is the number of opened vi's.

This python script_ mapped to `Alt`\ +\ `\`` with Autohotkey solves the issue in the following manner:

1) For normal (non-labview) windows it behaves just as alt-tab pressed once
2) For labview windows it switches to most recently used non-labview window.

For the browser vs labview problem described above it means that after switching to LabView 
from the browser you can work with several LabView files, switching between them with Alt-Tab, 
and then you press `Alt`\ +\ `\`` and you're in the browser again.

.. _script : https://github.com/axil/labview-switcher

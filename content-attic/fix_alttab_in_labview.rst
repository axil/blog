Fix Alt-Tab in Labview
======================

In all Windows application Alt-Tab switches to most recently used window.

In Labview it switches to most recently used window in Labview.

This means that to get back to the browser window if you have just alt-tabbed to Labview
it will take 2n-1 strokes of Alt-Tab where n is the number of opened vi's.

This python script mapped to alt-` with autohotkey solves the issue in the following manner:

1) For normal (non-labview) windows it behaves as alt-tab pressed once
2) For labview windows it switches to most recently used non-labview window.

For the browser vs labview problem described above it means that you can work with several labview files, 
switching between them with Alt-Tab, and then you press `Alt`+``` and you're in the browser again.


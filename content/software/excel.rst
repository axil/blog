Essential Microsoft Excel Keyboard Shortcuts
############################################

:tags: excel, shortcuts, tips

The most convenient and the least used shortcut of Excel is:

.. role:: kbd

* when editing a formula, press `f4` to toggle between absolute and relative reference

To use it, click a cell you want to reference, say, D5. Then press `f4` once (it will change to $D$5) 
to make the reference absolute so that it wont 'adapt' when you drag your formula to other 
rows or columns the way relative references do.

The problem with Excel keyboard shortcuts is that while they can make sheets editing
more effective they are so numerous and their documentation is so poorly structured
that people hardly ever use any of them.

I've come through all of them and here's a cheetsheet of shortcuts that I found useful:

Entering data
-------------

* moving around:

  - `tab` to move active cell to the right, 
  - `shift`\ +\ `tab` to the left, 
  - `enter` to go to the "start" of next line (to the column you originally started with, that is where you pressed `tab` or `enter` for the first time [*]_), 
  - `shift`\ +\ `enter` to move up

.. image:: img/Image-1a-blog.png
  :alt: enter and tab
  :class: centered-image

This "mode" is an alternative to using arrow keys. If you press an arrow key you switch out of the "mode"
and the "first column" is reset to the current position.

Selecting cells
---------------

* select row/column:  `shift`\ +\ `space` / `ctrl`\ +\ `space`

* expand/reduce selection: `shift`\ +\ arrows

* shift multi-cell selection box: ctrl-drag


Data manipulation
-----------------

* insert cell(s): `ctrl`\ +\ `+`
   
  - inserts row if a row is selected
  - inserts column if a column is selected
  - shows dialog if a cell is selected

* move several rows/columns: 

  - drag to move into an empty space
  - shift-drag to move and squeeze between existing rows/columns
  - `ctrl`\ +\ `x` to cut, then `ctrl`\ +\ `num+` to insert (shifting adjacent rows/columns accordingly)

* copy data into the current cell

  - copy formula above:  `ctrl`\ +\ `'` (and enter edit mode as if `f2` is pressed)
  - copy value above:  `ctrl`\ +\ `"` (without entering edit mode)
  - fill down:  `ctrl`\ +\ `d` (copy formula and format from the upper cell, no edit mode)
  - fill right:  `ctrl`\ +\ `r`  (copy formula and format from the left cell, no edit mode)
  - autocomplete text from adjacent cells in the current column: `alt`\ +\ `arrow down` [*]_

* copy data inside cell range

  - fill down:  `ctrl`\ +\ `d` (replicate the upper row downwards)
  - fill right:  `ctrl`\ +\ `r`  (replicate the leftmost column to the right)
  - thus fill rectangle will be `ctrl`\ +\ `d` followed by `ctrl`\ +\ `r`


Formatting
----------

* cell modes:

  - format cells:  `ctrl`\ +\ `1`
  - number mode:  `ctrl`\ + `shift` + `!`
  - modes:  general/number/time/date/currency/percentage/scientific

.. raw:: html

  <pre style="background:none;border:0;margin:-20px 0 -10px 153px;padding: 0">~      !     @    #      $         %          ^</pre>

* visual formatting: 

  - clear formatting:  `alt`\ +\ `'` then `enter`
  - add/remove borders:  `ctrl`\ +\ `shift` + `&`/`_`


Miscellaneous
-------------

* etc
  
  - repeat last action:  `f4` [*]_ or `ctrl`\ +\ `y` or `alt`\ +\ `enter`


* formulas: 
  
  - toggle formulas:  `ctrl`\ +\ `\``
  - autosum:  `alt`\ +\ `=`
  - toggle absolute and relative references:  `f4` [*]_
    
.. [*] the position is reset to the current cell if arrows are used for naviation
.. [*] with cell(s) selected
.. [*] other meaning for filtering and data validation, see this `blog post`_
.. _`blog post`: http://www.accountingweb.com/technology/excel/automating-data-validation-lists-in-excel
.. [*] when editing a cell with text cursor blinking inside the reference name


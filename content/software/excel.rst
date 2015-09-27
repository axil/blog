Microsoft Excel Keyboard Shortcuts
##################################

:tags: excel, shortcuts, tips

The most convenient and the least used shortcut of Excel is:

.. role:: kbd

* when editing a formula, press `f4` to toggle between absolute and relative reference

To use it, click a cell you want to reference, say, D4. Then press `f4` once (it will change to $D$4) 
to make the reference absolute so that it wont 'adapt' when you drag your formula to other 
rows or columns the way relative references do.

Now a couple of other shortcuts that might be useful every now and then:

* entering data: 

  - `tab` to move active cell to the right, 
  - `shift`\ +\ `tab` to the left, 
  - `enter` to go to the "start" of next line (to the column you started with in the the previous line [*]_), 
  - `shift`\ +\ `enter` to move up 

.. image:: img/Image-1a-blog.png
  :alt: enter and tab
  :class: centered-image

* select row/column:  `shift`\ +\ `space` / `ctrl`\ +\ `space`

* expand/reduce selection: `shift`\ +\ arrows

* insert cell(s): `ctrl`\ +\ `+`
   
  - inserts row if a row is selected
  - inserts column if a column is selected
  - shows dialog if a cell is selected

* move several rows/columns: 

  - drag to move into an empty space
  - shift-drag to move and squeeze between existing rows/columns
  - `ctrl`\ +\ `x` to cut, then `ctrl`\ +\ `num+` to insert (shifting adjacent rows/columns accordingly)

* shift multi-row selection box: ctrl-drag

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

* formatting: 

  - clear formatting:  `alt`\ +\ `'` then `enter`
  - format cells:  `ctrl`\ +\ `1`
  - number mode:  `ctrl`\ + `shift` + `!`
  - modes:  general/number/time/date/currency/percentage/scientific

.. raw:: html

  <pre style="background:none;border:0;margin:-20px 0 -10px 153px;padding: 0">~      !     @    #      $         %          ^</pre>

* borders: 

  - add/remove:  `ctrl`\ +\ `shift` + `&`/`_`

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


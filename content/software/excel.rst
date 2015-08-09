Microsoft Excel Keyboard Shortcuts
##################################

:tags: excel, shortcuts, tips

.. role:: kbd


* enter data: `Tab` to move active cell to the right, `Enter` to go to the start of next line (to the column that you started with in the the previous line)

.. image:: img/Image-1a-blog.png
  :alt: enter and tab
  :class: centered-image

* select row/column:  `shift`\ +\ `space` / `ctrl`\ +\ `space`

* expand/reduce selection: `shift`\ +\ arrows

* insert row/column:  `ctrl`\ +\ `+`

* move several rows/columns: 

  - drag to move into an empty space
  - shift-drag to move and squeeze between existing rows/columns
  - `ctrl`\ +\ `x` to cut, then `ctrl`\ +\ `num+` to insert (shifting adjacent rows/columns accordingly)

* shift multi-row selection box: ctrl-drag

* copy data into the current cell

  - copy formula above:  `ctrl`\ +\ `'` (and enter editing mode as if `f2` is pressed)
  - copy value above:  `ctrl`\ +\ `"` (no edit mode)
  - fill down:  `ctrl`\ +\ `d` (copy formula and format from the upper cell, no edit mode)
  - fill right:  `ctrl`\ +\ `r`  (copy formula and format from the left cell, no edit mode)

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
  - autocomplete from adjacent cells in the current column: `alt`\ +\ `arrow down` [*]_

* formulas: 
  
  - toggle formulas:  `ctrl`\ +\ `\``
  - autosum:  `alt`\ +\ `=`
  - toggle absolute and relative references:  `f4` [*]_
    
.. [*] with cell(s) selected
.. [*] other meaning for filtering and data validation, see this `blog post`_
.. _`blog post`: http://www.accountingweb.com/technology/excel/automating-data-validation-lists-in-excel
.. [*] when editing a cell with text cursor blinking inside the reference name


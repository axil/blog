Microsoft Excel Keyboard Shortcuts
##################################

:tags: excel, shortcuts, tips

.. role:: kbd


* select row/column:  `shift`\ +\ `space` / `ctrl`\ +\ `space`

* insert row/column:  `ctrl`\ +\ `+`

* move several rows/columns: 

  - shift-drag
  - `ctrl`\ +\ `x` to cut, then `ctrl`\ +\ `num+` to insert (shifting adjacent rows/columns accordingly)

* shift multi-row selection box: ctrl-drag

* formatting: 

  - clear formatting:  `alt`\ +\ `'` then `enter`
  - format cells:  `ctrl`\ +\ `1`
  - number mode:  `ctrl`\ + `shift` + `!`
  - modes:  general/number/time/date/currency/percentage/scientific

.. raw:: html

  <pre style="background:none;border:0;margin:-20px 0 -10px 153px;padding: 0">~      !     @    #      $         %          ^</pre>

* borders: 

  - add/remove:  `ctrl`\ +\ `shift` + `&`/`_`

* copy data into the current cell

  - copy formula above:  `ctrl`\ +\ `'` (and enter editing mode as if `f2` is pressed)
  - copy value above:  `ctrl`\ +\ `"` (no edit mode)
  - fill down:  `ctrl`\ +\ `d` (copy formula and format from the upper cell, no edit mode)
  - fill right:  `ctrl`\ +\ `r`  (copy formula and format from the left cell, no edit mode)

* copy data inside cell range

  - fill down:  `ctrl`\ +\ `d` (replicate the upper row downwards)
  - fill right:  `ctrl`\ +\ `r`  (replicate the leftmost column to the right)
  - thus fill rectangle will be `ctrl`\ +\ `d` followed by `ctrl`\ +\ `r`

* etc
  
  - repeat last action:  `f4` [*]_ or `ctrl`\ +\ `y` or `alt`\ +\ `enter`

* formulas: 
  
  - toggle formulas:  `ctrl`\ +\ `\``
  - autosum:  `alt`\ +\ `=`
  - toggle absolute and relative references:  `f4` [*]_
    
.. [*] with cell(s) selected
.. [*] when editing a cell with text cursor blinking inside the reference name


Jump to next error in vim
#########################

:tags: vim, quickfix, cnext, .vimrc
:date: 2016-12-07 22:00

vim can check syntax as you type using quickfix feature.
To jump to next/previous error you need to write :cnext or :cprev in 
the command line.

unimpaired plugin has shortcuts [q and ]q for that.

The problem with this is that if there's only one error, :cn and :cp don't work,
you need to use :cc. Which is an amazingly bad design decision in my opinion.

The following shortcuts solve this issue::

        nnoremap } :<C-R>=len(getqflist())==1?"cc":"cn"<CR><CR>
        nnoremap { :<C-R>=len(getqflist())==1?"cc":"cp"<CR><CR>

They map the '}' and '{' keys to jump to next/previous error even if there's only one
error in a file.

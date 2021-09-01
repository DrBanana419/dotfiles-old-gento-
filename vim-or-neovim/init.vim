call plug#begin()
Plug 'SirVer/ultisnips'
Plug 'lervag/vimtex'
Plug 'morhetz/gruvbox'
call plug#end()
set cursorline
highlight CursorLine cterm=NONE ctermbg=242
autocmd vimenter * ++nested colorscheme gruvbox
set number

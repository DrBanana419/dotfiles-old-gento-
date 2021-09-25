call plug#begin('~/.vim/plugged')
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'SirVer/ultisnips'
Plug 'lervag/vimtex'
Plug 'morhetz/gruvbox'
Plug 'ycm-core/YouCompleteMe'
call plug#end()
set cursorline
highlight CursorLine cterm=NONE ctermbg=242
autocmd vimenter * ++nested colorscheme gruvbox
set number
"Use 24-bit (true-color) mode in Vim/Neovim when outside tmux.
"If you're using tmux version 2.2 or later, you can remove the outermost $TMUX check and use tmux's 24-bit color support
"(see < http://sunaku.github.io/tmux-24bit-color.html#usage > for more information.)
if (empty($TMUX))
  if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >
  if (has("termguicolors"))
    set termguicolors
  endif
endif

set background=dark    " Setting dark mode

" <TAB>: completion.
"inoremap <expr><F1>  pumvisible() ? "\<C-n>" : "\<F1>"


" Enable folding
set foldmethod=indent
set foldlevel=99

" Trigger configuration. You need to change this to something other than <tab> if you use one of the following:
" - https://github.com/Valloric/YouCompleteMe
" - https://github.com/nvim-lua/completion-nvim
let g:UltiSnipsExpandTrigger="<Insert>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"

" If you want :UltiSnipsEdit to split your window.
let g:UltiSnipsEditSplit="vertical"

let g:airline_powerline_fonts = 1

inoremap ( ()<C-R>=UltiSnips#Anon('($1)$0', '()', 'double parentheses', 'i')<CR>

let g:airline_theme='base16_atelier_lakeside'

nnoremap <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>


let g:ycm_python_binary_path = '/usr/bin/python3'

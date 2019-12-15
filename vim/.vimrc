set ts=4
set shiftwidth=4
set softtabstop=4
set expandtab
set foldlevel=20

map <F2> :retab <CR> :wq! <CR>

colorscheme smitty
set bg=dark

filetype on            " enables filetype detection
filetype plugin on     " enables filetype specific plugins

:nnoremap <F5> "=strftime("%c")<CR>P
:inoremap <F5> <C-R>=strftime("%c")<CR>

set wildmenu

set spelllang=en_us

highlight clear SpellBad
highlight SpellBad term=standout ctermfg=1 term=underline cterm=underline
highlight clear SpellCap
highlight SpellCap term=underline cterm=underline
highlight clear SpellRare
highlight SpellRare term=underline cterm=underline
highlight clear SpellLocal
highlight SpellLocal term=underline cterm=underline

"colorscheme molokai
"let g:molokai_original = 1
"let g:rehash256 = 1
"if has('gui_running')
"    set background=light
"else
"    set background=dark
"endif
"colorscheme solarized
"let g:solarized_termtrans=1
"let g:solarized_termcolors=256
"let g:solarized_contrast="low"
"let g:solarized_visibility="low"

highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%80v.\+/
highlight ExtraWhitespace ctermbg=red guibg=red
match ExtraWhitespace /\s\+$/
autocmd BufWinEnter * match ExtraWhitespace /\s\+$/
autocmd InsertEnter * match ExtraWhitespace /\s\+\%#\@<!$/
autocmd InsertLeave * match ExtraWhitespace /\s\+$/
autocmd BufWinLeave * call clearmatches()


let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
"set statusline+=\ %=%#warningmsg#
"set statusline+=\ %=%{SyntasticStatuslineFlag()}
"set statusline+=\ %=%*
"
au BufRead,BufNewFile *.go set filetype=go
set autowrite
let g:go_def_mode='gopls'
let g:go_info_mode='gopls'
let g:go_metalinter_autosave = 1
let g:go_metalinter_autosave_enabled = ['vet', 'golint']
let g:go_highlight_fields = 1
let g:go_highlight_functions = 1
let g:go_highlight_types = 1
let g:go_fmt_command = "goimports"
"let g:go_fmt_fail_silently = 1
let g:go_addtags_transform = "camelcase"
let g:go_textobj_include_function_doc = 0


set statusline+="%f%m%r%h%w [%Y] [0x%02.2B]%< %F%=%4v,%4l %3p%% of %L"

autocmd FileType make set noexpandtab
" add yaml support
au! BufNewFile,BufReadPost *.{yaml,yml} set filetype=yaml foldmethod=indent
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab

set backspace=indent,eol,start

syntax on

packloadall
" Load all of the helptags now, after plugins have been loaded.
" All messages and errors will be ignored.
silent! helptags ALL

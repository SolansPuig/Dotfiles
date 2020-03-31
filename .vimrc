"initialize Vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

"plugins
Plugin 'VundleVim/Vundle.vim'
Plugin 'itchyny/lightline.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'
Plugin 'ryanoasis/vim-devicons'
Plugin 'vim-python/python-syntax'
Plugin 'tpope/vim-surround'
Plugin 'derekwyatt/vim-fswitch'
Plugin 'tpope/vim-obsession'
Plugin 'dhruvasagar/vim-prosession'
Plugin 'octol/vim-cpp-enhanced-highlight'
Plugin 'bfrg/vim-cpp-modern'
Plugin 'morhetz/gruvbox'
Plugin 'dylanaraps/wal.vim'

call vundle#end()
filetype plugin indent on

colorscheme gruvbox
set background=dark
let g:gruvbox_contrast_dark='medium'
let g:lightline = {
        \ 'colorscheme': 'gruvbox',
        \ }

set timeoutlen=1000 ttimeoutlen=0
set encoding=UTF-8
set laststatus=2
scriptencoding utf-8
set t_Co=256
let g:rehash256=1
set noshowmode
set mouse=nicr
set ttymouse=sgr

set splitbelow splitright

set path+=**
set wildmenu
set incsearch
set nobackup
set noswapfile

set guioptions-=m
set guioptions-=T
set guioptions-=r
set guioptions-=L

syntax on
let g:python_highlight_all=1

set number
set autoindent
set textwidth=80
set expandtab
set smarttab
set tabstop=4
set softtabstop=4
set shiftwidth=4
set fillchars+=vert:\ 

"nerd tree
map <C-n> : NERDTreeToggle<CR>
let NERDTreeShowLineNumbers=1
let NERDTreeShowHidden=1
let NERDTreeMinimalUI=1

"c indent options
set cinoptions+=g0,W4,(0,m1

command! Fs FSHere

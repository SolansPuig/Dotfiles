#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

(cat ~/.cache/wal/sequences &)

neofetch

alias ls='ls --color=auto'

source ~/.bash_prompt


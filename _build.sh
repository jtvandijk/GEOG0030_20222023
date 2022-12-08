#!/bin/sh

# option
set -ev

# render
Rscript _gitbook.R

# pretty fix HTML
# source activate html
# python _set_part.py

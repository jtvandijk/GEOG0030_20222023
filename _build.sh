#!/bin/sh

# option
set -ev

# render gitbook
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::gitbook')"

# render pdf
Rscript -e "bookdown::render_book('index.Rmd', 'bookdown::pdf_book')"

# pretty fix HTML
source activate html
python _set_part.py

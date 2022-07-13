#!/bin/sh

# option
set -ev

# serve gitbook
Rscript -e "bookdown::serve_book(dir = '.', output_dir = '_book',
  preview = TRUE, in_session = TRUE, quiet = FALSE,)"

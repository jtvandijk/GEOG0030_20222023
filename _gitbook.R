# libraries
library(rmarkdown)
library(bookdown)

# render
bookdown::render_book('index.Rmd', 'bookdown::gitbook')
bookdown::render_book('index.Rmd', 'bookdown::pdf_book')

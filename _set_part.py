# libraries
# conda env: html
import pandas as pd
import os
import glob

# placeholder
html_files = []

# get html files
files = glob.glob('docs/*')
for f in files:
    if os.path.basename(f).endswith('.html'):
        html_files.append(f)

# loop html files
for htmlf in html_files:

    # initialise template
    with open(htmlf) as file :
      html_content = file.read()

    # update TOC
    html_content = html_content.replace('<li class="chapter" data-level="" data-path="index.html"><a href="index.html"><i class="fa fa-check"></i>Module Overview</a></li>', \
                                        '<li class="part"><span><b>Module Overview</b></span></li>')
    html_content = html_content.replace('<li class="chapter" data-level="" data-path="foundational-concepts.html"><a href="foundational-concepts.html"><i class="fa fa-check"></i>Foundational Concepts</a></li>', \
                                        '<li class="part"><span><b>Foundational Concepts</b></span></li>')
    html_content = html_content.replace('<li class="chapter" data-level="" data-path="additional-resources.html"><a href="additional-resources.html"><i class="fa fa-check"></i>Additional Resources</a></li>', \
                                        '<li class="part"><span><b>Additional Resources</b></span></li>')

    # update back and forth buttons
    html_content = html_content.replace('<link rel="next" href="module-introduction.html"/>', \
                                        '<link rel="next" href="geocomputation-an-introduction.html"/>')

    # write
    with open(htmlf, 'w') as file:
        file.write(html_content)

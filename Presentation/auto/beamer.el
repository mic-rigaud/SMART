(TeX-add-style-hook
 "beamer"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("beamer" "10pt" "svgnames" "compress" "red")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("babel" "french")))
   (TeX-run-style-hooks
    "latex2e"
    "beamer10"
    "lmodern"
    "palatino"
    "fontenc"
    "inputenc"
    "babel"
    "multimedia"
    "graphics"
    "subfigure"
    "natbib"
    "caption"
    "frbib")
   (LaTeX-add-bibliographies
    "biblio")))


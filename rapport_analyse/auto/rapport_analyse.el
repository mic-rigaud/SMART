(TeX-add-style-hook
 "rapport_analyse"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("memoir" "a4paper" "11pt" "oneside")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("babel" "french") ("hyperref" "linktoc=all" "hidelinks") ("xcolor" "svgnames")))
   (TeX-run-style-hooks
    "latex2e"
    "Partie0"
    "Partie1"
    "Partie2"
    "Partie3"
    "memoir"
    "memoir11"
    "lmodern"
    "palatino"
    "fontenc"
    "inputenc"
    "babel"
    "hyperref"
    "float"
    "microtype"
    "graphicx"
    "xcolor"
    "caption"
    "pageGardeEnsta")
   (TeX-add-symbols
    '("couleurr" 1)
    '("couleurb" 1)
    '("latinloc" 1)
    '("attention" 1)
    '("theoreme" 2)
    '("remarque" 1)
    "etc"
    "eg"
    "ie"
    "cad"
    "st")
   (LaTeX-add-bibliographies
    "biblio")
   (LaTeX-add-counters
    "rem"
    "th")))


(TeX-add-style-hook
 "rapport"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("memoir" "a4paper" "11pt" "oneside" "oldfontcommands")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("babel" "french") ("hyperref" "linktoc=all" "hidelinks") ("titlesec" "explicit") ("xcolor" "svgnames") ("csquotes" "babel=true")))
   (TeX-run-style-hooks
    "latex2e"
    "Partie/Contexte"
    "Partie/Ingenieurie_systeme"
    "Partie/Realisation"
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
    "titlesec"
    "graphicx"
    "xcolor"
    "titletoc"
    "frbib"
    "csquotes"
    "eurosym"
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


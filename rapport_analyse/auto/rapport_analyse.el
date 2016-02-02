(TeX-add-style-hook
 "rapport_analyse"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("memoir" "a4paper" "11pt" "oneside" "oldfontcommands")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("inputenc" "utf8") ("babel" "french") ("hyperref" "linktoc=all" "hidelinks") ("xcolor" "svgnames") ("geometry" "a4paper" "top=2cm" "bottom=2cm") ("pdfpages" "final") ("csquotes" "babel=true")))
   (TeX-run-style-hooks
    "latex2e"
    "Partie_Contexte"
    "Partie_AnalyseFonctionnelle"
    "Partie_Radiogonio"
    "Partie_EtatArt"
    "Partie_Montreal"
    "Annexe_drones"
    "Partie_Organisation"
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
    "geometry"
    "pdfpages"
    "eurosym"
    "frbib"
    "csquotes"
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
   (LaTeX-add-labels
    "chap:mail")
   (LaTeX-add-bibliographies
    "biblio")
   (LaTeX-add-counters
    "rem"
    "th")))


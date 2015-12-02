(TeX-add-style-hook "rapport_analyse"
 (lambda ()
    (LaTeX-add-bibliographies
     "biblio")
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
    (TeX-run-style-hooks
     "pageGardeEnsta"
     "pdfpages"
     "final"
     "caption"
     "xcolor"
     "svgnames"
     "graphicx"
     "microtype"
     "float"
     "hyperref"
     "hidelinks"
     "linktoc=all"
     "babel"
     "french"
     "inputenc"
     "utf8"
     "fontenc"
     "T1"
     "palatino"
     "lmodern"
     ""
     "latex2e"
     "memoir11"
     "memoir"
     "oneside"
     "11pt"
     "a4paper"
     "Partie_Contexte"
     "Partie_AnalyseFonctionnelle"
     "Partie_Radiogonio"
     "Partie_Montreal"
     "Partie_Organisation")))


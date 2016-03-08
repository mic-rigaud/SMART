(TeX-add-style-hook "rapport"
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
     "eurosym"
     "csquotes"
     "babel=true"
     "frbib"
     "caption"
     "titletoc"
     "xcolor"
     "svgnames"
     "graphicx"
     "titlesec"
     "explicit"
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
     "oldfontcommands"
     "oneside"
     "11pt"
     "a4paper"
     "Partie/Contexte"
     "Partie/Ingenieurie_systeme"
     "Partie/Realisation"
     "Partie/Annexe_rpi"
     "Partie/Annexe_raspbian")))


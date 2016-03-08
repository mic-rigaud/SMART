(TeX-add-style-hook "pageGardeEnsta"
 (lambda ()
    (TeX-add-symbols
     '("logoSmart" 1)
     '("logoBas" 1)
     '("logoBasDroit" 1)
     '("logoBasGauche" 1)
     '("logoCentre" 1)
     '("imgGarde" 1)
     '("etablissement" 1)
     '("doctype" 1)
     '("version" 1)
     '("promo" 1)
     '("centre" 1)
     '("includegraphics" 1)
     "maketitle")
    (TeX-run-style-hooks
     "tikz"
     "graphics"
     "graphicx"
     "")))


# Soutenance RNCP — version Beamer visuelle

Ce dossier contient la traduction LaTeX/Beamer du support de soutenance EADL, reconstruite à partir du PDF de 44 slides.

## Principes retenus

- **44 slides**, avec la même progression générale que le support source ;
- introduction puis quatre blocs de compétences et conclusion ;
- passage en anglais au début de chaque bloc ;
- une idée principale et une preuve visuelle par slide ;
- le texte long du support source a été fortement réduit : le détail appartient au discours oral ;
- réutilisation des figures déjà présentes dans `figures/` (Ediacara, S-123, Brise-glace, piv2glz, Data/IA, Homelab et Lynx Immo) ;
- formulation prudente sur les points faibles du référentiel : C2.5, C3.5/C3.6 et C4.2/C4.6 ;
- la réunion de transmission Lynx Immo n'est **pas présentée comme réalisée** tant qu'un compte rendu réel n'est pas disponible.

## Structure

- `main.tex` : thème, composants visuels, pied de slide par bloc et assemblage ;
- `sections/00-introduction.tex` : slides 1 à 4 ;
- `sections/01-bloc1.tex` : slides 5 à 14 ;
- `sections/02-bloc2.tex` : slides 15 à 23 ;
- `sections/03-bloc3.tex` : slides 24 à 33 ;
- `sections/04-bloc4.tex` : slides 34 à 43 ;
- `sections/05-conclusion.tex` : slide 44.

Les anciens fichiers `*b-*-zooms.tex` et `90-annexes.tex` restent dans la branche héritée mais ne sont plus inclus dans `main.tex` : ils peuvent servir de réserve pour préparer les questions du jury.

## Compilation

Depuis la racine du dépôt :

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=soutenance soutenance/main.tex
```

Ou depuis le dossier `soutenance` :

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Le helper `\repofigure` cherche les images depuis la racine ou depuis `soutenance/`.

## Temps cible

- Introduction : 5 min maximum ;
- Bloc 1 : 20 min, dont 3–4 min en anglais ;
- Bloc 2 : 20 min, dont 3–4 min en anglais ;
- Bloc 3 : 20 min, dont 3–4 min en anglais ;
- Bloc 4 : 20 min, dont 3–4 min en anglais.

Le support est volontairement plus léger que le script oral : il doit soutenir la parole, pas la remplacer.

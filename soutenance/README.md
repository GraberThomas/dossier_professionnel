# Soutenance RNCP — slides Beamer

Ce dossier contient le support de soutenance du titre RNCP niveau 7 **Expert en Architecture et Développement Logiciel**.

## Structure

- `main.tex` : thème Beamer et assemblage du support ;
- `sections/00-introduction.tex` : introduction commune (5 min max) ;
- `sections/01-bloc1.tex` : Bloc 1 ;
- `sections/02-bloc2.tex` : Bloc 2 ;
- `sections/03-bloc3.tex` : Bloc 3 ;
- `sections/04-bloc4.tex` : Bloc 4 ;
- `sections/05-conclusion.tex` : conclusion très courte ;
- `sections/90-annexes.tex` : slides de secours pour les questions.

Les passages imposés en anglais sont placés **à la fin de chaque bloc** et leurs slides sont elles-mêmes rédigées en anglais. Le reste du support est en français.

## Compilation

Depuis la racine du dépôt :

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=soutenance soutenance/main.tex
```

Ou depuis le dossier `soutenance` :

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Le helper `\repofigure` cherche automatiquement les images depuis la racine du dépôt ou depuis `soutenance/`, ce qui permet les deux modes de compilation.

## Temps cible

- Introduction : 5 min maximum.
- Bloc 1 : 20 min, dont environ 4 min en anglais.
- Bloc 2 : 20 min, dont environ 4 min en anglais.
- Bloc 3 : 20 min, dont environ 4 min en anglais.
- Bloc 4 : 20 min, dont environ 4 min en anglais.

Les annexes de secours ne sont pas destinées à être déroulées pendant les 20 minutes de présentation.

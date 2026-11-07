# Introduction à l'Investigation Numérique (IIN)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](IIN_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE SEC4031** · École Nationale Supérieure Polytechnique de l'Université de Yaoundé I · Département de Génie Informatique · 60 heures
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Avant d'agir, comprendre ce que votre action va détruire.*

Un dossier judiciaire ne se perd pas au tribunal : il se perd sur la scène de crime, dans les dix premières minutes. Ce cours enseigne les fondements, la méthode et le cadre juridique de l'investigation numérique. Il couvre la philosophie et l'histoire de la discipline, les grandes affaires, les fondements théoriques (Locard, Shannon, graphes, Dolev-Yao), le Processus Investigatif Universel, les standards internationaux (ISO/IEC 2703x, NIST SP 800-86, RFC 3227, ACPO), la chaîne de custody, les outils d'acquisition, les conventions de Budapest et de Malabo, le droit étranger, le droit camerounais (lois n° 2010/012 et n° 2024/017) et la déontologie. Le Trilemme CRO (confidentialité, fiabilité, opposabilité) sert de fil rouge. Les affaires camerounaises MBONGO, ONAMBELE, TANGUE, MVOM et WOURI sont fictives, mais leurs mécanismes juridiques et techniques sont exacts.

L'analyse approfondie des artefacts (Windows, mémoire, réseau, mobile, nuage) relève de l'UE suivante, SEC4052 (Investigation numérique avancée).

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`IIN_main.pdf`](IIN_main.pdf) | Traité complet (prologue, 13 chapitres, annexes), compilé depuis [`IIN_main.tex`](IIN_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 31 présentations PowerPoint : vision d'ensemble et 30 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 14 fiches de 40 questions au format texte, à distribuer en attendant l'ouverture de NDAP SUKULU |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie3/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_IN.sty`](Style_IN.sty) | Sources du livre |

## Organisation du cours (60 heures, 30 séances de 2 heures)

| Partie | Chapitres | Séances | Fichiers |
|---|---|---|---|
| **Prologue** | 0. La scène de crime numérique | J01 – J02 | [`partie0/`](partie0/) |
| **I. Fondements épistémologiques et historiques** | 1. Philosophie et fondements · 2. Histoire de l'investigation numérique · 3. Les grandes affaires · 4. Fondements théoriques · 5. État de l'art et défis contemporains | J03 – J12 | [`partie1/`](partie1/) |
| **II. Processus et méthodologies d'investigation** | 6. Le Processus Investigatif Universel · 7. Méthodologies et standards internationaux · 8. Chaîne de custody et admissibilité · 9. Outils et techniques d'acquisition | J13 – J22 | [`partie2/`](partie2/) |
| **III. Cadre normatif, judiciaire et déontologique** | 10. Cadre normatif global · 11. Législation mondiale et régionale · 12. Droit camerounais et africain · 13. Déontologie de l'investigateur | J23 – J30 | [`partie3/`](partie3/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles de documents · D. Textes de loi · E. Bibliographie · F. Contacts | | [`annexes/`](annexes/) |

Chaque chapitre est traité en deux séances en moyenne ; la séance qui clôt un chapitre renvoie à sa fiche d'auto-évaluation, à faire hors présentiel.

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement compagnon du cours : une fiche d'auto-évaluation de 40 questions par chapitre, corrigée automatiquement, et un tableau de bord de progression. Le code de cours est **SEC4031**.

> **NDAP SUKULU en local.** La version téléchargeable et installable sur votre poste, avec un module autonome pour ce cours, est en cours de finalisation. En attendant, les fiches d'auto-évaluation de chaque chapitre (40 questions) sont fournies au format texte dans [`fiches/`](fiches/).

Les labs d'acquisition propres à ce cours sont en préparation. Les labs d'analyse (disque, mémoire, réseau, mobile) sont ceux de SEC4052.

## Compiler le livre

Avec une distribution LaTeX : `pdflatex IIN_main`, `biber IIN_main`, `makeindex IIN_main`, puis deux fois `pdflatex IIN_main`.
Les présentations se régénèrent avec `python Présentation/_sources/run.py IIN all` (Python 3 et python-pptx).

## Normes et documents sous licence

Les normes ISO/IEC et les autres documents sous licence cités dans le cours **ne sont pas fournis** dans ce dépôt.

## Licence

Contenu pédagogique : [CC BY-NC-SA 4.0](LICENSE.md). Code du générateur de présentations : MIT. Voir [`LICENSE.md`](LICENSE.md).

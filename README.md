# InfoPourBac — site statique

Cours d'informatique du Bac scientifique (Tunisie) : algorithme et Python côte à côte.

## Générer le site

```
python build.py
```

Le site complet est écrit dans `public/` : c'est ce dossier qu'on met en ligne (Netlify, Cloudflare Pages, GitHub Pages, ou n'importe quel hébergeur).

## Où modifier quoi

| Fichier | Contenu |
|---|---|
| `content/cours1.py` | Chapitres 1 à 6 |
| `content/cours2.py` | Chapitres 7 à 11 |
| `content/pages.py` | Algorithmes classiques, Bac pratique, glossaire |
| `build.py` | Gabarits, données structurées, sitemap, robots.txt, llms.txt. Le domaine (`BASE`) et la date de mise à jour (`UPDATED`) sont en haut du fichier |
| `static/style.css` | Design |

Après chaque modification, relance `python build.py`.

## Tester en local

```
cd public
python -m http.server 8000
```

Puis ouvre http://localhost:8000 (les liens commencent par `/`, il faut donc un serveur : un double-clic sur le fichier ne suffit pas).

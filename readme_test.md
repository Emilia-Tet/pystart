# README
This is a sample readme file.
``git clone``

```python
print('Hello World')
```
cmd folder + ``git status`` pokazuje biezacy stan repo
cmd git add + file name (or whole catalog)
cmd git reset + file name (or whole catalog) -> cofa zmiany, np git reset HEAD~1, 1 to jeden commit. Musze wiedziec ile ich cofnac. 
cmd git commit -m "Tresc zmiany"
cmd ``git log``, wychdzi sie ``q``
cmd ``git pull ``
cmd ``git push``
git flow cheat sheet - podpowiedzi nazywania branchy itd

branche:
1. pull najnowszej wersji
2. nazwanie brancha, np
feature/...
hotfix/...
release/1.0.1
release/1.0.2

3. utworzenie brancha
git checkout (przelacza miedzy branchami)
git checkout -b feature/SYS-16.... (przelacza do nowo utworzonego brancha)
git add, git commit (jesli duzy commit, to moge tez nie napisac -m, otworzy mi sie okno i tam moge wiecej napisac i wygodniej).
Przed git push, git status
"fatal: The current branch exercice/git has no upstream branch." -> jest branch lokalnie, ale nie zdalnie
to tworzy i od razu pushuje. 
potem moge sie przelaczac miedzy branchami przez git checkout. 
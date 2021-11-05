cat users.txt calls.txt | ./map1.py | sort -n | ./reduce1.py | sort > res1.txt && cat res1.txt |./map2.py | sort | ./reduce2.py > res2.txt  && cat res2.txt |./map3.py | sort > resultat.txt && subl resultat.txt &

# j'utilise l'editeur Sublim Text d'ou la commande subl pour consulter le fichier resultat.txt
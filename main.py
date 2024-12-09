

"""
------------------------------------------------------------------------------
!!! ATTENTION, BESOIN DU FICHIER table1.csv ET table2.csv POUR FONCTIONNER !!!
------------------------------------------------------------------------------


Comment accéder au tableau périodique ?

Numéro atomique:
int(anum[élément])
Ex: Neon
int(anum["Ne"])

Masse atomique:
amass[int(anum[élément])]
Ex: Neon
amass[int(anum["Ne"])]

Pour calculer la quantité de neutrons:

int(Masse atomique) - Nbr. atomique


-------------------------------------------------------------------------------------------------
!!! ATTENTION, SI MASSE ATOMIQUE = -1 MASSE ATOMIQUE INDÉFINIE (NBR DE NEUTRONS INCALCULABLE) !!!
-------------------------------------------------------------------------------------------------

"""

import csv

def opentable(filename):
  with open(filename, newline="") as f:
    reader = csv.reader(f)
    return list(reader)

anum = dict(opentable("/content/drive/MyDrive/table1.csv"))

amass = [float(x[0]) for x in opentable("/content/drive/MyDrive/table2.csv")]

print(anum)
print(amass)

print(int(anum["Ne"]))
print(amass[int(anum["Ne"])])

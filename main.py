import os

path = os.getcwd()

"""
-------------------------------------------------------------------------------------------------
!!!         ATTENTION, BESOIN DU FICHIER table1.csv ET table2.csv POUR FONCTIONNER            !!!
-------------------------------------------------------------------------------------------------


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

anum = dict(opentable(path + "/table1.csv"))

amass = [float(x[0]) for x in opentable(path + "/table2.csv")]


"""
No longer needed, used for debuging purposes

print(anum)
print(amass)

print(int(anum["Ne"]))
print(amass[int(anum["Ne"])])
"""


def nbr_particules(element, charge, nbr_atomes):
  # electrons
  electrons = int(anum[element])

  if int(charge) != 0:
    electrons = (electrons - int(charge)) * nbr_atomes





  # protons
  protons = (int(anum[element])) * nbr_atomes

  # neutrons
  if amass[int(anum[element])] == -1.0:
    return "Nombre(s) d'electrons: " + str(int(electrons))+ "\n"+ "Nombre(s) de protons: "+ str(int(protons))+"\n"+"Nombre(s) de neutrons: "+ "MASSE ATOMIQUE INDÉFINIE (NOMBRE DE NEUTRONS INCALCULABLE)"

  else:
    neutrons = ((round(amass[int(anum[element])], 0) - (int(anum[element])))) * nbr_atomes
    return "Nombre(s) d'electrons: " + str(int(electrons))+ "\n"+ "Nombre(s) de protons: "+ str(int(protons))+"\n"+"Nombre(s) de neutrons: "+ str(int(neutrons))



while True:
  atome = input("Entrez le symbole de l'atome (premiere lettre en majuscule): ")
  if atome in anum.keys():
    break
  else:
    print("Atome inconnu")

while True:
  charge_atomique = input("Entrez la charge de l'atome (entrez le symbole - ou + avant le chiffre): " )
  try:
    charge_atomique = int(charge_atomique)
    break

  except ValueError:
    print("Charge inconnu")

while True:
  nbr_atome = input('Entrez le nombre de particules (ex: si c est:  5.34 * 10**23 particules ecrivez 5.34e23): ')
  try:
    nbr_atome = float(nbr_atome)
    break

  except ValueError:
    print("Nombre inconnu")


print(nbr_particules(atome, charge_atomique,nbr_atome))

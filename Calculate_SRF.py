from typing import Union, Any

import pandas as pd

##############################################################################################################
#                 DEFINITION DES FONCTIONS DE RECUPERATION DE DONNEES DE L'UTILISATEUR                       #
##############################################################################################################

def recuperate_file(name, index_sheet):
    """Récupère une feuille du fichier Excel pour la transformer en objet liste """
    feuille_recup = pd.read_excel(name, sheet_name=index_sheet)
    return feuille_recup.values.tolist()


def fdico_economie(feuille):
    """ Définition du dictionnaire Economie contenant la correspondance entre l'index et son critère """
    dico_economie = {}
    for x in range(7,15):
        dico_economie[(feuille[x][2])] = (feuille[x][1])
    return dico_economie

def fdico_technique(feuille):
    """ Définition du dictionnaire Technique contenant la correspondance entre l'index et son critère """
    dico_technique = {}
    for x in range(18, 22):
        dico_technique[(feuille[x][2])] = (feuille[x][1])
    return dico_technique

def fdico_social(feuille):
    """ Définition du dictionnaire Social contenant la correspondance entre l'index et son critère """
    dico_social = {}
    for x in range(25,30):
        dico_social[(feuille[x][2])] = (feuille[x][1])
    return dico_social

def fdico_environnement(feuille):
    """ Définition du dictionnaire Environnement contenant la correspondance entre l'index et son critère """
    dico_environnement = {}
    for x in range(33,40):
        dico_environnement[(feuille[x][2])] = (feuille[x][1])
    return dico_environnement

def tableau_choix(feuille,dico,index):
    """Récupération des choix de l'utilisateur sous forme d'une liste. Retourne également le ratio Z"""
    tableau_choix_environnement = [[0 for j in range(4)] for i in range(15)]
    a = index[0]
    b = index[1]
    for x in range(a,b):
        tableau_choix_environnement[x - a][0]= x - a+1
        for y in range(2,5):
            tableau_choix_environnement[x - a][y - 1]=str(feuille[x][y])
            if (dico.get(tableau_choix_environnement[x - a][y - 1], 1) != 1) :
                tableau_choix_environnement[x - a][y - 1] = dico.get(tableau_choix_environnement[x - a][y - 1])
    return tableau_choix_environnement, feuille[index[1]+1][2]

""" DONNEES MURS !
Récupération des choix Critères ENVIRONNEMENTAL
tableau_choix_environnement = [[0 for j in range(4)] for i in range(15)]
for x in range(19,34):
    tableau_choix_environnement[x - 19][0]= x - 18
    for y in range(2,5):
        tableau_choix_environnement[x - 19][y - 1]=str(feuille3_liste[x][y])
        if (dico_environnement.get(tableau_choix_environnement[x - 19][y - 1], 1) != 1) :
            tableau_choix_environnement[x - 19][y - 1] = dico_economie.get(tableau_choix_environnement[x - 19][y - 1])
z_environnement = feuille2_liste[35][2]
"""

##############################################################################################################
#                             DEFINITION DES FONCTIONS DE CALCUL                                             #
##############################################################################################################

def traitement(l):
    """Permet de retirer les cartes blanches inutiles"""
    while l[-1][1] == 'nan':
        del l[-1]
    return l

def calcul_rang(l):
    listnouveaurang = [None]*len(l)
    for i in range(len(l)):
        listnouveaurang[i] = l[len(l)-i-1]
        listnouveaurang[i][0]=i+1
    return listnouveaurang

def calcul_n(l):
    n = 0
    for i in range(len(l)):
        for j in range(1, len(l[i])):
            if l[i][j] != 'nan':
                n +=1
    return n

def calcul_er_prime(l,n):
    for i in range(len(l)-1):
        if l[i+1][1] == 'nan':
            l[i].append(1)
        else:
            l[i].append(0)
    if n == 0:
        l[len(l)-1].append(1)
    else:
        l[len(l)-1].append(0)

    for i in range(1,len(l)):
        if l[len(l)-i-1][-1] != 0:
            l[len(l) - i - 1][-1] = l[len(l)-i-1][-1] + l[len(l)-i][-1]
    for i in range(len(l)):
        if l[i][1] == 'nan' and l[i][2] == 'nan' and l[i][3] == 'nan':
            l[i][-1] = 0
    return l

def calcul_er(l):
    e = 0
    for i in range(len(l)):
        l[i].append(l[i][-1]+1)
        e += l[i][-1]
    return l,e

def calcul_u(z,e):
    u = (z-1)/e
    return u

def calcul_k_i_prime(u,l):
    somme_er = 0
    for i in range(len(l)):
        if l[i][1] != 'nan':
            l[i].append(1+u*somme_er)
            somme_er += l[i][-2]
        else:
            l[i].append('nan')
            somme_er += l[i][-2]
    return l

def traitement2(l):
    """Permet d'obtenir un tableau avec le critère et son ki' associé"""
    liste_traitee = []
    for i in range(len(l)):
        for j in range(1 , 4):
            if l[i][j] != 'nan':
                liste_traitee.append([l[i][j],l[i][-1]])
    return liste_traitee

def calcul_K_prime(l):
  K_prime = 0
  for i in range(len(l)):
      K_prime += l[i][1]
  return K_prime

def calcul_ki_etoile(l,K_prime):
  for i in range(len(l)):
      l[i].append((100/K_prime)*l[i][1])
  return l

def calcul_ki_2prime(l):
  for i in range(len(l)):
      l[i].append(int(l[i][2]*100)/100)
  return l

def calcul_K_2prime(l):
  K_2prime = 0
  for i in range(len(l)):
      K_2prime += l[i][3]
  return K_2prime

def calcul_ki(l,K_2prime,n):
  w = 2
  for i in range(len(l)):
      l[i].append((10 ** (-w) - (l[i][2] - l[i][3])) / l[i][2])  # Calcul di
      l[i].append((l[i][2] - l[i][3]) / l[i][2])  # Calcul di_barre
      if l[i][4] > l[i][5]: #Calcul M
          l[i].append(1)
      else:
          l[i].append(0)
      if l[i][6] == 1: #Calcul di_M
          l[i].append(l[i][4])
      else:
          l[i].append('-')

  v = int(10 ** (w) * (100 - K_2prime))  # Calcul v
  m = 0  # Calcul m
  for i in range(len(l)):
      m += l[i][6]

  L = [] # Calcul L
  for i in range(len(l)):
      if l[i][7] != '-':
          L.append(l[i][7])
  L.sort()
  if L == []:
      L = [0] * n

  vmn = v + m - n
  if m+v > n:
      for i in range(vmn,len(L)):
          L[i] = 0
  else:
      L = [0]*n

  #Calcul flèche L
  for i in range(len(L)):
      compteur_di = 0
      if L[i] == l[0][4]:
          compteur_di +=1
  if compteur_di != 0:
          l[0].append(1)
  else:
          l[0].append(0)
  vmn =  v + m -n
  for i in range(1,len(l)):
      compteur_di = 0
      for j in range(len(L)):
          if L[j] == l[i][4]:
              compteur_di +=1
      if compteur_di != 0:
          s=0
          j = 0
          while j != i and i < len(L):
              s+=L[j]
              j +=1
          if s>vmn :
              l[i].append(0)
          else:
              l[i].append(1)

      else:
          l[i].append(0)


  for i in range(len(l)): #Calcul dibarre_différent_M
      if l[i][6] == 0:
          l[i].append(l[i][5])
      else:
          l[i].append('-')

  Lbarre = []  # Calcul Lbarre
  nvm = n - v -m
  for i in range(len(l)):
      if l[i][9] != '-':
          Lbarre.append(l[i][9])
  Lbarre.sort()
  if Lbarre == []:
      Lbarre = [0] * n

  if m + v < n:
      for i in range(nvm, len(Lbarre)):
          Lbarre[i] = 0
  else:
      Lbarre = [0] * n


  #Calcul flèche Lbarre

  for i in range(len(Lbarre)):
      compteur_dibarre = 0
      if Lbarre[i] == l[0][5]:
          compteur_di += 1
  if compteur_di != 0:
      l[0].append(1)
  else:
      l[0].append(0)

  for i in range(1, len(l)):
      compteur_dibarre = 0
      for j in range(len(Lbarre)):
          if Lbarre[j] == l[i][5]:
              compteur_dibarre += 1

      if compteur_dibarre != 0:
          s = 0
          j = 0
          while j != i and i < len(Lbarre):
              s += Lbarre[j]
              j +=1
          if s > nvm:
              l[i].append(0)
          else:
              l[i].append(1)
      else:
          l[i].append(0)
  #Calcul F+ / F-
  for i in range(len(l)):  # F+
      if m + v < n:
          conditionF = n - v - m
          if l[i][6] == 0:
              l[i].append(1)
          else:
              l[i].append(0)
      else:
          conditionF = n - v
  fbis = [0] * len(l)
  verif = 0
  j = n-1
  while verif < conditionF and j!=-1:
      if l[j][10]==1 and l[j][6]==0:
          fbis[j] = 0
          if verif <= nvm:
              l[j][11] = fbis[j]
              verif = verif +1
      j = j-1

  # Calcul F- puis ki
  for i in range(len(l)):
      if l[i][11] == 0: #F-
          l[i].append(1)
      else:
          l[i].append(0)
      if l[i][12] == 1: #ki
          l[i].append(int(l[i][2]*(10**w))/10**w)
      else:
          l[i].append(int(l[i][2]*(10**w)+1)/(10**w))
  veri = 0
  for i in range(len(l)):
      veri += l[i][13]
  return l,veri

##############################################################################################################
#                                 METHODE DE SIMOS-ROY-FIGUEIRA                                              #
##############################################################################################################

def SRF():
    #Récupération des feuilles depuis l'excel de choix des critères
    feuille1 = recuperate_file('Pondération critères.xlsm', 0)
    feuille2 = recuperate_file('Pondération critères.xlsm', 1)
    feuille3 = recuperate_file('Pondération critères.xlsm', 2)

    #Définition des critères et de leur index
    dico_economie = fdico_economie(feuille1)
    dico_environnement = fdico_environnement(feuille1)
    dico_social = fdico_social(feuille1)
    dico_technique = fdico_technique(feuille1)

    #Définition des index pour récupérer les données de choix dans l'excel
    index_environnement = [92,107]
    index_economie = [21,36]
    index_social = [69,84]
    index_technique = [45,60]

    #Récupération du tableau des choix de l'utilisateur
    tableau_choix_environnement, z_environnement = tableau_choix(feuille2,dico_environnement,index_environnement)
    tableau_choix_economie, z_economie = tableau_choix(feuille2,dico_economie,index_economie)
    tableau_choix_technique, z_technique = tableau_choix(feuille2,dico_technique,index_technique)
    tableau_choix_social, z_social = tableau_choix(feuille2,dico_social,index_social)

    tableau = traitement(tableau_choix_economie)

    tableau = calcul_rang(tableau)

    n = calcul_n(tableau)

    tableau = calcul_er_prime(tableau,n)

    tableau,e = calcul_er(tableau)

    u = calcul_u(z_economie,e)


    tableau = calcul_k_i_prime(u,tableau)

    tableau = traitement2(tableau)


    K_prime = calcul_K_prime(tableau)

    tableau = calcul_ki_etoile(tableau,K_prime)

    tableau = calcul_ki_2prime(tableau)

    K_2prime = calcul_K_2prime(tableau)

    tableau,total = calcul_ki(tableau,K_2prime,n)

    dico = {}
    dico_weights = {}
    for i in range(0,len(tableau)):
        dico[tableau[i][0]]=tableau[i][13]
    dico = sorted(dico.items(), key=lambda t: t[0])
    for i in range(0,len(dico)):
        dico_weights[dico[i][0]] = dico[i][1]
    print(dico_weights)
    return dico_weights
    #for i in range(0,len(tableau)):
     #   print(str(tableau[i][0])+" "+str(tableau[i][13]))
    #print("Somme des poids = "+str(total))


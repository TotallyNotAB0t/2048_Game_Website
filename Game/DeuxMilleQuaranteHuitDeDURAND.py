#Bibliothèques graphique (natives avec python 3)
from tkinter import *
from tkinter.messagebox import *
import copy #On veux cette bibliothèque pour pouvoir deepcopy notre grille.

#Bibliothèque de l'aléa (native avec python 3)
#Pour appeler un nombre entier au hasard entre a et b
#on fait poetiquement : randint(a, b)
from random import randint

auteur="Pierre Durand"

#Initialisation : début de partie
#Il y a trois ou quatres valeurs (en général 2 mais parfois, rarement, un 4)
def Init(dim) :
    X=dict()
    for i in range(dim) :
            X[i]=dict()
            for j in range(dim) :
                    X[i][j]=randint(0,100) #On choisit un nombre au hasard entre 0 et 100, pour simuler une probabilité.
                    if X[i][j]<70 : #On a 70% de chance de tomber sur un 0
                            X[i][j]=0
                    elif X[i][j]>=70 and X[i][j]<=95 : #On a 25% de chance de tomber sur un 2
                            X[i][j]=2
                    elif X[i][j]>95 : #On a 5% de chance de tomber sur un 4
                            X[i][j]=4
    return X

#Fonction pour ajouter un deux a chaque fois que l'on fait un mouvement
def ajouter_deux(grille) :
    dim = len(grille)
    x, y = randint(0, dim-1), randint(0, dim-1)
    while (grille[x][y]!=0) :
        x, y = randint(0, dim-1), randint(0, dim-1)
    grille[x][y] = 2
    return dim

#Renvoie 1 si c'est gagné
#Renvoie -1 si c'est perdu
#Renvoie 0 sinon
def TestFin(grille) :
    for i in range(len(grille)) :
        for j in range(len(grille[0])) :
            if grille[i][j]==2048 : #Si une case comporte 2048, on gagne
                return 1

    for i in range(len(grille)) :
        for j in range(len(grille[0])) :
            if grille[i][j]==0 : #Tant qu'une case est vide, on continue de jouer
                return 0

    for i in range(len(grille)-1): #On veux continuer de jouer même si tout est rempli et qu'on peux additionner des cases dans le tableau (colonnes)
        for j in range(len(grille)):
            if grille[i][j] == grille[i+1][j]:
                return 0

    for j in range(len(grille)-1): #On veux continuer de jouer même si tout est rempli et qu'on peux additionner des cases dans le tableau (lignes)
        for i in range(len(grille)):
            if grille[i][j] == grille[i][j+1]:
                return 0

    else : #Sinon, on perd
        return -1

#Renvoie la grille mise à jour après un mouvement vers le haut
#En entrée : la grille avant le mouvement
#En sortie : la grille après le mouvement
def ActionHaut(grille) :
    grilleA = copy.deepcopy(grille) #Copie de la grille avant coup
    dim=len(grille)
    for i in range(dim - 1) : #Déplacement haut
        for j in range(dim) :
            for k in range(dim -1) :
                if grille[k][j] == 0 and grille[k+1][j] != 0 :
                    grille[k][j] = grille[k+1][j]
                    grille[k+1][j] = 0

    for i in range(0, dim-1, 1): #Addition haut
        for j in range(dim) :
            if grille[i][j] == grille[i+1][j] and grille[i][j] !=0 :
                grille[i][j] *= 2
                grille[i+1][j] = 0
                for k in range(dim -1) : #On redéplace après addition pour ne pas qu'il y ai de trou dans le code
                    if grille[k][j] == 0 and grille[k+1][j] != 0 :
                        grille[k][j] = grille[k+1][j]
                        grille[k+1][j] = 0

    grilleB = copy.deepcopy(grille) #Copie de la grille après coup
    if grilleA == grilleB : #Si les deux sont égales, on ne change pas la grille.
        return grille
    else : #Si les grilles ont changé, alors on peux ajouter un deux.
        ajouter_deux(grille)
        return grille

#Renvoie la grille mise à jour après un mouvement vers le bas
#En entrée : la grille avant le mouvement
#En sortie : la grille après le mouvement
def ActionBas(grille) :
    grilleA = copy.deepcopy(grille) #Copie de la grille avant coup
    dim=len(grille)
    for i in range(dim - 1) : #Déplacement bas
        for j in range(dim) :
            for k in range(dim-1, 0, -1) :
                if grille[k][j] == 0 and grille[k-1][j] != 0 :
                    grille[k][j] = grille[k-1][j]
                    grille[k-1][j] = 0

    for i in range(dim-1, 0, -1): #Addition bas
        for j in range(dim) :
            if grille[i][j] == grille[i-1][j] :
                grille[i-1][j] = 0
                grille[i][j] *= 2
                for k in range(dim-1, 0, -1) : #On redéplace après addition pour ne pas qu'il y ai de trou dans le code
                    if grille[k][j] == 0 and grille[k-1][j] != 0 :
                        grille[k][j] = grille[k-1][j]
                        grille[k-1][j] = 0

    grilleB = copy.deepcopy(grille) #Copie de la grille après coup
    if grilleA == grilleB : #Si les deux sont égales, on ne change pas la grille.
        return grille
    else : #Si les grilles ont changé, alors on peux ajouter un deux.
        ajouter_deux(grille)
        return grille

#Renvoie la grille mise à jour après un mouvement vers la gauche
#En entrée : la grille avant le mouvement
#En sortie : la grille après le mouvement
def ActionGauche(grille) :
    grilleA = copy.deepcopy(grille) #Copie de la grille avant coup
    dim=len(grille)
    for j in range(1, dim) : #Déplacement gauche
        for i in range(dim) :
            for k in range(1, dim) :
                if grille[i][k-1] == 0 and grille[i][k] != 0 :
                    grille[i][k-1] = grille[i][k]
                    grille[i][k] = 0

    for i in range(dim) : #Addition gauche
        for j in range(dim - 1) :
            if grille[i][j] == grille[i][j+1] :
                grille[i][j] *= 2
                grille[i][j+1] = 0
                for k in range(1, dim) :
                    if grille[i][k-1] == 0 and grille[i][k] != 0 : #On redéplace après addition pour ne pas qu'il y ai de trou dans le code
                        grille[i][k-1] = grille[i][k]
                        grille[i][k] = 0

    grilleB = copy.deepcopy(grille) #Copie de la grille après coup
    if grilleA == grilleB : #Si les deux sont égales, on ne change pas la grille.
        return grille
    else : #Si les grilles ont changé, alors on peux ajouter un deux.
        ajouter_deux(grille)
        return grille

#Renvoie la grille mise à jour après un mouvement vers la droite
#En entrée : la grille avant le mouvement
#En sortie : la grille après le mouvement
def ActionDroite(grille) :
    grilleA = copy.deepcopy(grille) #Copie de la grille avant coup
    dim=len(grille)
    for j in range(dim-1, 0, -1) : #Déplacement droite
        for i in range(dim) :
            for k in range(dim-1, 0, -1) :
                if grille[i][k] == 0 and grille[i][k-1] != 0 :
                    grille[i][k] = grille[i][k-1]
                    grille[i][k-1] = 0

    for i in range(dim) : #Addition droite
        for j in range(dim-1, 0, -1) :
            if grille[i][j] == grille[i][j-1] :
                grille[i][j] *= 2
                grille[i][j-1] = 0
                for k in range(dim-1, 0, -1) :
                    if grille[i][k] == 0 and grille[i][k-1] != 0 :
                        grille[i][k] = grille[i][k-1]
                        grille[i][k-1] = 0

    grilleB = copy.deepcopy(grille) #Copie de la grille après coup
    if grilleA == grilleB : #Si les deux sont égales, on ne change pas la grille.
        return grille
    else : #Si les grilles ont changé, alors on peux ajouter un deux.
        ajouter_deux(grille)
        return grille

def FENETRE(dim) :

        def recupPartie() :
                dim=len(JEU)
                X=dict()
                for i in range(dim) :
                        X[i]=dict()
                        for j in range(dim) :
                                try : X[i][j]=int(JEU[i][j].get())
                                except : X[i][j]=0
                return X

        def InjectionPartie(X) :
                for i in range(dim) :
                        for j in range(dim) :
                                try : (JEU[i][j]).set(X[i][j])
                                except : (JEU[i][j]).set(0)

                                if(int(JEU[i][j].get())==0) : (JEU[i][j]).set("")

        def Clavier(mouvement):
                CMPT.set(CMPT.get()+1)

                touche = mouvement.keysym
                # déplacement vers le haut
                if touche == 'Up': ActionHaut0()
                # déplacement vers le bas
                if touche == 'Down': ActionBas0()
                # déplacement vers la droite
                if touche == 'Right': ActionDroite0()
                # déplacement vers la gauche
                if touche == 'Left': ActionGauche0()

        def ActionRecommencer() :
                X=Init(dim)
                for i in range(dim) :
                        for j in range(dim) :
                                (JEU[i][j]).set(X[i][j])
                                if(X[i][j]==0) : (JEU[i][j]).set("")
                CMPT.set(0)

        def ActionHaut0() :
                InjectionPartie(ActionHaut(recupPartie()))
                TestFin0(recupPartie())

        def ActionBas0() :
                InjectionPartie(ActionBas(recupPartie()))
                TestFin0(recupPartie())

        def ActionGauche0() :
                InjectionPartie(ActionGauche(recupPartie()))
                TestFin0(recupPartie())

        def ActionDroite0() :
                InjectionPartie(ActionDroite(recupPartie()))
                TestFin0(recupPartie())

        def TestFin0(X) :
                test=TestFin(X)
                if(test==1) : showinfo("FIN DE PARTIE", "Bravo ! Vous avez gagné en "+str(CMPT.get())+" coups. Je sens la triche...")
                if(test==-1) :showinfo("FIN DE PARTIE", "Perdu ! Il vous a fallu "+str(CMPT.get())+" coups pour perdre... OOF.")
                if(test!=0) : ActionRecommencer()

        fenetre = Tk()
        fenetre.title('2048 par '+auteur)

        CMPT=IntVar()
        CMPT.set(0)

        X=Init(dim)
        JEU=dict()
        for i in range(dim) :
                JEU[i]=dict()
                for j in range(dim) :
                        JEU[i][j]=StringVar()
                        (JEU[i][j]).set(X[i][j])
                        if(X[i][j]==0) : (JEU[i][j]).set("")

        base=70 #Taille en px d'un carré
        if(dim>7) : base=50
        marge=10 #Marge de beauté

        hauteur = dim*base+2*marge+100
        largeur = dim*base+2*marge

        canvas = Canvas(fenetre, background="#C0C0C0", width=largeur, height=hauteur )

        case=dict()
        for i in range(dim) :
                case[i]=dict()
                for j in range(dim) :
                        canvas.create_rectangle((base*i+marge,base*j+marge), (base*(i+1)+marge,base*(j+1)+marge), width=1)

                        c_fg='black'
                        c_bg ='#C0C0C0'

                        if((JEU[i][j]).get()==0) : c_fg='#C0C0C0'

                        L=Label(fenetre, textvariable=JEU[i][j], fg=c_fg, bg=c_bg)
                        L.place(x=base*j+base//2, y=base*i+base//2, anchor="nw")


        txt="Nombre de mouvement : "
        L=Label(fenetre, text=txt, fg='black', bg='#C0C0C0')
        L.place(x=marge, y=(hauteur-base), anchor="sw")
        L=Label(fenetre, textvariable=CMPT, fg='black', bg='#C0C0C0')
        L.place(x=marge+len(txt)*7, y=(hauteur-base), anchor="sw")

        fenetre.geometry(str(largeur)+"x"+str(hauteur))
        BoutonQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy)
        BoutonQuitter.place(x=marge, y=hauteur-marge, anchor="sw")
        BoutonRecommencer = Button(fenetre, text ='Recommencer', command = ActionRecommencer)
        BoutonRecommencer.place(x=largeur-marge, y=hauteur-marge, anchor="se")

        canvas.focus_set()
        canvas.bind('<Key>',Clavier)

        canvas.grid()
        fenetre.mainloop()

#Dimension du 2048 - usuellement 4
dim=0
while(dim<2 or dim>11) :
        try : dim=int(input("Choisissez la taille de votre 2048 (entre 3 et 10): "))
        except : dim=0

#Fonction principale
FENETRE(dim)

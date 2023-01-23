from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

convertisseur = Tk()
convertisseur.title("Convertisseur de monnaie")
convertisseur.geometry("380x480")
convertisseur.configure(bg="#cfd8d7")
convertisseur.resizable(height = False, width = False)
historique = [] # pour lister les précédente conversions


OPTIONS = {"EUR":1,"USD":1.08,"JPY":139.21,"CAD":0.69,"AUD":0.65,}  # menu option qui permet de choisir la devise + taux de conversion

def conv():                  # cette fonction est celle qui convertira nos valeurs et enregistre les valeurs dans un historique
    prixx = prix.get()
    if not prixx:
        messagebox.showerror("Erreur", "Entrez une valeur correcte")
        return
    if not prixx.isdigit():
        messagebox.showerror("Erreur", "valeur incorrecte, ne mettez pas de lettres")
        return
    qst = variable1.get()
    qst2 = variable2.get()
    DICT = OPTIONS.get(qst,None)
    DICT2 = OPTIONS.get(qst2,None)
    convertis = round(float(DICT2)*float(prixx)/float(DICT),2)
    resultat.config(state='normal')
    resultat.delete(1.0,END)
    resultat.insert(INSERT,prixx,INSERT," ",INSERT,qst,INSERT," = ",INSERT,convertis,INSERT," ",INSERT,qst2)
    resultat.config(state='disabled')
    historique.append(prixx + " " + qst + " = " + str(convertis) + " " + qst2)

def historique_resultat():
    messagebox.showinfo("Historique des résultats", "\n".join(historique))

def ajouter_devise():
    devise = simpledialog.askstring("Ajouter une devise", "Nom de la devise (3 lettres) :", parent=convertisseur)
    taux = simpledialog.askfloat("Ajouter une devise", "Taux de conversion :", parent=convertisseur)
    if devise and taux:
        OPTIONS[devise] = taux
        option.children["menu"].add_command(label=devise, command=lambda: variable1.set(devise))
        option2.children["menu"].add_command(label=devise, command=lambda: variable2.set(devise))


############################################# PHRASE ET FENETRE CONVERTISSEUR ##############################################################

nomApp = Label(convertisseur,text="CONVERTISSEUR DE MONNAIE",font=("Century Gothic",15,"bold"),fg="black",bg="#9f9aa4")
nomApp.place(x=40, y=50)

resultat = Text(convertisseur,height=2,width=30,font=("arial",10,"bold"),bd=5,state='disabled')
resultat.place(x=80, y=340)


############################################# BOUTON ET PHRASE POUR ENTRER UN NOMBRE ########################################################

fr = Label(convertisseur,text="Entrez un nombre :",font=("Cascadia Mono",10,"bold"),fg="black",bg="#cfd8d7")
fr.place(x=125, y=100)

prix = Entry(convertisseur,font=("arial",10))
prix.place(x=125, y=130,height=30,width=120)


############################################# PREMIERE OPTION QUI PERMET DE CHOISIR LA PREMIERE DEVISE ######################################

choix = Label(convertisseur,text="De :",font=("arial",10),fg="black",bg="#cfd8d7")
choix.place(x=115, y=180)

variable1 = StringVar(convertisseur)
variable1.set(None)
option = OptionMenu(convertisseur, variable1, *OPTIONS.keys())
option.place(x=165 , y=170,width=100, height=40)
option.configure(bg="#cab1bd")


####################### DEUXIEME OPTION QUI PERMET DE CHOISIR VERS QUEL DEVISE CONVERTIR NOTRE VALEUR #######################################

choix2 = Label(convertisseur,text="Vers :",font=("arial",10),fg="black",bg="#cfd8d7")
choix2.place(x=115, y=230)

variable2 = StringVar(convertisseur)
variable2.set(None)
option2 = OptionMenu(convertisseur, variable2, *OPTIONS.keys())
option2.place(x=165 , y=220,width=100, height=40)
option2.configure(bg="#cab1bd")



############################################# BOUTON QUI PERMET DE CONVERTIR ##############################################################

boutton = Button(convertisseur,text="CONVERSION",fg="white",font=("arial",12),bg="#e7cfcd",command=conv)
boutton.place(x=115, y=280,height=40,width=150)


############################################# BOUTON QUI AFFICHE L'HISTORIQUE DES CONVERSIONS #############################################

boutton_historique = Button(convertisseur,text="Historique",fg="white",font=("arial",8),bg="#b5c9c3",command=historique_resultat)
boutton_historique.place(x=60, y=410,height=30,width=120)

############################################# BOUTON QUI PERMET D'AJOUTER UNE NOUVELLE DEVISE #############################################

boutton_ajouter_devise = Button(convertisseur,text="Ajouter une devise",fg="white",font=("arial",8),bg="#b5c9c3",command=ajouter_devise)
boutton_ajouter_devise.place(x=200, y=410,height=30,width=120)


convertisseur.mainloop()
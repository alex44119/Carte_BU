resourcesPath = "Resources/"  # Laisser le string vide pour android

import os

if not resourcesPath:
    with open("carteBUandroid.py", "r") as thisScript:
        text = thisScript.read()
    with open("carteBUandroid.py", "w") as thisScript:
        ligne1 = "resourcesPath = \""+os.path.dirname(__file__)+"/resources/\""
        thisScript.write(ligne1+text[19:])
        
    resourcesPath = os.path.dirname(__file__)+"/Resources/"
import tkinter as tk
from PIL import ImageTk, Image
import requests
import time
from time import localtime as getTime
import webbrowser
with open(resourcesPath+"BaseDeDonnees.py") as BDD:
    exec(BDD.read())

dictypes = {3146:(0, "Place Standard"), 3147:(1, "Prise Electrique"), 3148:(2, "Ordinateur"), 3149:(3, "Travail en groupe"), 3150:(4, "Accès PMR"), 3161:(15, "Visite Express")}
jour = {0:"Aujourd'hui", 1:"Demain"} # Uniquement utilisé dans etat des lieux
invJour = {"Aujourd'hui":0, "Demain":1}
c = 1 # Compteur

def getInfo(info, place, EDL = {}, noError = True):
    """Gets the information about a place. String info can be "resource_id", "resource_name", "resource_type", "description", "site_timezone", "hours", "is_obsolete" or "reservation_link"."""
    assert (info in ["resource_id", "resource_name", "resource_type", "description", "site_timezone", "hours", "reservation_link", "is_obsolete"]) , \
           "La valeur prise par la variable info n'est pas valable. Pour plus d'informations, saisir la commande 'help(getInfo)'."

    try:
        return EDL[(place, 0)][info] # L'info est associée au jour même
    except:
        try:
            return EDL[(place, 1)][info] # L'info est associée au lendemain
        except:
            assert noError, "Erreur getInfo rencontrée veuillez contacter Alex M. R."
            EDL = etat_des_lieux_partiel() | EDL
            storeEDL(getEDL() | EDL)
            return getInfo(info, place, EDL, False)
# Cette variable noError est un peu moche mais elle est à but temporaire, afin de detecter une possible erreur

def etat_des_lieux_partiel():
    """Effectue un état des lieux rapide mais partiel (données volontairement manquantes) de TOUTES les places"""
    global c

    def create_dico(li, D):
        return {key : D[key] for key in li}

    
    url = f"https://reservation.affluences.com/api/resources/78a7dd22-c0f1-453b-902e-27608ab60df0" # url magique de l'API d'affluences
    print(url)
    
    te = requests.get(url).text # texte tel qu'il est présenté il représente une liste de dictionnaires en format json
    
    ListeDeDonnees = eval(te.replace("false", "False").replace("true", "True").replace("null", "None")) # conversion json -> python

    D = {}
    
    for el in ListeDeDonnees:
        noplace = f"Place sans numéro{c}"
        try:
            noplace = int(el["resource_name"][-4:])
        except:
            c += 1
            
        li = ["resource_id", "resource_name", "resource_type", "description"] # Selection des données UTILES
        
        D[(noplace, 0)] = create_dico(li, el)
        
        D[(noplace, 0)]["hours"] = []

        D[(noplace, 0)]["is_obsolete"] = True
        
        D[(noplace, 0)]["reservation_link"] = \
    f"https://affluences.com/universite-de-nantes-bibliotheques/bu-sante-nantes/reservation?type={el['resource_type']}&resource={el['resource_id']}"
        
    return D

def etat_des_lieux(typ = 0, date = 0): # Type : 0 - Place Standard, 1 - Prise électrique, 2 - Ordinateur, 3 - Travail en groupe, 4 - Place PMR, 15 - Visite Express
    """Effectue un état des lieux de TOUTES les places du couple (type, date) rentré en paramètre"""
    global c
    
    def create_dico(li, D):
        return {key : D[key] for key in li}

    def create_list(li, L):
        return [create_dico(li, D) for D in L]

    d = time.localtime(time.time()+24*60*60*date) # Extraction de la date
    d = f"&date={str(d.tm_year)}-{('0' + str(d.tm_mon))[-2:]}-{('0' + str(d.tm_mday))[-2:]}" # exemple : "date=2023-05-19"
    
    url = f"https://reservation.affluences.com/api/resources/78a7dd22-c0f1-453b-902e-27608ab60df0/available?{d}&type={3146+typ}" # url magique de l'API d'affluences
    print(url)
    
    te = requests.get(url).text # texte tel qu'il est présenté il représente une liste de dictionnaires en format json
    
    ListeDeDonnees = eval(te.replace("false", "False").replace("true", "True").replace("null", "None")) # conversion json -> python

    # Cette liste contient énormément de données qui sont inutiles tel que "max_places_per_reservation", "static_time_slot", ... 
    # Ainsi, pour plus de practicité, il faut que cette liste devienne un dictionnaire ayant pour clé le couple (place, date) et pour valeurs UNIQUEMENT les données UTILES :

    D = {}
    
    
    for el in ListeDeDonnees:
        noplace = f"Place sans numéro{c}"
        try:
            noplace = int(el["resource_name"][-4:])
        except:
            c += 1
            
        li = ["resource_id", "resource_name", "resource_type", "description", "site_timezone", "hours"] # Selection des données UTILES
        
        D[(noplace, date)] = create_dico(li, el)
        

        lihours = ["hour", "state", "person_count", "places_available"] # Idem. state : 1 Libre, 2 Occupe

        D[(noplace, date)]["hours"] = create_list(lihours, el["hours"])

        D[(noplace, date)]["is_obsolete"] = False
        
        D[(noplace, date)]["reservation_link"] = \
    f"https://affluences.com/universite-de-nantes-bibliotheques/bu-sante-nantes/reservation?type={el['resource_type']}&resource={el['resource_id']}"
        
    return D


# L[(noplace, date)] = (titre, sstitre, dictypes[3146+typ], jour[date], horraires)

def etat_des_lieux_adapte(li, date = 0):
    D = {}
    for i, el in enumerate(li):
        if el.get():
            D.update(etat_des_lieux(i, date))
    return D
        
        

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (100, 100, 100)

def est_dispo(place, heure, duree, date = 0, EDL = {}):
    """Vérifie si la place est disponible aux conditions renseignées"""
    def ajHeure(heure, i):
        """Ajoute i granularités à l'heure"""
        v = int(heure[:2])+int(heure[-2:])/60
        v += i*0.5
        v = f"{('0'+str(int(v)))[-2:]}:{('0'+str(int(60*int(100*(v-int(v)))/100)))[-2:]}"
        return v
    if ((place, date) in EDL) and (not EDL[(place, date)]["is_obsolete"]) :
        heures = EDL[(place, date)]["hours"]
        horaires = {el["hour"] : (el["places_available"] >= 1) for el in heures} # Selection des heures disponibles
        for i in range(int((duree-1)/30+1)):
            heureTest = ajHeure(heure, i)
            if not (heureTest in horaires):
                return "No" # La place n'est pas réservable
            elif not horaires[heureTest]:
                return "No" # La place est prise
            
        return "Yes" # La place est disponible
    return "Donnees indisponibles" # Les données ne sont pas disponibles ou obsoletes

def rendre_obsolete(EDL):
    for k in EDL:
        if (type(EDL[k]) == dict) and ("is_obsolete" in EDL[k]):
            EDL[k]["is_obsolete"] = True

def rect(image, color, a, coords, height, width):
    if color == None:
        return None
    r, g, b = color
    pixel_array = image.load()
    (x, y) = coords
    for i in range(x, x+width):
        for j in range(y-height, y):
            if len(pixel_array[0, 0]) == 3:
                ra, ga, ba = pixel_array[i, j]
                pixel_array[i, j] = (int(r*(1-a)+ra*a), int(g*(1-a)+ga*a), int(b*(1-a)+ba*a))
            else:
                ra, ga, ba, aa = pixel_array[i, j]
                pixel_array[i, j] = (int(r*(1-a)+ra*a), int(g*(1-a)+ga*a), int(b*(1-a)+ba*a), aa)


def remap(x, y, i):
    if i == 1:
        (a, b) = (281, 211)
        (c, d) = (218, 170)
        return (int(x/a*c), int(y/b*d))
    if i == 2:
        (a, b) = (282, 308)
        (c, d) = (395, 459)
        return (int(x/a*c), int(y/b*d))
    if i == 3:
        (a, b) = (290, 474)
        (c, d) = (408, 656)
        return (int(x/a*c), int(y/b*d))
    if i == 4:
        (a, b) = (320, 441)
        (c, d) = (342, 466)
        return (int(x/a*c), int(y/b*d))
    if i == 5:
        (a, b) = (305, 291)
        (c, d) = (329, 310)
        return (int(x/a*c), int(y/b*d))

def nextTime():
    actualTime = getTime(time.time()-1200)
    
    H = actualTime.tm_hour
    M = actualTime.tm_min

    if 23 <= H:
        return ("08:30", 240, "Demain")
    if H <= 7:
        return ("08:30", 240,"Aujourd'hui")
    if M < 30:
        return (f"0{H}:30"[-5:], 30, "Aujourd'hui")
    else:
        return (f'0{H+1}:00'[-5:], 30, "Aujourd'hui")

def listToDict(lst):
    return dict(lst)

def dictToList(di):
    L = list(di)
    return [(l, di[l]) for l in L]

def storeEDL(EDL):
    lst = dictToList(EDL)
    with open(f"{resourcesPath}data.txt", "w") as f:
        for item in lst:
            f.write(str(item) + "\n")

# storeEDL et getEDL restent des boites un peu noires : elles fonctionnent mais j'ai la flemme de m'assurer de leur correction
# On essaiera de toujours vérifier l'invariant : EDL contient "li" et "time"
def getEDL():
    try:
        with open(f"{resourcesPath}data.txt", "r") as f:
            data = []
            for line in f:
                data.append(eval(line))
        EDL = listToDict(data)
        
        nxtTime = nextTime()
        if BDDhour_options[EDL["li"][0]] < BDDhour_options[nxtTime[0]] and EDL["li"][2] == "Aujourd'hui":
            EDL["li"][0] = nxtTime[0] # Si jamais l'heure prévue est trop en avance, ça corrige
        
        return EDL
    except:
        EDL_init = {"li": [*nextTime(), False, False, False, False, False], "time" : time.time()}
        storeEDL(EDL_init)
        return EDL_init


def carteInteractive():
    cases = [[], [], [], [], []]
    class ImageCanvas:
        def __init__(self, master, image_path, width, height, plan, wright, hright, wleft, hleft, i, heureS, dureeS, dateS, EDL):
            def callback():
                root.destroy()
                carteInteractive()
            self.heureS, self.dureeS, self.dateS, self.EDL = heureS, dureeS, dateS, EDL
            self.i = i
            self.savedClick = False
            master.protocol("WM_DELETE_WINDOW", callback)
            self.master = master
            self.canvas = tk.Canvas(self.master, width=width, height=height)
            self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.canvas.bind("<Button-1>", self.on_canvas_click_pressed)
            self.canvas.bind("<ButtonRelease-1>", self.on_canvas_click_released)
            
            self.canvas.bind("<Button-2>", self.on_canvas_right_click)
            self.canvas.bind("<Button-3>", self.on_canvas_right_click)
            self.img = Image.open(image_path)
            for k in plan:
                if k["number"]<6:
                    cases[i-1].append(((k["x"], k["y"]), (k["w"], k["h"]), k["number"]))
                else:
                    dispo = est_dispo(k['number'], heureS, dureeS, dateS, EDL)
                    if dispo == "Yes":
                        col = None
                    elif dispo == "No":
                        col = RED
                    else: # dispo = "Donnees indisponibles"
                        col = GREY
                    if k["key_pressed"] == "right":
                        rect(self.img, col, 0.5, remap(k['x'], k['y'], i), hright, wright)
                        cases[i-1].append((remap(k['x'], k['y'], i), (wright, hright), k['number']))
                    else:
                        rect(self.img, col, 0.5, remap(k['x'], k['y'], i), hleft, wleft)
                        cases[i-1].append((remap(k['x'], k['y'], i), (wleft, hleft), k['number']))
            self.img = self.img.resize((width, height))
            self.photo_img = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(0, 0, anchor="nw", image=self.photo_img)
### Partie a effacer pour la version mobile ###
            self.scrollbarY = tk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.canvas.yview)
            self.scrollbarX = tk.Scrollbar(self.master, orient=tk.HORIZONTAL, command=self.canvas.xview)
            self.canvas.configure(yscrollcommand=self.scrollbarY.set)
            self.canvas.configure(xscrollcommand=self.scrollbarX.set)
            self.scrollbarY.pack(side=tk.RIGHT, fill=tk.Y)
            self.scrollbarX.pack(side=tk.BOTTOM, fill=tk.X)
            self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))

            self.canvas.bind("<MouseWheel>", self.on_mousewheel)
            
            
        def on_mousewheel(self, event):
            # Detection du scroll
            self.canvas.yview_scroll(int(-1 * (event.delta))/120, "units") # Sur Windows, il faut diviser delta par 120 !!!
### ###
 
            
        def on_canvas_click_pressed(self, event):
            xe, ye = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
            for (x, y), (w, h), pl in cases[self.i-1]:
                if x < xe and ye < y  and xe < x+w and y-h < ye:
                    self.savedClick = (x, y), (w, h), pl
                    return ()

        def on_canvas_click_released(self, event):
            xe, ye = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
            if self.savedClick :
                (x, y), (w, h), pl = self.savedClick
                if pl < 6 :
                    if x < xe and ye < y  and xe < x+w and y-h < ye:
                        if pl == self.i:
                            self.master.destroy()
                        elif pl == 1:
                            self.master.destroy()
                            Root1(self.heureS, self.dureeS, self.dateS, self.EDL)
                        elif pl == 2:
                            self.master.destroy()
                            Root2(self.heureS, self.dureeS, self.dateS, self.EDL)
                        elif pl == 3:
                            self.master.destroy()
                            Root3(self.heureS, self.dureeS, self.dateS, self.EDL)
                        elif pl == 4:
                            self.master.destroy()
                            Root4(self.heureS, self.dureeS, self.dateS, self.EDL)
                        elif pl == 5:
                            self.master.destroy()
                            Root5(self.heureS, self.dureeS, self.dateS, self.EDL)
                        return ()
                            
                elif x < xe and ye < y  and xe < x+w and y-h < ye:
                    d = time.localtime(time.time()+24*60*60*self.dateS)
                    d = f"&date={str(d.tm_year)}-{('0' + str(d.tm_mon))[-2:]}-{('0' + str(d.tm_mday))[-2:]}"
                    URL = getInfo("reservation_link", pl, self.EDL)+d
                    webbrowser.open(URL)
                    
                self.savedClick = False

            
        def on_canvas_right_click(self, event):
            xe, ye = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
            for (x, y), (w, h), pl in cases[self.i-1]:
                if x < xe and ye < y  and xe < x+w and y-h < ye and pl >= 6:
                    d = time.localtime(time.time()+24*60*60*self.dateS)
                    d = f"&date={str(d.tm_year)}-{('0' + str(d.tm_mon))[-2:]}-{('0' + str(d.tm_mday))[-2:]}"
                    URL = getInfo("reservation_link", pl, self.EDL)+d
                    root.clipboard_clear()
                    root.clipboard_append(URL)
            # Lors d'un click droit, le lien est copié
            

    if __name__ == "__main__":
        root = tk.Tk()
        photo = tk.PhotoImage(file = resourcesPath+'Icone/bumap.png')
        root.wm_iconphoto(False, photo)
        root.minsize(300, 0)
        root.title("Carte Interactive BU Santé")
        
        EDL = getEDL()
        li = EDL["li"]
        # Liste déroulante nº1 : Heure
        time_options = ['08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00']
        time_var = tk.StringVar(value = li[0])
        time_dropdown = tk.OptionMenu(root, time_var, *time_options)
        time_dropdown.pack()

        # Liste déroulante nº1 : Durée
        duree_options = ["30min", "1h00", "1h30", "2h00", "2h30", "3h00", "3h30", "4h00", "4h30", "5h00"]
        duree_var = tk.StringVar(value = BDDminToHour(li[1]))
        duree_dropdown = tk.OptionMenu(root, duree_var, *duree_options)
        duree_dropdown.pack()
        
        # Liste déroulante nº1 : Jour
        date_options = ["Aujourd'hui", "Demain"]
        date_var = tk.StringVar(value = li[2])
        date_dropdown = tk.OptionMenu(root, date_var, *date_options)
        date_dropdown.pack()

    # Frame
        labelFrame = tk.Frame(root)
        labelFrame.pack()
        
        # Label
        regen = tk.Label(labelFrame, text="Données à télécharger :", fg = "black")
        regen.pack(side = tk.LEFT)

        # Help Button
        def helpPlease():
            if message.get() == "" :
                message.set("Si rien n'est coché, les dernières\n données seront affichées.")
            else :
                message.set("")
                
        helpButt = tk.Button(labelFrame, text="?", command=helpPlease)
        helpButt.pack(side = tk.RIGHT)

        # Help Message
        message = tk.StringVar()
        message.set("")
        helpMess = tk.Label(root, textvariable = message ,fg = "green")
        helpMess.pack()

    # End Frame
    
        # Checkboxes
        ck_list = []
        
        is_regen_standard = tk.BooleanVar(value = li[3])
        ck_standard = tk.Checkbutton(root, text="Standard", variable=is_regen_standard)
        ck_standard.pack()
        ck_list.append(is_regen_standard)
        
        is_regen_prise = tk.BooleanVar(value = li[4])
        ck_prise = tk.Checkbutton(root, text="Place avec prise", variable=is_regen_prise)
        ck_prise.pack()
        ck_list.append(is_regen_prise)

        is_regen_ordinateur = tk.BooleanVar(value = li[5])
        ck_ordinateur = tk.Checkbutton(root, text="Ordinateur", variable=is_regen_ordinateur)
        ck_ordinateur.pack()
        ck_list.append(is_regen_ordinateur)

        is_regen_travailGroupe = tk.BooleanVar(value = li[6])
        ck_travailGroupe = tk.Checkbutton(root, text="Travail en groupe", variable=is_regen_travailGroupe)
        ck_travailGroupe.pack()
        ck_list.append(is_regen_travailGroupe)

        is_regen_PMR = tk.BooleanVar(value = li[7])
        ck_PMR = tk.Checkbutton(root, text="PMR", variable=is_regen_PMR)
        ck_PMR.pack()
        ck_list.append(is_regen_PMR)


        # Text
        text = tk.Label(root, text = "\n" ,fg = "red")
        text.pack()
        
        # Validation button
        def validate():
            text.config(text = "Chargement des données...\n(cela peut prendre quelques instants)")
            validate_button.config(state = 'disabled')
            root.update()
            EDL = getEDL()
            EDL["li"] = [time_var.get(), BDDhourToMin(duree_var.get()), date_var.get(), *[el.get() for el in ck_list]]
            storeEDL(EDL)
            if BDDhour_options[time_var.get()] < BDDhour_options[nextTime()[0]] and date_var.get() == "Aujourd'hui":
                EDLtemp = {} # Si jamais l'heure prévue est trop en avance, ça évite de perdre du temps
            else :
                EDLtemp = etat_des_lieux_adapte(ck_list, invJour[date_var.get()])
            if bool(EDLtemp) : # False dans le cas où cklist = [False, ..., False]
                EDLtemp["li"] = [time_var.get(), BDDhourToMin(duree_var.get()), date_var.get(), *[el.get() for el in ck_list]]
                EDLtemp["time"] = time.time()
                rendre_obsolete(EDL)
                EDL.update(EDLtemp)
            storeEDL(EDL)
            
            root.withdraw()
            Root1(time_var.get(), BDDhourToMin(duree_var.get()), invJour[date_var.get()], EDL)

        validate_button = tk.Button(root, text="Valider", command=validate)
        validate_button.pack()
        def Root1(heureS, dureeS, dateS, EDL):
            root1 = tk.Toplevel()
            # Canvas nº1 - Salle Madeleine Bres
            canvas1 = ImageCanvas(root1, f"{resourcesPath}Plans-niv61.jpeg", 1169, 634, BDDK1, 28, 22, 22, 28, 1, heureS, dureeS, dateS, EDL)
            
        def Root2(heureS, dureeS, dateS, EDL):
            root2 = tk.Toplevel()
            # Canvas nº2 - Salle Louis Pasteur
            canvas2 = ImageCanvas(root2, f"{resourcesPath}Plans-niv62.jpeg", 841, 1190, BDDK2, 28, 22, 22, 28, 2, heureS, dureeS, dateS, EDL)
            
        def Root3(heureS, dureeS, dateS, EDL):
            root3 = tk.Toplevel()
            # Canvas nº3 - Salle Marie Curie
            canvas3 = ImageCanvas(root3, f"{resourcesPath}Plans-niv63.jpeg", 841, 1106, BDDK3, 28, 22, 22, 28, 3, heureS, dureeS, dateS, EDL)
        def Root4(heureS, dureeS, dateS, EDL):
            root4 = tk.Toplevel()
            # Canvas nº4 - Salle Loire
            canvas4 = ImageCanvas(root4, f"{resourcesPath}5loire.jpeg",587, 845 , BDDniv5LOIRE, 28, 20, 18, 22, 4, heureS, dureeS, dateS, EDL)
        def Root5(heureS, dureeS, dateS, EDL):
            root5 = tk.Toplevel()
            # Canvas nº5 - Salle Erdre
            canvas5 = ImageCanvas(root5, f"{resourcesPath}5erdre.jpeg", 593, 849, BDDniv5ERDRE, 28, 20, 18, 22, 5, heureS, dureeS, dateS, EDL)
        root.mainloop()


carteInteractive()

import CreateBaseandcomplete
import pymysql

CreateBaseandcomplete.CreateBaseMySQL()

#Requêtes pour le CRUD
 
def visualRemboursement():
    db=CreateBaseandcomplete.connect()
    cursor = db.cursor()
    req = cursor.execute("SELECT numticket, date, prixnuit, premierrepas, deuxiemerepas, prixplein,prixpeage FROM remboursejour ORDER BY numticket;")
    return cursor.fetchall()

def visualRemboursementtoString(remboursement : tuple) -> str:
    return f"Pour le ticket de remboursement : {remboursement[0]}, on était le : {remboursement[1]}, le prix de la nuit était de : {remboursement[2]}, le prix du premier repas de la journée était de : {remboursement[3]}, le deuxième plat de la journée était de : {remboursement[4]}, le prix du plein était de {remboursement[5]} et le tarif des péages était de {remboursement[6]}"
def visualRemboursementTotaltoString(remboursement: tuple) -> str:
    remb1erplat = 30.00
    remb2emeplat = 30.00
    rembnuit = 110.00
    totalremb = 0

    # Convertissez les valeurs de la liste en float avant les comparaisons
    if rembnuit > float(remboursement[2]):
        rembnuit = float(remboursement[2])
    if remb1erplat > float(remboursement[3]):
        remb1erplat = float(remboursement[3])
    if remb2emeplat > float(remboursement[4]):
        remb2emeplat = float(remboursement[4])

    # Convertissez les valeurs de la liste en float avant l'addition
    totalremb = rembnuit + remb1erplat + remb2emeplat + float(remboursement[5]) + float(remboursement[6])

    return f"Pour le ticket de remboursement : {remboursement[0]}, le remboursement total est de {totalremb}, car la nuit est remboursée de {rembnuit}, car le premier plat est remboursé de {remb1erplat}, le deuxième de {remb2emeplat}, le prix du plein remboursé totalement : {remboursement[5]}, et le prix des péages qui était de {remboursement[6]}"
def PrintRemboursement():
    remboursement_list = []
    for e in visualRemboursement():
        remboursement_str = visualRemboursementtoString(e)
        remboursement_str = visualRemboursementTotaltoString(e)
        remboursement_list.append(remboursement_str)
    return remboursement_list   

def AddRemboursement():
    numticket=input("Saisir la date de sortie du 1er épisode (AAAA-MM-JJ) :")
    date=input("Saisir la date de sortie du 1er épisode (AAAA-MM-JJ) :")
    prixnuit = float(input("Saisie du prix de la nuit"))
    premierrepas =input("Saisie du plat (ex : Déjeuner/Diner/Aucun)")
    deuxiemerepas=input("Saisie du plat (ex : Déjeuner/Diner/Aucun)")
    prixplein= float(input("Saisie du prix du plein"))
    prixpeage = float(input("Saisie du prix total des péages"))
    try :
        InsertRemboursement(numticket,date,prixnuit,premierrepas,deuxiemerepas,prixplein,prixpeage)
    except ValueError as e:
        print(f"\n ERREUR : {e} \n")
def InsertRemboursement(numticket : str, date :str,prixnuit:float,premierrepas:str,deuxiemerepas:str,prixplein:float,prixpeage:float):
    db = CreateBaseandcomplete.connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO remboursejour (numticket,date, prixnuit, premierrepas, deuxiemerepas, prixplein, prixpeage) VALUES(%s, %s, %s, %s, %s, %s,%s);",
                   (numticket,date, prixnuit, premierrepas, deuxiemerepas, prixplein, prixpeage))
    db.commit()
    cursor.close()

def removeReqRemboursement(numticket):
    db = CreateBaseandcomplete.connect()
    cursor = db.cursor()
    req = cursor.execute("SELECT * from remboursejour WHERE numticket = %s;", (numticket,))
def removeRemboursement(numticket):
    db = CreateBaseandcomplete.connect()
    cursor = db.cursor()
    req = removeReqRemboursement(numticket)
    cursor.execute("DELETE FROM remboursejour where numticket=%s;", (numticket,))
    db.commit()
def deleteRemboursement():
    numticket = input("Saisissez le numéro de ticket :")
    try :
        removeRemboursement(numticket)
    except ValueError as e:
        print(f"\n ERREUR : {e}\n")
        
def choix():
    choix = 0
    while choix != 7:
        print("\n ==================================")
        print(" =========== Mode CLI =============")
        print(" ==================================\n")
        print(" ==================================\n")
        print(" ============= CRUD ===============")
        print("1 - Visualiser l'ensemble des Remboursement")
        print("2 - Ajout d'une journée de remboursement ")
        print("3 - Suppresion du ticket de remboursement")

        choix =int(input("Entrez votre choix : "))


        if choix==1:
            PrintRemboursement()
        elif choix==2:
            AddRemboursement()
        elif choix==3:
            deleteRemboursement()
    print("Bye")
        
    

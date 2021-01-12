import pandas as pd
from database import insert_deliveries, find_operator_id, find_city_id, find_territory_id
import time



def donnees_electricite_2008_2017():
    for annee in range(2008,2018,1):
        df = pd.read_csv(f'data/electricite/donnees_elec_{annee}.csv', sep = ';', encoding='latin-1')
        inc = 0
        # print(annee)
        # print(len(df))
        # print("-----")

        for nb in range(0,len(df),1):
            try:
                #for nb in range(0,200,1):
                inc +=1
                conso = 0

                value = df.iloc[nb,:]
                operateur = value[0]
                operateur = operateur.replace("'","")

                date = int(value[1])
                territoire = value[3]
                adresse = "Null"
                ville ="Null"
                energie_id = 1  #A MODIF DANS GAZ
                operator_id = 0
                city_id = 0

                consoa = round(float(value[5].replace(",", ".")),2)
                consoi = round(float(value[8].replace(",", ".")),2)
                consot = round(float(value[11].replace(",", ".")),2)
                consor = round(float(value[14].replace(",", ".")),2)
                consona = round(float(value[19].replace(",", ".")),2)



                if consoa > 0 :
                    conso += int(consoa)
                    
                if consoi > 0 :
                    conso += int(consoi)

                if consot > 0 :
                    conso += int(consot)

                if consor > 0 :
                    conso += int(consor)

                if consona > 0 :
                    conso += int(consona)
                

                if consoa > consoi and consoa > consot and consoa > consor and consoa > consona :
                    #secteur = "A"
                    secteur_id = 1

                elif consoi > consoa and consoi > consot and consoi > consor and consoi > consona :
                    #secteur = "I"
                    secteur_id = 2

                elif consot > consoa and consot > consoi and consot > consor and consot > consona :
                    #secteur = "T"
                    secteur_id = 3

                elif consor > consoa and consor > consoi and consor > consot and consor > consona :
                    #secteur = "R"
                    secteur_id = 4

                elif consona > consoa and consona > consoi and consona > consor and consona > consot :
                    #secteur = "X"
                    secteur_id = 5

                else:
                    #secteur = "ERROR"
                    secteur_id = -1
                
                
                
                
                
                
                #time.sleep(0.01)
                territory_id = find_territory_id(territoire)
                operator_id = find_operator_id(operateur)
                city_id = find_city_id(ville)
                
                print(energie_id, operator_id, date, territory_id, secteur_id, conso, adresse, city_id)
                #print(type(energie_id), type(operator_id), type(date), type(territoire), type(secteur_id), type(conso), type(adresse), type(city_id))


                insert_deliveries(energie_id, operator_id, date, territory_id, secteur_id, conso, adresse, city_id)
            except:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def donnees_electricite_2018_2019():
    for annee in range(2018,2020,1):
        df = pd.read_csv(f'data/electricite/donnees_elec_adresse_{annee}.csv', sep = ';', encoding='utf8')
        inc = 0


        territoire = "IRIS"



        for nb in range(0,len(df),1):
            try:
                value = df.iloc[nb,:]
                if value[7] != "s":
                    inc +=1

                    operateur = value[0]
                    operateur = operateur.replace("'","")
                    date = int(value[1])
                    secteur = value[6]
                    operator_id = 0
                    city_id = 0
                    ville = value[5]
                    ville = ville.replace("'","")
                    energie_id = 1   #A MODIF DANS GAZ


                    if secteur == "A":
                        secteur_id = 1

                    elif secteur == "I":
                        secteur_id = 2

                    elif secteur == "T":
                        secteur_id = 3

                    elif secteur == "R":
                        secteur_id = 4

                    elif secteur == "X":
                        secteur_id = 5


                    adresse = value[4]
                    try:
                        adresse = adresse.replace("'","")
                    except:
                        pass



                    try :
                        conso = int(float((value[7].replace(",", "."))))
                    except:
                        try:
                            conso = int(value[7])
                        except:
                            conso = 0





                    
                    
                    
                    #time.sleep(0.01)
                    territory_id = find_territory_id(territoire)
                    operator_id = find_operator_id(operateur)
                    city_id = find_city_id(ville)
                    
                    print(energie_id, operator_id, date, territory_id, secteur_id, conso, adresse, city_id)
                    #print(type(energie_id), type(operator_id), type(date), type(territoire), type(secteur_id), type(conso), type(adresse), type(city_id))


                    insert_deliveries(energie_id, operator_id, date, territory_id, secteur_id, conso, adresse, city_id)
            except:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")














# SELECT * FROM cities;
# SELECT * FROM deliveries;
# SELECT * FROM energies;
# SELECT * FROM operators;
# SELECT * FROM sectors;
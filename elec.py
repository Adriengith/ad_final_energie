import pandas as pd

def donnees_electricite_2008_2017():
    for annee in range(2008,2018,1):
        df = pd.read_csv(f'data/electricite/donnees_elec_{annee}.csv', sep = ';', encoding='latin-1')
        inc = 0
        # print(annee)
        # print(len(df))
        # print("-----")

        for nb in range(0,len(df),1):
            #for nb in range(0,200,1):
            inc +=1
            conso = 0
            secteur = "Null"

            value = df.iloc[nb,:]
            operateur = value[0]
            date = value[1]
            territoire = value[3]
            code = value[4]

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
                secteur = "A"

            elif consoi > consoa and consoi > consot and consoi > consor and consoi > consona :
                secteur = "I"

            elif consot > consoa and consot > consoi and consot > consor and consot > consona :
                secteur = "T"

            elif consor > consoa and consor > consoi and consor > consot and consor > consona :
                secteur = "R"

            elif consona > consoa and consona > consoi and consona > consor and consona > consot :
                secteur = "X"

            else:
                secteur = "ERROR"


            
            print(inc,"| operateur :",operateur,"|","date :",date,"|","territoire :",territoire,"|","code :",code,"|","secteur :",secteur,"|","conso :",conso)
            
            print("-"*100)


def donnees_electricite_2018_2019():
    for annee in range(2018,2020,1):
        for maille in ["adresse","iris","epci","region"]:
            df = pd.read_csv(f'data/electricite/donnees_elec_{maille}_{annee}.csv', sep = ';', encoding='latin-1')
            inc = 0


            if maille == "iris" or maille == "adresse":
                territoire = "IRIS"
            elif maille == "epci":
                territoire = "EPCI"
            elif maille == "region":
                territoire = "REGION"


            print(annee, maille)
            print(len(df))
            print("-----")

            for nb in range(0,len(df),1):
                value = df.iloc[nb,:]
                if value[7] != "s":
                    inc +=1

                    operateur = value[0]
                    date = value[1]
                    code = value[3]
                    secteur = value[6]


                    try :
                        conso = int(float((value[7].replace(",", "."))))
                    except:
                        try:
                            conso = int(value[7])
                        except:
                            conso = 0





                    
                    print(inc,"| operateur :",operateur,"|","date :",date,"|","territoire :",territoire,"|","code :",code,"|","secteur :",secteur,"|","conso :",conso)
                    
                    print("-"*100)


#donnees_electricite_2008_2017()
donnees_electricite_2018_2019()
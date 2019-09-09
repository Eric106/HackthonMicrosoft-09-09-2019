# -*- coding: utf-8 -*-
from os import system,listdir

def files_to_list(sintomas):
    listaSintom=listdir(sintomas)
    content=[]
    for i in range(len(listaSintom)):
        archivo=open("sintomas/"+listaSintom[i],"r",encoding="utf-8")
        content.append(archivo.readlines())
    for i in range(len(listaSintom)):
        for j in range(len(content[i])):
            content[i][j]=content[i][j].rstrip()
    return content

def main():
    system("cls")
    logo = '''
                               /$$   /$$           /$$                                       
                              | $$  | $$          | $$                                       
                              | $$  | $$  /$$$$$$ | $$  /$$$$$$                              
                              | $$$$$$$$ /$$__  $$| $$ /$$__  $$                             
                              | $$__  $$| $$$$$$$$| $$| $$  \ $$                             
                              | $$  | $$| $$_____/| $$| $$  | $$                             
                              | $$  | $$|  $$$$$$$| $$| $$$$$$$/                             
                              |__/  |__/ \_______/|__/| $$____/                              
                                                      | $$                                   
                                                      | $$                                   
                                                      |__/                                   
 /$$$$$$       /$$                                           /$$$$$$$           /$$          
|_  $$_/      | $$                                          | $$__  $$         |__/          
  | $$        | $$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$       | $$  \ $$ /$$$$$$  /$$ /$$$$$$$ 
  | $$        | $$__  $$ |____  $$|  $$  /$$//$$__  $$      | $$$$$$$/|____  $$| $$| $$__  $$
  | $$        | $$  \ $$  /$$$$$$$ \  $$/$$/| $$$$$$$$      | $$____/  /$$$$$$$| $$| $$  \ $$
  | $$        | $$  | $$ /$$__  $$  \  $$$/ | $$_____/      | $$      /$$__  $$| $$| $$  | $$
 /$$$$$$      | $$  | $$|  $$$$$$$   \  $/  |  $$$$$$$      | $$     |  $$$$$$$| $$| $$  | $$
|______/      |__/  |__/ \_______/    \_/    \_______/      |__/      \_______/|__/|__/  |__/

-By KEERF(1/2)- Give us our Backpacks
----------------------------------------------------------------------------------------------
'''
    print(logo)
    print("Hola bb <3 ")
    print("Dame tus sintomas: ")
    listaSintomas=[]
    try: 
        currentSyntom=input("   Dame tu 1° sintoma ==> ")
        while(currentSyntom==""):
            currentSyntom=input("   Dame tu 1° sintoma ==> ")
        numSin=2
        while(currentSyntom!="es todo"):
            currentSyntom=input("   Dame tu "+str(numSin)+"° nuevo ==> ")
            if(currentSyntom!=""):
                listaSintomas.append(currentSyntom)
            numSin+=1
    
    except Exception as e:
        print(e)
        return main()
    listaArchivos=listdir("sintomas")
    listaContent=files_to_list("sintomas")
    listaPuntos=[]
    for fileCont in listaContent:
        puntos=0
        for sintom in listaSintomas:
            if(sintom in fileCont):
                puntos+=1
        listaPuntos.append((puntos/len(fileCont)*100))
    listaResult=[]
    for i in range(len(listaPuntos)):
        if (listaPuntos[i]>0):
            listaResult.append(listaArchivos[i].rstrip(".csv")+" "+str(listaPuntos[i])+"%")
    print("----------------------------------------------------------------------------------------------")
    print("Tus probabilidades son: ")
    print(listaResult)
    ret=input("Presiona [ENTER] para continuar ==> ")
    while(ret!=""):
        ret=input("Presiona [ENTER] para continuar ==> ")
    else:
        main()
main()
# -*- coding: utf-8 -*-
from os import system

def main():
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
        currentSyntom=input("Dame tu 1° sintoma ==> ")
        while(currentSyntom==""):
            currentSyntom=input("Dame tu 1° sintoma ==> ")
        while(currentSyntom!="nada mas"):
            currentSyntom=input("Dame un sintoma nuevo ==> ")
            if(currentSyntom!=""):
                listaSintomas.append(currentSyntom)
    except Exception as e:
        print(e)
        return main()
    
main()
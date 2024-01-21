#Harry Potter
print('''
 _                                    _         _                             
| |                                  | |       | |                            
| |__   ___   __ ___      ____ _ _ __| |_ ___  | | ___  __ _  __ _  ___ _   _ 
| '_ \ / _ \ / _` \ \ /\ / / _` | '__| __/ __| | |/ _ \/ _` |/ _` |/ __| | | |
| | | | (_) | (_| |\ V  V / (_| | |  | |_\__ \ | |  __/ (_| | (_| | (__| |_| |
|_| |_|\___/ \__, | \_/\_/ \__,_|_|   \__|___/ |_|\___|\__, |\__,_|\___|\__, |
              __/ |                                     __/ |            __/ |
             |___/                                     |___/            |___/ 


      ''')

print("Vitejte v Bradavicich! \nNyní se vypravíte do svých kolejí")
koleje = input("Chcete následovat spolužáky na ubikace? A/N: ")
if koleje == "A":
    print("Jdete s nima na ubikace a jdete spát. Uvidíme se zítra")
elif koleje == "N":
    rozcesti = input("Oddělili jste se od spolužáků a stojíte na rozcestí, chcete doleva či doprava? L/R: ")    
    if rozcesti == "L":
        finch = input("Chytil tě školník Finch..., chceš na něj použít Avada Kedavra? A/N: ")
        if finch == "A":
            print("Netrefils a jdeš do Azkabanu :( GAME OVER. ")
        else:
            print("Uff, přemohl ses a toho starýho bídáka si neodpálil, odvedl tě na pokoj do postele. Konec hry.")
    elif rozcesti == "R":
        schody = input("Došel si k pohybujícímu se schodišti, vlezeš na něj? A/N: ")
        if schody == "A":
            print("Schody se pod tebou propadly a zlomil sis všechny kosti v těle, skončils na ošetřovně... hra bude poračovat, až se zotavíš (cca za týden)")
        else:
            print("Vyměkls a dorazil si na ubikace do postele, kde už na tebe čekala nadrbaná Hermiona, rozumné rozhodnutí.")
        
        

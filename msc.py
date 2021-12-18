import requests
import json
import os

print("Minecraft Automatic Server Creator")
print("Made by alex.#0637")
while True:
    print("Select Type of server:")
    print("[1]Plugins - PaperMC(Recommended)")
    print("[2]Mods - Forge/Fabric")
    print("[3]Vanilla")
    stype = input("Select a number: ")

    if(stype=="1"):
        pvurl = "https://papermc.io/api/v2/projects/paper/"
        json1 = requests.get(pvurl)
        json1 = json1.text
        y = json.loads(json1)
        vll = len(y["versions"])
        nnv = vll - 1
        nv= y["versions"][nnv]
        vexist = False
        pblurl=None
        while True:
            print("Warning PaperMC versions below 1.17 are considered legacy versions and not guranted to work. You will not recive support for these versions from the PaperMC team!")
            print("Type version: ")
            pversion =input("1.8.8-"+nv+": ")
            for version in y["versions"]:
                if version == pversion:
                    pblurl = "https://papermc.io/api/v2/projects/paper/versions/" + pversion
                    break
            if pblurl: break    
            else:
                print("This version doesn't exist or doesnt support PaperMC!")
                vlist = input("Do you want to list all supported versions?[y/n]")
                if vlist.lower() == "y":
                    print(y["versions"])
        
        json2 = requests.get(pblurl)
        json2 = json2.text
        z = json.loads(json2)
        bll = len(z["builds"])
        nnb = bll - 1
        nb = z["builds"][nnb]
        pburl = None
        while True:
            pbuild =input("Type build leave blank for newest build("+str(nb)+"): ")
            if not pbuild: pbuild=str(nb)
            for build in z["builds"]:
                if str(build) == pbuild:
                    pburl = "https://papermc.io/api/v2/projects/paper/versions/"+pversion+"/builds/"+str(pbuild)+"/downloads/"
                    break
            if pburl:break
            else:
                print("This build doesn't exist!")
                blist = input("Do you want to list all builds for this version?[y/n]")
                if blist == "y":
                    print(z["builds"])
        
        
        djar = "paper-"+str(pversion)+"-"+str(pbuild)+".jar"
        pdurl = pburl + djar
        print("Downloading server jar...")
        pdown = requests.get(pdurl, stream=True,allow_redirects=True)
        open(djar,"wb").write(pdown.content)
    
        break
        
    elif(stype=="2"):
        print("Coming Soon!")
        

    elif(stype=="3"):
        vvurl = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
        json3 = requests.get(vvurl)
        json3 = json3.text
        x = json.loads(json3)
        vvl = x["versions"]
        vdurl = None
        while True:
            iv = input("Type version: ")
            for i in vvl:
                if i["id"] == iv:
                    vdurl=i['url']
            if vdurl:
                break
            else: print("This Version doesn't exist")          
    
        json4 = requests.get(vdurl)
        json4 = json4.text
        a = json.loads(json4)
        durl = a["downloads"]["server"]["url"]
        print("Downloading server jar...")
        vdown = requests.get(durl, stream=True,allow_redirects=True)
        open("server.jar","wb").write(vdown.content)
        print("Downloaded server jar!")
        break
if stype == "1":
    try:
        os.rename(djar, "server.jar")
        print("Downloaded server jar!")
    except FileExistsError:
        print("Server jar already Exists!")
        print("Removing existing server jar file!")
        os.remove("server.jar")
        os.rename(djar, "server.jar")
        print('Done donwloading and replacing server jar!')
startbat = open("run.bat","w")
print("For vanilla and small plugin servers 2GB is good enough")
while True:
    ram = input("Type how many GB of ram to allocate: ")
    try: 
        ram = int(ram)
        if ram > 0:
            break
        elif ram <= 0:
            print("Please type a number over 0!")  
    except: 
        print("Please type a number over 0!")
ram = str(ram)
startbat.write("java -Xmx"+ram+"G -Xms"+ram+"G -jar server.jar nogui")  
startbat.write("\nPAUSE")
startbat.close()
print("Do you agree to mojang's EULA (https://account.mojang.com/documents/minecraft_eula)")
while True:
    ia = input("[y/n]")
    if ia.lower() == "n":
        print("Can't create server without aggreing to the EULA!")
        os.remove("server.jar")
        os.remove("run.bat")
        input()
        exit()
    if ia.lower() == "y":
        eula = open("eula.txt","w")
        eula.write("eula=true")
        break
while True:
    crack = input("Do you want the server to be cracked?[y/n]")
    crack = crack.lower()
    if crack == "y":
        crack = "false"
        break
    elif crack == "n":
        crack = "true"
        break
port = None
while  True:
    port = input("What port do you want the server to run on?(leave blank for default port): ")
    if not port:
        port = "25565" 
        break
    try: 
        port = int(port)
    except:
        print("Port has to be a number!")
    if port != int or port > 65535: 
        print("Invalid port!")
    else:break 
sproperties = open("server.properties","w")
sproperties.write("online-mode="+crack+"\nserver-port="+port)
print("Server creation complete start server by opening run.bat!")
input()




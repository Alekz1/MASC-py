import requests
import json
import os

print("Basic Minecraft Automatic Server Creator")
print("Made by alex.#0637")
while True:
    print("Select Type of server:")
    print("[1]Plugins - PaperMC")
    print("[2]Mods - Forge/Fabric")
    print("[3]Vanilla")
    stype = input("Select a number: ")

    if(stype=="1"):
        pvurl = "https://papermc.io/api/v2/projects/paper/"
        json1 = requests.get(pvurl)
        json1 = json1.text
        y = json.loads(json1)
        print(y)
        vll = len(y["versions"])
        nnv = vll - 1
        nv= y["versions"][nnv]
        print("Type version: ")
        pversion =input("1.8.8-"+nv+": ")
        
        pblurl = "https://papermc.io/api/v2/projects/paper/versions/" + pversion
        json2 = requests.get(pblurl)
        json2 = json2.text
        z = json.loads(json2)
        bll = len(z["builds"])
        nnb = bll - 1
        nb = z["builds"][nnb]
        pbuild =input("Type build leave blank for newest: ")
        if not pbuild: pbuild=nb
        pburl = "https://papermc.io/api/v2/projects/paper/versions/"+pversion+"/builds/"+str(pbuild)+"/downloads/"
        print(pburl)
        djar = "paper-"+str(pversion)+"-"+str(pbuild)+".jar"
        pdurl = pburl + djar
        print(pdurl)
        pdown = requests.get(pdurl, stream=True,allow_redirects=True)
        open(djar,"wb").write(pdown.content)
    elif(stype=="2"):
        print("Coming Soon!")
        

    elif(stype=="3"):
        vvurl = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
        json3 = requests.get(vvurl)
        json3 = json3.text
        x = json.loads(json3)
        vvl = x["versions"]
        print(vvl)
        iv = input("Type version: ")
        for i in vvl:
            if i["id"] == iv:
                vdurl=i['url']
        json4 = requests.get(vdurl)
        json4 = json4.text
        a = json.loads(json4)
        durl = a["downloads"]["server"]["url"]
        vdown = requests.get(durl, stream=True,allow_redirects=True)
        open("server.jar","wb").write(vdown.content)
        
        



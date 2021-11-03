import json
import requests

f=open('api-all.json')

data=json.load(f)

cantPaths=0
cantEPs=0

for i in data:
    print (i['id'])
    cantPaths+=1
    count = 0

    ep=requests.get('https://api-dev.goorange.sixt.com/v1/docs/'+i['id'])
    try:
        for j in ep.json()['paths']:
            print(j)

            cantEPs +=1
            count +=1
        print ("Endpoints available: " + str(count))
    except:
        print ('no endpoints available')
    
f.close()
print ('[+] Cantidad de Paths = ' + str(cantPaths))
print ('[+] Cantidad de EPs = ' + str(cantEPs))

import http.client
import json
import csv
import sys

"""import sys, os
#sys.path.insert(0, "C:/Users/maria/OneDrive/Documentos/GitHub/TP2_AD-Django") # /home/projects/my-djproj

#sys.path.insert(0, 'C:/Users/maria/OneDrive/Documentos/GitHub/TP2_AD-Django/tp2')
import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings')

import django
django.setup()"""
def get(conn, req):
    conn.request("GET", req)
    return conn.getresponse()

conn = http.client.HTTPConnection("127.0.0.1",8000)
headers = {'Content-type': 'application/json'}

conn.request("GET", '/medicamentos/', headers=headers)
data = conn.getresponse()
mydata=data.read()
#print(mydata)
mydata=json.loads(mydata)

for obj in mydata:
    conn = http.client.HTTPConnection("127.0.0.1", 8000)
    print(obj)
    stock = {
        'farmaco': obj['id'],
        'quant':505
    }
    conn.request("POST", '/stock_med/', json.dumps(stock), headers=headers)
    r = conn.getresponse()
    #print(r.status, r.reason, r.read())
    if r.status == 400: #se der erro
        conn = http.client.HTTPConnection("127.0.0.1", 8000)
        conn.request("GET", f"/stockmed/?med={obj['id']}", json.dumps(stock), headers=headers)
        r = conn.getresponse()
        if r.status == 200: #se der erro
            info_stock = json.loads(r.read())

            if len(info_stock) == 1:
                stock = {
                    'farmaco': obj['id'],
                    'quant': 45,
                }
                conn.request("PUT", f"/stock_med/{info_stock[0]['id']}/", json.dumps(stock), headers=headers)
                r = conn.getresponse()
                if r.status != 200:
                    print(r.status, r.reason, r.read())
            else:
                print(f"ERRO farmaco {obj['id']} sem stock")
#
# stock = {
#     'farmaco': 1,
#     'id': 1,
#     'quant': 40
# }
# conn.request("PUT", '/stock_med/', json.dumps(stock), headers=headers)
# r = conn.getresponse()
# print(r.status, r.reason, r.read())
# sys.exit(0)
import http.client
import json
import csv

def get(conn, req):
    conn.request("GET", req)
    return conn.getresponse()

conn = http.client.HTTPConnection("127.0.0.1",8000)
headers = {'Content-type': 'application/json'}
f = open(r'C:\Users\user\Downloads\tp2ad\tp2ad\loads\farmaceuticos.csv', encoding='latin-1')
csvr = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_ALL)

for index,u in enumerate(csvr):
    ut = {
            'username': 'farm'+str(index),
            'password': 'pbkdf2_sha256$320000$Y0q1kt8tr2Hxkh9Msd1QV9$q4rvnr60qBtLogt8MgsGLWDnQ5716PeMrBIUFSvd2Y8=',
            'nome': u['Nome'],
            'bi': u['BI'],
            'NIF': u['NIF'],
            'morada': u['Morada'],
            'codigo_postal': u['Codigo postal']
        }
    conn.request("POST", '/farmaceuticos/', json.dumps(ut), headers=headers)
    r = conn.getresponse()
    #print(r.status, r.reason, r.read())
    conn2 = http.client.HTTPConnection("127.0.0.1", 8000)
    grupo = r.read()
    grupo = json.loads(grupo)
    print(grupo)
    conn2.request("GET", f"/addgroup/{grupo['id']}/4/")
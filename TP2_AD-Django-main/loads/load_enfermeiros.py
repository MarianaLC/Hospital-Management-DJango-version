import http.client
import json
import csv

def get(conn, req):
    conn.request("GET", req)
    return conn.getresponse()

conn = http.client.HTTPConnection("127.0.0.1",8000)
headers = {'Content-type': 'application/json'}
f = open(r'C:\Users\user\Downloads\tp2ad\tp2ad\loads\enfermeiros.csv', encoding='latin-1')
csvr = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_ALL)

for index, m in enumerate(csvr):
    md = {
            'username': 'enf'+str(index),
            'password': 'pbkdf2_sha256$320000$Y0q1kt8tr2Hxkh9Msd1QV9$q4rvnr60qBtLogt8MgsGLWDnQ5716PeMrBIUFSvd2Y8=',
            'nome': m['Nome'],
            'bi': m['BI'],
            'NIF': m['NIF'],
            'morada': m['Morada'],
            'codigo_postal': m['Codigo postal'],
            'especialidade': m['Especialidade']
        }
    conn.request("POST", '/enfermeiros/', json.dumps(md), headers=headers)
    r = conn.getresponse()
    #print(r.status, r.reason, r.read())
    conn2 = http.client.HTTPConnection("127.0.0.1", 8000)
    grupo = r.read()
    grupo = json.loads(grupo)
    print(grupo)
    conn2.request("GET", f"/addgroup/{grupo['id']}/2/")
import http.client
import json
import csv
def get(conn, req):
    conn.request("GET", req)
    return conn.getresponse()

conn = http.client.HTTPConnection("127.0.0.1",8000)
headers = {'Content-type': 'application/json'}
f= open(r'C:\Users\user\Downloads\Hospital\TP2_AD-Django-main\loads\outrosartigos1.csv', encoding='latin-1')
csvr = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_ALL)
for o in csvr:
    data = {
        "nome_artigo": o['Nome Artigo'],
        "fornecedor": o['Titular AIM']
    }
    conn.request("POST", '/outroartigos/', json.dumps(data), headers=headers)
    r = conn.getresponse()
    print(r.status, r.reason, r.read())

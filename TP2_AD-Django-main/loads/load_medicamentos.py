import http.client
import json
import csv
import sys


def get(conn, req):
    conn.request("GET", req)
    return conn.getresponse()

conn = http.client.HTTPConnection("127.0.0.1",8000)
headers = {'Content-type': 'application/json'}
#f= open(r'C:\Users\user\Downloads\Hospital\TP2_AD-Django-main\loads\lista_infomed.csv', encoding='latin-1')
f= open(r'C:\Users\user\Downloads\TP2_AD-Django-main (1)\TP2_AD-Django-main\loads\lista_infomed.csv', encoding='latin-1')
csvr = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_ALL)
i=0
for l in csvr:
    i+=1
    if i > 100:
        sys.exit(0)
    data = {
        "dci": l['DCI / Nome Genérico'],
        "nome_medicamento": l['Nome do Medicamento'],
        "forma_farmaceutica": l['Forma Farmacêutica'],
        "dosagem": l['Dosagem'],
        "titular_AIM": l['Titular de AIM']

    }
    if l['Estado de Autorização'] == 'Autorizado':
        data["estado_autorizacao"] = True
    else:
        data["estado_autorizacao"] = False
    if l['Genérico'] == 'N':
        data['generico'] = False
    else:
        data['generico'] = True
    conn.request("POST", '/medicamentos/', json.dumps(data), headers=headers)
    r = conn.getresponse()
    print(r.status, r.reason, r.read())

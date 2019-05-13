import psutil
import json

processo = int(input('Digite o PID do processo:'))

def imprimir_processo(processo):
    p = psutil.Process(processo)
    conn = p.connections()
    print(json.dumps(conn, indent=4, sort_keys=True))
    
imprimir_processo(processo)
import psutil
import time
import json

nomes = []
def imprimir_redes(nomes):
    io_status = psutil.net_io_counters(pernic=True)
    for i in io_status:
        nomes.append(str(i))
    for j in nomes:
        textoa = j,"\t"+str(io_status[j])
        print(json.dumps(textoa, indent=4, sort_keys=True))
    for i in range(4):
        time.sleep(1)
        io_status = psutil.net_io_counters(pernic=True)
    for j in nomes:
        textoc = j,"\t"+str(io_status[j])
        print(json.dumps(textoc, indent=4, sort_keys=True))

imprimir_redes(nomes)
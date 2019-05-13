import psutil
import netifaces
import json

def imprimir_dados_da_rede():
    ip = psutil.net_if_addrs()['Ethernet'][1][1]
    mask = psutil.net_if_addrs()['Ethernet'][1][2]
    get_gateway = netifaces.gateways()
    gateway = get_gateway['default'][netifaces.AF_INET][0]
    texto = 'IP: '+ str(ip),'Gateway: ' + str(gateway),'Mascara: ' + str(mask)
    print(json.dumps(texto, indent=4, sort_keys=True))
    
imprimir_dados_da_rede()
# Variables con las distancias administrativas de los protocolos
OSPF = 110
RIP = 120
EIGRP = 90
BGP = 20

# Solicitar al usuario el nombre del protocolo
protocolo = input("Ingrese el nombre del protocolo (OSPF, RIP, EIGRP, BGP): ").upper()

# Usar condicionales if/elif/else para verificar el protocolo
if protocolo == "OSPF":
    print(f"La distancia administrativa de OSPF es {OSPF}.")
elif protocolo == "RIP":
    print(f"La distancia administrativa de RIP es {RIP}.")
elif protocolo == "EIGRP":
    print(f"La distancia administrativa de EIGRP es {EIGRP}.")
elif protocolo == "BGP":
    print(f"La distancia administrativa de BGP es {BGP}.")
else:
    print("Protocolo no reconocido. Por favor, ingrese uno de los siguientes: OSPF, RIP, EIGRP, BGP.")

# Simple packet simulator that produces JSON objects representing packets.
import random, time
from datetime import datetime

PROTOCOLS = ['TCP','UDP','ICMP','ARP','HTTP','DNS']
IP_POOL = ['192.168.1.'+str(i) for i in range(2,50)] + ['10.0.0.'+str(i) for i in range(2,50)]

def generate_packet(idx:int):
    src = random.choice(IP_POOL)
    dst = random.choice([ip for ip in IP_POOL if ip!=src])
    proto = random.choices(PROTOCOLS, weights=[40,30,5,2,15,8])[0]
    size = random.randint(40,1500)
    ts = datetime.utcnow().isoformat() + 'Z'
    return {'id': idx, 'timestamp': ts, 'src': src, 'dst': dst, 'proto': proto, 'size': size}

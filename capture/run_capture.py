# Simulated packet capture utility.
import argparse, random, json, time
from datetime import datetime
from capture.simulator import generate_packet

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--outfile', default='data/packets.json')
    p.add_argument('--count', type=int, default=100)
    args = p.parse_args()

    packets = []
    for i in range(args.count):
        packets.append(generate_packet(i))
        if i % 20 == 0:
            time.sleep(0.01)
    # ensure data directory exists
    import os
    os.makedirs('data', exist_ok=True)
    with open(args.outfile, 'w') as f:
        json.dump(packets, f, indent=2)
    print('Saved', len(packets), 'packets to', args.outfile)

if __name__ == '__main__':
    main()

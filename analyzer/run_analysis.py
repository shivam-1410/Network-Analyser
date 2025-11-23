# Simple analysis driver
import argparse, json
from analyzer.core import analyze_packets

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--infile', default='data/packets.json')
    p.add_argument('--outfile', default='data/summary.json')
    args = p.parse_args()
    with open(args.infile) as f:
        packets = json.load(f)
    summary = analyze_packets(packets)
    with open(args.outfile,'w') as f:
        json.dump(summary, f, indent=2)
    print('Wrote summary to', args.outfile)

if __name__ == '__main__':
    main()

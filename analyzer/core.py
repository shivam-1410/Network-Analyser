# Core analysis functions: compute top talkers, protocol distribution, byte counts
from collections import Counter, defaultdict

def analyze_packets(packets):
    total = len(packets)
    protocols = Counter(p['proto'] for p in packets)
    by_src = Counter(p['src'] for p in packets)
    by_dst = Counter(p['dst'] for p in packets)
    bytes_per_proto = defaultdict(int)
    for p in packets:
        bytes_per_proto[p['proto']] += p.get('size',0)

    top_src = by_src.most_common(10)
    top_dst = by_dst.most_common(10)
    proto_dist = protocols.most_common()
    total_bytes = sum(bytes_per_proto.values())
    return {
        'total_packets': total,
        'total_bytes': total_bytes,
        'protocol_distribution': proto_dist,
        'top_src': top_src,
        'top_dst': top_dst,
        'bytes_per_proto': dict(bytes_per_proto)
    }

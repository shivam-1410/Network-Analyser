from analyzer.core import analyze_packets

def test_analyze_empty():
    res = analyze_packets([])
    assert res['total_packets'] == 0
    assert res['total_bytes'] == 0

def test_analyze_sample():
    pkts = [
        {'id':1,'src':'1.1.1.1','dst':'2.2.2.2','proto':'TCP','size':100},
        {'id':2,'src':'1.1.1.1','dst':'3.3.3.3','proto':'UDP','size':200},
    ]
    res = analyze_packets(pkts)
    assert res['total_packets'] == 2
    assert res['total_bytes'] == 300

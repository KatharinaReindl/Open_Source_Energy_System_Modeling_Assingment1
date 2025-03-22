from Pv_power import area,numbers,pv_power,feed

def test_area():
    assert area(4,5)==20

def test_numbers():
    assert numbers(20,3) == 6

def test_pv_power():
    assert pv_power(6,400) == 2400

def test_feed():
    assert feed(7,10) == 3
    assert feed(10,7) == 0        

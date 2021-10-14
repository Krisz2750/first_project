from fuggveny_defin import szumma, atlag, szoveg


def test_sum_numbers():
    result = szumma(2, 3)
    assert result == 5

def test_atlag_2():
    szamok = [2, 2, 2, 2, 2]
    result = atlag(szamok)
    assert result == 2

def test_atlag_4():
    szamok = [2, 4, 6, 4 ]
    result = atlag(szamok)
    assert result == 4

def szoveg_eleje():
    result = szoveg(" 343434 ")
    assert result == 2

def szoveg_sok():
    result = szoveg(" 3 4 3 4 3 4 ")
    assert result == 7
from ..Parser.shakespeare import ShakespeareParser

parser = ShakespeareParser()

def test_next_character_normal():
    test = "DUNCAN\tWhat bloody man is that? He can report,"
    assert parser._is_next_character(test) == True

def test_next_character_spaces():
    test = "MALCOLM\t                 This is the seargant"
    assert parser._is_next_character(test) == True

def test_next_character_act():
    test = "ACT II"
    assert parser._is_next_character(test) == False

def test_next_character_scene():
    test = "SCENE IV"
    assert parser._is_next_character(test) == False

def test_next_character_warbl():
    test = "fickenhitler"
    assert parser._is_next_character(test) == False



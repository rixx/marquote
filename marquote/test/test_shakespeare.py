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

def test_next_character_text():
    test = "\tIn thunder, lightning, or in rain?"
    assert parser._is_next_character(test) == False

def test_next_character_warbl():
    test = "fickenhitler"
    assert parser._is_next_character(test) == False

def test_next_character_empty():
    test = ""
    assert parser._is_next_character(test) == False


def test_is_text_normal():
    test = "\tIn thunder, lightning, or in rain?"
    assert parser._is_text(test) == True

def test_is_text_spaces():
    test = "\t        Upon the heath."
    assert parser._is_text(test) == True

def test_is_text_onlytab():
    test = "\t"
    assert parser._is_text(test) == False

def test_is_text_character():
    test = "DUNCAN\tWhat bloody man is that? He can report,"
    assert parser._is_text(test) == False

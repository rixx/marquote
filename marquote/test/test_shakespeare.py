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


def test_parse_play_line_regular_half_sentence():
    parser.sentences = []
    line = "When shall we three meet again"
    remainder = parser._parse_play_line(line, "First Witch", [])

    assert (remainder == line.lower().split()) \
            and (parser.sentences == [])

def test_parse_play_line_regular_one_sentence():
    parser.sentences = []
    line = "That will be ere the set of sun."
    remainder = parser._parse_play_line(line, "Third Witch", [])

    assert (remainder == []) and (len(parser.sentences) == 1) \
            and (parser.sentences[0].text == line[:-1].lower().split())

def test_parse_play_line_regular_two_sentences():
    parser.sentences = []
    line = "O valiant cousin! worthy gentleman!"
    remainder = parser._parse_play_line(line, "Seargant", [])

    assert (remainder == []) and (len(parser.sentences) == 2) \
            and (parser.sentences[1].text == ["o", "valiant", "cousin"]) \
            and (parser.sentences[0].text == ["worthy", "gentleman"])

def test_parse_play_line_regular_one_half_sentences():
    parser.sentences = []
    line = "What bloody man is that? He can report,"
    remainder = parser._parse_play_line(line, "DUNCAN", [])

    assert (remainder == ["he", "can", "report,"]) \
            and (len(parser.sentences) == 1) \
            and (parser.sentences[0].text == ["what", "bloody", "man", "is", "that"])

def test_parse_play_line_regular_aside_one_sentence():
    parser.sentences = []
    line = "[Aside] That will be ere the set of sun."
    remainder = parser._parse_play_line(line, "Third Witch", [])

    assert (remainder == []) and (len(parser.sentences) == 1) \
            and (parser.sentences[0].text == line[7:-1].lower().split())

def test_parse_play_line_remainder_half_sentence():
    parser.sentences = []
    line = "Who like a good and hardy soldier fought"
    r = ["this", "is", "the", "seargant"]
    remainder = parser._parse_play_line(line, "MALCOLM", r)

    assert (remainder == r + line.lower().split()) and (parser.sentences == [])

def test_parse_play_line_remainder_one_sentence():
    parser.sentences = []
    line = "in thunder, lightning, or in rain?"
    r = ["when", "shall", "we", "three", "meet", "again"]
    remainder = parser._parse_play_line(line, "First Witch", r)

    assert (remainder == []) and (len(parser.sentences) == 1) \
            and (parser.sentences[0].text == r + line[:-1].lower().split())

def test_parse_play_line_remainder_two_sentences():
    parser.sentences = []
    line = "'Gainst my captivity. Hail, brave friend!"
    r = ["who", "like", "a", "good", "and", "hardy", "soldier", "fought"]
    remainder = parser._parse_play_line(line, "MALCOLM", r)

    assert (remainder == []) and (len(parser.sentences) == 2) \
            and (parser.sentences[1].text == r + line[:20].lower().split()) \
            and (parser.sentences[0].text == line[22:-1].lower().split())


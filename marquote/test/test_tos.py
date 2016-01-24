def test_first():
    from ..chain import Chain
    from ..Backend.mysqlbackend import SQLBackend

    chain = Chain(SQLBackend("mysql+mysqlconnector://marquote:marquote@localhost/marquote"))
    print(chain.get("TOS", character="Scott", lookahead=2))

    assert True

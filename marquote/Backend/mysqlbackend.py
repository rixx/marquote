import random
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SQLBackend():

    def __init__(self, connect_string):
        self.engine = create_engine(connect_string, echo=False)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.SENTENCE_START = '\r'
        self.SENTENCE_END = '\n'

    def get(self, start,  source, character):
        lookahead = len(start)
        session = self.Session()

        qry_dict = {'series': self._get_simple(session, Series, title=source)}

        if character:
            qry_dict['character'] = self._get_simple(session, Character, name=character)

        for i in range(len(start)):
            qry_dict['word' + str(i)] = self._get_simple(session, Word, word=start[i])

        attr = getattr(Sentence, "word" + str(lookahead if lookahead <= len(start) else len(start)) + "_id")

        results = session.query(func.sum(Sentence.count), attr).\
                group_by(attr).\
                filter_by(**qry_dict).all()

        if results:
            result = random.choice([val for cnt, val in results for i in range(int(cnt))])
            result = self._get_simple(session, Word, id=result).word
            return result
        else:
            return self.SENTENCE_END


    def put(self, sentence, source, character):
        session = self.Session()
        sentence.extend((None, None, None, None))

        for i in range(len(sentence) - 5):
            words = sentence[i:i+6]

            entry = self._get_sentence(session, words[0], words[1], words[2], words[3],\
                    words[4], words[5], source, character)

            session.add(entry)

            entry.count += 1

        session.commit()

    def _get_sentence(self, session, w0, w1, w2, w3, w4, w5, source, char):

        word0=self._get_simple(session, Word, word=w0)
        word1=self._get_simple(session, Word, word=w1)
        word2=self._get_simple(session, Word, word=w2)
        word3=self._get_simple(session, Word, word=w3)
        word4=self._get_simple(session, Word, word=w4)
        word5=self._get_simple(session, Word, word=w5)
        character=self._get_simple(session, Character, name=char)
        series=self._get_simple(session, Series, title=source)
        
        test = session.query(Sentence).filter_by(word0=word0, word1=word1, word2=word2, word3=word3, word4=word4, word5=word5, series=series, character=character).first()

        if not test:
            test = Sentence(word0=word0, word1=word1, word2=word2, \
                    word3=word3, word4=word4, word5=word5, \
                    character=character, series=series, count=0)

            session.add(test)
            session.commit()

        return test


    def _get_simple(self, session, model, **kwargs):
        instance = session.query(model).filter_by(**kwargs).first()

        if not instance:
            instance = model(**kwargs)
            session.add(instance)
            session.commit()

        return instance


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String(30))


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))


class Sentence(Base):
    __tablename__ = 'sentences'
    id = Column(Integer, primary_key=True)
    count = Column(Integer, default=0)
    word0_id = Column(Integer, ForeignKey('words.id'))
    word1_id = Column(Integer, ForeignKey('words.id'))
    word2_id = Column(Integer, ForeignKey('words.id'))
    word3_id = Column(Integer, ForeignKey('words.id'))
    word4_id = Column(Integer, ForeignKey('words.id'))
    word5_id = Column(Integer, ForeignKey('words.id'))
    char_id = Column(Integer, ForeignKey('characters.id'))
    series_id = Column(Integer, ForeignKey('series.id'))

    word0 = relationship("Word", foreign_keys=[word0_id])
    word1 = relationship("Word", foreign_keys=[word1_id])
    word2 = relationship("Word", foreign_keys=[word2_id])
    word3 = relationship("Word", foreign_keys=[word3_id])
    word4 = relationship("Word", foreign_keys=[word4_id])
    word5 = relationship("Word", foreign_keys=[word5_id])
    character = relationship("Character", foreign_keys=[char_id])
    series = relationship("Series", foreign_keys=[series_id])


class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    title = Column(String(30))

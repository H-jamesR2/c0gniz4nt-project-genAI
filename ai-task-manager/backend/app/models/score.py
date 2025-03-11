class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, index=True)
    score = Column(Integer)
    date = Column(Date)
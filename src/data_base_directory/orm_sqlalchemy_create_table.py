from sqlalchemy import create_engine, Integer, VARCHAR, \
    ForeignKey, Table, Column, MetaData

metadata = MetaData()
eng = create_engine('mysql+mysqlconnector://alfob:13losegu@192.168.1.111/Ball_Scoreboard_db')

players = Table('Players', metadata,
                Column('ID', Integer(), primary_key=True),
                Column('Name', VARCHAR(255), nullable=False, index=True)
                )

matches = Table('Matches', metadata,
                Column('ID', Integer(), primary_key=True),
                Column('Player1', Integer(), ForeignKey("Players.ID"), nullable=False),
                Column('Player2', Integer(), ForeignKey("Players.ID"), nullable=False),
                Column('Winner', Integer(), ForeignKey("Players.ID"), nullable=False)
                )

metadata.create_all(eng)

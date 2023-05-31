from sqlalchemy import create_engine, Integer, VARCHAR, \
    ForeignKey, Table, Column, MetaData

metadata = MetaData()

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

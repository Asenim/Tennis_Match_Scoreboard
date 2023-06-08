# Импорты типов и constraints для БД
from sqlalchemy import Integer, VARCHAR, \
    ForeignKey, Column, create_engine
# Импорт класса для наследования наших классов-таблиц и
# Session - служит для работы с БД
from sqlalchemy.orm import declarative_base, Session

# Импорт констант для подключения к базе данных
from config_env import SQL_DRIVER, DB_HOST, \
    DB_NAME, DB_PORT, DB_PASS, DB_USER

# ############################### #
#     Объекты для подключения     #
#     и работы с Базой Данных     #
# ############################### #

engine = create_engine(f'{SQL_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
session = Session(engine)
Base = declarative_base()

# ############################### #
#         Модели Таблиц           #
# ############################### #


class Players(Base):
    __tablename__ = "Players"

    ID = Column(Integer(), primary_key=True)
    Name = Column(VARCHAR(255), nullable=False, index=True)


class Matches(Base):
    __tablename__ = "Matches"

    ID = Column(Integer(), primary_key=True)
    Player1 = Column(Integer(), ForeignKey('Players.ID'), nullable=False)
    Player2 = Column(Integer(), ForeignKey('Players.ID'), nullable=False)
    Winner = Column(Integer(), ForeignKey('Players.ID'), nullable=False)

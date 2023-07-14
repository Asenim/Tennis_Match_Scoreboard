# Импорты типов и constraints для БД
from sqlalchemy import Integer, VARCHAR, \
    ForeignKey, Column, create_engine
# Импорт класса для наследования наших классов-таблиц и
# Класс Session - служит для работы с БД из других файлов
from sqlalchemy.orm import declarative_base, relationship, Session

# Импорт констант для подключения к базе данных
from config_env import SQL_DRIVER, DB_HOST, \
    DB_NAME, DB_PORT, DB_PASS, DB_USER

# ############################### #
#     Объекты для подключения     #
#     и работы с Базой Данных     #
# ############################### #

engine = create_engine(f'{SQL_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
# Объект session будет создаваться  #
# каждый раз при обращении к БД     #
# в методах - сервисах приложения   #
# Пример: session = Session(bind=engine) #
Base = declarative_base()

# ############################### #
#         Модели Таблиц           #
# ############################### #


class Player(Base):
    __tablename__ = "Player"

    ID = Column(Integer(), primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(255), nullable=False, index=True, unique=True)


class Matche(Base):
    __tablename__ = "Matche"

    ID = Column(Integer(), primary_key=True, autoincrement=True)
    Player1 = Column(Integer(), ForeignKey('Player.ID', ondelete="CASCADE"), nullable=False)
    Player2 = Column(Integer(), ForeignKey('Player.ID', ondelete="CASCADE"), nullable=False)
    Winner = Column(Integer(), ForeignKey('Player.ID', ondelete="CASCADE"), nullable=False)

    player1 = relationship(
        "Player",
        foreign_keys=[Player1],
    )
    player2 = relationship(
        "Player",
        foreign_keys=[Player2],
    )
    winner = relationship(
        "Player",
        foreign_keys=[Winner],
    )

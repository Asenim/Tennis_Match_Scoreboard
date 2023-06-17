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


class Players(Base):
    __tablename__ = "Players"

    ID = Column(Integer(), primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(255), nullable=False, index=True)
    # matches = relationship(
    #     "Matches",
    #     back_populates="players",
    #     cascade="all, delete",
    #     passive_deletes=True
    # )


class Matches(Base):
    __tablename__ = "Matches"

    ID = Column(Integer(), primary_key=True, autoincrement=True)
    Player1 = Column(Integer(), ForeignKey('Players.ID', ondelete="CASCADE"), nullable=False)
    Player2 = Column(Integer(), ForeignKey('Players.ID', ondelete="CASCADE"), nullable=False)
    Winner = Column(Integer(), ForeignKey('Players.ID', ondelete="CASCADE"), nullable=False)

    players1 = relationship(
        "Players",
        foreign_keys=[Player1],
    )
    players2 = relationship(
        "Players",
        foreign_keys=[Player2],
    )
    winners = relationship(
        "Players",
        foreign_keys=[Winner],
    )

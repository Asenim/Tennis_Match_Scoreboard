from src.data_base_directory.db_schema_conf \
    import *


# players
def insert_players():
    """
    Функция будет добавлять игроков в таблицу players
    :return:
    """
    p1 = Players(
        Name='Ziya'
    )
    print(p1)
    print(p1.Name)
    session.add(p1)
    print(session.new)
    session.commit()


def delete_players():
    """
    Функция будет удалять игроков из таблицы players
    :return:
    """

    player = session.query(Players).filter(Players.ID == '1').one()
    session.delete(player)
    session.commit()


# matches
def insert_matches():
    """
    Функция добавляет результаты игры в таблицу matches
    :return:
    """
    pass


def delete_matches():
    """
    Функция удаляет данные из таблицы matches
    :return:
    """
    pass


# insert_players()
delete_players()

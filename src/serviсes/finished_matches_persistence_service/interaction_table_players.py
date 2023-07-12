from src.serviсes.finished_matches_persistence_service.interaction_table_ABS \
    import InteractionTable
from src.data_base_directory.db_schema_conf import *
import inspect


def foo():
    """
    Функция проверяющая  откуда вызван метод.
    """
    # возьми текущий фрейм объект (frame object)
    current_frame = inspect.currentframe()

    # получи фрейм объект, который его вызвал
    caller_frame = current_frame.f_back

    # возьми у вызвавшего фрейма исполняемый в нём объект типа "код" (code object)
    code_obj = caller_frame.f_code

    # и получи его имя
    code_obj_name = code_obj.co_name

    print("Имя вызывающего объекта: ", code_obj_name)


class InteractionTablePlayers(InteractionTable):
    @staticmethod
    def select_one_player(name):
        """
        Метод делает выборку из таблицы
        Players, для проверки того -
        существует ли игрок с таким именем
        в нашей таблице.
        Этот метод используется в связке
        с insert_one player.
        :param name: Имя игрока для выборки.
        :return True/False:
        """
        foo()
        session = Session(bind=engine)
        try:
            select_all_player = session.query(Players).all()

            for selected_player in select_all_player:
                if selected_player.Name == name:
                    print(selected_player.ID, selected_player.Name)
                    return selected_player

            return False

        except ConnectionError:
            print("Failed to connect to database")

        finally:
            session.close()
            print("Session closed!")

    # @staticmethod
    def insert_one_player(self, name):
        """
        Функция добавляет игроков в таблицу players
        :return:
        """
        session = Session(bind=engine)
        try:
            __player = Players(
                Name=name
            )
            if not self.select_one_player(name):
                session.add(__player)
                print(session.new)
                session.commit()
                print("Data added to db")
            else:
                print(f"This {__player.ID, __player.Name} is already in the database")

        except ConnectionError:
            print("Failed to connect to database")

        finally:
            session.close()
            print("Session closed!")

    # @staticmethod
    def delete_one_player(self, name=None, id=None):
        """
        Функция будет удалять игроков из таблицы players
        :return:
        """
        session = Session(bind=engine)
        try:
            if id is not None:
                __player = session.query(Players).filter(Players.ID == id).one()

                if self.select_one_player(__player.Name):
                    session.delete(__player)
                    session.commit()
                    print(f"Data {__player.ID, __player.Name} deleted!")
                else:
                    print('There are no players with this ID in the players table')
            else:
                __player = session.query(Players).filter(Players.Name == name).one()

                if self.select_one_player(__player.Name):
                    session.delete(__player)
                    session.commit()
                    print(f"Data {__player.ID, __player.Name} deleted!")
                else:
                    print('There are no players with this Name in the players table')

        except ConnectionError:
            print("Failed to connect to database")
        finally:
            session.close()
            print("Session closed!")


if "__main__" == __name__:
    foo()
    play = InteractionTablePlayers()
    print(play.select_one_player('Alfob'))
    # print(play.select_one_player('Sergey'))
    # print(play.select_one_player('Ichigo'))
    # print('-----')
    # print(play.select_one_player('Kiril'))
    # print(play.select_one_player('Seva'))
    play.insert_one_player('Alfob')
    # play.insert_one_player('Alsu')
    # play.insert_one_player('Pasha')
    # play.insert_one_player('Misha')
    # play.insert_one_player('Asta')
    # play.insert_one_player('Lina')
    # play.insert_one_player('Ichigo')
    # play.insert_one_player('Sergey')
    # play.delete_one_player(id=13)
    # play.delete_one_player(name='Ziya')
    # play.insert_one_player("Ziya")
    # play.delete_one_player(name="Ziya")

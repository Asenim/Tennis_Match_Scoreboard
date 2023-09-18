from src.services.finished_matches_persistence_service.interaction_table_players import InteractionTablePlayers


class OngoingMatchesService:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.interaction_table_players = InteractionTablePlayers()

    def insert_in_table_players(self):
        """
        Метод добавляет игроков в базу данных Players
        :return:
        """
        self.interaction_table_players.insert_one_player(self.player_1)
        self.interaction_table_players.insert_one_player(self.player_2)

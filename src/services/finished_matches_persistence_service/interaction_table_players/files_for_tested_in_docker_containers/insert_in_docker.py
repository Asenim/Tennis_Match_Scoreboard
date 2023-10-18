from src.services.finished_matches_persistence_service.interaction_table_players.interaction_table_players \
    import InteractionTablePlayers


if "__main__" == __name__:
    play = InteractionTablePlayers()
    play.insert_one_player_and_return_player_object('Alfob')
    play.insert_one_player_and_return_player_object('Sergey')
    play.insert_one_player_and_return_player_object('Alsu')
    play.insert_one_player_and_return_player_object('Ziya')

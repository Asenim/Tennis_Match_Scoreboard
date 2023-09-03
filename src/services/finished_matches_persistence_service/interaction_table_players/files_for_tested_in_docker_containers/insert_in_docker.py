from src.services.finished_matches_persistence_service.interaction_table_players.interaction_table_players \
    import InteractionTablePlayers


if "__main__" == __name__:
    play = InteractionTablePlayers()
    play.insert_one_player('Alfob')
    play.insert_one_player('Sergey')
    play.insert_one_player('Alsu')
    play.insert_one_player('Ziya')

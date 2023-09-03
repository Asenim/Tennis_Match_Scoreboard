from src.services.finished_matches_persistence_service.interaction_table_players.interaction_table_players \
    import InteractionTablePlayers

if "__main__" == __name__:
    play = InteractionTablePlayers()
    play.delete_one_player(name='Alfob')

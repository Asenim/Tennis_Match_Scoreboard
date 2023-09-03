from src.services.finished_matches_persistence_service.interaction_table_players.select_table_players \
    import SelectInteractionTablePlayers

if "__main__" == __name__:
    select_all_player = SelectInteractionTablePlayers()
    select_all_player.select_all()

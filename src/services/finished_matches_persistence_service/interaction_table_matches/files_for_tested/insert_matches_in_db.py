from src.services.finished_matches_persistence_service.interaction_table_matches.insert_table_matches \
    import InsertTableMatches


if "__main__" == __name__:
    match_insert = InsertTableMatches()
    match_insert.insert_matches(2, 3, 3)
    match_insert.insert_matches(4, 5, 4)

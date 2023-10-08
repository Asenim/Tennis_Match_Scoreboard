import json


class ObjectToJsonToDB:
    def __init__(self, object_player_1, object_player_2):
        self.object_player_1 = object_player_1
        self.object_player_2 = object_player_2

    def object_to_json(self):
        data_players_score = {'player_1': self.object_player_1.__dict__,
                              'player_2': self.object_player_2.__dict__}

        dict_to_json_players_score = json.dumps(data_players_score)
        return dict_to_json_players_score

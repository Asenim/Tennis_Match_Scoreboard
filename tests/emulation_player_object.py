class EmulationPlayerObject:
    def __init__(self, id_int, name):
        """
        Класс занимается имитацией объектов моделей БД
        :param id_int: ID игрока
        :param name: Имя игрока
        """
        self.ID = id_int
        self.Name = name

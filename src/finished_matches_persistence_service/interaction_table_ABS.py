class InteractionTable:
    @staticmethod
    def output_console_list_result(list_output):
        """
        Метод позволяет выводить в консоль информацию
        о всех выборках.
        :param list_output: параметр принимает в себя
        список с результатами выборки.
        """
        for item in list_output:
            print(*item)

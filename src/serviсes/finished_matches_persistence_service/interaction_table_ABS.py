class InteractionTable:
    @staticmethod
    def output_console_list_result(output_list_name, list_output):
        """
        Метод позволяет выводить в консоль информацию
        о всех выборках.
        :param output_list_name: Параметр принимает в себя
        строку с именем списка который будет выводиться на
        экран.
        :param list_output: Параметр принимает в себя
        список с результатами выборки.
        """
        print(f"---{output_list_name}---")

        for item in list_output:
            print(*item)

    # def sort_all_item_in_list(self, sortable_list):
    #     sorted_list = []
    #
    #
    #
    #     return sorted_list

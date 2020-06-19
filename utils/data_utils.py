class DataUtils:

    @staticmethod
    def parse_arr_data_to_clear_str_data(array_data: []) -> str:
        return str(array_data).replace(' ', '').replace(',', '').replace('[', '').replace(']', '').replace('\'', '')

    @staticmethod
    def parse_arr_data_to_comma_str_data(array_data: []) -> str:
        return str(array_data).replace(' ', '').replace('],', ',').replace('[', '').replace(']', '').replace('\'', '')

import re

from model.question_data import QuestionData
from service.rule_base import RuleBase


# 公式检查，对某两个单元格中的数值进行公式关系计算比较，满足公式关系返回true，否则返回false
# 使用cell_value(x,y)的格式进行取单元格数值，举例：cell_value(1,3) * 2 == cell_value(1,4)
class RuleFormulaCheck(RuleBase):
    formula_str = ''
    cell_list = []

    # 使用cell_value(x,y)的格式进行取单元格数值，举例：cell_value(1,3) * 2 == cell_value(1,4)
    def cell_value(self, x: int, y: int) -> float:
        result_value = self.question_data.calculate_data[y][x]
        return 0.0 if result_value == '' else float(result_value)

    def __init__(self, question_data: QuestionData, params: str) -> None:
        super().__init__(question_data, params)
        self.formula_str = params
        self.cell_list = []
        for item in re.finditer("cell_value[(]\d+,\d+", params):
            this_location_str = item.group().replace('cell_value(', '').replace(',', '-')
            self.question_data.rules_relation_map[this_location_str].append(self)
            item_str = this_location_str.split('-')
            cell_location_item = [int(item_str[0]), int(item_str[1])]
            if cell_location_item not in self.cell_list:
                self.cell_list.append(cell_location_item)

    def check(self) -> bool:
        for cell_location in self.cell_list:
            if self.question_data.calculate_data[cell_location[1]][cell_location[0]] == '':
                return True
        try:
            result = eval(self.formula_str, {'cell_value': self.cell_value})
            return result
        except ZeroDivisionError:
            return False

    def filter_candidate_data(self) -> int:
        super().filter_candidate_data()
        return 0

    def get_rule_data_str(self) -> str:
        return self.formula_str

    def get_rule_parameters_str(self) -> str:
        return ''

    def get_rule_name_str(self) -> str:
        return 'FORMULA_CHECK'

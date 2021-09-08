from service.resolver_base import ResolverBase
from service.rule_formula_check import RuleFormulaCheck
from service.rule_item_mutex import RuleItemMutex


# 六宫摩天楼
class Resolver1662(ResolverBase):
    ANSWER_RANGE = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def get_answer_range(self) -> []:
        return Resolver1662.ANSWER_RANGE

    def calculate_rules(self):
        super().calculate_rules()
        self.question_data.rules_list = [
            RuleItemMutex(self.question_data, '0,0;0,1;0,2;0,3;0,4;0,5'),
            RuleItemMutex(self.question_data, '1,0;1,1;1,2;1,3;1,4;1,5'),
            RuleItemMutex(self.question_data, '2,0;2,1;2,2;2,3;2,4;2,5'),
            RuleItemMutex(self.question_data, '3,0;3,1;3,2;3,3;3,4;3,5'),
            RuleItemMutex(self.question_data, '4,0;4,1;4,2;4,3;4,4;4,5'),
            RuleItemMutex(self.question_data, '5,0;5,1;5,2;5,3;5,4;5,5'),

            RuleItemMutex(self.question_data, '0,0;1,0;2,0;3,0;4,0;5,0'),
            RuleItemMutex(self.question_data, '0,1;1,1;2,1;3,1;4,1;5,1'),
            RuleItemMutex(self.question_data, '0,2;1,2;2,2;3,2;4,2;5,2'),
            RuleItemMutex(self.question_data, '0,3;1,3;2,3;3,3;4,3;5,3'),
            RuleItemMutex(self.question_data, '0,4;1,4;2,4;3,4;4,4;5,4'),
            RuleItemMutex(self.question_data, '0,5;1,5;2,5;3,5;4,5;5,5'),

            RuleItemMutex(self.question_data, '0,0;1,0;2,0;0,1;1,1;2,1'),
            RuleItemMutex(self.question_data, '3,0;4,0;5,0;3,1;4,1;5,1'),
            RuleItemMutex(self.question_data, '0,2;1,2;2,2;0,3;1,3;2,3'),
            RuleItemMutex(self.question_data, '3,2;4,2;5,2;3,3;4,3;5,3'),
            RuleItemMutex(self.question_data, '0,4;1,4;2,4;0,5;1,5;2,5'),
            RuleItemMutex(self.question_data, '3,4;4,4;5,4;3,5;4,5;5,5'),
        ]
        # 读取Excel中所有DBG函数，生成奇数灰格子的互斥规则
        for draw_function_data in self.question_data.draw_function_list:
            if draw_function_data.function_name == 'DOE':
                index = 0
                for location_tag in draw_function_data.data.split(','):
                    if locoation_tag is not '0':
                        cell_list = []
                        if draw_function_data.parameters[0] is 'T':
                            for i in range(self.question_data.dimensionY):
                                cell_list.append('cell_value(' + str(index) + ',' + str(i) + ')')
                        if draw_function_data.parameters[0] is 'B':
                            for i in range(self.question_data.dimensionY - 1, -1, -1):
                                cell_list.append('cell_value(' + str(index) + ',' + str(i) + ')')
                        if draw_function_data.parameters[0] is 'L':
                            for i in range(self.question_data.dimensionX):
                                cell_list.append('cell_value(' + str(i) + ',' + str(index) + ')')
                        if draw_function_data.parameters[0] is 'R':
                            for i in range(self.question_data.dimensionX - 1, -1, -1):
                                cell_list.append('cell_value(' + str(i) + ',' + str(index) + ')')
                        rule_str = 'calculate_max_count([' + ','.join(cell_list) + ']) == ' + location_tag
                        self.question_data.rules_list.append(RuleFormulaCheck(self.question_data, rule_str))
                    index = index + 1

    def calculate_editable_original_data(self):
        super().calculate_editable_original_data()
        for y_index in range(len(self.question_data.editable_original_data)):
            for x_index in range(len(self.question_data.editable_original_data[y_index])):
                if self.question_data.editable_original_data[y_index][x_index] == '':
                    self.question_data.editable_original_data[y_index][x_index] = '#'

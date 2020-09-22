from service.resolver_base import ResolverBase
from service.rule_formula_check import RuleFormulaCheck
from service.rule_item_mutex import RuleItemMutex


# 九宫X和数独
class Resolver1964(ResolverBase):
    ANSWER_RANGE = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def get_answer_range(self) -> []:
        return Resolver1964.ANSWER_RANGE

    def calculate_rules(self):
        super().calculate_rules()
        self.question_data.rules_list = [
            RuleItemMutex(self.question_data, '0,0;0,1;0,2;0,3;0,4;0,5;0,6;0,7;0,8'),
            RuleItemMutex(self.question_data, '1,0;1,1;1,2;1,3;1,4;1,5;1,6;1,7;1,8'),
            RuleItemMutex(self.question_data, '2,0;2,1;2,2;2,3;2,4;2,5;2,6;2,7;2,8'),
            RuleItemMutex(self.question_data, '3,0;3,1;3,2;3,3;3,4;3,5;3,6;3,7;3,8'),
            RuleItemMutex(self.question_data, '4,0;4,1;4,2;4,3;4,4;4,5;4,6;4,7;4,8'),
            RuleItemMutex(self.question_data, '5,0;5,1;5,2;5,3;5,4;5,5;5,6;5,7;5,8'),
            RuleItemMutex(self.question_data, '6,0;6,1;6,2;6,3;6,4;6,5;6,6;6,7;6,8'),
            RuleItemMutex(self.question_data, '7,0;7,1;7,2;7,3;7,4;7,5;7,6;7,7;7,8'),
            RuleItemMutex(self.question_data, '8,0;8,1;8,2;8,3;8,4;8,5;8,6;8,7;8,8'),

            RuleItemMutex(self.question_data, '0,0;1,0;2,0;3,0;4,0;5,0;6,0;7,0;8,0'),
            RuleItemMutex(self.question_data, '0,1;1,1;2,1;3,1;4,1;5,1;6,1;7,1;8,1'),
            RuleItemMutex(self.question_data, '0,2;1,2;2,2;3,2;4,2;5,2;6,2;7,2;8,2'),
            RuleItemMutex(self.question_data, '0,3;1,3;2,3;3,3;4,3;5,3;6,3;7,3;8,3'),
            RuleItemMutex(self.question_data, '0,4;1,4;2,4;3,4;4,4;5,4;6,4;7,4;8,4'),
            RuleItemMutex(self.question_data, '0,5;1,5;2,5;3,5;4,5;5,5;6,5;7,5;8,5'),
            RuleItemMutex(self.question_data, '0,6;1,6;2,6;3,6;4,6;5,6;6,6;7,6;8,6'),
            RuleItemMutex(self.question_data, '0,7;1,7;2,7;3,7;4,7;5,7;6,7;7,7;8,7'),
            RuleItemMutex(self.question_data, '0,8;1,8;2,8;3,8;4,8;5,8;6,8;7,8;8,8'),

            RuleItemMutex(self.question_data, '0,0;0,1;0,2;1,0;1,1;1,2;2,0;2,1;2,2'),
            RuleItemMutex(self.question_data, '3,0;3,1;3,2;4,0;4,1;4,2;5,0;5,1;5,2'),
            RuleItemMutex(self.question_data, '6,0;6,1;6,2;7,0;7,1;7,2;8,0;8,1;8,2'),
            RuleItemMutex(self.question_data, '0,3;0,4;0,5;1,3;1,4;1,5;2,3;2,4;2,5'),
            RuleItemMutex(self.question_data, '3,3;3,4;3,5;4,3;4,4;4,5;5,3;5,4;5,5'),
            RuleItemMutex(self.question_data, '6,3;6,4;6,5;7,3;7,4;7,5;8,3;8,4;8,5'),
            RuleItemMutex(self.question_data, '0,6;0,7;0,8;1,6;1,7;1,8;2,6;2,7;2,8'),
            RuleItemMutex(self.question_data, '3,6;3,7;3,8;4,6;4,7;4,8;5,6;5,7;5,8'),
            RuleItemMutex(self.question_data, '6,6;6,7;6,8;7,6;7,7;7,8;8,6;8,7;8,8'),
        ]
        # 读取Excel中所有DBG函数，生成奇数灰格子的互斥规则
        for draw_function_data in self.question_data.draw_function_list:
            if draw_function_data.function_name == 'DOE':
                index = 0
                for location_tag in draw_function_data.data.split(','):
                    if location_tag is not '0':
                        cell_list = []
                        cell_count_formula = ''
                        if draw_function_data.parameters[0] is 'T':
                            cell_count_formula = 'cell_value(' + str(index) + ',0)'
                            for i in range(self.question_data.dimensionY):
                                cell_list.append('cell_value(' + str(index) + ',' + str(i) + ')')
                        if draw_function_data.parameters[0] is 'B':
                            cell_count_formula = 'cell_value(' + str(index) + ',' + str(self.question_data.dimensionY - 1) + ')'
                            for i in range(self.question_data.dimensionY - 1, -1, -1):
                                cell_list.append('cell_value(' + str(index) + ',' + str(i) + ')')
                        if draw_function_data.parameters[0] is 'L':
                            cell_count_formula = 'cell_value(0,' + str(index) + ')'
                            for i in range(self.question_data.dimensionX):
                                cell_list.append('cell_value(' + str(i) + ',' + str(index) + ')')
                        if draw_function_data.parameters[0] is 'R':
                            cell_count_formula = 'cell_value(' + str(self.question_data.dimensionX - 1) + ',' + str(index) + ')'
                            for i in range(self.question_data.dimensionX - 1, -1, -1):
                                cell_list.append('cell_value(' + str(i) + ',' + str(index) + ')')
                        rule_str = 'sum([' + ','.join(cell_list) + '][:int(' + cell_count_formula + ')]) == ' + location_tag
                        self.question_data.rules_list.append(RuleFormulaCheck(self.question_data, rule_str))
                    index = index + 1

    def calculate_editable_original_data(self):
        super().calculate_editable_original_data()
        for y_index in range(len(self.question_data.editable_original_data)):
            for x_index in range(len(self.question_data.editable_original_data[y_index])):
                if self.question_data.editable_original_data[y_index][x_index] == '':
                    self.question_data.editable_original_data[y_index][x_index] = '#'

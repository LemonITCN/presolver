from service.resolver_base import ResolverBase
from service.rule_formula_check import RuleFormulaCheck
from service.rule_item_mutex import RuleItemMutex


# 六宫加法数独
class Resolver1611(ResolverBase):
    ANSWER_RANGE = ['1', '2', '3', '4', '5', '6']

    def get_answer_range(self) -> []:
        return Resolver1611.ANSWER_RANGE

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
        for draw_function_data in self.question_data.draw_function_list:
            if (draw_function_data.data is None) | (draw_function_data.data == ''):
                continue
            if draw_function_data.function_name == 'DLE':
                relation_direction = draw_function_data.parameters[0]
                for param_group in draw_function_data.data.split(';'):
                    param_group_split = param_group.split(':')
                    if len(param_group_split) > 1:
                        for location_tag in param_group_split[0].split(','):
                            # 将单元格tag转换成坐标，如A3 -> 2,0
                            location = [int(location_tag[1]) - 1, ord(location_tag[0]) - 65]
                            cell1 = ''
                            cell2 = ''
                            if relation_direction == 'R':
                                cell1 = str(location[0]) + ',' + str(location[1])
                                cell2 = str(location[0] + 1) + ',' + str(location[1])
                            elif relation_direction == 'B':
                                cell1 = str(location[0]) + ',' + str(location[1])
                                cell2 = str(location[0]) + ',' + str(location[1] + 1)
                            rule_str = 'cell_value(' + cell1 + ') * cell_value(' + cell2 + ') == ' + param_group_split[
                                1]
                            self.question_data.rules_list.append(RuleFormulaCheck(self.question_data, rule_str))

    def calculate_editable_original_data(self):
        super().calculate_editable_original_data()
        for y_index in range(len(self.question_data.editable_original_data)):
            for x_index in range(len(self.question_data.editable_original_data[y_index])):
                if self.question_data.editable_original_data[y_index][x_index] == '':
                    self.question_data.editable_original_data[y_index][x_index] = '#'

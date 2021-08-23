from service.resolver_base import ResolverBase
from service.rule_item_mutex import RuleItemMutex


# 七宫不规则数独 七宫锯齿数独
class Resolver1752(ResolverBase):
    ANSWER_RANGE = ['1', '2', '3', '4', '5', '6', '7']

    def get_answer_range(self) -> []:
        return Resolver1752.ANSWER_RANGE

    def calculate_rules(self):
        super().calculate_rules()
        self.question_data.rules_list = [
            RuleItemMutex(self.question_data, '0,0;0,1;0,2;0,3;0,4;0,5;0,6'),
            RuleItemMutex(self.question_data, '1,0;1,1;1,2;1,3;1,4;1,5;1,6'),
            RuleItemMutex(self.question_data, '2,0;2,1;2,2;2,3;2,4;2,5;2,6'),
            RuleItemMutex(self.question_data, '3,0;3,1;3,2;3,3;3,4;3,5;3,6'),
            RuleItemMutex(self.question_data, '4,0;4,1;4,2;4,3;4,4;4,5;4,6'),
            RuleItemMutex(self.question_data, '5,0;5,1;5,2;5,3;5,4;5,5;5,6'),
            RuleItemMutex(self.question_data, '6,0;6,1;6,2;6,3;6,4;6,5;6,6'),

            RuleItemMutex(self.question_data, '0,0;1,0;2,0;3,0;4,0;5,0;6,0'),
            RuleItemMutex(self.question_data, '0,1;1,1;2,1;3,1;4,1;5,1;6,1'),
            RuleItemMutex(self.question_data, '0,2;1,2;2,2;3,2;4,2;5,2;6,2'),
            RuleItemMutex(self.question_data, '0,3;1,3;2,3;3,3;4,3;5,3;6,3'),
            RuleItemMutex(self.question_data, '0,4;1,4;2,4;3,4;4,4;5,4;6,4'),
            RuleItemMutex(self.question_data, '0,5;1,5;2,5;3,5;4,5;5,5;6,5'),
            RuleItemMutex(self.question_data, '0,6;1,6;2,6;3,6;4,6;5,6;6,6'),
        ]
        # 读取Excel中所有DBG函数，生成互斥规则
        for draw_function_data in self.question_data.draw_function_list:
            if draw_function_data.function_name == 'DMD':
                for location_group in draw_function_data.data.split(';'):
                    if location_group != '':
                        cells_list = []
                        for location_tag in location_group.split(':'):
                            if location_tag != '':
                                # 将单元格tag转换成坐标，如A3 -> 2,0
                                location = [int(location_tag[1]) - 1, ord(location_tag[0]) - 65]
                                cell = str(location[0]) + ',' + str(location[1])
                                cells_list.append(cell)
                                self.question_data.rules_list.append(RuleItemMutex(self.question_data, ';'.join(cells_list)))


    def calculate_editable_original_data(self):
        super().calculate_editable_original_data()
        for y_index in range(len(self.question_data.editable_original_data)):
            for x_index in range(len(self.question_data.editable_original_data[y_index])):
                if self.question_data.editable_original_data[y_index][x_index] == '':
                    self.question_data.editable_original_data[y_index][x_index] = '#'

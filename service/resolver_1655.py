from service.resolver_base import ResolverBase
from service.rule_item_mutex import RuleItemMutex


# 6宫同位数独
# DB 互斥规则已写入
class Resolver1655(ResolverBase):
    ANSWER_RANGE = ['1', '2', '3', '4', '5', '6']

    def get_answer_range(self) -> []:
        return Resolver1655.ANSWER_RANGE

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

        for y in range(2):
            for x in range(3):
                rule_str = ''
                for ys in [0, 2, 4]:
                    for xs in [0, 3]:
                        rule_str = rule_str + str(x + xs) + ',' + str(y + ys) + ';'
                self.question_data.rules_list.append(RuleItemMutex(self.question_data, rule_str))

    def calculate_editable_original_data(self):
        super().calculate_editable_original_data()
        for y_index in range(len(self.question_data.editable_original_data)):
            for x_index in range(len(self.question_data.editable_original_data[y_index])):
                if self.question_data.editable_original_data[y_index][x_index] == '':
                    self.question_data.editable_original_data[y_index][x_index] = '#'

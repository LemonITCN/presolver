from service.resolver_base import ResolverBase
from service.rule_item_mutex import RuleItemMutex


class Resolver1623(ResolverBase):
    ANSWER_RANGE = ['1', '2', '3', '4', '5', '6']

    def get_answer_range(self) -> []:
        return Resolver1623.ANSWER_RANGE

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

            # 1
            RuleItemMutex(self.question_data, '0,0;1,2'),
            RuleItemMutex(self.question_data, '0,1;1,3'),
            RuleItemMutex(self.question_data, '0,2;1,4'),
            RuleItemMutex(self.question_data, '0,3;1,5'),

            RuleItemMutex(self.question_data, '1,0;2,2'),
            RuleItemMutex(self.question_data, '1,1;2,3'),
            RuleItemMutex(self.question_data, '1,2;2,4'),
            RuleItemMutex(self.question_data, '1,3;2,5'),

            RuleItemMutex(self.question_data, '2,0;3,2'),
            RuleItemMutex(self.question_data, '2,1;3,3'),
            RuleItemMutex(self.question_data, '2,2;3,4'),
            RuleItemMutex(self.question_data, '2,3;3,5'),

            RuleItemMutex(self.question_data, '3,0;4,2'),
            RuleItemMutex(self.question_data, '3,1;4,3'),
            RuleItemMutex(self.question_data, '3,2;4,4'),
            RuleItemMutex(self.question_data, '3,3;4,5'),

            RuleItemMutex(self.question_data, '4,0;5,2'),
            RuleItemMutex(self.question_data, '4,1;5,3'),
            RuleItemMutex(self.question_data, '4,2;5,4'),
            RuleItemMutex(self.question_data, '4,3;5,5'),

            # 2

            RuleItemMutex(self.question_data, '0,0;2,1'),
            RuleItemMutex(self.question_data, '1,0;3,1'),
            RuleItemMutex(self.question_data, '2,0;4,1'),
            RuleItemMutex(self.question_data, '3,0;5,1'),

            RuleItemMutex(self.question_data, '0,1;2,2'),
            RuleItemMutex(self.question_data, '1,1;3,2'),
            RuleItemMutex(self.question_data, '2,1;4,2'),
            RuleItemMutex(self.question_data, '3,1;5,2'),

            RuleItemMutex(self.question_data, '0,2;2,3'),
            RuleItemMutex(self.question_data, '1,2;3,3'),
            RuleItemMutex(self.question_data, '2,2;4,3'),
            RuleItemMutex(self.question_data, '3,2;5,3'),

            RuleItemMutex(self.question_data, '0,3;2,4'),
            RuleItemMutex(self.question_data, '1,3;3,4'),
            RuleItemMutex(self.question_data, '2,3;4,4'),
            RuleItemMutex(self.question_data, '3,3;5,4'),

            RuleItemMutex(self.question_data, '0,4;2,5'),
            RuleItemMutex(self.question_data, '1,4;3,5'),
            RuleItemMutex(self.question_data, '2,4;4,5'),
            RuleItemMutex(self.question_data, '3,4;5,5'),

            # 3
            RuleItemMutex(self.question_data, '0,1;2,0'),
            RuleItemMutex(self.question_data, '1,1;3,0'),
            RuleItemMutex(self.question_data, '2,1;4,0'),
            RuleItemMutex(self.question_data, '3,1;5,0'),

            RuleItemMutex(self.question_data, '0,2;2,1'),
            RuleItemMutex(self.question_data, '1,2;3,1'),
            RuleItemMutex(self.question_data, '2,2;4,1'),
            RuleItemMutex(self.question_data, '3,2;5,1'),

            RuleItemMutex(self.question_data, '0,3;2,2'),
            RuleItemMutex(self.question_data, '1,3;3,2'),
            RuleItemMutex(self.question_data, '2,3;4,2'),
            RuleItemMutex(self.question_data, '3,3;5,2'),

            RuleItemMutex(self.question_data, '0,4;2,3'),
            RuleItemMutex(self.question_data, '1,4;3,3'),
            RuleItemMutex(self.question_data, '2,4;4,3'),
            RuleItemMutex(self.question_data, '3,4;5,3'),

            RuleItemMutex(self.question_data, '0,5;2,4'),
            RuleItemMutex(self.question_data, '1,5;3,4'),
            RuleItemMutex(self.question_data, '2,5;4,4'),
            RuleItemMutex(self.question_data, '3,5;5,4'),

            # 4
            RuleItemMutex(self.question_data, '0,2;1,0'),
            RuleItemMutex(self.question_data, '1,2;2,0'),
            RuleItemMutex(self.question_data, '2,2;3,0'),
            RuleItemMutex(self.question_data, '3,2;4,0'),
            RuleItemMutex(self.question_data, '4,2;5,0'),

            RuleItemMutex(self.question_data, '0,3;1,1'),
            RuleItemMutex(self.question_data, '1,3;2,1'),
            RuleItemMutex(self.question_data, '2,3;3,1'),
            RuleItemMutex(self.question_data, '3,3;4,1'),
            RuleItemMutex(self.question_data, '4,3;5,1'),

            RuleItemMutex(self.question_data, '0,4;1,2'),
            RuleItemMutex(self.question_data, '1,4;2,2'),
            RuleItemMutex(self.question_data, '2,4;3,2'),
            RuleItemMutex(self.question_data, '3,4;4,2'),
            RuleItemMutex(self.question_data, '4,4;5,2'),

            RuleItemMutex(self.question_data, '0,5;1,3'),
            RuleItemMutex(self.question_data, '1,5;2,3'),
            RuleItemMutex(self.question_data, '2,5;3,3'),
            RuleItemMutex(self.question_data, '3,5;4,3'),
            RuleItemMutex(self.question_data, '4,5;5,3'),

        ]

    def calculate_editable_original_data(self):
        super().calculate_editable_original_data()
        for y_index in range(len(self.question_data.editable_original_data)):
            for x_index in range(len(self.question_data.editable_original_data[y_index])):
                if self.question_data.editable_original_data[y_index][x_index] == '':
                    self.question_data.editable_original_data[y_index][x_index] = '#'

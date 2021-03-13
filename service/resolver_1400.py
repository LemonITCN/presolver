from service.resolver_base import ResolverBase
from service.rule_item_mutex import RuleItemMutex


# DB 互斥规则已写入
class Resolver1400(ResolverBase):
    ANSWER_RANGE = ['1', '2', '3', '4']

    def get_answer_range(self) -> []:
        return Resolver1400.ANSWER_RANGE

    def calculate_rules(self):
        super().calculate_rules()
        self.question_data.rules_list = [
            RuleItemMutex(self.question_data, '0,0;0,1;0,2;0,3'),
            RuleItemMutex(self.question_data, '1,0;1,1;1,2;1,3'),
            RuleItemMutex(self.question_data, '2,0;2,1;2,2;2,3'),
            RuleItemMutex(self.question_data, '3,0;3,1;3,2;3,3'),

            RuleItemMutex(self.question_data, '0,0;1,0;2,0;3,0'),
            RuleItemMutex(self.question_data, '0,1;1,1;2,1;3,1'),
            RuleItemMutex(self.question_data, '0,2;1,2;2,2;3,2'),
            RuleItemMutex(self.question_data, '0,3;1,3;2,3;3,3'),

            RuleItemMutex(self.question_data, '0,0;1,0;0,1;1,1'),
            RuleItemMutex(self.question_data, '0,2;0,3;1,2;1,3'),
            RuleItemMutex(self.question_data, '2,0;2,1;3,0;3,1'),
            RuleItemMutex(self.question_data, '2,2;2,3;3,2;3,3'),
        ]

    def calculate_editable_original_data(self):
        super().calculate_editable_original_data()
        for y_index in range(len(self.question_data.editable_original_data)):
            for x_index in range(len(self.question_data.editable_original_data[y_index])):
                if self.question_data.editable_original_data[y_index][x_index] == '':
                    self.question_data.editable_original_data[y_index][x_index] = '#'

import copy

from service.resolver_base import ResolverBase
from service.rule_num_mutex import RuleNumMutex


class Resolver1900(ResolverBase):
    ANSWER_RANGE = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def improve_data(self):
        super().improve_data()
        self.question_data.answer_range = Resolver1900.ANSWER_RANGE
        self.question_data.candidate_data = []
        # 重新初始化计算待选数据
        for y in range(self.question_data.dimensionY):
            for x in range(self.question_data.dimensionX):
                if len(self.question_data.candidate_data) == y:
                    self.question_data.candidate_data.append([])
                if self.question_data.original_data[y][x] != '':
                    self.question_data.candidate_data[y].append([self.question_data.original_data[y][x]])
                else:
                    self.question_data.candidate_data[y].append(copy.deepcopy(self.question_data.answer_range))

    def calculate_rules(self):
        super().calculate_rules()
        self.question_data.rules_list = [
            RuleNumMutex(self.question_data, '0,0;0,1;0,2;0,3;0,4;0,5;0,6;0,7;0,8'),
            RuleNumMutex(self.question_data, '1,0;1,1;1,2;1,3;1,4;1,5;1,6;1,7;1,8'),
            RuleNumMutex(self.question_data, '2,0;2,1;2,2;2,3;2,4;2,5;2,6;2,7;2,8'),
            RuleNumMutex(self.question_data, '3,0;3,1;3,2;3,3;3,4;3,5;3,6;3,7;3,8'),
            RuleNumMutex(self.question_data, '4,0;4,1;4,2;4,3;4,4;4,5;4,6;4,7;4,8'),
            RuleNumMutex(self.question_data, '5,0;5,1;5,2;5,3;5,4;5,5;5,6;5,7;5,8'),
            RuleNumMutex(self.question_data, '6,0;6,1;6,2;6,3;6,4;6,5;6,6;6,7;6,8'),
            RuleNumMutex(self.question_data, '7,0;7,1;7,2;7,3;7,4;7,5;7,6;7,7;7,8'),
            RuleNumMutex(self.question_data, '8,0;8,1;8,2;8,3;8,4;8,5;8,6;8,7;8,8'),

            RuleNumMutex(self.question_data, '0,0;1,0;2,0;3,0;4,0;5,0;6,0;7,0;8,0'),
            RuleNumMutex(self.question_data, '0,1;1,1;2,1;3,1;4,1;5,1;6,1;7,1;8,1'),
            RuleNumMutex(self.question_data, '0,2;1,2;2,2;3,2;4,2;5,2;6,2;7,2;8,2'),
            RuleNumMutex(self.question_data, '0,3;1,3;2,3;3,3;4,3;5,3;6,3;7,3;8,3'),
            RuleNumMutex(self.question_data, '0,4;1,4;2,4;3,4;4,4;5,4;6,4;7,4;8,4'),
            RuleNumMutex(self.question_data, '0,5;1,5;2,5;3,5;4,5;5,5;6,5;7,5;8,5'),
            RuleNumMutex(self.question_data, '0,6;1,6;2,6;3,6;4,6;5,6;6,6;7,6;8,6'),
            RuleNumMutex(self.question_data, '0,7;1,7;2,7;3,7;4,7;5,7;6,7;7,7;8,7'),
            RuleNumMutex(self.question_data, '0,8;1,8;2,8;3,8;4,8;5,8;6,8;7,8;8,8'),

            RuleNumMutex(self.question_data, '0,0;0,1;0,2;1,0;1,1;1,2;2,0;2,1;2,2'),
            RuleNumMutex(self.question_data, '3,0;3,1;3,2;4,0;4,1;4,2;5,0;5,1;5,2'),
            RuleNumMutex(self.question_data, '6,0;6,1;6,2;7,0;7,1;7,2;8,0;8,1;8,2'),
            RuleNumMutex(self.question_data, '0,3;0,4;0,5;1,3;1,4;1,5;2,3;2,4;2,5'),
            RuleNumMutex(self.question_data, '3,3;3,4;3,5;4,3;4,4;4,5;5,3;5,4;5,5'),
            RuleNumMutex(self.question_data, '6,3;6,4;6,5;7,3;7,4;7,5;8,3;8,4;8,5'),
            RuleNumMutex(self.question_data, '0,6;0,7;0,8;1,6;1,7;1,8;2,6;2,7;2,8'),
            RuleNumMutex(self.question_data, '3,6;3,7;3,8;4,6;4,7;4,8;5,6;5,7;5,8'),
            RuleNumMutex(self.question_data, '6,6;6,7;6,8;7,6;7,7;7,8;8,6;8,7;8,8'),
        ]

    def calculate_answer(self):
        super().calculate_answer()
        print(self.question_data)

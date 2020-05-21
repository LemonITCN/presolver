from service.resolver_base import ResolverBase
from service.rule_num_mutex import RuleNumMutex


class Resolver1900(ResolverBase):
    @staticmethod
    def calculate_rules(question) -> []:
        super().calculate_rules(question)
        question.rules = [
            RuleNumMutex(question, '0,0;0,1;0,2;0,3;0,4;0,5;0,6;0,7;0,8'),
            RuleNumMutex(question, '1,0;1,1;1,2;1,3;1,4;1,5;1,6;1,7;1,8'),
            RuleNumMutex(question, '2,0;2,1;2,2;2,3;2,4;2,5;2,6;2,7;2,8'),
            RuleNumMutex(question, '3,0;3,1;3,2;3,3;3,4;3,5;3,6;3,7;3,8'),
            RuleNumMutex(question, '4,0;4,1;4,2;4,3;4,4;4,5;4,6;4,7;4,8'),
            RuleNumMutex(question, '5,0;5,1;5,2;5,3;5,4;5,5;5,6;5,7;5,8'),
            RuleNumMutex(question, '6,0;6,1;6,2;6,3;6,4;6,5;6,6;6,7;6,8'),
            RuleNumMutex(question, '7,0;7,1;7,2;7,3;7,4;7,5;7,6;7,7;7,8'),
            RuleNumMutex(question, '8,0;8,1;8,2;8,3;8,4;8,5;8,6;8,7;8,8'),

            RuleNumMutex(question, '0,0;1,0;2,0;3,0;4,0;5,0;6,0;7,0;8,0'),
            RuleNumMutex(question, '0,1;1,1;2,1;3,1;4,1;5,1;6,1;7,1;8,1'),
            RuleNumMutex(question, '0,2;1,2;2,2;3,2;4,2;5,2;6,2;7,2;8,2'),
            RuleNumMutex(question, '0,3;1,3;2,3;3,3;4,3;5,3;6,3;7,3;8,3'),
            RuleNumMutex(question, '0,4;1,4;2,4;3,4;4,4;5,4;6,4;7,4;8,4'),
            RuleNumMutex(question, '0,5;1,5;2,5;3,5;4,5;5,5;6,5;7,5;8,5'),
            RuleNumMutex(question, '0,6;1,6;2,6;3,6;4,6;5,6;6,6;7,6;8,6'),
            RuleNumMutex(question, '0,7;1,7;2,7;3,7;4,7;5,7;6,7;7,7;8,7'),
            RuleNumMutex(question, '0,8;1,8;2,8;3,8;4,8;5,8;6,8;7,8;8,8'),

            RuleNumMutex(question, '0,0;0,1;0,2;1,0;1,1;1,2;2,0;2,1;2,2'),
            RuleNumMutex(question, '3,0;3,1;3,2;4,0;4,1;4,2;5,0;5,1;5,2'),
            RuleNumMutex(question, '6,0;6,1;6,2;7,0;7,1;7,2;8,0;8,1;8,2'),
            RuleNumMutex(question, '0,3;0,4;0,5;1,3;1,4;1,5;2,3;2,4;2,5'),
            RuleNumMutex(question, '3,3;3,4;3,5;4,3;4,4;4,5;5,3;5,4;5,5'),
            RuleNumMutex(question, '6,3;6,4;6,5;7,3;7,4;7,5;8,3;8,4;8,5'),
            RuleNumMutex(question, '0,6;0,7;0,8;1,6;1,7;1,8;2,6;2,7;2,8'),
            RuleNumMutex(question, '3,6;3,7;3,8;4,6;4,7;4,8;5,6;5,7;5,8'),
            RuleNumMutex(question, '6,6;6,7;6,8;7,6;7,7;7,8;8,6;8,7;8,8'),
        ]
        return question.rules

    @staticmethod
    def calculate_answer(question):
        super().calculate_answer(question)

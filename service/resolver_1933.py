from service.resolver_base import ResolverBase
from service.rule_item_mutex import RuleItemMutex


# 九宫斜线数独
class Resolver1933(ResolverBase):
    ANSWER_RANGE = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def get_answer_range(self) -> []:
        return Resolver1933.ANSWER_RANGE

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
        # 读取Excel中所有DPL函数，计算DPL的每一组数据分别经过了哪些单元格，然后添加互斥规则
        for draw_function_data in self.question_data.draw_function_list:
            if draw_function_data.function_name == 'DPL':
                for data_group in draw_function_data.data.split(';'):
                    data_group_split = data_group.split(':')
                    if len(data_group_split) == 2:
                        # 算法只处理DPL是两点之间的线
                        point_0 = data_group_split[0].split(',')
                        point_1 = data_group_split[1].split(',')
                        x_start = int(point_0[0])
                        y_start = int(point_0[1])
                        x_min = min(int(point_0[0]), int(point_1[0]))
                        x_max = max(int(point_0[0]), int(point_1[0]))
                        y_min = min(int(point_0[1]), int(point_1[1]))
                        y_max = max(int(point_0[1]), int(point_1[1]))
                        x_sub = 1 if int(point_1[0]) > int(point_0[0]) else -1
                        if x_sub == -1:
                            x_start = x_start - 1
                        y_sub = 1 if int(point_1[1]) > int(point_0[1]) else -1
                        if y_sub == -1:
                            y_start = y_start - 1
                        x_range = x_max - x_min
                        y_range = y_max - y_min
                        rule_str = ''
                        if x_range == y_range:
                            # 算法现在只处理经过单元格对角线的DPL
                            for i in range(x_range):
                                rule_str = rule_str + str(i * x_sub + x_start) + ',' + str(i * y_sub + y_start) + ';'
                            self.question_data.rules_list.append(RuleItemMutex(self.question_data, rule_str))

from model.question_data import QuestionData
from service.rule_base import RuleBase


# 和值检查，对某些单元格的数值进行相加，然后对结果进行判断，
# 支持对和值的判断类型有：equal: 等于, not_equal: 不等于，大于 greater， 小于 less，大于等于：greater_equal，小于等于：less_equal
class RuleSumCheck(RuleBase):
    location_list = []
    check_type = ''
    check_aim_value = 0

    # 使用:分割后成三类数据，分别为：
    # :1: 计算和值的单元格坐标列表，坐标之间用分号分隔，每个坐标的xy之间用英文半角逗号分隔。
    # "2: 对比方式：equal: 等于, not_equal: 不等于，大于 greater， 小于 less，大于等于：greater_equal，小于等于：less_equal
    # :3: 欲对比的结果，数值型，如10， 5等
    # 举例：0,0;0,1@equal@10
    # 举例：0,1;1,1@not_equal@5

    def __init__(self, question_data: QuestionData, params: str) -> None:
        super().__init__(question_data, params)
        params_split = params.split(':')
        self.location_list = []
        for location in params_split[0].split(';'):
            if location == '':
                continue
            location_x = int(location.split(',')[0])
            location_y = int(location.split(',')[1])
            this_location = [location_x, location_y]
            this_location_str = str(location_x) + '-' + str(location_y)
            self.location_list.append(this_location)
            if this_location_str not in self.question_data.rules_relation_map:
                self.question_data.rules_relation_map[this_location_str] = []
            self.question_data.rules_relation_map[this_location_str].append(self)
        self.check_type = params_split[1]
        self.check_aim_value = int(params_split[2])

    def check(self) -> bool:
        sum_value = 0
        for location in self.location_list:
            this_value = self.question_data.calculate_data[location[1]][location[0]]
            if not this_value == '':
                sum_value = sum_value + int(this_value)
            else:
                return True
        if self.check_type == 'equal':
            return sum_value == self.check_aim_value
        elif self.check_type == 'not_equal':
            return sum_value != self.check_aim_value
        elif self.check_type == 'greater':
            return sum_value > self.check_aim_value
        elif self.check_type == 'less':
            return sum_value < self.check_aim_value
        elif self.check_type == 'greater_equal':
            return sum_value >= self.check_aim_value
        elif self.check_type == 'less_equal':
            return sum_value <= self.check_aim_value
        else:
            return False

    def filter_candidate_data(self) -> int:
        super().filter_candidate_data()
        filtered_count = 0
        if self.check_type.startswith('less') or self.check_type == 'equal' or self.check_type == 'not_equal':
            # 只有小于和小于等于才可以进行过滤
            for location in self.location_list:
                for candidate_data_item in self.question_data.candidate_data[location[1]][location[0]]:
                    if self.check_type == 'less' and int(candidate_data_item) >= self.check_aim_value:
                        self.question_data.candidate_data[location[1]][location[0]].remove(candidate_data_item)
                        filtered_count = filtered_count + 1
                    if self.check_type == 'less_equal' and int(candidate_data_item) > self.check_aim_value:
                        self.question_data.candidate_data[location[1]][location[0]].remove(candidate_data_item)
                        filtered_count = filtered_count + 1
                    if self.check_type == 'equal' and int(candidate_data_item) > self.check_aim_value:
                        self.question_data.candidate_data[location[1]][location[0]].remove(candidate_data_item)
                        filtered_count = filtered_count + 1
        return filtered_count

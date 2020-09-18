from model.question_data import QuestionData
from service.rule_base import RuleBase


class RuleItemMutex(RuleBase):
    location_list = []

    # params format: 互斥的单元格坐标列表，坐标之间用分号分隔，每个坐标的xy之间用英文半角逗号分隔
    # 举例：0,0;0,1;0,2;0,3;0,4;0,5;0,6;0,7;0,8

    def __init__(self, question_data: QuestionData, params: str) -> None:
        super().__init__(question_data, params)
        self.location_list = []
        for location in params.split(';'):
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

    def check(self) -> bool:
        check_list = []
        for location in self.location_list:
            this_value = self.question_data.calculate_data[location[1]][location[0]]
            if not this_value == '':
                if this_value in check_list:
                    return False
                check_list.append(this_value)
        return True

    def filter_candidate_data(self) -> int:
        super().filter_candidate_data()
        exists_item_list = []
        # 提取当前规则范围内的已知数字
        for location in self.location_list:
            this_value = self.question_data.filtered_original_data[location[1]][location[0]]
            if not this_value == '':
                exists_item_list.append(this_value)
        filtered_count = 0
        # 去除、过滤已知数字
        for location in self.location_list:
            this_value = self.question_data.filtered_original_data[location[1]][location[0]]
            if this_value == '':
                for exists_item in exists_item_list:
                    if exists_item in self.question_data.candidate_data[location[1]][location[0]]:
                        self.question_data.candidate_data[location[1]][location[0]].remove(exists_item)
                        if len(self.question_data.candidate_data[location[1]][location[0]]) == 1:
                            self.question_data.filtered_original_data[location[1]][location[0]] = \
                                self.question_data.candidate_data[location[1]][location[0]][0]
                        filtered_count = filtered_count + 1
        return filtered_count

    def get_rule_data_str(self) -> str:
        result_str = '["'
        for location in self.location_list:
            result_str = result_str + str(location[0]) + ',' + str(location[1]) + ';'
        result_str = result_str + '"]'
        return result_str

    def get_rule_parameters_str(self) -> str:
        return ''

    def get_rule_name_str(self) -> str:
        return 'ITEM_MUTEX'

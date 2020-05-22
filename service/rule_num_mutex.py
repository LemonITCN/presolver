from model.question_data import QuestionData
from service.rule_base import RuleBase


class RuleNumMutex(RuleBase):
    location_list = []

    # params format: 互斥的单元格坐标列表，坐标之间用分号分隔，每个坐标的xy之间用英文半角逗号分隔
    # 举例：0,0;0,1;0,2;0,3;0,4;0,5;0,6;0,7;0,8

    def __init__(self, question_data: QuestionData, params: str) -> None:
        super().__init__(question_data, params)
        self.location_list = []
        for location in params.split(';'):
            location_x = int(location.split(',')[0])
            location_y = int(location.split(',')[1])
            self.location_list.append([location_x, location_y])

    def check(self) -> bool:
        check_list = []
        for location in self.location_list:
            this_value = self.question_data.calculate_data[location[0]][location[1]]
            if this_value in check_list:
                return False
            check_list.append(this_value)
        return True

    def filter_candidate_data(self):
        super().filter_candidate_data()
        exists_item_list = []
        # 提取当前规则范围内的已知数字
        for location in self.location_list:
            this_value = self.question_data.original_data[location[1]][location[0]]
            if not this_value == '':
                exists_item_list.append(this_value)
        # 去除、过滤已知数字
        for location in self.location_list:
            this_value = self.question_data.original_data[location[1]][location[0]]
            if this_value == '':
                for exists_item in exists_item_list:
                    if exists_item in self.question_data.candidate_data[location[1]][location[0]]:
                        self.question_data.candidate_data[location[1]][location[0]].remove(exists_item)

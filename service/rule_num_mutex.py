from service.rule_base import RuleBase


class RuleNumMutex(RuleBase):

    # params format: 互斥的单元格坐标列表，坐标之间用分号分隔，每个坐标的xy之间用英文半角逗号分隔
    # 举例：0,0;0,1;0,2;0,3;0,4;0,5;0,6;0,7;0,8

    def check(self) -> bool:
        check_list = []
        for location in self.params.split(';'):
            location_x = int(location.split(',')[0])
            location_y = int(location.split(',')[1])
            this_value = self.question_data.original_data[location_y][location_x]
            if this_value in check_list:
                return False
            check_list.append(this_value)
        return True

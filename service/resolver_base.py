import time

from model.question_data import QuestionData


class ResolverBase:
    question_data = QuestionData()

    def __init__(self, question_data: QuestionData) -> None:
        super().__init__()
        self.question_data = question_data

    def calculate_original_data(self):
        print('开始计算题目的原始数据：' + self.question_data.question_key)
        self.question_data.original_data = []
        for draw_function in self.question_data.draw_function_list:
            # 发现是DBN函数，开始读取题目原始数据
            if draw_function.function_name == 'DBN':
                for y in range(self.question_data.dimensionY):
                    if len(self.question_data.original_data) == y:
                        self.question_data.original_data.append([])
                    else:
                        self.question_data.original_data[y] = []
                    for x in range(self.question_data.dimensionX):
                        num_index = y * self.question_data.dimensionX + x
                        if num_index < len(draw_function.data):
                            item_value = draw_function.data[num_index]
                            self.question_data.original_data[y].append('' if item_value == '0' else item_value)
                        else:
                            self.question_data.original_data[y].append('')
        pass

    def improve_data(self):
        print('开始完善题目的基础数据：' + self.question_data.question_key)
        pass

    def calculate_rules(self):
        print('开始计算题目规则列表：' + self.question_data.question_key)
        pass

    def filter_all_rules_candidate_data(self) -> int:
        print('开始遍历所有规则，对待选数字进行过滤筛选：' + self.question_data.question_key)
        filtered_count = 0
        for rule in self.question_data.rules_list:
            filtered_count = filtered_count + rule.filter_candidate_data()
        return filtered_count

    # def calculate_check_current(self) -> bool:
    #     print("开始检查当前生成的答案是否正确：" + self.question_data.question_key)
    #     for rule in self.question_data.rules_list:
    #         if not rule.check():
    #             return False

    def calculate_answer(self):
        print("开始求解题目答案：" + self.question_data.question_key)
        start_time = int(round(time.time() * 1000))
        self.calculate_original_data()
        self.improve_data()
        self.calculate_rules()
        this_time_filter_count = 1
        while this_time_filter_count != 0:
            this_time_filter_count = self.filter_all_rules_candidate_data()
        self.question_data.calculate_answer = []
        self.question_data.need_calculate_location_list = []
        for y in range(self.question_data.dimensionY):
            if len(self.question_data.calculate_data) == y:
                self.question_data.calculate_data.append([])
            for x in range(self.question_data.dimensionX):
                if len(self.question_data.candidate_data[y][x]) > 1:
                    this_location = [x, y]
                    self.question_data.need_calculate_location_list.append(this_location)
                    self.question_data.calculate_data[y].append('')
                else:
                    self.question_data.calculate_data[y].append(self.question_data.candidate_data[y][x][0])
        print('开始计算题目[' + self.question_data.question_key + ']待计算单元格数量：' + str(
            len(self.question_data.need_calculate_location_list)))
        if self.calculate_answer_frame(0):
            print('题目成功计算出答案：' + self.question_data.question_key + ', 耗时：' + str(
                int(round(time.time() * 1000)) - start_time) + 'ms')
        else:
            print('题目计算答案失败，无解：' + self.question_data.question_key)
        pass

    def calculate_answer_frame(self, calculate_index: int):
        if calculate_index == len(self.question_data.need_calculate_location_list):
            self.question_data.answer_data = self.question_data.calculate_data
            return True
        this_location = self.question_data.need_calculate_location_list[calculate_index]
        for this_item in self.question_data.candidate_data[this_location[1]][this_location[0]]:
            self.question_data.calculate_data[this_location[1]][this_location[0]] = this_item
            if self.check_frame(calculate_index):
                # 当前帧计算通过
                if self.calculate_answer_frame(calculate_index + 1):
                    return True
            else:
                self.question_data.calculate_data[this_location[1]][this_location[0]] = ''
        self.question_data.calculate_data[this_location[1]][this_location[0]] = ''
        return False

    def check_frame(self, calculate_index: int):
        this_location = self.question_data.need_calculate_location_list[calculate_index]
        this_location_str = str(this_location[0]) + '-' + str(this_location[1])
        for rule in self.question_data.rules_relation_map[this_location_str]:
            if not rule.check():
                return False
        return True

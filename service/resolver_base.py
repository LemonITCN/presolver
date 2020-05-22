from itertools import product

from numpy import array

from model.question_data import QuestionData


class ResolverBase:
    question_data = QuestionData()

    def __init__(self, question_data: QuestionData) -> None:
        super().__init__()
        self.question_data = question_data

    def calculate_original_data(self):
        print('开始计算题目的原始数据：' + self.question_data.question_key)
        for draw_function in self.question_data.draw_function_list:
            # 发现是DBN函数，开始读取题目原始数据
            if draw_function.function_name == 'DBN':
                for y in range(self.question_data.dimensionY):
                    for x in range(self.question_data.dimensionX):
                        if len(self.question_data.original_data) == y:
                            self.question_data.original_data.append([])
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

    def filter_all_rules_candidate_data(self):
        print('开始遍历所有规则，对待选数字进行过滤筛选：' + self.question_data.question_key)
        for rule in self.question_data.rules_list:
            rule.filter_candidate_data()

    def calculate_check_current(self) -> bool:
        print("开始检查当前生成的答案是否正确：" + self.question_data.question_key)
        for rule in self.question_data.rules_list:
            if not rule.check():
                return False

    def calculate_answer(self):
        print("开始求解题目答案：" + self.question_data.question_key)
        a = product(*array(self.question_data.candidate_data).flatten())
        ai = 0
        for item_data in a:
            # print(item_data)
            ai = ai + 1
            # print(len(a))
            # self.question_data.calculate_data = self.list_split(item_data, self.question_data.dimensionX)
            # if self.calculate_check_current():
            #     self.question_data.answer_data = self.question_data.calculate_data
        print('ok')
        pass

    def list_split(self, items, n):
        return [items[i:i + n] for i in range(0, len(items), n)]

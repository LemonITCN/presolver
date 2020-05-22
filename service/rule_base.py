from model.question_data import QuestionData


class RuleBase:
    question_data = QuestionData()

    def __init__(self, question_data: QuestionData, params: str) -> None:
        super().__init__()
        self.question_data = question_data

    def check(self) -> bool:
        pass

    # 过滤待选数字，根据自身规则及参数，对待选数字进行过滤筛选
    def filter_candidate_data(self):
        print('开始使用规则进行待选数字过滤:' + self.question_data.question_key)
        pass

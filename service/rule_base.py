from model.question_data import QuestionData


class RuleBase:
    question_data = QuestionData()

    def __init__(self, question_data: QuestionData, params: str) -> None:
        super().__init__()
        self.question_data = question_data

    def check(self) -> bool:
        pass

    # 过滤待选数字，根据自身规则及参数，对待选数字进行过滤筛选
    def filter_candidate_data(self) -> int:
        return 0
        pass

    def get_rule_data_str(self) -> str:
        return ''
        pass

    def get_rule_parameters_str(self) -> str:
        return ''
        pass

    def get_rule_name_str(self) -> str:
        return ''
        pass

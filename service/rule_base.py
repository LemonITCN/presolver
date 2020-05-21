from model.question_data import QuestionData


class RuleBase:
    question_data = QuestionData()
    params = ''

    def __init__(self, question_data: QuestionData, params: str) -> None:
        super().__init__()
        self.question_data = question_data
        self.params = params

    def check(self) -> bool:
        pass

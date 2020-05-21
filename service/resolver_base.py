from model.question_data import QuestionData


class ResolverBase:
    @staticmethod
    def calculate_rules(question: QuestionData):
        pass

    @staticmethod
    def calculate_check_current(question: QuestionData) -> bool:
        for rule in question.rules_list:
            if not rule.check():
                return False

    @staticmethod
    def calculate_answer(question: QuestionData):
        pass

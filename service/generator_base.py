import copy

from model.question_data import QuestionData
from service.presolver import PResolver


class GeneratorBase:
    question_seed = QuestionData()

    def get_answer_range(self) -> []:
        return []
        pass

    def __init__(self, question_seed: QuestionData) -> None:
        super().__init__()
        self.question_seed = question_seed

    def generate_new_question(self, question_key: str) -> QuestionData:
        new_question = copy.deepcopy(self.question_seed)
        new_question.question_key = question_key
        PResolver.calculate_answer(new_question)
        self.random_disruption(new_question)
        self.random_process_topic(new_question)
        return new_question

    # 对种子题目直接生成出来的数据进行打乱题干顺序
    def random_disruption(self, question: QuestionData):
        pass

    # 随机处理题干，删除题干中的一些数字等操作，因题型而异
    def random_process_topic(self, question: QuestionData):
        pass

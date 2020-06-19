import random

from model.question_data import QuestionData
from service.generator_base import GeneratorBase
import copy


class Generator1900(GeneratorBase):
    ANSWER_RANGE = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def get_answer_range(self) -> []:
        return Generator1900.ANSWER_RANGE

    def random_disruption(self, question: QuestionData):
        for start_index in [0, 3, 6]:
            # 先交换行
            index_list = [0, 1, 2]
            del index_list[random.randint(0, 2)]
            row_temp = question.answer_data[start_index + index_list[0]]
            question.answer_data[start_index + index_list[0]] = question.answer_data[start_index + index_list[1]]
            question.answer_data[start_index + index_list[1]] = row_temp
            # 在交换列
            index_list = [0, 1, 2]
            del index_list[random.randint(0, 2)]
            for row_index in range(9):
                num_temp = question.answer_data[row_index][start_index + index_list[0]]
                question.answer_data[row_index][start_index + index_list[0]] = question.answer_data[row_index][
                    start_index + index_list[1]]
                question.answer_data[row_index][start_index + index_list[1]] = num_temp
        question.original_data = copy.deepcopy(question.answer_data)

    def random_process_topic(self, question: QuestionData):
        super().random_process_topic(question)
        question.draw_function_list[0].data = question.get_original_data_str().replace(',', '')

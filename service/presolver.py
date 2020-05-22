import logging

import openpyxl

from model.draw_function_data import DrawFunctionData
from model.question_data import QuestionData
from service.resolver_1900 import Resolver1900


class PResolver:
    @staticmethod
    def read_excel(excel_file_path: str) -> []:
        print('开始读取Excel中的题目数据...')
        workbook = openpyxl.load_workbook(excel_file_path)
        row_index = 0
        question_pool = {}
        for row in workbook.worksheets[0].rows:
            if row[0].value is not None and row_index > 0:
                if row[0].value.strip() != '':
                    question_key = row[3].value
                    # 获取问题对象，如果不存在那么先创建
                    if question_key not in question_pool:
                        temp_question_data = QuestionData()
                        temp_question_data.row_index = row_index
                        temp_question_data.author = row[0].value
                        temp_question_data.question_type_name = row[1].value
                        temp_question_data.question_level = row[2].value
                        temp_question_data.question_key = row[3].value
                        temp_question_data.question_type_key = row[4].value
                        temp_question_data.dimensionX = int(row[8].value.split(',')[0])
                        temp_question_data.dimensionY = int(row[8].value.split(',')[1])
                        question_pool[question_key] = temp_question_data
                    question_data = question_pool[question_key]
                    # 创建问题绘制函数对象
                    draw_function = DrawFunctionData()
                    draw_function.belong_question = question_data
                    draw_function.function_name = row[5].value
                    draw_function.data = row[6].value
                    draw_function.parameters = row[7].value
                    question_data.draw_function_list.append(draw_function)
            row_index = row_index + 1
        return question_pool.values()

    @staticmethod
    def calculate_answer(question_data: QuestionData):
        logging.info('【静态调用】开始计算题目答案：' + question_data.question_key)
        if question_data.question_key.startswith('1900'):
            resolver = Resolver1900(question_data)
            resolver.calculate_original_data()
            resolver.improve_data()
            resolver.calculate_rules()
            resolver.filter_all_rules_candidate_data()
            resolver.calculate_answer()
        else:
            print('暂不支持次此题型')

    @staticmethod
    def calculate_answer_list(question_data_list: []):
        logging.info('start calculate answer list')
        for question in question_data_list:
            PResolver.calculate_answer(question)

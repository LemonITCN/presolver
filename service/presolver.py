import logging

import openpyxl

from model.draw_function_data import DrawFunctionData
from model.question_data import QuestionData


class PResolver:
    @staticmethod
    def read_excel(excel_file_path):
        print('start read excel')
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
                    # 发现是DBN函数，开始读取题目原始数据
                    if draw_function.function_name == 'DBN':
                        for y in range(question_data.dimensionY):
                            for x in range(question_data.dimensionX):
                                if len(question_data.original_data) == y:
                                    question_data.original_data.append([])
                                num_index = y * question_data.dimensionX + x
                                if num_index < len(row[6].value):
                                    question_data.original_data[y].append(row[6].value[num_index])
            row_index = row_index + 1
        return question_pool.values()

    @staticmethod
    def calculate_answer(question_data):
        logging.info('start calculate answer')

    @staticmethod
    def calculate_answer_list(question_data_list):
        logging.info('start calculate answer list')

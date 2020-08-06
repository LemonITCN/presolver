import sys

from model.question_data import QuestionData
from service.presolver import PResolver

# question_list = PResolver.read_excel('/Users/liuri/Documents/code/lemonit-workdata/易学而乐/2020年3月开始e学数独第一期资料/九宫题目模板.xlsx')
# excel_path = '/Users/liuri/Desktop/易学数独算法/窗口数独20200613.xlsx'
# excel_path = '/Users/liuri/Desktop/易学数独算法/VX数独20200613.xlsx'
# excel_path = '/Users/liuri/Desktop/易学数独算法/斜线数独20200613.xlsx'

# 正常情况下，求解时使用
if len(sys.argv) < 2:
    print('请您传入要处理的Excel的路径')
    sys.exit(1)
excel_path = sys.argv[1]
question_list = PResolver.read_excel(excel_path)


def calculate_success_callback(question: QuestionData):
    PResolver.write_calculate_result_data_to_excel(excel_path, [question])
    rule_excel_path_split = excel_path.split('/')
    rule_excel_path_split.pop(len(rule_excel_path_split) - 1)
    PResolver.write_check_rule_data_to_excel(
        '/'.join(rule_excel_path_split) + '/check-rule-' + question.question_key + '.xlsx', [question])


PResolver.calculate_answer_list(question_list, calculate_success_callback)

# 生成数感练习题目时使用
# question_seed = QuestionData()
# question_seed.author = 'yoyolearn'
# question_seed.question_type_name = '九宫标准'
# question_seed.question_level = 'A'
# question_seed.question_type_key = '1900'
# question_seed.dimensionX = 9
# question_seed.dimensionY = 9
# draw_function_data = DrawFunctionData()
# draw_function_data.function_name = 'DBN'
# draw_function_data.belong_question = question_seed
# draw_function_data.data = '123456789000000000000000000000000000000000000000000000000000000000000000000000000'
# question_seed.draw_function_list.append(draw_function_data)
# question_list = []
# for question_key_index in range(5000):
#     question_list.append(PGenerator.generate(question_seed, '19SGA' + str(question_key_index + 1).zfill(4)))
# PGenerator.write_calculate_result_data_to_excel('/Users/liuri/Desktop/001.xlsx', question_list)

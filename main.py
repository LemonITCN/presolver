from service.presolver import PResolver

# question_list = PResolver.read_excel('/Users/liuri/Documents/code/lemonit-workdata/易学而乐/2020年3月开始e学数独第一期资料/九宫题目模板.xlsx')
# excel_path = '/Users/liuri/Desktop/易学数独算法/窗口数独20200613.xlsx'
excel_path = '/Users/liuri/Desktop/易学数独算法/VX数独20200613.xlsx'
# excel_path = '/Users/liuri/Desktop/易学数独算法/斜线数独20200613.xlsx'
question_list = PResolver.read_excel(excel_path)
PResolver.calculate_answer_list(question_list)
PResolver.write_calculate_result_data_to_excel(excel_path, question_list)

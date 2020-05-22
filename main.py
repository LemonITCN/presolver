from service.presolver import PResolver

question_list = PResolver.read_excel('/Users/liuri/Documents/code/lemonit-workdata/易学而乐/2020年3月开始e学数独第一期资料/九宫题目模板.xlsx')
PResolver.calculate_answer_list(question_list)

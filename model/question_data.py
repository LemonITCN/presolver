class QuestionData:
    row_index = 0
    author = ''
    question_type_name = ''
    question_level = ''
    question_key = ''
    question_type_key = ''
    dimensionX = 0
    dimensionY = 0
    draw_function_list = []
    original_data = []
    # 候选数字，三维数组
    candidate_data = []
    # 引擎不断填入尝试各种数字后产生的数据
    calculate_data = []
    # 答案数据范围，就是最基础题目规则中每个格子的答案范围，如九宫标准数独的答案范围是:1,2,3,4,5,6,7,8,9
    answer_range = []
    answer_data = []
    rules_list = []

    def __init__(self) -> None:
        super().__init__()
        self.row_index = 0
        self.author = 0
        self.question_type_name = ''
        self.question_level = ''
        self.question_key = ''
        self.question_type_key = ''
        self.dimensionX = 0
        self.dimensionY = 0
        self.draw_function_list = []
        self.original_data = []
        self.calculate_data = []
        self.answer_data = []
        self.rules_list = []

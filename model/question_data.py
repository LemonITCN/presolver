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
        self.answer_data = []
        self.rules_list = []

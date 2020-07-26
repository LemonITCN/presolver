from utils.data_utils import DataUtils


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
    # 原始数据，包含题目和可编辑区域信息，数据长度等同于题目的维度X 乘以 维度Y
    # 英文半角  # 标识当前格子留空，并且可以编辑，英文半角%标识当前格子留空，不可以编辑
    original_data = []
    editable_original_data = []
    # 过滤后的原始数据，经过rules层层过滤后的数据
    filtered_original_data = []
    # 候选数字，三维数组
    candidate_data = []
    # 引擎不断填入尝试各种数字后产生的数据
    calculate_data = []
    # 答案数据范围，就是最基础题目规则中每个格子的答案范围，如九宫标准数独的答案范围是:1,2,3,4,5,6,7,8,9
    answer_range = []
    answer_data = []
    rules_list = []
    # 规则关系map，坐标:单元格所拥有的关系数组
    rules_relation_map = {}
    need_calculate_location_list = []

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
        self.editable_original_data = []
        self.calculate_data = []
        self.answer_data = []
        self.rules_list = []
        self.rules_relation_map = {}
        self.need_calculate_location_list = []

    # 原始数据，包含题目和可编辑区域信息，数据长度等同于题目的维度X 乘以 维度Y
    # 英文半角#标识当前格子留空，并且可以编辑，英文半角%标识当前格子留空，不可以编辑
    # 举例：1,2,3,4,5,6,7,8,9,1,2,3,4,5,#,#,#,6,7,8,9,1,2,%,%,%,%,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9
    # 之所以使用逗号分隔是因为郭哥说过未来某些种类题型可能会出现单个单元格的内容为两位数或多位数的
    def get_editable_original_data_str(self) -> str:
        return DataUtils.parse_arr_data_to_comma_str_data(self.editable_original_data)

    # 答案数据，包含题目和可编辑区域的答案信息，数据长度应该等同于原始数据
    # 其中原始数据中的#部分必须有有效对应值，其他部分可不填，用英文半角逗号分隔后留空，但是强烈建议其他数据与原始数据保持一致
    # 举例：1,2,3,4,5,6,7,8,9,1,2,3,4,5,5,6,7,6,7,8,9,1,2,2,3,4,5,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9
    # 之所以使用逗号分隔是因为郭哥说过未来某些种类题型可能会出现单个单元格的内容为两位数或多位数的
    def get_answer_data_str(self) -> str:
        return DataUtils.parse_arr_data_to_comma_str_data(self.answer_data)

    def get_dimension_data_str(self) -> str:
        return str(self.dimensionY) + ',' + str(self.dimensionY)

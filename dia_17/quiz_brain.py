class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def nex_question(self):
        current_cuestion = self.question_list[self.question_number]
        input(f"Q.{self.question_number}: {current_cuestion.text} (True/False): ")
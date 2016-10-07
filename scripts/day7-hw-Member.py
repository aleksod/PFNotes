class Member():

    def __init__(self, name, hair_color, birthdate, code_string,
    num_lines_coded = 0, coding_level = 'beginner'):
        self.name = name
        self.hair_color = hair_color
        self.birthdate = birthdate
        self.questions_asked = list()
        self.code_string = str()
        self.num_lines_coded = num_lines_coded
        self.coding_level = coding_level

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def add_coded_line(self, code_string):
        self.code_string.append(code_string)
        self.num_lines_coded += 1
        def get_coding_level(self):
            if self.num_lines_coded <= 100:
                self.coding_level = 'beginner'
            elif self.num_lines_coded <= 1000:
                self.coding_level = 'novice'
            elif self.num_lines_coded <= 10000:
                self.coding_level = 'intermediate'
            else:
                self.coding_level = 'master'

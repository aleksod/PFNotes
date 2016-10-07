class OurClass():

    def __init__(self, name, location, members=None, size=0):
        self.name = name
        self.location = location
        self.members = members
        self.size = size
        self.check_if_at_capacity()
        if self.members == None:
            self.members = list()

    def get_num_questions_asked(self):
        questions_total = 0
        for i in self.members:
            questions_total += len(i.questions_asked)
        print questions_total
        return questions_total

    def get_num_lines_code(self):
        lines_total = 0
        for i in self.members:
            lines_total += len(i.lines_of_code)
        return lines_total

    def add_class_members(self, member):
        self.members.append(member)
        self.size += 1
        self.check_if_at_capacity()

    def check_if_at_capacity(self):
        if self.size >= 20:
           print 'Capacity Reached!!'
           self.at_capacity = True
        else:
           self.at_capacity = False
        return self.at_capacity

class Member():

    def __init__(self, name, hair_color, birthdate, num_lines_coded = 0, coding_level = 'beginner'):
        self.name = name
        self.hair_color = hair_color
        self.birthdate = birthdate
        self.questions_asked = list()
        self.code_string = str()
        self.num_lines_coded = num_lines_coded
        self.coding_level = coding_level
        self.lines_of_code = list()

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def add_coded_line(self, code_string):
        self.lines_of_code.append(code_string)
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

class Instructor():
    def __init__(self, name, questions_answered=None):
        self.name = name
        self.questions_answered = questions_answered
        if self.questions_answered == None:
            self.questions_answered = list()

    def add_question_answered(self, question):
        self.questions_answered.append(question)
        

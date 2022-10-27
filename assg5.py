

class Assignment:
    def __init__(self,name,max_score):
        self.name = name 
        self.max_Score = max_score
        self.grade = None 
    def assign_grade(self,grade):
        # might need to fix this self.grade should this line be there? 
        self.grade = grade 
        if self.grade > self.max_Score:
            self.grade = None 
        else: 
            self.grade = self.grade 




class Student: 
    def __init__(self,id,first_name, last_name,assignments):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.assignments = assignments

    def get_full_name(self):
        self.full_name= str(self.first_name + ' ' +self.last_name)
        return self.full_name
        # print(self.full_name)
    
    def get_assignments(self):
        
        
        self.assignments = []
    
    def get_assignment(self,name):
        if self.assignments.count(name) > 0:
            return self.assignments(name)
        else:
            return 'None'
        # self.grade = int(grade)
        # self.max_score = int(max_score)
        
        print(self.assignments)
        return self.assignments
    def get_average(self):
        pass


student=Student(725,'kp','jk','7kp')
student.get_full_name()
student.get_assignment()
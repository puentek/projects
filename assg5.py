

class Assignment:
    def __init__(self,name,max_score):
        self.name = name 
        self.max_Score = max_score
        self.grade = None 
    def assign_grade(self,grade):
        
        self.grade = grade 
        if self.grade > self.max_Score:
            self.grade = None 
            # print(self.grade)
        else: 
            self.grade = self.grade
            # print(self.grade) 

assignment = Assignment('asign',10)
assignment.assign_grade(9)
# student has a list of assignment objects submited 
# 2 indepedent thingss
# list of assignmet 

class Student: 
    def __init__(self,id,first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.assignments = []
        

    def get_full_name(self):
        self.full_name= str(self.first_name + ' ' +self.last_name)
        return self.full_name
        # print(self.full_name)
    
    def get_assignments(self):
        return self.assignments.copy()
        
    
    # def get_assignment(self,name):
        # returns the number of elements in the list 
        
        # for i in self.assignments:
        #     if self.assignments == self.name:

                

        # if self.assignments.count(name) > 0:
        #     return self.assignments(name)
        # else:
        #     return 'None'

        # 
        # self.grade = int(grade)
        # self.max_score = int(max_score)
        
        # print(self.assignments)
        # return self.assignments
    def get_average(self):
        # start with zeros that get updated 
        i = 0
        scr = 0
        for assignment in range(len(self.assignments)):
            if self.assignments[assignment].grade != None:
                avg = self.assignments[assignment.grade]/self.assignments[assignment].max_score
                scr += avg 
                i += 1
        return scr/i 


    def submit_assignmet(self,assignment):
        self.assignments = [assignment]+self.assignments
   
    def remove_assignment(self,rem):
        lst = []
        for assignment in range(len(self.assignments)):
            lst.append(self.assignments[assignment].name)
        if rem in lst: 
            rem_assign = lst.index(rem)
            del self.assignments[rem_assign]
         


student=Student(725,'kp','jk','7kp')
# initializer with an empty list 
student.get_full_name()
student.submit_assignmet(assignment)


# student.get_assignment()
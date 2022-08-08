
class Departments:
    
    def __init__(self, _dept_name, _dept_id) -> None:
        self._Department_Name = _dept_name
        self._Department_ID   = _dept_id
    
    def getDepartmentInfo(self):
        print(f'Departemnt Name is : {self._Department_Name}')
        print(f'Department ID is : {self._Department_ID}')
    
    def _set_courses(self, course_1, course_2, course_3):
        self._course_1 = course_1
        self._course_2 = course_2
        self._course_3 = course_3

    def courses_info(self):
        print('Provided Courses are :{} , {} , {} '.format(self._course_1, 
                                                       self._course_2, self._course_3)
              )


# taking the initial inputs
print('Provide the Department Info you want to see!')

while True:

    dept_name = input('Enter the Department Name:')
    dept_id = input('Enter the Department ID:')
    print('=============================================================')
    
    if dept_name == 'CSE' and dept_id == '011':
        # creating the class instance
        cse_dept = Departments(dept_name, dept_id)
        
        print('\t\t Department Information')
        print('=============================================================')
        # getting departements information
        cse_dept.getDepartmentInfo()
        # setting the courses for the deparments
        print('=============================================================')
        print('\n\n')
        print('\t\tDepatment Provided Course Info')
        print('=============================================================')
        
        # set the courses for cse dept using protected _set_courses()
        cse_dept._set_courses(course_1='Algorithm', course_2='Network', course_3='Software')
        cse_dept.courses_info()
        print('=============================================================')
        print('\n\n')
    elif dept_name == 'EEE' and dept_id == '111':
        eee_dept = Departments(dept_name, dept_id)
        
        print('\t\tDepatment Provided Course Info')
        print('=============================================================')
        # getting departements information
        eee_dept.getDepartmentInfo()
        print('=============================================================')
        print('\n\n')
        
        print('\t\tDepatment Provided Course Info')
        print('=============================================================')
        # setting the courses for the deparments
        # set the courses for eee dept using protected _set_courses()
        eee_dept._set_courses(course_1='Power', course_2='Communication', course_3='Electronics')
        eee_dept.courses_info()
        print('=============================================================')
        print('\n\n')
    else:
        print('Exiting the Query Box')
        print('Provide the correct Info')
        exit()
    
      
    
    

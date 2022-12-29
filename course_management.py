class Course:
    """For storing information dictionary as object"""
    def __init__(self,course_code,course_title,course_credit,course_prerequisite):
        self.information = {}
        self.information['course_code'] = course_code
        self.information['course_title'] = course_title
        self.information['course_credit'] = course_credit
        self.information['course_prerequisite'] = course_prerequisite
        
user_interface_input = 0

def user_interface ():
    """Displaying Menu/User Interface"""
    print ("\nCOURSE MANAGEMENT SYSTEM\n")
    print ("1. Add Course")
    print ("2. Update Course")
    print ("3. Delete Course")
    print ("4. Show All Course")
    print ("5. Search Course")
    print ("6. Store Course Information To Text File\n")
    user_interface_input =input("Chose An Option From 1-6 Or Press quit To Exit : ")
    return user_interface_input

course_catalogue =[]

def check_prequisite(course_prerequisite):
    """Checking if the prerequisite exist or not"""
    for course in course_catalogue:
        if course_prerequisite in course.information['course_code']:
            return True
    return False

def add_course ():
    """To add new course in the course catalogue list"""
    print ("\n*** ADD NEW COURSE ***")
    course_code = input ("\nEnter Course Code : ")
    course_title = input ("Enter Course Name : ")
    course_credit = input ("Enter Course Credit Hour : ")
    course_prerequisite = input ("Enter Course Prerequisite : ")
    if course_prerequisite == 'N/A':
        course_catalogue.append (Course(course_code,course_title,course_credit,course_prerequisite))
        print ("\n*** Course Added ***")
    elif check_prequisite(course_prerequisite):
        course = Course(course_code,course_title,course_credit,course_prerequisite)
        course_catalogue.append(course)
        print ("\n*** Course Added ***")
    else:
        print ("\n*** Course Prerequisite Doesn't Exist, Add It First ***")
        add_course()

def update_course ():
    """Update Course Information"""
    print ("\n*** UPDATE COURSE ***")
    found = False
    course_code = input ("\nSearch the Course You want To Update, Search With Course Code: ")
    for course in course_catalogue:
        if course_code in course.information['course_code']:
            found = True
            print ("\n*** Course Found! Course Information ***\n")
            print (f"Course Code: {course.information['course_code']}")
            print (f"Course Name: {course.information['course_title']}")
            print (f"Course Credit Hour: {course.information['course_credit']}")
            print (f"Course Prerequisite: {course.information['course_prerequisite']}\n")
            print ("\n*** UPDATE INFORMATION ***\n")
            course.information['course_title']=input("Enter New Course Name: ")
            course.information['course_credit']=input("Enter New Credit Hour: ")
            course.information['course_prerequisite']=input("Enter New Prerequisite: ")

            print ("\n*** Course Updated ***")

    if(found==False):
        print("\n*** Sorry, Course doesn't exist ***")

   
def delete_course ():
    """Deleteing Course From Course Catalogue"""
    print ("\n*** DELETE COURSE ***")
    found = False
    course_code = input ("\nEnter Course Code of The Course To Be Deleted: ")
    for course in course_catalogue:
        if course_code in course.information['course_code']:
            found = True
            print ("\n*** Course Found! Course Information ***\n")
            print (f"Course Code: {course.information['course_code']}")
            print (f"Course Name: {course.information['course_title']}")
            print (f"Course Credit Hour: {course.information['course_credit']}")
            print (f"Course Prerequisite: {course.information['course_prerequisite']}\n")
            user_input_delete = input("Do You Want To Delete This Course, Press y To Delete The Course: ")
            if (user_input_delete == "y"):
                course_catalogue.remove (course)
                print ("\n*** Course Deleted ***")
    if(found==False):
        print("\n*** Sorry, Course doesn't exist ***")

def show_all_course ():
    """Display Information of All Course"""
    if len(course_catalogue)== 0:
        print ("\n*** Nothing To Show, Add Course ***")
    else:
        print ("\n*** Course Catalogue ***\n")
    for i in range(len(course_catalogue)):
        print (f"Course Code: {course_catalogue[i].information['course_code']}")
        print (f"Course Name: {course_catalogue[i].information['course_title']}")
        print (f"Course Credit Hour: {course_catalogue[i].information['course_credit']}")
        print (f"Course Prerequisite: {course_catalogue[i].information['course_prerequisite']}\n")

def search_course ():
    """Search Course And Displays Information If Found"""
    print ("\n*** SEARCH COURSE ***")
    found = False
    course_code = input ("\nEnter Course Code To Search: ")
    for course in course_catalogue:
        if course_code in course.information['course_code']:
            found = True
            print ("\n*** Course Found! Course Information ***\n")
            print (f"Course Code: {course.information['course_code']}")
            print (f"Course Name: {course.information['course_title']}")
            print (f"Course Credit Hour: {course.information['course_credit']}")
            print (f"Course Prerequisite: {course.information['course_prerequisite']}\n")
    if(found==False):
        print("\n*** Sorry, Course doesn't exist ***")
        add_course ()

    
def store_course_to_text ():
    """Store Course From System To A Text File"""
    file_name="course_catalogue.txt"
    with open(file_name,'w') as file_obj:
        for i in range(len(course_catalogue)):
            file_obj.writelines("\n")
            file_obj.writelines(f"Course Code: {course_catalogue[i].information['course_code']}\n")
            file_obj.writelines(f"Course Name: {course_catalogue[i].information['course_title']}\n")
            file_obj.writelines(f"Course Credit Hour: {course_catalogue[i].information['course_credit']}\n")
            file_obj.writelines(f"Course Prerequisite: {course_catalogue[i].information['course_prerequisite']}\n")
        print ("\n*** Course Information Stored ***")
   

user_interface_input = user_interface ()

while(user_interface_input != "quit"):

    if(user_interface_input == "1"):
        add_course()
        user_interface_input = user_interface ()
    elif(user_interface_input == "2"):
        update_course()
        user_interface_input = user_interface ()
    elif(user_interface_input == "3"):
        delete_course()
        user_interface_input = user_interface ()
    elif(user_interface_input == "4"):
        show_all_course()
        user_interface_input = user_interface ()
    elif(user_interface_input == "5"):
        search_course()
        user_interface_input = user_interface ()
    elif(user_interface_input == "6"):
        store_course_to_text()
        user_interface_input = user_interface ()
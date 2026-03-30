from models import students
def name():
        #where I ask to the client enter yhe name and valid the information with a.isalpha
        name_1=input("please enter the student name: ")
        if not name_1.isalpha():
            print("name not valid please try again")
            return name()
        else:
            return name_1
def new_name():
        #where I ask for the new name of the student and valid then with a .isalpha
        name_1=input("please enter a new name: ")
        if not name_1.isalpha():
            print("name not valid please try again")
            return new_name()
        else:
            return name_1
def age():
    #I ask for the age of the student and valid de age with if and try 
    try:
        age_1=int(input("please enter the student age: "))
        if age_1<0:
            print("invalid age please try again")
            return age()
        else:
            return age_1
    except ValueError:
        print("age not valid please try again")
        return age()
def new_age():
    #I ask for the new age of the student and valid de age with if and try 
    try:
        age_1=int(input("please enter a new age: "))
        if age_1<0:
            print("invalis age please try again")
            return new_age()
        else:
            return age_1
    except ValueError:
        print("de price not valid please try again")
        return new_age()
def grade_select():
    #where I print a list with all grades and the client choose I valid that option and return
    grade=["1°","2°","3°","4°","5°","6°","7°","8°","9°","10°","11°"]
    for i, op in enumerate(grade, start=1):
        print(f"{i}- {op}")    
    try:
        plan1=int(input("please enter the student grade: "))
        if plan1<0:
            print("invalid options please try again")
            return grade_select()
        elif plan1>11:
            print("invalid options please try again")
            return grade_select()
        else:
            return grade[plan1-1]
    except ValueError:
        print("invalid options please try again")
        return grade_select()
def new_grade_select():
    #where I print a list with all grades and the client choose the new grade
    grade=["1°","2°","3°","4°","5°","6°","7°","8°","9°","10°","11°"]
    for i, op in enumerate(grade, start=1):
        print(f"{i}- {op}")    
    try:
        plan1=int(input("please enter the new grade: "))
        if plan1<0:
            print("invalid options please try again")
            return new_grade_select()
        elif plan1>11:
            print("invalid options please try again")
            return new_grade_select()
        else:
            return grade[plan1-1]
    except ValueError:
        print("invalid options please try again")
        return new_grade_select()
def status():
    # where I ask for the status of the student
    status_1=["active","inactive"]
    for i, op in enumerate(status_1, start=1):
        print(f"{i}- {op}")    
    try:
        status1=int(input("please enter the status of your student: "))
        if status1<0:
            print("invalid options please try again")
            return status()
        elif status1>2:
            print("invalid options please try again")
            return status()
        else:
            return status_1[status1-1]
    except ValueError:
        print("invalid options please try again")
        return status()
def new_status():
    # and where the news one
    status_1=["active","inactive"]
    for i, op in enumerate(status_1, start=1):
        print(f"{i}- {op}")    
    try:
        status1=int(input("please enter the status for your plan: "))
        if status1<0:
            print("invalid options please try again")
            return new_status()
        elif status1>2:
            print("invalid options please try again")
            return new_status()
        else:
            return status_1[status1-1]
    except ValueError:
        print("invalid options please try again")
        return new_status()
def options():
    # i valid the menu options
    try:
        op_1=int(input("please enter a option: "))
        if op_1<0:
            print("invalis age please try again")
            return options()
        elif op_1>8:
            print("invalis age please try again")
            return options()
        else:
            return op_1
    except ValueError:
        print("de option selected are invalid please try again")
        return options()
def option_to_delete():
    try:
        op_1=int(input("please enter a option: "))
        if op_1<0:
            print("invalis age please try again")
            return option_to_delete()
        elif op_1>len(students):
            print("invalis age please try again")
            return option_to_delete()
        else:
            return op_1
    except ValueError:
        print("the option selected are invalid please try again")
        return option_to_delete()
def search_1():

    #where I valid the options for what index you want to search the student
    print("why index do you want to search?\n1. ID\n2. Name")
    try:
        op_1=int(input("please enter a option: "))
        if op_1<0:
            print("invalid option please try again")
            return search_1()
        elif op_1>2:
            print("invalis option please try again")
            return search_1()
        else:
            return op_1
    except ValueError:
        print("de option selected are invalid please try again")
        return search_1()
def search_id():
    try:
        op_1=int(input("please enter a ID: "))
        if op_1<100:
            print("invalid ID please try again")
            return search_id()
        elif op_1>999:
            print("invalid ID please try again")
            return search_id()
        else:
            return op_1
    except ValueError:
        print("the option selected are invalid please try again")
        return search_id()
def uptade_student():
    print("why index do you want to search?\n1. Name\n2. Age\n3. Grade\n4. status")
    try:
        op_1=int(input("please enter a option: "))
        if op_1<0:
            print("invalis age please try again")
            return uptade_student()
        elif op_1>4:
            print("invalis age please try again")
            return uptade_student()
        else:
            return op_1
    except ValueError:
        print("de option selected are invalid please try again")
        return uptade_student()
def show_students():
    if not students:
        print("not students register")
    else:
        print("\nstudents register are\n")
        for n,i in enumerate(students, start=1):
            print(f"{n}-students: ID-{i["ID"]}\nName| {i["name"]}| Age| {i["age"]}\nGrade| {i["grade"]}| Status| {i["status"]}\n")
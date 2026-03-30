from services import *
from models import students
from APP import *
import random
def menu():
    while True:
        option=["create student","list students","search students", "uptade student","delete student","save students", "upload students","exit"]
        print("---welcome to menu---")
        for i, op in enumerate(option, start=1):
            print(f"{i}- {op}")
        op_1=options()   
        if op_1 ==1:
            name_1=name()
            age_1=age()
            Grade=grade_select()
            status_1=status()
            id= random.randint(100,999)
            students.append({"ID":id,"name":name_1,"age":age_1,"grade":Grade,"status":status_1})
            print("student create correctly")
        elif op_1 ==2:
            show_students()
        elif op_1 ==3:
            ser = search_1()
            if ser ==1:
                print("please enter the ID that you want to search")
                searchs=search_id()
                result=None
                for i in students:
                    if i["ID"]==searchs:
                        result=i
                if result:
                    print(f"\nfound: ID-{result["ID"]}\nName| {result["name"]} Age| {result["age"]}\nGrade| {result["grade"]} Status| {result["status"]}")
                else:
                    print("not found")
            if ser == 2:
                print("please enter the name what you want search")
                searchs=name()
                result=None
                for i in students:
                    if i["name"]==searchs:
                        result=i
                if result:
                    print(f"found: ID-{result["ID"]}\nName| {result["name"]} Age| {result["age"]}\nGrade| {result["grade"]} Status| {result["status"]}")
                else:
                    print("not found")
        elif op_1==4:
            ser=uptade_student()
            show_students()  
            print("please enter the name of the student what you want to uptade")
            if ser ==1:
                search = str(name())
                new_nam = str(new_name())              
                try:
                    for i in students:
                        if i["name"] == search:
                            i["name"] = new_nam
                            c=i
                        elif c:
                            print(f"client uptade correctly: {c["name"]}")
                        else:
                            print("not found") 
                        
                except:
                        print("not found") 
            elif ser ==2:
                search = str(name())
                new_ag=int(new_age())   
                try:             
                    for i in students:
                        if i["name"] == search:
                            i["age"] = new_ag
                            c=i                        
                        elif c:
                            print(f"client uptade correctly: {c["age"]}")
                        else:
                            print("not found")
                except:
                    print("not found") 
            elif ser == 3:
                search = str(name())
                print("please select the new garde of the student")
                new_grade = str(new_grade_select())                
                try:
                    for i in students:
                        if i["name"] == search:
                            i["grade"] = new_grade
                            c=i                            
                        elif c:
                            print(f"client uptade correctly: {c["plan"]}")
                        else:
                            print("not found")     
                except:
                    print("not found")
            elif ser ==4:
                search = str(name())
                new_statu = str(status())                
                try:
                    for i in students:
                        if i["name"] == search:
                            i["status"] = new_statu                            
                            c=i
                        elif c:
                            print(f"client uptade correctly: {c["status"]}")
                        else:
                            print("not found")
                except:print("not found") 
        elif op_1 ==5:
            show_students()
            print("what client do you want to delete")
            op=option_to_delete()
            students.pop(op-1)
        elif op_1 ==6:
            save_students()
            print("clients save correctly")
        elif op_1 ==7:
            upload_students()
            print("upload made corectly")
        elif op_1==8:
            print("thanks to use exits correctly...")
            exit()

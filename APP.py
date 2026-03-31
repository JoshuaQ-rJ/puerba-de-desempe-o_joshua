import csv
from models import students
def save_students():
    #where I create and write in the life .csv
    if not students:
        print("not students register")
    else:
        with open("data/data.csv", "w", newline="", encoding="utf-8") as f:
            write = csv.DictWriter(f, fieldnames=["ID","name", "age", "grade", "status" ])
            write.writeheader()
            write.writerows(students)
save_students()
def read_register():
    #where I read the .csv document and return a list 
    with open("data/data.csv","r",newline="", encoding="utf-8") as read:
        reads=csv.DictReader(read)
        return list(reads)
def upload_students():
    # where I put in the list all thinks we are in the .csv
    registers=read_register()
    if len(registers)==0:
        print("no are register, please save and try again")
        return False
    with open("data/data.csv","r",newline="", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        for r in reader:
            name_1=r["name"]
            age_1=int(r["age"])
            Grade=r["grade"]
            status_1=r["status"]
            id=int(r["ID"])
            students.append({"ID":id,"name":name_1,"age":age_1,"grade":Grade,"status":status_1})
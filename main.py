import firebase_admin
from firebase_admin import db
import communication
from communication import send_notification
import time
import random
import os


cred_obj = firebase_admin.credentials.Certificate('co-flower-firebase-adminsdk-oo196-1e4ae65dc7.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL':'https://co-flower-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference("/students")
students = ref.get()
surnames = students['surnames'].split(',')
print(surnames)
picked_surnames = []
sent = False


def pick_student():
    student = ""
    while student == "":
        student = random.choice(surnames)
        if student in picked_surnames:
            student = ""
    picked_surnames.append(student)
    return student


def pick_random_group():
    global picked_surnames
    student1 = pick_student()
    student2 = pick_student()
    student3 = None
    if len(surnames) - len(picked_surnames) == 1:
        student3 = pick_student()
        picked_surnames = []

    return student1, student2, student3


run = True
notifi = ""
while run:
    ref = db.reference("/plant_data")
    data = ref.get()
    moisture = int(data['moisture'])
    airtemperature = float(data['airtemperature'])
    print(str(moisture) + "\n" + str(airtemperature))

    need_help = False
    if moisture < 40:
        notifi += "Roslina nie ma wody. \n"
        need_help = True
    elif airtemperature < 20:
        notifi += "Roslince jest zimno. \n"
        need_help = True
    elif airtemperature > 30:
        notifi += "Roslince jest goraco. \n"
        need_help = True

    elif moisture >= 2 and airtemperature >= 20:
        sent = False

    if need_help is True and sent is False:
        group = pick_random_group()
        names = ""
        for name in group:
            if name is not None:
                names += name + ", "

        final_names = names[:-2]

        notifi += "Wybrano uczniow: " + final_names

        sent = True
        print("Wysylam powiadomienie " + notifi + ".")
        communication.send_notification(notifi, os.getenv('CHID'))
    notifi = ""
    time.sleep(5)

"""בפייתון, ישנן מספר פקודות שאתה יכול להשתמש בהן כדי לעבוד עם קבצים. הן מחולקות למספר מצבים של גישה:

1. `'r'`: פתיחת קובץ לקריאה בלבד. המצביע ממוקם בתחילת הקובץ.
2. `'w'`: פתיחת קובץ לכתיבה. אם הקובץ קיים, הנתונים מוחקים ונכתבים מחדש.
3. `'a'`: פתיחת קובץ להוספה. המצביע ממוקם בסוף הקובץ.
4. `'r+'`: פתיחת הקובץ לקריאה ולכתיבה.
5. `'w+'`: פתיחת הקובץ לקריאה ולכתיבה. אם הקובץ קיים, הנתונים מוחקים ונכתבים מחדש.
6. `'a+'`: פתיחת הקובץ לקריאה ולהוספה.
7. `'x'`: יצירה בלעדית של קובץ. אם הקובץ כבר קיים, הפונקציה `open()` תזרוק חריגה מסוג `FileExistsError`.

ההבדלים בין המצבים הם בפעולות שאפשר לבצע עם הקובץ (קריאה, כתיבה, הוספה) ובמה שקורה כאשר הקובץ נפתח (האם הנתונים מוחקים, האם המצביע ממוקם בתחילת הקובץ או בסוף הקובץ, האם ניתן ליצור קובץ חדש).
"""

class Contacts:
    def __init__(self):
        contacts = "contacts.txt"
        self.name = input()
        self.email = input()

    def file_create(self):
        with open("contacts.txt", mode="x") as file:
            file.write("I am Groot!")

    def add_contact(self):
        with open("contacts.txt", mode="a") as file:
            file.write(self.name + self.email + "\n")

contacts = Contacts
#Contacts.file_create(contacts)
contacts.add_contact(contacts)
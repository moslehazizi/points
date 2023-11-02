import csv
from accounts.models import CustomUser
from pages.models import Person

def run():
    fhand = open('csvFiles/UserInfo_1.csv')
    reader = csv.reader(fhand)
    next(reader)

    CustomUser.objects.filter(is_staff=False).delete()
    Person.objects.all().delete()

    for row in reader:
        print(row)

        u, created = CustomUser.objects.get_or_create(username=row[0], email=row[1], password=row[2], first_name=row[3], 
                        last_name=row[4], )
        r = Person.STUDENT
        if row[5] == 'T' : r = Person.TEACHER

        p = Person(person=u, father_name=row[7], phone_number=row[8], role=r)

        p.save()
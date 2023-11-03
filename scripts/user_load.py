import csv
from accounts.models import CustomUser
from pages.models import Person
from django.contrib.auth.hashers import make_password

def run():
    fhand = open('csvFiles/UserInfo_1.csv')
    reader = csv.reader(fhand)
    next(reader)

    CustomUser.objects.filter(is_staff=False).delete()
    Person.objects.all().delete()

    for row in reader:
        print(row)
        
        u, created = CustomUser.objects.get_or_create(username=row[0], email=row[1],
                                                       first_name=row[3], last_name=row[4])
        CustomUser.password = CustomUser.set_password(u, raw_password=str(row[2]))      
        r = Person.STUDENT
        if row[5] == 'T' : r = Person.TEACHER

        
        p = Person(person=u, father_name=row[6], phone_number=row[7], role=r)
        p.save()
        u.save()
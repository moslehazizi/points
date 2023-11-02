import csv
from accounts.models import CustomUser
from pages.models import StudentPresent, Course, DayDate

def run():
    fhand = open('csvFiles/DayInfo_3.csv')
    reader = csv.reader(fhand)
    next(reader)

    StudentPresent.objects.all().delete()

    for row in reader:
        print(row)

        c, created = Course.objects.get_or_create(name=row[0])
        s, created = CustomUser.objects.get_or_create(username=row[1])
        o, created = CustomUser.objects.get_or_create(username=row[2])

        sd = StudentPresent(course=c, student=s, owner=o, day=row[3])

        sd.save()
    
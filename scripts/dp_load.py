import csv
from accounts.models import CustomUser
from pages.models import StudentPresent, Course, DayDate

def run():
    fhand = open('csvFiles/DpInfo_4.csv')
    reader = csv.reader(fhand)
    next(reader)

    DayDate.objects.all().delete()

    for row in reader:
        print(row)

        c, created = Course.objects.get_or_create(name=row[1])
        o, created = CustomUser.objects.get_or_create(username=row[2])

        for pd in StudentPresent.objects.filter(day=row[0]):
            pd, created = StudentPresent.objects.get_or_create(day=row[0])
        d = DayDate(day=row[0], course=c, owner=o)

        d.save()
        d.present_state.add(pd)

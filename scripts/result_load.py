import csv
from accounts.models import CustomUser
from pages.models import Result, Course

def run():
    fhand = open('csvFiles/ResInfo_5.csv')
    reader = csv.reader(fhand)
    next(reader)

    Result.objects.all().delete()

    for row in reader:
        print(row)

        c, created = Course.objects.get_or_create(name=row[0])
        o, created = CustomUser.objects.get_or_create(username=row[2])
        s, created = CustomUser.objects.get_or_create(username=row[3])

        r = Result(course=c, date=row[1], owner=o, student_select=s)

        r.save()
    
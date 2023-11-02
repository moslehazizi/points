import csv
from accounts.models import CustomUser
from pages.models import Course

def run():
    fhand = open('csvFiles/CourseInfo_2.csv')
    reader = csv.reader(fhand)
    next(reader)

    Course.objects.all().delete()

    for row in reader:
        print(row)
        o, created = CustomUser.objects.get_or_create(username=row[1])
        for s in CustomUser.objects.filter(username=row[2]):
            s, created = CustomUser.objects.get_or_create(username=row[2])
        c = Course(name=row[0], description=row[3], owner=o)
        
        c.save()
        c.student.add(s)

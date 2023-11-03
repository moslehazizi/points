import csv
from accounts.models import CustomUser
from pages.models import Test, Course, Result

def run():
    fhand = open('csvFiles/ExamInfo_6.csv')
    reader = csv.reader(fhand)
    next(reader)

    Test.objects.all().delete()

    for row in reader:
        print(row)

        c, created = Course.objects.get_or_create(name=row[1])
        o, created = CustomUser.objects.get_or_create(username=row[2])

        for r in Result.objects.filter(date=row[3]):
            r, created = Result.objects.get_or_create(date=row[3])
        e = Test(title=row[0], course=c, owner=o, day=row[3])

        e.save()
        e.result.add(r)
        
        

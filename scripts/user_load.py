import csv
from accounts.models import CustomUser

def run():
    fhand = open('csvFiles/UserInfo1.csv')
    reader = csv.reader(fhand)
    next(reader)

    CustomUser.objects.filter(is_staff=False).delete()

    for row in reader:
        print(row)
        ui = CustomUser(username=row[0], email=row[1], password=row[2], first_name=row[3], 
                        last_name=row[4], )
        ui.save()
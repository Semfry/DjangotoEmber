import csv
from mypages.models import modeltimerecordscsvs, modeltotalhours

with open("basepandastimerecords.csv") as f:
    reader = csv.reader(f)
    next(reader, None)  # skip the headers
    for row in reader:
        _, created = modeltimerecordscsvs.objects.get_or_create(
            date=row[0],
            user=row[1],
            minutes=row[2],
            ticket=row[3],
            code=row[4],
            billable=row[5],
        )

with open("totalhours.csv") as f:
    reader = csv.reader(f)
    next(reader, None)  # skip the headers
    for row in reader:
        _, created = modeltotalhours.objects.get_or_create(
            user=row[0],
            totalminutes=row[1],
            totalhours=row[2],
        )

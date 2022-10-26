import csv
from mypages.models import modeltimerecordscsvs

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

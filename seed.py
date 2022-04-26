from models import *
import datetime

db.connect()
db.drop_tables([Cohort, Student])
db.create_tables([Cohort, Student])

Cohort(name='Cosmic Binturongs', cohort_type='SEI',
       start_date=datetime.date(2022, 2, 15)).save()
Cohort(name='Banana Kings', cohort_type='SEI',
       start_date=datetime.date(2018, 11, 6)).save()

Student(name='Eric', age=26, cohort_id=1).save()
Student(name='Mustafa', age=19, cohort_id=1).save()
Student(name='Kevin', age=23, cohort_id=1).save()
Student(name='Lawrence', age=31, cohort_id=1).save()
Student(name='George', age=30, cohort_id=1).save()
Student(name='Mike', age=20, cohort_id=1).save()
Student(name='Jefe', age=29, cohort_id=1).save()
Student(name='Cat', age=100, cohort_id=2).save()
Student(name='Dog', age=77, cohort_id=2).save()

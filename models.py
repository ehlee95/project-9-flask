from peewee import *

db = PostgresqlDatabase('generalassembly', user='ericlee',
                        password='password', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Student(BaseModel):
    name = CharField()
    age = IntegerField()
    cohort_id = IntegerField()


class Cohort(BaseModel):
    name = CharField()
    cohort_type = CharField()
    start_date = DateTimeField()

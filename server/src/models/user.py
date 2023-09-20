from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    surname = fields.CharField(max_length=255)
    login = fields.CharField(max_length=16)
    password = fields.CharField(max_length=255)
    role = fields.CharField(max_length=10)

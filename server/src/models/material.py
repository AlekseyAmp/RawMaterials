from tortoise.models import Model
from tortoise import fields


class Material(Model):
    id = fields.IntField(pk=True)
    added_date = fields.CharField(max_length=10)
    material_name = fields.CharField(max_length=50)
    iron_content = fields.FloatField()
    silicion_content = fields.FloatField()
    aluminum_content = fields.FloatField()
    calcium_content = fields.FloatField()
    sulphur_content = fields.FloatField()

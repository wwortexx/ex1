from PIL.Image import Image
from django.db.models import AutoField, Model, TextField, FileField

# Create your models here.
from django.forms import forms


class MImg(Model):
    id = AutoField(primary_key=True)
    path = TextField()
    content = FileField(upload_to='images/', null=True)
    name = TextField()


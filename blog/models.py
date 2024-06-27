from django.db.models import (
    Model, 
    CharField, 
    TextField,
    DateTimeField,
)

class Post(Model):
    title = CharField(max_length=200)
    content = TextField()
    author = CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.title}'

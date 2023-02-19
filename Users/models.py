from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    sms=models.TextField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()


class Todo(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    deadline=models.DateTimeField()
    notifications=models.IntegerField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    user_ID=models.ForeignKey(User,on_delete=models.CASCADE)


class Category(models.Model):
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Comment(models.Model):
    body=models.TextField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    user_ID=models.ForeignKey(User,on_delete=models.CASCADE)
    todo_ID=models.ForeignKey(Todo,on_delete=models.CASCADE)


class Todo_category(models.Model):
    todo_ID=models.ForeignKey(Todo,on_delete=models.CASCADE)
    category_ID=models.ForeignKey(Category,on_delete=models.CASCADE)





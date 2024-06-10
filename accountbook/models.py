from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    bgcolor = models.CharField(max_length=7)
    # accountbook_set : 해당 category와 연결되어있는 accountbook 여러개를 가져온다.

    def __str__(self):
        return f'{self.name}: {self.bgcolor}'

class Meta:
    verbose_name_plural = 'categories' # 복수형 단어 설정

class AccountBook(models.Model):
    TYPE_CHOICES = [
        (0, '지출'),
        (1, '소비'),
    ]

    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=0)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time = models.DateTimeField()
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.type}{self.price}{self.category}{self.time}'
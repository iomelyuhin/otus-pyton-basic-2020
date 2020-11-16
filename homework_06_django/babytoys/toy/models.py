from django.db import models


class Category(models.Model):
    # Категория товара - напр. "Книжки 21*21см"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Element(models.Model):
    # Элемент товара - напр. "Странички"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    # Карточка товара - напр. "Кукольный домик"
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='goods', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    image = models.ImageField(upload_to='goods')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.card} - {self.image}'

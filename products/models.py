from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Phone(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    description = models.TextField(blank=False, null=False)
    slug = AutoSlugField(populate_from="name")
    price = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.name}"


class Notebook(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    description = models.TextField(blank=False, null=False)
    slug = AutoSlugField(populate_from="name")
    price = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.name}"


class Tablet(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    description = models.TextField(blank=False, null=False)
    slug = AutoSlugField(populate_from="name")
    price = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.name}"
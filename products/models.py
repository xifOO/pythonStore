from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Phone(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    image = models.ImageField(upload_to="products", blank=False, null=False, verbose_name="phone_image")
    description = models.TextField(blank=False, null=False)
    slug = AutoSlugField(populate_from="name")
    price = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('acticle_detail', kwargs={'slug': self.slug})


class Notebook(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    image = models.ImageField(upload_to="products", blank=False, null=False, verbose_name="notebook_image")
    description = models.TextField(blank=False, null=False)
    slug = AutoSlugField(populate_from="name")
    price = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('acticle_detail', kwargs={'slug': self.slug})


class Tablet(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Category")
    image = models.ImageField(upload_to="products", blank=False, null=False, verbose_name="tablet_image")
    description = models.TextField(blank=False, null=False)
    slug = AutoSlugField(populate_from="name")
    price = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('acticle_detail', kwargs={'slug': self.slug})
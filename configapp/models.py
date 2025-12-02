from django.db import models
from django.utils.text import slugify


# Create your models here.

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=100)
    employee = models.CharField(max_length=100, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    required_date = models.DateField(blank=True, null=True)
    shipped_date = models.DateField(blank=True, null=True)
    ship_via = models.CharField(max_length=100, blank=True, null=True)
    freight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ship_name = models.CharField(max_length=100, blank=True, null=True)
    ship_address = models.CharField(max_length=200, blank=True, null=True)
    ship_city = models.CharField(max_length=100, blank=True, null=True)
    ship_region = models.CharField(max_length=100, blank=True, null=True)
    ship_postal_code = models.CharField(max_length=20, blank=True, null=True)
    ship_country = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.employee)
            slug = base_slug
            counter = 1

            while Order.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.ship_name


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contact_title = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.company_name)
            slug = base_slug
            counter = 1

            while Customer.objects.filter(slug=slug):
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name


class Employees(models.Model):
    employees_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    title_of_courtesy = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    home_phone = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=100, null=True, blank=True)
    notes = models.CharField(max_length=100, null=True, blank=True)
    reports_to = models.IntegerField()
    photo_path = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.last_name)
            slug = base_slug
            counter = 1

            while Employees.objects.filter(slug=slug):
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.last_name
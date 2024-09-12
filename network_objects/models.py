from django.db import models

NULLABLE = {"null": True, "blank": True}

class Product(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Введите название продукта"
    )
    model = models.TextField(
        verbose_name="Модель",
        help_text="Введите название модели",
        **NULLABLE
    )
    release_date = models.DateTimeField(
        verbose_name="дата выхода",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Supplier(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="название", help_text="Укажите название поставщика"
    )
    email = models.EmailField(verbose_name="email", **NULLABLE)
    country = models.TextField(verbose_name="Страна", **NULLABLE)
    city = models.TextField(verbose_name="Город", **NULLABLE)
    street = models.TextField(verbose_name="Улица", **NULLABLE)
    house_number = models.TextField(verbose_name="Номер дома", **NULLABLE)
    product = models.ManyToManyField(Product, verbose_name='Продукт')
    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name="Задолженность", **NULLABLE)

    release_date = models.DateTimeField(
        auto_now=True,
        verbose_name="дата создания",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

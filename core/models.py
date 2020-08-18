from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='Plate', blank=True, null=True)
    state = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ['name']

class Item(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item')
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='item', blank=True, null=True)
    state = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['name']

class Table(models.Model):
    number = models.CharField(max_length=2, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.number

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'
        ordering = ['number']

class Order(models.Model):
    state_type = (
        ('In Order', 'in order'),
        ('Paid Out', 'paid out'),
        ('cancelled', 'cancelled')
    )
    number_order = models.CharField(max_length=20, blank=True, null=True)
    date_order = models.DateTimeField()
    state = models.CharField(max_length=20, choices=state_type)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='order')

    def __str__(self):
        return '%s  %s' % (self.number_order, self.state)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['date_order']

class OrderDetail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='orderdetail_item')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderdetail_order')
    quantity = models.IntegerField()

    def __str__(self):
        return '%s ' % self.order.number_order

    class Meta:
        verbose_name = 'OrderDetail'
        verbose_name_plural = 'OrderDetails'
        ordering = ['id']
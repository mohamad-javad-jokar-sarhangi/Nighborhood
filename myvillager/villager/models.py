from django.db import models

class User(models.Model):
    """
    کلاس پایه برای تمام کاربران (روستایی، راننده، رهبر، فروشنده)
    """
    USER_ROLES = [
        ('villager', 'Villager'),
        ('driver', 'Driver'),
        ('leader', 'Leader'),
        ('seller', 'Seller'),
    ]
    id = models.AutoField(primary_key=True)  # کلید اصلی
    first_name = models.CharField(max_length=50)  # نام
    last_name = models.CharField(max_length=50)  # نام خانوادگی
    phone_number = models.CharField(max_length=15)  # شماره تماس
    role = models.CharField(max_length=20, choices=USER_ROLES, default='villager')  # نقش کاربر

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Villager(models.Model):
    """
    کلاس برای روستاییان
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Villager)"

    class Meta:
        verbose_name = "Villager"
        verbose_name_plural = "Villagers"


class Driver(models.Model):
    """
    کلاس برای رانندگان
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20, blank=True, null=True)  # شماره گواهینامه

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Driver)"

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Leader(models.Model):
    """
    کلاس برای رهبران (دهیار/شورا)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, blank=True, null=True)  # سمت

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Leader)"

    class Meta:
        verbose_name = "Leader"
        verbose_name_plural = "Leaders"


class Seller(models.Model):
    """
    کلاس برای فروشندگان
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100, blank=True, null=True)  # نام فروشگاه

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Seller)"

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"

from django.db import models

def generate_primary_key():
	return uuid.uuid4().hex

# Create your models here.
class Base(models.Model):
	id = models.CharField(primary_key=True, default=generate_primary_key, unique=True)
	name = models.CharField(max_length=25, unique=True, blank=True)

	class Meta:
		abstract: True

class Brand(models.Model):

	def __str__(self):
		return self.name
class Position(models.Model):
	
	def __str__(self):
		return self.name

class ProductType(models.Model):

	def __str__(self):
		return self.name

class Product(Base):
	""" id = models.CharField(primary_key=True, default=generate_primary_key, unique=True)
	name = models.CharField(max_length=25, unique=True, blank=True) """
	quantity = models.IntegerField(default=0)
	photo = models.ImageField(upload_to='warehouseMedia')
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False)
	position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False)
	type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=False)
	




from django.db import models

# Create your models here.
class Product(models.Model):
    code = "code"
    name = "name"
    description = "description"
    price = 0
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        # 생성될 때 stock quantity를 0으로 초기화 로직
        pass

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'code', 'description', 'price', 'size']
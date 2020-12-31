from django.db import models

# Create your models here.
recipes = {
        "bread,bread,bread,bread": 'loaf_of_bread',
        "lettuce,lettuce,lettuce,lettuce": 'cabbage',
        "prawn,prawn,prawn,prawn": 'seriously_huge_prawn',
        "bread,prawn,prawn,prawn": 'cereal_prawn',
        "bread,bread,prawn,prawn": 'breaded_prawn',
        "bread,bread,lettuce,prawn": 'ebi_burger',
        "bread,lettuce,prawn,prawn": 'double_ebi_burger',
        "bread,bread,bread,prawn": 'prawn_pizza',
        "bread,lettuce,lettuce,lettuce": 'vegetable_wrap',
        "lettuce,lettuce,lettuce,prawn": 'thai_prawn_salad',
        "lettuce,lettuce,prawn,prawn": 'vietnamese_spring_rolls',
        "lettuce,prawn,prawn,prawn": 'prawn_and_papaya_salad',
        "bread,lettuce,lettuce,prawn": 'shrimp_salad_rolls',
        "bread,bread,lettuce,lettuce": 'seaweed_bread',
        "bread,bread,bread,lettuce": 'wholemeal_bread',
    }
class Recipes(models.Model):
    name = models.CharField(max_length=256)
    ingredients = models.TextField()
    product_img = models.TextField()

    @classmethod
    def _create_data(cls):
        for key,value in recipes.items():
            Recipes.objects.create(name = value,ingredients=key,product_img='backend_api/recipes/'+value+'.jpg')
    @classmethod
    def _delete_data(cls):
        Recipes.objects.all().delete()




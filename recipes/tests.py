from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe

class RecipeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='password')
        testuser1.save()

        testpost = Recipe.objects.create(
            author=testuser1,
            title='Pasta',
            body='Pasta recipe.',
        )
        testpost.save()
    
    def test_recipe_content(self):
        recipe = Recipe.objects.get(id=1)
        actual_author = str(recipe.author)
        actual_title = str(recipe.title)
        actual_body = str(recipe.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'Pasta')
        self.assertEqual(actual_body, 'Pasta recipe.')
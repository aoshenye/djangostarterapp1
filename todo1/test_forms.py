from django.test import TestCase
from .forms import Itemform


class TestItemform(TestCase):

        def test_item_name_is_required(self):
            form = Itemform({'name': ''})
            self.assertFalse(form.is_valid())
            self.assertIn('name', form.errors.keys())
            self.assertEqual(form.errors['name'](0), 'This field is required.')

        def test_done_field_is_not_required(self):
            form = Itemform({'name': 'Test Todo Item'})
            self.assertTrue(form.is_valid())

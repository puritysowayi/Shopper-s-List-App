from unittest import TestCase
from classes.shopping_list import Shopping_list

class TestShopping_list(TestCase);
	def setUp(self):
		self.shopping_list = Shopping_list(name)

	def test_empty_name(self):
		self.assertTrue(
			self.shopping_list.add_item(["name"]),"invalid item name"
		
		)

	def test_item_name_is_string(self):
		self.assertIsInstance(self.shopping_list.item_name, str)

	def test_shopping_list_is_list(self):
		self.assertIsInstance(self.shopping_list.item names, list)

	def test_update_missing_list_name(self):
		self.assertTrue(self.shopping_list.update(None),"Enter list name")

	def test_create_new_list(self):
		self.shopping_list.update("new_list")
		self.assertEqual(
			self.shopping_list.list_name, "new list"
		)
	def test_remove_item(self):
		self.shopping_list.add_item("word")
		item_to_delete = self.shopping_list.add_item("Test")

		self.assertTrue(
			self.shopping_list.remove_item(item_to_delete), "Deleted"
		)
		
	
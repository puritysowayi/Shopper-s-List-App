import unittest
 
 class TestItem(unittest.TestCase):
 	"""docstring for item_unuttests"""
 	def test_name_is_string(self, name):

 		self.assertIsInstance(self.name,str), "invalid item name"

 	def test_item_name_is_not_empty(self);

 		self.assertTrue(self.name.update(None), "invalid item name"

 	
 	def test_method_updates(self):
 	 	test_method_updates(self);

 		self.update("new name")
 		self.assertEqual(self.name,"new name")


 	if __name__ == '__main__':
    unittest.main()


 		
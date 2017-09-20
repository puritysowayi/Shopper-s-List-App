class Item(object):

	def __init__(self, name):

		"""
			Function initializes an instance of class item
			Attribute:
				name(str): Name of item to be added to list
		"""
		self.name = name

	def update(self, name):

		"""
			Function adds items to the shopping list.

		"""
		item_names = []
		if name is None:
			return "Invalid item name"
		elif not isinstance(name, str):
			return "invalid item name"
		elif:
			item_names.append(name)

			return item_names

	
		

		

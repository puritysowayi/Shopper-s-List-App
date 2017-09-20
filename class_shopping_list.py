import Item

class Shopping_list(object):
	def __init__(self,list_name):

		"""
			Attribute:

			list_name (str) or []: A label for an existing shopping 
			list.
			item_name (str): A name for a single product on the  shopping list
		"""
		#making local variables accessible outside the class

		self.list_name = list_name
		self.item_names = []        #attribute "item_name" inherited from class item

		def add_item(self, item_name):
			""" Appends a new item onto an existing shopping list

			Attribute:
				item_name: A new item meant to be appended to the 
				shopping list
			"""
			if item_name is None:
				return "invalid item name"

			if not isinstance(item_name, str):
				return "invalid item name"

				#creates a new instance of class item
				new_item = Item(item_name)
				self.item_names.append(new_item)

		def create_list(self):
			""" creates a new shopping list of items
			 Attribute:
			 	self: an instance of class shopping list
			"""
			new_list = []
			for item_name in self.item_names:
				new_list.append(item_name)
			return new_list


		def delete_item(self, item_name):
			""" Function deletes an item from the shopping list
				Attribute:
				item_name (str): The name of the item to be removed 
				from list"""
				#if item name is not an instance of the shopping list:

			if not isinstance(item_name, self.item_names): 
				return "Item not found"

			else:
				count = 0
				for item_name in self.item_names:
					if item_name == item_name:
						self.item_names.pop(count)
							del item_name
							return True
							count += 1







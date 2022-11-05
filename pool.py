class Question:

	def __init(self, row):
		self.question = row[0]
		self.mark = row[1]
		self.answer = row[2]
		self.explanation = row[3]
		self.options = []
		self.type = "question"

class TextBlock:

	def __init__(self, row):
		self.type = "text_block"
		self.random_show = row[1]
		self.children = None


class Options:

	def __init__(self, row):
		if row[0] == "":
			self.option = row[1]
		else:
			self.answer = row[1]

class Pool:

	def __init__(self, row):
		self.type = "pool"
		self.random_show = "100%"
		self.children = []

	# def addChildren(self, data, type, level):
	# 	if data == None and type == "end":
	# 		pass
	# 	# qs.append(structure.pop())

	# 	if type == "pool":
	# 		if len(self.children) < 1:
	# 			self.children.append(data)
	# 		else:
	# 			children = None

	def get_children(self):
			childrens = []
			for item in self.children:
				try:
					if item.type == "group" or item.type == "pool":
						childrens.append(item.get_children())
					else:
						childrens.append(item)
				except:
					childrens.append(item)
			return childrens

	def serialize(self):
		return {
			"type": self.type,
			"random_show": self.random_show,
			"children": self.get_children()
		}
	def __str__(self):
		return f"'type' : {self.type}, 'random_show' : {self.random_show}, 'children' : {self.get_children()}"


class Group:

	def __init__(self, row):
		self.type = "group"
		self.children = []

	def get_children(self):
			childrens = []
			for item in self.children:
				try:
					if item.type == "group" or item.type == "pool":
						childrens.append(item.get_children())
				except:
					childrens.append(item)
			return childrens


	
	def serialize(self):

		return {
			"type": self.type,
			"children": self.get_children()
		}

	def __str__(self):
		return f"{self.type} {self.get_children()}"
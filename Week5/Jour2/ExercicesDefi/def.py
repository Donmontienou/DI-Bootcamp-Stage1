from os import system
class pagintation():
	def __init__(self,items=[],pageSize=10):
		self.items=items
		self.pageSize=pageSize

	def getVisibleItems(self):
		
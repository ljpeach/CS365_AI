'''
AI lab1
'''
class Node:
		
		__slots__ = '_element', '_parent'

		def __init__(self, element, parent=None):
			self._element = element
			self._parent = parent
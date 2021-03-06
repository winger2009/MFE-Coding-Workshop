class Student:
	def __init__(self, name):
		self.name = name


class UCBMFE(Student):
	@property  # this allow us to call like: `student.showGPA`, instead of `student.showGPA()`
	def showGPA(self):
		return 4.0

class CMUMFE(Students):
	@property
	def show_GPA(self): # inconsistent naming!
		return 3.9 

# we want 1) consistnet GPA retrival, 2) Student cannot be innitialized

from abc import ABC, abstractmethod

class Student(ABC):
	def __init__(self, name):
		self.name = name

	@abstractmethod
	@property
	def showGPA(self):
		pass

class UCBMFE(Student):
	@property
	def showGPA(self):
		return 4.0

class CMUMFE(Students):
	@property
	def show_GPA(self): # inconsistent naming!
		return 3.9 

s1 = UCBMFE('Frank Xia')
# s2 = CMUMFE('Random Name') # fail! need to implement `showGPA`!
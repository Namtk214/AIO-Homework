#EXERCISE 1
# import torch
# import torch.nn as nn
# data = torch.Tensor([1, 2, 3])
# data
# soft_max = nn.Softmax(dim=0)
# print(soft_max(data))
# class StableSoftmax(nn.Module):
#   def __init__(self):
#     super().__init__()
#   def forward(self, x):
#     c = torch.max(x, dim=0, keepdim=True) #???
#     x_exp = torch.exp(x - c.values)     #>???
#     total = x_exp.sum(0, keepdim=True)
#     return x_exp / total
# bien = StableSoftmax()
# print(bien(data))

#EXERCISE 2:
from abc import ABC, abstractmethod

class Person(ABC):
  def __init__(self, name, yob):
    self._name = name
    self._yob = yob
  @abstractmethod
  def describe(self):
    pass

  def get_yob(self):
    return self._yob

class Student(Person):
  def __init__(self, name, yob, grade):
    super().__init__(name, yob)
    self.__grade = grade
  def describe(self):
    print(f"Student - Name:{self._name} - YOB:{self._yob} - Grade:{self.__grade}")

student1 = Student("Nam", 2005, 12)
student1.describe()

class Doctor(Person):
  def __init__(self, name, yob, specialist):
    super().__init__(name, yob)
    self.__specialist = specialist
  def describe(self):
    print(f"Doctor - Name:{self._name} - YOB:{self._yob} - Specialist:{self.__specialist}")

docror1 = Doctor("Nam", 2005, "Endocrinologists")
docror1.describe()

class Teacher(Person):
  def __init__(self, name, yob, subject):
    super().__init__(name, yob)
    self.__subject = subject
  def describe(self):
    print(f"Teacher - Name:{self._name} - YOB:{self._yob} - Subject:{self.__subject}")

teacher1 = Teacher("Nam", 2005, "Math")
teacher1.describe()

class Ward:
  def __init__(self, name):
    self.__name = name
    self.__list_people = list()

  def add_person(self, person):
    self.__list_people.append(person)

  def describe(self):
    print(f"Ward: {self.__name}")
    for person in self.__list_people:
      person.describe()

  def count_doctor(self):
    count = 0
    for person in self.__list_people:
      if isinstance(person, Doctor):
        count += 1
    return count

  def sort_yob(self):
    self.__list_people.sort(key = lambda x: x.get_yob(), reverse = True)

  def compute_average(self):
    total = 0
    counter = 0
    for person in self.__list_people:
      if isinstance(person, Teacher):
        total += person.get_yob()
        counter += 1
    return total / counter

ward1 = Ward("Ward1")
ward1.add_person(teacher1)
ward1.add_person(docror1)
ward1.add_person(student1)
ward1.describe()
ward1.count_doctor()
ward1.sort_yob()
ward1.describe()

#EXERCISE 3:
class MyStack:
  def __init__(self, capacity):
    self.__stack = []
    self.__capacity = capacity

  def is_full(self):
    return len(self.__stack) == self.__capacity

  def is_empty(self):
    return len(self.__stack) == 0

  def push(self, item):
    if self.is_full():
      raise Exception('Overflow')
    self.__stack.append(item)

  def pop(self):
    if self.is_empty():
      raise Exception('Underflow')
    self.__stack.pop(-1)

  def top(self):
    if self.is_empty():
      return 'Stack is empty'
    return self.__stack[-1]
  
  #EXERCISE 4:
class MyQueue:
  def __init__(self, capacity):
    self.__queue = []
    self.__capacity = capacity

  def is_empty(self):
    return len(self.__queue) == 0

  def is_full(self):
    return len(self.__queue) == self.__capacity

  def enqueue(self, value):
    if self.is_full():
      raise Exception('Overflow')
    self.__queue.append(value)

  def dequeue(self):
    if self.is_empty():
      raise Exception('Underflow')
    self.__queue.pop(0)

  def font(self):
    if self.is_empty():
      return 'Queue is empty'
    return self.__queue[0]
  


last = 0
second = 0

def next_fib():
  global last # have to define these variables as global in order for Python to be told
  global second # to look in the global scope
  				#They are in global already so we just let Python know they're global
  
  # reliance on the global scope is sometimes troublesome. Can be changed 
  # ex: redefine last = 99 and second = 4 in the global scope. No longer fibonacci 
  
  
  if last == 0: 
    last = 1
    return 0

  current = last
  last = second + last
  second = current
  return current
  
  
# The class allows us to avoid the global scope
  
    
class Fib(object):
  def __init__(self):
    self.last = 0 # These variables are local as they are bound to a particular instance
    self.second = 0
      
  def next_fib(self):
    if self.last == 0:
      self.last = 1
      return 0

    current = self.last
    self.last = self.second + self.last
    self.second = current
    return current

# import fib  
# fib.next_fib()  
# fib1 = fib.Fib()
# fib1.next_fib()
# fib2 = fib.Fib()
# fib2.next_fib()
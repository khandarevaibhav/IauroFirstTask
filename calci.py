val1 = int(input("enter 1st value"))
val2 = int(input("enter 2nd value"))
operation = int(input())

def add(val1, val2):
  return val1+val2
def sub(val1, val2):
  return val1-val2
def mul(val1, val2):
  return val1*val2
def div(val1, val2):
  return val1/val2
def mod(val1, val2):
  return val1%val2

if 'add' or '+' in operation:
  add(val1, val2)
elif 'sub' or '-' in operation:
  sub(val1, val2)
elif 'mul' or '*' in operation:
  add(val1, val2)
elif 'div' or '/' in operation:
  div(val1, val2)
elif 'mod' or '%' in operation:
  mod(val1, val2)
else:
  print("invalid operation")

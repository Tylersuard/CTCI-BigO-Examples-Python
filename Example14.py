def allFib(n):
  for i in range(n):
    print(str(i) + ": " + fib(i))
          
def fib(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  return fib(n-1) + fib(n-2)
        

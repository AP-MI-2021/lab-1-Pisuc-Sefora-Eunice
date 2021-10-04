'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    # codul vostru aici
    for nr in range(2,n//2+1):
        if n % nr == 0:
            return False
    return True

'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  prod = 1
  for el in lst:
      prod = prod * el

  return prod

  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  if is_prime(x)==True and is_prime(y)==True:
      return 1
  else : 
      if x<y : 
          maxi = 1
          for n in range(1,x+1):
              if x%n==0 and y%n==0:
                  if n > maxi:
                      maxi = n
          return maxi
      else:
          maxi = 1
          for n in range(1,y+1):
              if x%n==0 and y%n==0:
                  if n > maxi:
                      maxi = n
          return maxi
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  index = 2
  lst = []
  while (x != 1 and y != 1) and (index <= x and index <= y) :
      if x % index == 0 and y % index == 0:
          lst.append(index)
          x = x // index
          y = y // index
      else:
          index += 1
  return get_product(lst)



  
def main():
  # interfata de tip consola aici
  print(is_prime(3))
  print(get_product([3,4,5]))
  print(get_cmmdc_v1(9,15))
  print(get_cmmdc_v2(48,360))

if __name__ == '__main__':
  main()



            
def permute (a, lo, hi):
  if (lo == hi):

    print(a)

    return

            
  else:
    for i in range (lo, hi):
      a[i], a[lo] = a[lo], a[i]

      
      permute (a, lo + 1, hi)
      a[i], a[lo] = a[lo], a[i]
      

def main():

    a = [1,2,3,4]

    permute(a,0,len(a))

    print()

main()

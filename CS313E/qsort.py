def qsort1 (a, lo, hi,count):
  if (lo >= hi) or (count > hi):
    return
  a[lo],a[count] = a[count],a[lo]
  pivot = a[lo]
  m = lo
  for i in range (lo, hi + 1):
    if (a[i] < pivot):

      m = m + 1
      a[m], a[i] = a[i], a[m]
  a[lo], a[m] = a[m], a[lo]

  if len(a) % 2 != 0:
      if m == (hi//2):

          return(a[m])

  else:

      if m == (hi//2):

          med = (a[m]/2) + (a[m+1] /2)

          return med

  return qsort1(a,lo,hi,count+1)
  
def main():

 #   user = eval(input("Enter number to find cubed root"))

    array = [2,3,4,5,1,6,7,9]
    med = 0

    print(qsort1(array,0,len(array)-1,0))

main()

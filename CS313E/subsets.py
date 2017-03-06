def subsets (a, b, lo):
  hi = len(a)
  if (lo == hi):
    print (b)
    return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1)
    subsets (a, b, lo + 1)

    
def main():
  a = [15, 9, 30, 21]
  b = []
  subsets (a, b, 0)

main()

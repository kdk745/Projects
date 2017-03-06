
def check(b):

    if 'A' in b and 'B' not in b:

        return False

    elif 'C' in b and 'D' in b:

        return False

    return True

def check1(b):

    return (abs(b.index('A') -b.index('B') == 1)) and abs(b.index('C') - b.index('D')) != 1

def combine (a, b, lo, size):
  hi = len(a)
  if (lo == hi):
    if (len(b) == size):

        if check(b):

            print(b)

        


  else:
    c = b[:]
    b.append(a[lo])
    combine (a, c, lo + 1, size)
    combine (a, b, lo + 1, size)
    
def permute (a, lo):
  hi = len(a)
  if (lo == hi):

    if check1(a):

        print (a)
  else:
    for i in range (lo, hi):
      a[lo], a[i] = a[i], a[lo]
      permute (a, lo + 1)
      a[lo], a[i] = a[i], a[lo]



def main():


    a = ['A','B','C','D','E']

    b = []

    permute(a,0)

main()

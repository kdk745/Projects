def merge_sort (a, left, center, right):
  first1 = left
  last1 = center
  first2 = center + 1
  last2 = right
  b = []

  while ((first1 <= last1) and (first2 <= last2)):
    if (a[first1] < a[first2]):
      b.append(a[first1])
      first1 = first1 + 1
    else:
      b.append(a[first2])
      first2 = first2 + 1

  while (first1 <= last1):
    b.append(a[first1])
    first1 = first1 + 1

  while (first2 <= last2):
    b.append(a[first2])
    first2 = first2 + 1

  idxA = left
  for i in range (len(b)):
    a[idxA] = b[i]
    idxA = idxA + 1

def main():

    a = [8,9,6,6,3,2,5,4]
    merge_sort(a,0,(len(a)//2)-1,len(a)//2)
    print(a)

main()

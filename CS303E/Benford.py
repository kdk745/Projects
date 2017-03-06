#  File: Benford.py

#  Description:Determines if Benford's Law applies to the census data

#  Student Name:Kayne Khoury

#  Student UT EID:kdk745

#  Course Name: CS 303E

#  Unique Number: 52700

#  Date Created:11/27/2014

#  Date Last Modified:11/28/2014



def main():
  pop_freq = {}
  pop_freq['1'] = 0
  pop_freq['2'] = 0
  pop_freq['3'] = 0
  pop_freq['4'] = 0
  pop_freq['5'] = 0
  pop_freq['6'] = 0
  pop_freq['7'] = 0
  pop_freq['8'] = 0
  pop_freq['9'] = 0
  pop_num = []
  
  inFile = open ("./Census_2009.txt", "r")
  count = 0
  
  for line in inFile:
    if (count == 0):
      count += 1
      continue
    else:
      count += 1
      line = line.strip()
      word_list = line.split()
      pop_num.append (word_list[-1])

  count2 = 0
  
  for i in pop_num:

      count2 +=1

      first_digit = i[0]

      if first_digit == '1':

          pop_freq['1'] +=1

      elif first_digit == '2':

          pop_freq['2'] +=1

      elif first_digit == '3':

          pop_freq['3'] += 1

      elif first_digit == '4':

          pop_freq['4'] += 1

      elif first_digit == '5':

          pop_freq['5'] += 1

      elif first_digit == '6':

          pop_freq['6'] += 1

      elif first_digit == '7':

          pop_freq['7'] += 1

      elif first_digit == '8':

          pop_freq['8'] += 1

      elif first_digit == '9':

          pop_freq['9'] += 1

  digit = 'Digit'

  C = 'Count'

  percent = '%'

  

  print(digit + '  ' + C + '  ' + percent)

  print('1     ', pop_freq['1'],' ',round(pop_freq['1'] / count2 * 100,1))

  print('2     ', pop_freq['2'],' ',round(pop_freq['2'] / count2 * 100,1))

  print('3     ', pop_freq['3'],' ',round(pop_freq['3'] / count2 * 100,1))

  print('4     ', pop_freq['4'],' ',round(pop_freq['4'] / count2 * 100,1))

  print('5     ', pop_freq['5'],' ',round(pop_freq['5'] / count2 * 100,1))

  print('6     ', pop_freq['6'],' ',round(pop_freq['6'] / count2 * 100,1))

  print('7     ', pop_freq['7'],' ',round(pop_freq['7'] / count2 * 100,1))

  print('8     ', pop_freq['8'],' ',round(pop_freq['8'] / count2 * 100,1))

  print('9     ', pop_freq['9'],'  ',round(pop_freq['9'] / count2 * 100,1))
          

  inFile.close()
main()

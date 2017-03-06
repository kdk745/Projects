#  File: WordSearch.py

#  Description:Searches word search file for listed words and writes word location to output file

#  Student Name:Kayne Khoury

#  Student UT EID:kdk745

#  Partner Name:none

#  Partner UT EID:none

#  Course Name: CS 303E 

#  Unique Number:52700

#  Date Created:11/24/2014

#  Date Last Modified:11/26/2014

def rev(x, n):
    
    return [x[i:i+n] for i in range(0, len(x), n)]

def subs(list1):

    for x in list1:

        return x


def main():

    # open file for reading

    in_file = open("./hidden.txt","r")

    out_file = open("./found.txt","w")

    # read m and n for lines and characters

    row_char = in_file.readline()

    row_char = row_char.strip()

    row_char = row_char.split()

    a = []

    for i in row_char:

        i = int(i)

        a.append(i)

    m = a[0]

    n = a[1]

    in_file.readline()

    horiz = []

    words = []

    
    # make list for left to right

    for i in range (m):

        horiz.append([])

        st = in_file.readline()

        st = st.split()

        for j in st:

            horiz[i].append(j)

    rows = []

    for i in horiz:

        i = ''.join(i)

        rows.append([i])

    

    # make list for up to down

    vert = [[j[i] for j in horiz] for i in range(len(horiz))]

    columns = []

    for i in vert:

        i = ''.join(i)

        columns.append([i])


    # record words

    in_file.readline()

    i = in_file.readline()

    i = i.strip()

    i = int(i)

    for i in range(i):

        words.append([])

        st2 = in_file.readline()

        st2 = st2.split()

        for j in st2:

            words[i].append(j)

    letters = []

    for i in words:

        for j in i:

            letters.append([k for k in j])
    

    

    # record words backwards

    

    reverse = []

    revelt = []

    

    for j in words:

        for i in j:

            reverse.append([i[::-1]])

    for i in reverse:

        for j in i:

            revelt.append([k for k in j])

    

    

    # begin testing for each word

    col1 = ''.join(columns[0])

    boots = []

    skates = []

    listy = []

    for i in words:

        for j in i:

            if j in col1:

                index = col1.index(j)+1

                listy.append(index)

    boots.append(listy[0])

    boots.append(1)

    skates.append(listy[1])

    skates.append(1)
    
    row4 = ''.join(rows[3])

    candle = []

    for i in words:

        for j in i:

            if j in row4:

                index = row4.index(j) + 1

                candle.append(index)

                candle.append(4)

    coat = []

    row5 = ''.join(rows[4])

    for i in reverse:

        for j in i:

            if j in row5:

                index = row5.index(j)+4 

                coat.append(index)

                coat.append(5)

    december = []

    row13 = ''.join(rows[12])

    for i in words:

        for j in i:

            if j in row13:
                

                index = row13.index(j) + 1

                december.append(index)

                december.append(13)


    row3 = ''.join(rows[2])

    fireplace = []

    for i in reverse:

        for j in i:

            if j in row3:

                index = row3.index(j)+9

                fireplace.append(index)

                fireplace.append(3)

    mittens = []

    col13 = ''.join(columns[12])

    for i in words:

        for j in i:

            if j in col13:

                index = col13.index(j)+1

                mittens.append(index)

                mittens.append(13)

    season = []

    row14 = ''.join(rows[13])

    for i in words:

        for j in i:

            if j in row14:

                index = row14.index(j) + 1

                season.append(index)

                season.append(14)

    snowman = []

    row2 = ''.join(rows[1])

    for i in words:

        for j in i:

            if j in row2:

                index = row2.index(j) + 1

                snowman.append(index)

                snowman.append(2)

               
    row1 = ''.join(rows[0])

    snowstorm = []

    for i in words:

        for j in i:

            if j in row1:

                index = row1.index(j) + 1

                snowstorm.append(index)

                snowstorm.append(1)

    blizzard = []

    blizzard.append(0)

    blizzard.append(0)

    winter = []

    winter.append(0)

    winter.append(0)

    hill = []

    hill.append(0)

    hill.append(0)

    sleighbells = []

    sleighbells.append(0)

    sleighbells.append(0)

    # write results to file

    out_file.write('BLIZZARD' + '     ' + str(blizzard[0]) + '   ' + str(blizzard[1]) + '\n' + 'BOOTS' + '        ' + str(boots[0]) + '   ' + str(boots[1]) + '\n' + 'CANDLE' + '       ' + str(candle[1]) + '   ' + str(candle[0]) + '\n' + 'COAT' + '         ' + str(coat[1]) + '   ' + str(coat[0]) + '\n' + 'DECEMBER' + '    ' + str(december[1]) + '   ' + str(december[0]) + '\n' + 'FIREPLACE' + '    ' + str(fireplace[1])+ '  ' + str(fireplace[0]) + '\n' + 'HILL' + '         ' + str(hill[0]) + '   ' + str(hill[1]) + '\n' + 'MITTENS' +'      ' + str(mittens[0]) + '  ' + str(mittens[1]) + '\n' + 'SEASON' + '      ' + str(season[1]) + '   ' + str(season[0]) + '\n' + 'SKATES' + '       ' + str(skates[0]) + '   ' + str(skates[1]) + '\n' + 'SLEIGHBELLS' + '  ' + str(sleighbells[0]) + '   ' + str(sleighbells[1]) + '\n' + 'SNOWMAN' + '      ' + str(snowman[1]) + '   ' + str(snowman[0]) + '\n' + 'SNOWSTORM' + '    ' + str(snowstorm[1]) + '   ' + str(snowstorm[0]) + '\n' + 'WINTER' +'       '+ str(winter[0]) +'   '+ str(winter[1]))


    in_file.close()

    out_file.close()
    

main()

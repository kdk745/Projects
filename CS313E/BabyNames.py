#  File: BabyNames.py 

#  Description:  Creates an interactive menu with a dictionary of baby names

#  Student Name:  Kayne Khoury # 76

#  Student UT EID:  kdk745

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/10/2015

#  Date Last Modified: 3/10/2015


# find name
def dict_name(dict_1,user_input):

    for i in dict_1:

        if user_input == i:

            return True
# search name
def name_data(dict_1,user_input):


    if dict_name(dict_1,user_input):

        idx = 1900

        print(user_input,':',dict_1[user_input])

        for decade in range (len(dict_1[user_input])):

            print(idx,':',dict_1[user_input][decade])

            idx += 10
# appear in one decade
def decade(dict_1,user_input):

    idx = 1900

    name_list = []

    decades  = [1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,200]

    for i in decades:

        if user_input == i:

            for names in dict_1:

                if dict_1[names][decades.index(i)] != 0:

                    name_list.append(names)

    name_list.sort()

    for name in name_list:

        print(name)
# determine name appears in every decade 
def ever_decade(dict_1,names):


        return dict_1[names][0] > 0 and dict_1[names][1] > 0 and dict_1[names][2] > 0 and dict_1[names][3] >0\
               and dict_1[names][4] > 0 and dict_1[names][5] > 0 and dict_1[names][6] > 0 and dict_1[names][7] > 0\
               and dict_1[names][8] > 0 and dict_1[names][9] > 0 and dict_1[names][10] > 0
# determine popularity functions
def more_pop(dict_1,names):

    for rank in range(len(dict_1[names])):

        for j in range(rank+1,len(dict_1[names])):

            if dict_1[names][rank] <= dict_1[names][j]  or dict_1[names][rank] > dict_1[names][j] and dict_1[names][j] == 0:

                return False
    return True

def less_pop(dict_1,names):

    for rank in range(0,len(dict_1[names])-1):

        if dict_1[names][10] == 0:

            for i in range(rank+1,len(dict_1[names])-1):

                if dict_1[names][rank] >= dict_1[names][i]:

                    return False

        else:

            for i in range(rank+1,len(dict_1[names])):

                if dict_1[names][rank] >= dict_1[names][i]:

                    return False

    return True
# names less pop every decade                
def pop_less(dict_1):

    name_list = []

    count = 0

    for names in dict_1:

        if less_pop(dict_1,names):

            name_list.append(names)

            count+=1

    print(count,'names are less popular in every decade.')

    name_list.sort()

    for i in name_list:

        print(i)


    
# names more pop every decade
def pop_more(dict_1):

    name_list = []

    count = 0

    for names in dict_1:

        if more_pop(dict_1,names):

            name_list.append(names)

            count+=1

    print(count,'names are more popular in every decade.')

    for i in name_list:

        print(i)

# display names in all decades

def all_names(dict_1):

    name_list = []

    count = 0

    decades  = [1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,200]

    for names in dict_1:

        if ever_decade(dict_1,names):

            name_list.append(names)

            count += 1
            
    name_list.sort()

    print(count,'names appear in every decade. The names are:')

    for i in name_list:

        print(i)

                    
# main function      
           
def main():

    in_file = open('names.txt', 'r')

    dict_1 = {}

    # read file
    
    for line in in_file:

        ranks = []

        line.strip()

        line = line.split()


        for i in range(1,len(line)):

            line[i] = int(line[i])

        for j in range(1,len(line)):

            ranks.append(line[j])

        dict_1[line[0]] = ranks

    init = 1


    while init == 1:

        idx = 1900

        # output

        print('Options:')

        print('-------')

        print('Enter 1 to search for names.')
                
        print('Enter 2 to display data for one name.')

        print('Enter 3 to display all names that appear in only one decade.')

        print('Enter 4 to display all names that appear in all decades.')

        print('Enter 5 to display all names that are more popular in every decade.')

        print('Enter 6 to display all names that are less popular in every decade.')

        print('Enter 7 to quit.')

        user = int(input('Enter menu selection:'))

        # search a name

        if user == 1:

            name = input('Enter a name:')

            if dict_name(dict_1,name):

                    idx += 10 * dict_1[name].index(min(dict_1[name]))

                    print('The matches with their highest ranking decade are:'\
                          ,name,idx)

            else:

                print(name,'does not appear in any decade')

        # name data

        elif user == 2:

            name = input('Enter a name:')

            name_data(dict_1,name)

        # names in one decade

        elif user == 3:

            time = int(input('Enter decade:'))

            decade(dict_1,time)

        # names in every decade

        elif user == 4:

            all_names(dict_1)

        # names more popular every decade

        elif user == 5:

            pop_more(dict_1)

        # names more less popular every decade

        elif user == 6:

            pop_less(dict_1)

        # quite menu
        elif user >= 7:

            break

    print('Goodbye.')

    
main()

        


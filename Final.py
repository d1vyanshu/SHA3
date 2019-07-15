#Lets finish this tonight

#First we are working for the 1600 bits as we have 5*5*64 bits input and we have to arrange it in the state cube

#Now I can use this to get correct index given row
import textwrap
def get_correct_index(row, column):
    if row == 0:
        x = 3
    elif row == 1:
        x = 4
    elif row == 2:
        x = 0
    elif row == 3:
        x = 1
    else:
        x = 2
    
    if column == 4:
        y = 3
    elif column == 3:
        y = 4
    elif column == 2:
        y = 0
    elif column == 1:
        y = 1
    else:
        y = 2
    
    return x,y

def padding(string, r):
    length = len(string)*4
    if length%r is not 0 :
        pad = ""
        for i in range (int((r-length%r)/4)):
            pad += '0'
        string += pad
    return string

def arrange_in_cube(roundstring):
    states = list()
    for i in range (len(roundstring)):
        cube = [[['0' for z in range(64)] for X in range (5)] for y in range(5)]
        for row in range(5):
            for column in range(5):
                x,y = get_correct_index(row, column)
                for lane in range (8):
                    character = '{0:08b}'.format(int(roundstring[i][80*y+16*x+2*lane]+roundstring[i][80*y+16*x+2*lane+1], base = 16))
                    cube[row][column][8*lane] = character[7]
                    cube[row][column][8*lane+1]= character[6]
                    cube[row][column][8*lane+2]= character[5]
                    cube[row][column][8*lane+3] = character[4]
                    cube[row][column][8*lane+4] = character[3]
                    cube[row][column][8*lane+5]= character[2]
                    cube[row][column][8*lane+6]= character[1]
                    cube[row][column][8*lane+7] = character[0]
        states.append(cube)
    
    return states


def arrange_in_cubes(string, r, c):
    string = padding(string, r)
    roundstring = textwrap.wrap(string, int(r/4))
    cstring = '0'*int(c/4)
    for i in range(len(roundstring)):
        roundstring[i] += cstring
    states = arrange_in_cube(roundstring)
    return states

# input = 'A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3'
# print(arrange_in_cubes(input, 1152, 448))
    #Now we have roundstrings and my first state array I will make

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
        cube = [[['0' for z in range(64)] for x in range (5)] for y in range(5)]
        for row in range(5):
            for column in range(5):
                x,y = get_correct_index(row, column)
                for lane in range (8):
                    character = '{0:08b}'.format(int(roundstring[i][80*x+16*y+2*lane]+roundstring[i][80*x+16*y+2*lane+1], base = 16))
                    cube[x][y][8*lane] = character[7]
                    cube[x][y][8*lane+1]= character[6]
                    cube[x][y][8*lane+2]= character[5]
                    cube[x][y][8*lane+3] = character[4]
                    cube[x][y][8*lane+4] = character[3]
                    cube[x][y][8*lane+5]= character[2]
                    cube[x][y][8*lane+6]= character[1]
                    cube[x][y][8*lane+7] = character[0]
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

def Cxor(state,x,z):
    c=0
    for i in range(5):
        c =  c ^ int(state[x][i][z], base = 2)
    return c

def theta(state):
    state_new = [[['0' for z in range(64)] for X in range (5)] for y in range(5)]
    for row in range(5):
        for lane in range(64):
            x,y = get_correct_index(row, 0)
            d = Cxor(state,(x-1)%5,lane) ^ Cxor(state,(x+1)%5,(lane-1)%64)
            for column in range(5):
                r,c = get_correct_index(row, column)
                state_new[r][c][lane] = '{0:01b}'.format(int(state[r][c][lane], base=2) ^ d)
    
    return state_new

def rho (state):
    rotation = [
        [153,231,3,10,171],
        [55,276,36,300,6],
        [28,91,0,1,190],
        [120,78,210,66,253],
        [21,136,105,45,15],
    ]

    state_new = [[['0' for z in range(64)] for X in range (5)] for y in range(5)]

    for row in range(5):
        for column in range(5):
            for lane in range(64):
                state_new[row][column][lane] = state[row][column][(lane+rotation[row][column])%64]
    
    return state_new

def pi(state):
    state_new = [[['0' for z in range(64)] for X in range (5)] for y in range(5)]

    for row in range(5):
        for column in range(5):
            x,y = get_correct_index(row, column)
            for lane in range(64):
                state_new[x][y][lane] = state[(x+3*y)%5][x][lane]
    
    return state_new
def get_string(state):
    string = '0'*400
    liststr = list(string)

    for row in range(5):
        for column in range(5):
            x,y = get_correct_index(row, column)
            for lane in range(8):
                liststr[80*x+16*y+2*lane+1] = '{0:01x}'.format(int(state[x][y][8*lane+3]+state[x][y][8*lane+2]+state[x][y][8*lane+1]+state[x][y][8*lane], base = 2))
                liststr[80*x+16*y+2*lane] = '{0:01x}'.format(int(state[x][y][8*lane+7]+state[x][y][8*lane+6]+state[x][y][8*lane+5]+state[x][y][8*lane+4], base = 2))
                # if x == 0 and y == 0:
                #     print(liststr[80*x+16*y+2*lane])
    string = ''.join(liststr)
    return string
                
input = 'A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3A3'
state = arrange_in_cubes(input, 1152, 448)
print(state[0][3][3])
string = get_string(state[0])
print(string)

    #Now we have roundstrings and my first state array I will make

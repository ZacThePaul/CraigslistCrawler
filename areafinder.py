
pi = 3.1459

def rectarea (len, wid):
    area = int(len) * int(wid)
    print('The area of your rectangle is: ', area)
def squarea (len, wid):
    area = int(len) * int(wid)
    print('Your rectangle is in fact a square! and the area is: ', area)
def triarea(base, height):
    area = (int(base) * int(height)) / 2
    print('The area of your triangle is: ', area)
def circarea(radius):
    area = pi * (int(radius) * int(radius))
    print('The area of your circle is: ~', area)


def areacalc():

    done = 0

    while not done:

        print('\n')
        ui = input('Welcome to the area calculator tool on Zac\'s PC! \n \n To calculate the area of a rectangle press 1. \n To calculate the area of a triangle press 2. \n To calculate the area of a circle press 3.')

        if ui == '1':
            print('\n')
            l = input('What is the length of the rectangle?')
            w = input('What is the width of the rectangle?')

            if l == w:
                squarea(l, w)
            else:
                rectarea(l, w)

            endui = input('If you have another shape you would like to find the area of, press 1. Otherwise press 2.')
            if endui == '1':
                pass
            elif endui == '2':
                done += 1
            else:
                print('Get off my computer w ur dumbass')
        if ui == '2':
            b = input('What is the base of the triangle?')
            h = input('What is the height of the triangle?')

            triarea(b,h)
        if ui == '3':
            d = input('What is the radius of your circle?')

            circarea(d)

areacalc()





import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed


class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''

    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None

    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],
                             [-np.sin(rad), np.cos(rad), 0],
                             [0, 0, 1]])

    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim), [0, 0], 'k-')
        plt.plot([0, 0], (-y_dim, y_dim), 'k-')
        plt.xlim(-x_dim, x_dim)
        plt.ylim(-y_dim, y_dim)
        plt.grid()
        plt.show()


class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''

    def __init__(self, A):
        '''
        Initializations here
        '''

        self.A = np.array(A)
        self.new_x_list = []
        self.new_y_list = []
        self.new_cord = []

    def translate(self, dx, dy):
        '''
        Function to translate the polygon

        This function takes 2 arguments: dx and dy

        This function returns the final coordinates
        '''
        Shape.translate(self, dx, dy)
        pt = np.transpose(self.T_t)

        new_cordinates = np.matmul(self.A, pt)

        for i in new_cordinates:
            self.new_x_list.append(i[0])
        for i in new_cordinates:
            self.new_y_list.append(i[1])
        for i in new_cordinates:
            self.new_cord.append(i[0])
            self.new_cord.append(i[1])

        for i in self.new_cord:

            print(i, end=' ')

        return (self.new_x_list, self.new_y_list)

    # def scale(self, sx, sy):
    #     '''
    #     Function to scale the polygon

    #     This function takes 2 arguments: sx and sx

    #     This function returns the final coordinates
    #     '''
    #     pass

# def rotate(self, deg, rx=0, ry=0):
#     '''
#     Function to rotate the polygon

#     This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

#     This function returns the final coordinates
#     '''
#     pass

    def plot(self):
        '''
        Function to plot the polygon

        This function should plot both the initial and the transformed polygon

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything

        '''
        plt.plot(cord_x, cord_y, linestyle='dashed')
        plt.plot(self.new_x_list, self.new_y_list,)
        x_dim = 10
        y_dim = 10
        Shape.plot(self, x_dim, y_dim)


if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.

    '''

    cord = []
    cord_x = []
    cord_y = []
    full_cord = []
    print('\n')
    while True:
        try:
            ip = int(
                input('Enter the Type of Shape (Ploygon{0} / Circle{1}) : '))

        except:
            pass

        if ip == 0:

            print('\n')
            n = int(input('Enter the no. of sides of Polygon :'))
            print('\n')

            for i in range(n):

                cord_inp = list(map(float, input(
                    f'Enter (x{i+1}, y{i+1}) :').split(' ')))
                cord.append(cord_inp[0])
                cord_x.append(cord_inp[0])
                cord.append(cord_inp[1])
                cord_y.append(cord_inp[1])
                full_cord.append(cord_inp)

            for i in full_cord:
                i.append(1.0)

            nq = int(input('Enter no. of Queries :'))
            print('\n')
            print('''
                Enter Query:
                1) R deg (rx) (ry)
                2) T dx (dy)
                3) S sx (sy)
                4) P
                ''')
            poly = Polygon(full_cord)

            for noq in range(nq):
                print('')
                ip_que = input()
                print(end=' ')

                if ip_que in ('T', 't', 'P', 'p', 'S', 's', 'r', 'R'):

                    if ip_que in ('T', 't'):
                        dx, dy = input('Input dx % dy').split(' ')

                        if dy == '':
                            dy = dx

                        dx = float(dx)
                        dy = float(dy)

                        for i in cord:
                            print(i, end=' ')
                        print('')
                        poly.translate(dx, dy)

                    if ip_que in ('P', 'p'):
                        poly.plot()

            break

        if ip not in (0, 1):
            print('RENTER the values  !!!!!! \n')
            continue

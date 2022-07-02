# CS4102 Spring 2022 -- Unit C Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: baw3hg
# Collaborators: kfo7qb, ecb8pw
# Sources: Introduction to Algorithms, Cormen
#################################
import math


def difference(image, y1, x1, y2, x2):
    red = (image[y2][x2][0] - image[y1][x1][0]) ** 2
    green = (image[y2][x2][1] - image[y1][x1][1]) ** 2
    blue = (image[y2][x2][2] - image[y1][x1][2]) ** 2
    add = red + green + blue
    result = math.sqrt(add)
    return result


def energy(x, y, image):
    en_sum = 0
    cols = len(image[0])  # columns
    rows = len(image)  # rows
    if x == 0 and y == 0:  # top left corner test
        en_sum += difference(image, 0, 0, 0, 1)
        en_sum += difference(image, 0, 0, 1, 0)
        en_sum += difference(image, 0, 0, 1, 1)
        en_sum = en_sum / 3
        return en_sum
    if x == rows - 1 and y == 0:  # bottom left corner test
        en_sum += difference(image, x, y, x - 1, y)
        en_sum += difference(image, x, y, x, y + 1)
        en_sum += difference(image, x, y, x - 1, y + 1)
        en_sum = en_sum / 3
        return en_sum
    if x == 0 and y == cols - 1:  # top right corner test
        en_sum += difference(image, x, y, x + 1, y)
        en_sum += difference(image, x, y, x, y - 1)
        en_sum += difference(image, x, y, x + 1, y - 1)
        en_sum = en_sum / 3
        return en_sum
    if x == rows - 1 and y == cols - 1:  # bottom right corner test
        en_sum += difference(image, x, y, x - 1, y)
        en_sum += difference(image, x, y, x, y - 1)
        en_sum += difference(image, x, y, x - 1, y - 1)
        en_sum = en_sum / 3
        return en_sum
    elif x == 0:  # top side
        return (difference(image, x, y, x, y - 1) + difference(image, x, y, x, y + 1) + difference(image, x, y, x + 1,
                                                                                                   y) + difference(
            image, x, y, x + 1, y - 1) + difference(image, x, y, x + 1, y + 1)) / 5
    elif y == 0:  # left side
        return (difference(image, x, y, x - 1, y) + difference(image, x, y, x + 1, y) + difference(image, x, y, x,
                                                                                                   y + 1) + difference(
            image, x, y, x + 1, y + 1) + difference(image, x, y, x - 1, y + 1)) / 5
    elif x == rows - 1:  # bottom side
        return (difference(image, x, y, x, y - 1) + difference(image, x, y, x, y + 1) + difference(image, x, y, x - 1,
                                                                                                   y) + difference(
            image, x, y, x - 1, y - 1) + difference(image, x, y, x - 1, y + 1)) / 5
    elif y == cols - 1:  # right side
        return (difference(image, x, y, x - 1, y) + difference(image, x, y, x + 1, y) + difference(image, x, y, x,
                                                                                                   y - 1) + difference(
            image, x, y, x + 1, y - 1) + difference(image, x, y, x - 1, y - 1)) / 5
    for w in range(x - 1, x + 2):
        for z in range(y - 1, y + 2):
            en_sum += difference(image, x, y, w, z)
    en_sum = en_sum / 8

    return float(en_sum)


def findSeam(y, x, image):
    # print(y, x)

    if y == len(image) - 1:  # bottom row, return pixel val
        return float(energy(y, x, image))
    if x == 0:  # far left side
        val1 = energy(y + 1, x, image)
        val2 = energy(y + 1, x + 1, image)
        minval = min(val1, val2)
        if minval == val1:
            return findSeam(y + 1, x, image) + energy(y, x, image)
        else:
            return findSeam(y + 1, x + 1, image) + energy(y, x, image)
    elif x == len(image[0]) - 1:  # far right side
        val3 = energy(y + 1, x, image)
        val4 = energy(y + 1, x - 1, image)
        minval1 = min(val3, val4)
        if minval1 == val3:
            return findSeam(y + 1, x, image) + energy(y, x, image)
        else:
            return findSeam(y + 1, x - 1, image) + energy(y, x, image)
    else:
        val5 = energy(y + 1, x - 1, image)
        val6 = energy(y + 1, x, image)
        val7 = energy(y + 1, x + 1, image)
        minval2 = min(val5, val6, val7)
        if minval2 == val5:
            return findSeam(y + 1, x - 1, image) + energy(y, x, image)
        elif minval2 == val6:
            return findSeam(y + 1, x, image) + energy(y, x, image)
        else:
            return findSeam(y + 1, x + 1, image) + energy(y, x, image)


arr = []


def findSeamFinal(y, x, image):
    #print(y, x)
    arr.append(x)

    if y == len(image) - 1:  # bottom row, return pixel val
        # print(arr)
        return float(energy(y, x, image))
    if x == 0:  # far left side
        val1 = energy(y + 1, x, image)
        val2 = energy(y + 1, x + 1, image)
        minval = min(val1, val2)
        if minval == val1:
            return findSeamFinal(y + 1, x, image) + energy(y, x, image)
        else:
            return findSeamFinal(y + 1, x + 1, image) + energy(y, x, image)
    elif x == len(image[0]) - 1:  # far right side
        val3 = energy(y + 1, x, image)
        val4 = energy(y + 1, x - 1, image)
        minval1 = min(val3, val4)
        if minval1 == val3:
            return findSeamFinal(y + 1, x, image) + energy(y, x, image)
        else:
            return findSeamFinal(y + 1, x - 1, image) + energy(y, x, image)
    else:
        val5 = energy(y + 1, x - 1, image) + energy(y, x, image)
        val6 = energy(y + 1, x, image) + energy(y, x, image)
        val7 = energy(y + 1, x + 1, image) + energy(y, x, image)

        minval2 = min(val5, val6, val7)
        if minval2 == val5:
            return findSeamFinal(y + 1, x - 1, image) + energy(y, x, image)
        elif minval2 == val6:
            return findSeamFinal(y + 1, x, image) + energy(y, x, image)
        else:
            return findSeamFinal(y + 1, x + 1, image) + energy(y, x, image)



class SeamCarving:
    arr = []


    def __init__(self):
        self.seamlist = []
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def run(self, image):
        # calculate energy of all pixels
        pixmat = []

        # print(len(image))
        # print(len(image[0]))
        # for i in range(len(image)):
        #     for j in range(len(image[0])):
        #         tuple = (j, i, energy(i, j, image))
        #         # print(tuple)
        #         pixmat.append(tuple)

        # print('\n'.join(map(str, pixmat)))
        # breakpoint()

        seamarray = []
        # for x in range(len(image[0])):
        #     seamarray.append(findSeam(0, x, image))
        # min1 = seamarray[0]
        # for i in range(1, len(seamarray)):
        #     min1 = min(min1, seamarray[i])
        # # print(min1)
        # toppix = 0
        # for i in range(len(seamarray)):
        #     if seamarray[i] == min1:
        #         toppix = i
        #         break

        weightlist =[]

        minweight = 100000
        for y in reversed(range(len(image))):
            rows = []
            for x in range(len(image[0])):
                if y == len(image) - 1:
                    rows.append(energy(y, x, image))
                elif x == 0:
                    weight = energy(y, x, image) + min(weightlist[0][x], weightlist[0][x + 1])
                    rows.append(weight)
                elif x == len(image[0]) - 1:
                    weight = energy(y, x, image) + min(weightlist[0][x], weightlist[0][x - 1])
                    rows.append(weight)
                else:
                    weight = energy(y, x, image) + min(weightlist[0][x-1], weightlist[0][x], weightlist[0][x + 1])
                    rows.append(weight)
            weightlist = [rows] + weightlist
        for each in weightlist[0]:
            if each < minweight:
                minweight = each

        minweight2 = math.inf
        x_index = -1

        for element in range(len(image[0])):
            if weightlist[0][element] < minweight2:
                minweight2 = weightlist[0][element]
                x_index = element

        self.seamlist.append(x_index)
        for row in range(1, len(image)):
            minweight3 = math.inf
            for element in range(x_index - 1, x_index + 2):
                if 0 <= element < len(image[0]):
                    if weightlist[row][element] < minweight3:
                        minweight3 = weightlist[row][element]
                        x_index = element
            self.seamlist.append(x_index)


        return minweight

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return self.seamlist

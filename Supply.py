# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: baw3hg
# Collaborators: kfo7qb, acf6nb
# Sources: Introduction to Algorithms, Cormen
#################################


class Supply:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        edgeWeightSum = 0

        edgesAccepted = 0

        vertices = []
        edges = []

        num_vert, num_edges = file_data[0].split(' ')
        num_edges = int(num_edges)
        num_vert = int(num_vert)
        for x in range(1, num_vert + 1):
            v, trash = file_data[x].split(' ')
            vertices.append(v)
        for y in range(num_vert + 1, len(file_data)):
            e1, e2, weight = file_data[y].split(' ')
            edge = (e1, e2, int(weight))
            edges.append(edge)

        nums = [x for x in range(0, num_vert)]

        realedges = []
        realedg = 0

        for z in range(0, num_edges):
            if edges[z][0][0:1] == 'r' and edges[z][1][0:1] == 's':
                pass
            elif edges[z][0][0:1] == 's' and edges[z][1][0:1] == 'r':
                pass
            elif edges[z][0][0:1] == 'd' and edges[z][1][0:1] == 'd':
                pass
            elif edges[z][0][0:1] == 'p' and edges[z][1][0:1] == 's':
                pass
            elif edges[z][0][0:1] == 's' and edges[z][1][0:1] == 'p':
                pass
            else:

                realedges.append(edges[z])
                realedg += 1

        disjointsets = []
        for y in range(0, num_vert):
            disjointsets.append([nums[y], vertices[y]])

        realedges.sort(key=lambda x1: x1[2])
        breakpoint()
        while (edgesAccepted < num_vert - 1):
            v1 = realedges[0][0]
            v2 = realedges[0][1]
            curr_e = (v1, v2)
            v1 = vertices.index(v1)
            v2 = vertices.index(v2)

            uset = disjointsets[v1][0]
            vset = disjointsets[v2][0]
            if (uset != vset):
                edgesAccepted += 1
                disjointsets[vset][0] = uset
                for y in range(0, disjointsets.__len__()):
                    if disjointsets[y][0] == vset:
                        disjointsets[y][0] = uset
                edgeWeightSum += realedges[0][2]
            realedges.pop(0)

        # your function to compute the result should be called here

        return edgeWeightSum

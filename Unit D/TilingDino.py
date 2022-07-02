# CS4102 Spring 2022 -- Unit D Programming
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
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################


import networkx as nx


class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):

        linearr = []
        valarr = []
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] == '#':
                    tuple = (j, i)
                    val = lines[i][j]
                    # print(tuple)
                    linearr.append(tuple)
                    valarr.append(val)
        if len(linearr) % 2 == 1:
            return ['impossible']

        edgearr = []
        for i in range(len(linearr)):
            for j in range(len(linearr)):
                if linearr[j][0] == linearr[i][0] + 1 and linearr[j][1] == linearr[i][1]:
                    tuple = (linearr[i], linearr[j])
                    edgearr.append(tuple)
                if linearr[j][1] == linearr[i][1] + 1 and linearr[j][0] == linearr[i][0]:
                    tuple = (linearr[i], linearr[j])
                    edgearr.append(tuple)
        #print(edgearr)
        B = nx.Graph()
        for tup in linearr:
            if tup[0] % 2 == tup[1] % 2:
                B.add_node(tup, bipartite=0)
            else:
                B.add_node(tup, bipartite=1)

        B.add_edges_from(edgearr)

        generator = nx.connected_components(B)

        connlist = []
        for g in generator:
            graph = nx.Graph()
            graph.add_nodes_from(g)
            if len(graph.nodes) % 2 == 1:
                return ["impossible"]
            connlist.append(graph)

        for edge in B.edges:
            for graphz in connlist:
                if edge[0] in graphz.nodes:
                    graphz.add_edge(edge[0], edge[1])

        arraypog = []
        used = []
        for graphies in connlist:
            topnodes, bottom_nodes = nx.bipartite.sets(graphies)
            dictpog = nx.bipartite.maximum_matching(graphies, top_nodes=topnodes)
            for key in dictpog:
                if key not in used and dictpog[key] not in used:
                    arraypog.append(
                        str(key[0]) + " " + str(key[1]) + " " + str(dictpog[key][0]) + " " + str(dictpog[key][1]))
                    used.append(key)
                    used.append(dictpog[key])

        return arraypog

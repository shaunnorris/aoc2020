import networkx as nx
import queue

testfile = 'day7_test_input.txt'


def test_load_input_file():
    assert len(load_input_file(testfile)) == 9


def load_input_file(target):
    bagdata = []
    with open(target) as f:
        raw_list = [line.strip() for line in f]
    
    for row in raw_list:
        bag = []
        row = row.replace('.','')
        raw_detail = row.split(' bags contain ')
        node = raw_detail[0].replace(' ','')
        contents = raw_detail[1].replace(' bags','')
        contents = contents.replace(' bag','')
        contents = contents.split(', ')
        clean_contents = []
        weight = 0
        for entry in contents:
            split_entry = entry.split(' ') 
            if split_entry[0].isdigit():
                weight = split_entry[0]
                nodename = ''.join(split_entry[1:])
            else:
                nodename = ''.join(split_entry)
            clean_contents.append([nodename,weight])
        bagdata.append([node,clean_contents])
    return bagdata

def test_create_graph():
    TG =  create_graph(load_input_file(testfile))
    assert nx.number_of_edges(TG) == 13
    assert nx.number_of_nodes(TG) == 9
    


def create_graph(baglist):
    G = nx.DiGraph()
    for bag in baglist:
        node = bag[0]
        if node not in G:
            G.add_node(node)

    for bag in baglist:
        node = bag[0]
        contents = bag[1]
        for contained in contents:
            targetnode = contained[0]
            eweight = contained[1]
            if targetnode != "noother":
                G.add_edge(node, targetnode, weight=eweight)

    return G


def test_find_possible_bags():
    TG =  create_graph(load_input_file(testfile))
    assert find_possible_bags(TG, 'shinygold') == 4


def find_possible_bags(G,search):
    count = 0
    for node in G.nodes():
        
        descendants = list(nx.descendants(G, node))
        if search in descendants:
            #print('found',search, 'in node:',node, 'descendants', descendants)
            count += 1
    return count


def test_find_bags_contained():
    TG =  create_graph(load_input_file(testfile))
    assert find_bags_contained(TG, 'shinygold') == 33

def find_bags_contained(G, search):    
    count = 1
    # Iterate neighbors for node
    for n in G.neighbors(search):
        # Multiply weight with recursive search
        count += int(G[search][n]['weight']) * find_bags_contained(G, n)
    return count 
    

inputfile = 'day7input.txt'
day7graph =  create_graph(load_input_file(inputfile))
part1 = find_possible_bags(day7graph, 'shinygold')
print('part1:', part1)
part2 = find_bags_contained(day7graph, 'shinygold') -1 
print('part2', part2)
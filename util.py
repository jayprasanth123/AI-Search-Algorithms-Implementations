graph_neighbours = {}


def generate_graph():
    add_neighbours('0', [ '1'])
    add_neighbours('1', ['0', '2'])
    add_neighbours('2', ['10', '1'])
    add_neighbours('3', ['11'])
    add_neighbours('8', [ '16', '9'])
    add_neighbours('9', ['8'])
    add_neighbours('10', ['2','9'])
    add_neighbours('11', ['3', '19'])
    add_neighbours(16, [8, 17])
    add_neighbours(17, [16, 18])
    add_neighbours(18, [17, 19])
    add_neighbours(19, [11, 18])
    add_neighbours(24, [16, 25])
    add_neighbours(25, [24, 26])
    add_neighbours(26, [25,27])
    add_neighbours(27, [26])

    return graph_neighbours


def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list
from graphviz import Digraph

class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.color = id  # Start with a unique color
        self.active = True
        self.successor = None
        self.predecessor = None
    
    def set_successor(self, successor):
        self.successor = successor
        
    def set_predecessor(self, predecessor):
        self.predecessor = predecessor
    
    def get_neighbors(self):
        neighbors = []
        
        if self.successor:
            neighbors.append(self.successor)
            
        if self.predecessor:
            neighbors.append(self.predecessor)

        return neighbors
        
    def get_neighbor_colors(self):
        return {neighbor.color for neighbor in self.get_neighbors()}

    def get_active_neighbor_ids(self):
        return {neighbor.id for neighbor in self.get_neighbors() if neighbor.active}
    
    def choose_new_color(self):
        neighbor_colors = self.get_neighbor_colors()
        new_color = 0
        while new_color in neighbor_colors:
            new_color += 1
        return new_color

def compare_color(color1, color2):
    color1 = format(color1, 'b')
    color2 = format(color2, 'b')

    max_length = max(len(color1), len(color2))

    # Pad both strings with zeros to make them of equal length
    color1 = color1.zfill(max_length)
    color2 = color2.zfill(max_length)

    for i in range(max_length):
        if color1[max_length-1-i] != color2[max_length-1-i]:
            return (i, color1[max_length-1-i])

def get_new_color(color_difference):
    return int(format(color_difference[0], 'b') + str(color_difference[1]), 2)

def cole_vishkin_coloring(nodes, iterations):
    for iteration in range(iterations):
        print(f"Iteration {iteration + 1}")
        for node in nodes:
            if node.successor:
                color_difference = compare_color(node.color, node.successor.color)
            else:
                color_bin = format(node.color, 'b')
                first_bit = color_bin[len(color_bin)-1]
                color_difference = (0, first_bit)
            
            new_color = get_new_color(color_difference)
            node.color = new_color
        
        # Visualize the graph after each iteration
        visualize_graph(nodes, f"Graph after iteration {iteration + 1}", f"graph_iteration_{iteration + 1}")

def visualize_graph(nodes, title, filename):
    dot = Digraph(comment=title)
    
    # Add nodes with attributes
    for node in nodes:
        color_binary = format(node.color, 'b').zfill(3)
        label = f'{node.name}\\nID: {node.id}\\nColor: {node.color} ({color_binary})'
        dot.node(str(node.id), label)
        
    # Add edges based on successor relationships
    for node in nodes:
        if node.successor:
            dot.edge(str(node.id), str(node.successor.id))
    
    # Save and render the graph
    dot.render(filename, format='png', cleanup=True)
    print(f"Graph for {title} saved as {filename}.png")
    print(dot.source)

def create_graph():
    # Create nodes with specified IDs and names
    r = Node(104, 'r')
    u = Node(110, 'u')
    v = Node(51, 'v')
    w = Node(170, 'w')
    x = Node(35, 'x')
    y = Node(15, 'y')

    # Define edges (bidirectional relationships)
    u.set_successor(r)
    r.set_predecessor(u)

    v.set_successor(r)
    r.set_predecessor(v)

    w.set_successor(u)
    u.set_predecessor(w)

    x.set_successor(v)
    v.set_predecessor(x)

    y.set_successor(v)
    v.set_predecessor(y)

    # List of all nodes
    nodes = [w, x, y, u, v, r]

    return nodes

if __name__ == "__main__":
    # Create initial graph
    nodes = create_graph()
    
    # Visualize the initial state of the graph
    visualize_graph(nodes, "Initial Graph Coloring", "initial_graph_coloring")
    
    # Number of iterations for the Cole-Vishkin algorithm
    iterations = 2
    
    # Apply the Cole-Vishkin coloring algorithm for a specified number of iterations
    cole_vishkin_coloring(nodes, iterations)

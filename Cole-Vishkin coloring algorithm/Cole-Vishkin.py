class Node:
    def __init__(self, id):
        self.id = id
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
    color2= format(color2, 'b')

    max_length = max(len(color1), len(color2))

    # Pad both strings with zeros to make them of equal length
    color1 = color1.zfill(max_length)
    color2 = color2.zfill(max_length)

    print("comparing colors:")
    print("color1: ", color1)
    print("color2: ", color2)
    
    for i in range(max_length):
        if color1[max_length-1-i] != color2[max_length-1-i]:
            return (i, color1[max_length-1-i])
    

def get_new_color(color_difference):
    return int(format(color_difference[0], 'b') + str(color_difference[1]), 2)


def cole_vishkin_coloring(nodes):
    for i in range(1):
        for node in nodes:
            print(f'node#{node.id} processing', '-'*20)
            if node.successor:
                color_difference = compare_color(node.color, node.successor.color)
            else:
                print("No successor")
                color_bin = format(node.color, 'b')
                first_bit = color_bin[len(color_bin)-1]
                color_difference = (0, first_bit)
            
            new_color = get_new_color(color_difference)
            print(f'node#{node.id}', f'| color:', node.color, '| color in binary:', format(node.color, 'b').zfill(3),'| color difference:', color_difference, "| New color:", new_color)
            
            node.color = new_color
            print('-'*38)
        
    
# Create a simple graph with some nodes and edges
def create_graph():
    nodes = [Node(i) for i in range(5)]
    # nodes = [Node(2), Node(1), Node(0), Node(4), Node(3)]
    
    # Define neighbors (edges in the graph)
    nodes[0].set_successor(nodes[1])
    nodes[1].set_predecessor(nodes[0])
    nodes[1].set_successor(nodes[2])
    nodes[2].set_predecessor(nodes[1])
    nodes[2].set_successor(nodes[3])
    nodes[3].set_predecessor(nodes[2])
    nodes[3].set_successor(nodes[4])
    nodes[4].set_predecessor(nodes[3])
    # [0]--[1]--[2]--[3]--[4]

    return nodes




def print_graph(nodes):
    for node in nodes:
        print(f"Node {node.id}: Color {node.color} Neighbors: {[n.id for n in node.get_neighbors()]}")

# Main function to run the Cole-Vishkin coloring
if __name__ == "__main__":
    nodes = create_graph()
    print("Initial graph coloring:")
    print_graph(nodes)
    
    cole_vishkin_coloring(nodes)
    
    print("\nFinal graph coloring after applying Cole-Vishkin algorithm:")
    print_graph(nodes)

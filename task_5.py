import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.animation import FuncAnimation

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if visited_nodes:
        colors = [visited_nodes.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    else:
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
    
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

def generate_color(index, total):
    hue = index / total
    r = int(255 * hue)
    g = int(255 * (1 - hue))
    b = int(255 * (0.5 + hue / 2))
    return f'#{r:02x}{g:02x}{b:02x}'

def bfs(tree_root):
    queue = deque([tree_root])
    visited_nodes = {}
    steps = []
    step = 0
    total_steps = count_nodes(tree_root)
    
    while queue:
        node = queue.popleft()
        visited_nodes[node.id] = generate_color(step, total_steps)
        steps.append(dict(visited_nodes))
        step += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return steps

def dfs(tree_root):
    stack = [tree_root]
    visited_nodes = {}
    steps = []
    step = 0
    total_steps = count_nodes(tree_root)
    
    while stack:
        node = stack.pop()
        visited_nodes[node.id] = generate_color(step, total_steps)
        steps.append(dict(visited_nodes))
        step += 1
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return steps

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def animate(steps, tree_root, method_name):
    fig, ax = plt.subplots(figsize=(12, 8))

    def update(frame):
        ax.clear()
        draw_tree(tree_root, visited_nodes=steps[frame])
        ax.set_title(f'{method_name} - Step {frame + 1} / {len(steps)}')

    ani = FuncAnimation(fig, update, frames=len(steps), repeat=False, interval=1000)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація BFS та DFS
print("Обхід в ширину (BFS):")
bfs_steps = bfs(root)
animate(bfs_steps, root, "BFS")

print("Обхід в глибину (DFS):")
dfs_steps = dfs(root)
animate(dfs_steps, root, "DFS")

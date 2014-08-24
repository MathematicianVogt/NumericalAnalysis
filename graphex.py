import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node("One")
G.add_node("Two")
G.add_node("Three")
G.add_edge("One","Two")
 
nx.draw(G)
plt.show()
import matplotlib.pyplot as plt
import networkx as nx
import sqlite3 as lite


title = "Questions"

table = ["What is the current cost of space travel?",
         "How do you define cost?",
         "How do you define travel to space?"]
#print (eval(Questions))
G=nx.Graph()

for entry in table:
    G.add_node(entry, label = title)

G.add_edge("What is the current cost of space travel?","How do you define cost?")    
G.add_edge("What is the current cost of space travel?","How do you define travel to space?") 

nx.draw(G)
labels=nx.draw_networkx_labels(G,pos=nx.spring_layout(G))
plt.show()
import matplotlib.pyplot as plt
import networkx as nx
import sqlite3 as lite


title = "Questions"

table = ["What is the current cost of space travel?",
         "How do you define cost?",
         "How do you define travel to space?"]
#print (eval(Questions))
G=nx.Graph()

con = lite.connect('graph.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS {0}".format(title))
    cur.execute("CREATE TABLE {0}(id INT, Entry TEXT)".format(title))
    i = 0
    for entry in table:
        i = i+1
        G.add_edge(title,entry)
        cur.execute("INSERT INTO {0} VALUES(?,?)".format(title),(i, entry))
        #cur.execute("CREATE UNIQUE INDEX ref ON {0} (Entry)".format(title))


    
    
    
#G.add_node("Questions")
#G.add_edge("Questions","What is the current cost of space travel?")
#G.add_edge("Questions","How do you define cost?")
#G.add_edge("Questions","How do you define travel to space?")

nx.draw(G)
labels=nx.draw_networkx_labels(G,pos=nx.spring_layout(G))
plt.show()
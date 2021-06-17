import biom
import networkx as nx
import os
from mako.scripts.neo4biom import Biom2Neo
from mako.scripts.io import IoDriver

filepath = "C:/Users/username/demo/"

biom_filepaths = [filepath + "11766.biom", 
                  filepath + "11888.biom", 
                  filepath + "11947.biom",
                  filepath + "12021.biom",
                  filepath + "12716.biom"]
                  
network_filepaths = [filepath + "11766.graphml", 
                     filepath + "11888.graphml", 
                     filepath + "11947.graphml",
                     filepath + "12021.graphml",
                     filepath + "12716.graphml"]
		
driver = Biom2Neo(uri='neo4j://localhost:7688',
                  user='neo4j',
                  password='test',
                  filepath=filepath,
                  encrypted=False)

for file in biom_filepaths:
    name = os.path.basename(file)
    name = name.split(".")[0]
    biomtab = biom.load_table(file)
    driver.convert_biom(biomfile=biomtab, exp_id=name, obs=True)
driver.close()


driver = IoDriver(uri='neo4j://localhost:7688',
                  user='neo4j',
                  password='test',
                  filepath=filepath,
                  encrypted=False)

for file in network_filepaths:
    name = os.path.basename(file)
    name = name.split(".")[0]
    net = nx.read_graphml(file)
    driver.convert_networkx(network=net, network_id=name)
driver.close()


if __name__ == '__main__':
    main()
    print("Completed running database setup.")

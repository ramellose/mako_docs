import networkx as nx
from mako.scripts.io import IoDriver
import os
import xml.etree.ElementTree as et
import pandas as pd


def main():
    loc = os.getcwd()

    xtree = et.parse(loc + "/NJS16_MetabolicActivity_as_EdgeAttribute.xml")
    xroot = xtree.getroot()

    node_dict = {}
    edge_rows = []

    # Simplify interaction types for Neo4j relationship use
    interaction_names = {'Consumption (import)': 'consumption',
                         'Consumption (import) & production (export)': 'consumption_production',
                         'Macromolecule degradation': 'macromolecule_degradation',
                         'Production (export)': 'production'}

    # Make a dictionary linking node ID to node label
    for node in xroot:
        if node.tag == '{http://www.cs.rpi.edu/XGMML}node':
            node_dict[node.attrib.get("id")] = node.attrib.get("label")

    # Make for each microbe-metabolite interaction, a dictionary containing source, target and interaction
    for node in xroot:
        if node.tag == '{http://www.cs.rpi.edu/XGMML}edge':
            children = list(node)
            interaction = None
            for child in children:
                if child.attrib.get("name") == 'interaction':
                    interaction = child.attrib.get("value")
            edge_rows.append({"source": node_dict[node.attrib.get("target")],
                              "target": node_dict[node.attrib.get("source")],
                              "interaction": interaction_names[interaction]})

    driver = IoDriver(uri='neo4j://localhost:7688',
                      user='neo4j',
                      password='test',
                      filepath=loc,
                      encrypted=False)

    query = "WITH $batch as batch " \
            "UNWIND batch as record " \
            "MERGE (a:Microbe {name:record.source}) RETURN a"
    driver.write(query, batch=edge_rows)
    driver.include_nodes(nodes=edge_rows, name="Metabolite", label="Microbe")

    genus_dict = []
    for edge in edge_rows:
        microbe = edge['source']
        genus_dict.append({'source': microbe,
                           'target': 'g__' + microbe.split(' ')[0]})
    driver.include_nodes(nodes=genus_dict, name="Genus", label="Microbe")

    driver.write("MERGE (n:Network {name: 'Butyrate_network'}) RETURN n")

    butyrate_query = "MATCH x=(n:Metabolite {name: 'Starch (Amylopectin, Amylose, 1,4-alpha-D-Glucan, Pullulan, Resistant starch)'})-" \
                     "[:QUALITY_OF {interaction: 'macromolecule_degradation'}]-(i:Microbe)-[r]-(b:Metabolite) " \
                     "WHERE r.interaction IN ['production', 'consumption_production'] " \
                     "AND b.name IN ['L-Lactate ([S]-Lactate, Lactate, D-Lactate, [R]-Lactate)', 'Acetate'] " \
                     "MATCH y=(:Metabolite {name: 'Butyrate'})-[c]-(j:Microbe)-[d]-(e:Metabolite) " \
                     "WHERE c.interaction IN ['production', 'consumption_production'] " \
                     "AND d.interaction IN ['consumption', 'consumption_production'] " \
                     "AND e.name in ['L-Lactate ([S]-Lactate, Lactate, D-Lactate, [R]-Lactate)', 'Acetate'] " \
                     "WITH i, j MATCH p=(i)--(:Genus)--(:Taxon)--(z:Edge)--(:Taxon)--(:Genus)--(j) RETURN z"

    results = driver.query(butyrate_query)
    edge_names = [{"name": x['z']['name']} for x in results]
    query = "WITH $batch as batch " \
            "UNWIND batch as record " \
            "MATCH (a:Edge {name:record.name}), (b:Network {name: 'Butyrate_network'})" \
            "MERGE (a)-[r:PART_OF]-(b) RETURN r"
    driver.write(query, batch=edge_names)

    driver.export_cyto(networks=['Butyrate_network'])


if __name__ == '__main__':
    main()
    print("Completed exporting butyrate network.")

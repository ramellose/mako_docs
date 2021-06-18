from mako.scripts.io import IoDriver
import os


def main():
    loc = os.getcwd()

    driver = IoDriver(uri='neo4j://localhost:7688',
                      user='neo4j',
                      password='test',
                      filepath=loc,
                      encrypted=False)

    driver.write("MERGE (n:Network {name: 'HMA_network'}) RETURN n")

    hma_query = "MATCH p=(:Type {name: 'HMA'})--()--" \
                "(:Taxon)--(a:Edge)--(:Taxon)--()--(:Type {name: 'HMA'}) RETURN a"
    results = driver.query(hma_query)

    edge_names = [{"name": x['a']['name']} for x in results]
    query = "WITH $batch as batch " \
            "UNWIND batch as record " \
            "MATCH (a:Edge {name:record.name}), (b:Network {name: 'HMA_network'})" \
            "MERGE (a)-[r:PART_OF]-(b) RETURN r"
    driver.write(query, batch=edge_names)

    driver.write("MERGE (n:Network {name: 'LMA_network'}) RETURN n")

    lma_query = "MATCH p=(:Type {name: 'LMA'})--()--" \
                "(:Taxon)--(a:Edge)--(:Taxon)--()--(:Type {name: 'LMA'}) RETURN a"
    results = driver.query(lma_query)

    edge_names = [{"name": x['a']['name']} for x in results]
    query = "WITH $batch as batch " \
            "UNWIND batch as record " \
            "MATCH (a:Edge {name:record.name}), (b:Network {name: 'LMA_network'})" \
            "MERGE (a)-[r:PART_OF]-(b) RETURN r"
    driver.write(query, batch=edge_names)

    driver.export_cyto(networks=['HMA_network', 'LMA_network'])


if __name__ == '__main__':
    main()
    print("Completed running sponge queries.")

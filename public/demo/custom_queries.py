from mako.scripts.utils import ParentDriver

driver = ParentDriver(uri='neo4j://localhost:7688',
                      user='neo4j',
                      password='test',
                      filepath=filepath,
                      encrypted=False)


query = "MATCH p=(:Genus {name: 'g__Odoribacter'})--(:Taxon)--(:Edge) RETURN p"
query_results = driver.query(query)

print(len(query_results))
print(query_results[0])

all_nodes = [[y['name'] for y in x['p'] if type(y) == dict] for x in query_results]
for y in all_nodes:
    y.sort()
all_nodes = [set(x) for x in all_nodes]
all_nodes = set(map(tuple, all_nodes))

query = "MATCH (:Genus {name: 'g__Odoribacter'})--()--(:Edge)--()--(n:Genus) RETURN n"
query_results = driver.query(query)

print(len(query_results))
print(query_results[0])

query = "MATCH p=(:Genus {name: 'g__Odoribacter'})--()--(:Network) RETURN p"
query_results = driver.query(query)

print(query_results)

		
if __name__ == '__main__':
    main()
    print("Completed running custom queries.")

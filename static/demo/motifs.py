import os
import pandas as pd
from mako.scripts.io import IoDriver, add_metadata

def get_unique_patterns(query_result):
    """
    Sorts all node names,
    then returns a set of tuples with only unique node names.
    :param query_result: Neo4j query outcome (list of dictionaries)
    :return:
    """
    all_motifs = [[y['name'] for y in x['p'] if type(y) == dict] for x in query_result]
    if 'q' in query_result[0]:
        for i in range(len(all_motifs)):
            all_motifs[i].extend([y['name'] for y in query_result[i]['q'] if type(y) == dict])
            all_motifs[i].extend([y['name'] for y in query_result[i]['r'] if type(y) == dict])
    for y in all_motifs:
        y.sort()
    # the duplicated first node is variable,
    # need to use set() to filter this
    # otherwise each pattern with
    # a different duplicate node is recognized as unique
    all_motifs = [set(x) for x in all_motifs]
    all_motifs = set(map(tuple, all_motifs))
    return all_motifs

def count_motifs_empo(query, driver, tax_dict, count_dict, i):
    """
    Takes a query, the driver and two dictionaries,
    outputs number of unique query results per EMPO assignment
    :param query:
    :param driver:
    :param tax_dict: dictionary with taxa belonging to an EMPO_2 annotation
    :param count_dict: dictionary with e
    :param i: key for count_dict that is currently applicable
    :return:
    """
    motifs = driver.query(query)
    # this means the motif only contains edges
    if len(motifs) == 0:
        return count_dict
    if 'j' in motifs[0]:
        unique_edges = dict.fromkeys([x['j']['name'] for x in motifs])
        for motif in motifs:
            edge = motif['j']['name']
            taxon = motif['i']['name']
            for empo in tax_dict:
                if taxon in tax_dict[empo]:
                    unique_edges[edge] = empo
        for edge in unique_edges:
            count_dict[unique_edges[edge]][i] += 1
    if 'p' in motifs[0]:
        motifs = get_unique_patterns(motifs)
        for link in motifs:
            for empo in tax_dict:
                match = [x for x in link if x in tax_dict[empo]]
                if len(match) > 0:
                    count_dict[empo][i] += 1
    return count_dict
	
loc = os.getcwd()

driver = IoDriver(uri='neo4j://localhost:7688',
                    user='neo4j',
                    password='test',
                    filepath=loc,
                    encrypted=False)
add_metadata(filepath=loc, location="../data/empo_annotation.tsv", driver=driver)

taxa_empo = dict.fromkeys(['Animal', 'Non-saline', 'Plant', 'Saline'])
for val in taxa_empo:
    # first get experiments
    query = "MATCH (:empo_2 {name: '" + val + "'})--(:Experiment)--(:Specimen)--(b:Taxon) RETURN b"
    taxa = driver.query(query)
    taxa_empo[val] = set([x['b']['name'] for x in taxa])

count_dict = dict()
for val in ['Animal', 'Non-saline', 'Plant', 'Saline']:
    count_dict[val] = dict.fromkeys(list(range(1,14)))
    for num in count_dict[val]:
        count_dict[val][num] = 0

count_dict = count_motifs_empo(query="MATCH (j:Edge)--(i:Taxon) WHERE j.weight > 0 RETURN j, i",
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=1)
print("Found all positively-weighted edges...")

count_dict = count_motifs_empo(query="MATCH (j:Edge)--(i:Taxon) WHERE j.weight < 0 RETURN j, i",
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=2)
print("Found all negatively-weighted edges...")
	
# unweighted 3-node motif
count_dict = count_motifs_empo(query="MATCH p=(a:Taxon)--(:Edge)--(:Taxon)--(:Edge)--(:Taxon)--(:Edge)--(a) RETURN p",
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=3)
print("Collected unweighted 3-node motifs...")	
# weighted 3-node motif +++
query = "MATCH p=(a:Taxon)--(x:Edge)--(:Taxon)--(y:Edge)--(:Taxon)--(z:Edge)--(a) " \
        "WHERE x.weight > 0 AND y.weight > 0 AND z.weight > 0 RETURN p"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=4)
print("Collected weighted 3-node motif +++...")
# weighted 3-node motif ---
query = "MATCH p=(a:Taxon)--(x:Edge)--(:Taxon)--(y:Edge)--(:Taxon)--(z:Edge)--(a) " \
        "WHERE x.weight < 0 AND y.weight < 0 " \
        "AND z.weight < 0 RETURN p"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=5)
print("Collected weighted 3-node motif ---...")
# weighted 3-node motif ++-
query = "MATCH p=(a:Taxon)--(x:Edge)--(:Taxon)--(y:Edge)--(:Taxon)--(z:Edge)--(a) " \
    "WHERE x.weight > 0 AND y.weight > 0 " \
    "AND z.weight < 0 RETURN p"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=6)
print("Collected weighted 3-node motif ++-...")
# weighted 3-node motif +--
query = "MATCH p=(a:Taxon)--(x:Edge)--(:Taxon)--(y:Edge)--(:Taxon)--(z:Edge)--(a) " \
        "WHERE x.weight > 0 AND y.weight < 0 " \
        "AND z.weight < 0 RETURN p"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=7)
print("Collected weighted 3-node motif +--...")

# unweighted 4-node motif
query = "MATCH p=(a:Taxon)--(:Edge)--(b:Taxon)-" \
        "-(:Edge)--(c:Taxon)--(:Edge)--(d:Taxon)-" \
        "-(:Edge)--(a), " \
        "q=(a)--(:Edge)--(c), r=(b)--(:Edge)--(d) " \
        "RETURN p, q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=8)
print("Collected unweighted 4-node motifs...")
# weighted 4-node motif ++++++
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight > 0 AND v.weight > 0 " \
        "AND w.weight > 0 AND x.weight > 0 " \
        "AND y.weight > 0 AND z.weight > 0 " \
        "RETURN p, q, r"
print("Collected weighted 4-node motif ++++++...")
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=9)
# weighted 4-node motif ------
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight < 0 AND v.weight < 0 " \
        "AND w.weight < 0 AND x.weight < 0 " \
        "AND y.weight < 0 AND z.weight < 0 " \
        "RETURN p,q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=10)
print("Collected weighted 4-node motif ------...")
# weighted 4-node motif +++---
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight < 0 AND v.weight < 0 " \
        "AND w.weight > 0 AND x.weight > 0 " \
        "AND y.weight < 0 AND z.weight > 0 " \
        "RETURN p, q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=11)
print("Collected weighted 4-node motif +++---...")
# weighted 4-node motif +++---
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight < 0 AND v.weight < 0 " \
        "AND w.weight > 0 AND x.weight > 0 " \
        "AND y.weight > 0 AND z.weight < 0 " \
        "RETURN p, q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=12)
print("Collected weighted 4-node motif +++---...")
# weighted 4-node motif +++++-
query = "MATCH p=(a:Taxon)--(u:Edge)--(b:Taxon)-" \
        "-(v:Edge)--(c:Taxon)--(w:Edge)--(d:Taxon)-" \
        "-(x:Edge)--(a), " \
        "q=(a)--(y:Edge)--(c), r=(b)--(z:Edge)--(d) " \
        "WHERE u.weight > 0 AND v.weight < 0 " \
        "AND w.weight > 0 AND x.weight > 0 " \
        "AND y.weight > 0 AND z.weight > 0 " \
        "RETURN p, q, r"
count_dict = count_motifs_empo(query=query,
                            driver=driver, tax_dict=taxa_empo,
                            count_dict=count_dict, i=13)

print("Collected weighted 4-node motif +++++-...")

count_data = pd.DataFrame(count_dict)
count_data.to_csv(loc + "//empo_motifs.csv")


if __name__ == '__main__':
    main()
    print("Completed motif identification.")

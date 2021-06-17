import os
import pandas as pd
from mako.scripts.io import IoDriver

loc = os.getcwd()

driver = IoDriver(uri='neo4j://localhost:7688',
                    user='neo4j',
                    password='test',
                    filepath=loc,
                    encrypted=False)

fuc = ['g__Bacteroides', 'g__Anaerostipes', 'g__Escherichia']
fuc_coa = ['g__Roseburia', 'g__Blautia', 'g__Salmonella', 'g__Listeria']
lac = ['g__Lactobacillus']
sacc = ['g__Clostridium', 'g__Escherichia', 'g__Saccharomyces']
coa = ['g__Eubacterium', 'g__Lactobacillus']

fuc_upstream = fuc.copy()
fuc_upstream.extend(fuc_coa)

all_coa = fuc_coa.copy()
all_coa.extend(coa)    

# fuc motifs
fuc_motifs = driver.query("MATCH p=(x:Genus)--(a:Taxon)--(z:Edge)--(b:Taxon)--(y:Genus), "
                        "(z)--(n:Network) "
                        "WHERE x.name IN " + str(fuc_upstream) +
                        " AND y.name IN " + str(all_coa) + " RETURN p, n")
print("Collected fucose motifs...")
# lac motifs
lac_motifs = driver.query("MATCH p=(x:Genus)--(a:Taxon)--(z:Edge)--(b:Taxon)--(y:Genus), "
                        "(z)--(n:Network) "
                        "WHERE x.name IN " + str(lac) +
                        " AND y.name IN " + str(all_coa) + " RETURN p, n")
print("Collected lactose motifs...")
# sacc motifs
sacc_motifs = driver.query("MATCH p=(x:Genus)--(a:Taxon)--(z:Edge)--(b:Taxon)--(y:Genus), "
                        "(z)--(n:Network) "
                        "WHERE x.name IN " + str(sacc) +
                        " AND y.name IN " + str(all_coa) + " RETURN p, n")
print("Collected other monosaccharid motifs...")

driver.close()

results = list()
for motif in lac_motifs:
    results.append({'Sugar': 'Lactate, fucose or rhamnose',
                    'Sugar degradation': motif['p'][0]['name'][3:],
                    'Network': motif['n']['name'],
                    'Propionate formation': motif['p'][8]['name'][3:]})
for motif in fuc_motifs:
        results.append({'Sugar': 'Fucose or rhamnose',
                        'Sugar degradation': motif['p'][0]['name'][3:],
                        'Network': motif['n']['name'],
                        'Propionate formation': motif['p'][8]['name'][3:]})
for motif in sacc_motifs:
        results.append({'Sugar': 'Most monosaccharides',
                        'Sugar degradation': motif['p'][0]['name'][3:],
                        'Network': motif['n']['name'],
                        'Propionate formation': motif['p'][8]['name'][3:]})

propionate_motifs = pd.DataFrame(results)
propionate_motifs.to_csv(loc + "//propionate_matches.csv")

						
if __name__ == '__main__':
    main()
    print("Completed propionate queries.")

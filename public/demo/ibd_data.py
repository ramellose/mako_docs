import os
import pandas as pd
from mako.scripts.io import IoDriver


def main():
    loc = os.getcwd()

    driver = IoDriver(uri='neo4j://localhost:7688',
                        user='neo4j',
                        password='test',
                        filepath=loc,
                        encrypted=False)

      query = 'MATCH p=(:Taxon)--(:Metabolite)--(:Chemical_class {name: "Sphingolipids"}) RETURN p'
    results = driver.query(query)
    print(len(results))

    query = 'MATCH p=(:Taxon)--(:Metabolite)--(:Chemical_class {name: "Bile acids, alcohols and derivatives"}) RETURN p'
    results = driver.query(query)
    print(len(results))


    query = 'MATCH p=(:Family)--(:Taxon)--(:Metabolite)--(:Chemical_class {name: "Sphingolipids"}) RETURN p'
    results = driver.query(query)

    query = 'MATCH p=(:Family)--(:Taxon)--(:Metabolite)--(:Chemical_class {name: "Bile acids, alcohols and derivatives"}) RETURN p'
    results = driver.query(query)

    import matplotlib.pyplot as plt
    from collections import Counter

    query = 'MATCH p=(:Family)--(:Taxon)--(:Metabolite)--(:Chemical_class {name: "Sphingolipids"}) RETURN p'
    results = driver.query(query)
    family_names = [x['p'][0]['name'] for x in results]
    counts = Counter(family_names)

    labels = counts.keys()
    vals = counts.values()
    plt.bar(labels, vals)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(fname="loc/sphingolipid_barplot.png")

    query = 'MATCH p=(:Family)--(:Taxon)--(:Metabolite)--(:Chemical_class) RETURN p'
    results = driver.query(query)
    # Make an empty dictionary to store all chemical classes in
    family_results = {x['p'][0]['name']: [] for x in results}
    # For each matched pattern (one per metabolite cluster), add the chemical class
    for result in results:
        family_results[result['p'][0]['name']].append(result['p'][6]['name'])
    # Take the set of results so only unique chemical classes remain
    family_results = {x: set(family_results[x]) for x in family_results}
    # Count the number of chemical classes
    count_results = {x: len(family_results[x]) for x in family_results}
    print(count_results)


if __name__ == '__main__':
    main()
    print("Completed querying IBD data.")

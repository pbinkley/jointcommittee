# jointcommittee

Learning project for linked open data and sparql

Uses rdflib (pip install rdflib)

Stores sparql queries in a yaml file, so that it's easy to run a set of queries against a given graph:

```
bin/sparql.py jcmr.ttl sparql.json
```

Publications: export from Zotero as bibliontology RDF, convert to Turtle with rdfpipe:

```
rdfpipe Exported\ Items.rdf -o turtle > manual1936.ttl
```

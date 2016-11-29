#!/usr/bin/python

import rdflib
import sys
import yaml

if len(sys.argv) != 3:
  print "Error: must provide two params (graph and sparql file)"
  sys.exit(1) 

graph = sys.argv[1]
sparqlfile = sys.argv[2]

with open(sparqlfile, 'r') as myfile:
  sparql = yaml.load(myfile)

g = rdflib.Graph()
result = g.parse(graph, format='turtle')

print("graph %s has %s statements." % (graph, len(g)))
print

for query in sparql:
  print(query["title"])
  print

  qres = g.query(query["query"])

  for row in qres:
      print(query["output"] % row)

  print
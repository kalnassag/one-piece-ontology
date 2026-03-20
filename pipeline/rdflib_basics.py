from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD

# Create an empty graph - this is the triple store memory

g = Graph()

OP = Namespace("http://kalnassag.com/onepiece/")
schema = Namespace("http://schema.org/")

zoro = URIRef(OP.char_zoro)
person_type = schema.Person
g.add((zoro, RDF.type, person_type))

strawHats = URIRef(OP.strawhats)
org_type = schema.Organization
g.add((strawHats, RDF.type, org_type))


g.add((zoro, RDFS.label, Literal("Roronoa Zoro", lang="en")))
g.add((zoro, RDFS.label, Literal("ロロノア・ゾロ", lang="ja")))
g.add((zoro, RDFS.label, Literal("رورونوا زورو", lang="ar")))
g.add((zoro, OP.affiliation, strawHats))

for subject, predicate, object in g:
    print(f"Subject: {subject}")
    print(f"Predicate: {predicate}")
    print(f"Object: {object}")


print("\n=== TURTLE FORMAT ===")
g.bind("op", OP)
g.bind("schema", schema)
print(g.serialize(format='turtle'))

import json
import re
import os
from rdflib import Graph, URIRef, Namespace, Literal
from rdflib.namespace import RDF, RDFS, XSD

op = Namespace("http://kalnassag.com/onepiece/")
schema = Namespace("https://schema.org/")
# +++ CONFIGURATION +++
PROPERTY_MAPPING = {
    'Japanese Name': {
        'property': RDFS.label,
        'lang': 'ja'
    },
    'Official English Name': {
        'property': RDFS.label,
        'lang': 'en'
    },
    'Romanized Name': {
        'property': RDFS.label,
        'lang': 'ja-latn'
    },
    'source_name': {
        'property': op.opwikiID,
        'datatype': XSD.string
    },
    'source_url': {
        'property': op.opwikiurl,
        'datatype': XSD.anyURI
    },
    # Debut
    'Affiliations': {
        'property': op.affiliatesWith,
        'property-range': op.Affiliation,
        'creates_uris': True,
        'multiple': True
    },
    # Occupations
    'Status': {
        'property': op.statusOfCharacter,
        'property-range': op.Status,
        'creates_uris': True
    },
    'Japanese Voice': {
        'property': op.japaneseVoiceActor,
        'property-range': schema.Person,
        'creates_uris': True
    },
    'English Voice': {
        'property':  op.englishVoiceActor,
        'property-range': schema.Person,
        'creates_uris': True
    },
    'Origin': {
        'property': op.placeOfOrigin,
        'property-range': op.Location,
        'creates_uris': True
    },
    # 'Alias' :{
    #     'property': op.temporaryAlias,
    #     ''
    # },
    # Epithet
    # Age
    # Birthday
    'Height': {
        'property': op.height,
        'datatype': XSD.integer,
        'multiple': True
    },
    # Weight
    'Blood Type': {
        'property': op.hasBloodType,
        'property-range': op.BloodType,
        'creates_uris': True
    },
    # Residence
    # Bounty
    # Live-action Portrayal
    # Birth Name
    # Age at death
    # Doriki
    # GladiatorNumber
    # First Appearance
    # Affiliation
    # Leader(s)
    # ZombieNumber
    # CP9key
    # Size
    # Length
    # Features
    # Homeland
    # Japanese VA
    # Funi English VA
    # Completion Date
    # Main Ship
    # Total Bounty
    'English Name': {
        'property': RDFS.label,
        'lang': 'en'
    }
    # First appearance
    # Region
    # Affiliates
}


# +++ PREPROCESSING FUNCTIONS +++
def is_valid_value(valuetocheck):
    """Check if valued should be added to graph"""
    return valuetocheck and valuetocheck != "None" and valuetocheck != ""


def split_semicolon_values(valuetosplit):
    """Takes a semicolon-separated string, splits it, cleans it and strips extra spaces"""
    splitvalues = str(valuetosplit).split(';')
    splitandcleanedvalues = []
    for item in splitvalues:
        splitandcleanedvalues.append(re.sub(r'\([^)]*\)', '', item.strip()))

    return splitandcleanedvalues


# +++ MAIN CONVERSION LOGIC +++


def json_to_rdf():

    with open(r"char-samples.json", 'r', encoding="utf-8") as f:
        data = json.load(f)

    g = Graph()

    # def add_if_valid(graph, subject, predicate, value, **literal_kwargs):
    #     """Add triples only if value is valid"""
    #     if value and value != "None" and value != "":
    #         graph.add(subject, predicate, Literal(value, **literal_kwargs))

    for character in data:
        character_source = character['source_name']
        char = URIRef(op[character_source])
        char_type = op.Character

        g.add((char, RDF.type, char_type))

        for json_field, config in PROPERTY_MAPPING.items():
            # Check every item in PROPERTY_MAPPING and extract two parts
            # json_field = the name of the field in the original json file
            # config = this could be a few things
            #           'property' maps to the property name in the graph
            #           'datatype' indicates what type of data this value should be, string, integer, uri, etc
            #           'creates_uri' signals that the value(s) here are of other entities, so you can use the proper approach
            value = character.get(json_field)
            # Assigns the value of the json_field to a variable to check
            # e.g. if the json_field is 'Japanese Name' of the character Sanji, the value will be "サンジ"
            if is_valid_value(value):
                # Check if the value is not null, to avoid adding null values in the graph from empty fields
                clean_value = re.sub(r'\([^)]*\)',
                                     '', character[json_field]).strip()
                if 'lang' in config:
                    # Checks if there is a 'lang' attribute in config
                    # If it exists, then this is an rdfs:label triple and is added to the graph accordingly
                    lang_tag = config['lang']
                    g.add((char, RDFS.label, Literal(
                        clean_value, lang=lang_tag)))
                elif 'datatype' in config:
                    # Checks if there's a 'datatype' attribute in config
                    # If it exists, then it adds a triple with a Literal value using the 'datatype'
                    rdf_property = config['property']
                    g.add((char, rdf_property, Literal(
                        clean_value, datatype=config['datatype']
                    )))

                elif 'creates_uris' in config:
                    # Checks if creates_uris exists in config
                    # If it exists, then it adds a triple that links to another entity in the graph, assuming consistency in graph data
                    rdf_property = config['property']
                    rdf_class = config['property-range']

                    if 'multiple' in config:
                        items_list = split_semicolon_values(clean_value)

                        for item in items_list:
                            created_uri = op[item.replace(' ', '_')]
                            g.add((char, rdf_property, created_uri))
                            g.add((created_uri, RDF.type, rdf_class))
                    else:
                        created_uri = op[clean_value.replace(' ', '_')]
                        g.add((char, rdf_property, created_uri))
                        g.add((created_uri, RDF.type, rdf_class))

    g.bind("op", op)
    with open('sample-graph.ttl', 'w', encoding='utf-8') as f:
        f.write(g.serialize(format='turtle'))
        print("\n=== TURTLE FORMAT ===")
        print(f"File can be found in {os.path.abspath('sample-graph.ttl')}")


# +++ EXECUTION +++
if __name__ == "__main__":
    json_to_rdf()

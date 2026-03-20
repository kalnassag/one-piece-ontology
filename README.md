# one-piece-ontology

An ontology of the One Piece fictional universe and its representations in Manga, Anime and other media.

The initial point of start for this ontology is the Characters information extracted from https://onepiece.fandom.com, you can find that information in the files of this project, and more will be added later.

The goal is to build a comprehensive ontology that captures all the different relationships in the One Piece universe, which can be split into two main branches:

## 1. The Story

As told by Eiichiro Oda, which contains all the characters, events and locations of the One Piece universe.

## 2. The Representation

As implemented in the form of the manga, anime series, live action series or anime movies and any other representations over the years.

The story part is not strictly tied to the representation; for example, we don't necessarily need to know which manga issue or anime episode a character appeared in if we only want to document the story of One Piece.
Canon and Non-canon entities of the One Piece universe need differentiation for the sake of accuracy, and that can affect how we proceed with the ontology creation and the information associated with it.

This ontology is not building everything from scratch, and it utilises some established ontologies like FOAF, Schema, dbo and any other relevant ontologies, suggestions for expansion and ontology utilisation are always welcome.

## Project Structure

```
├── scraper/          # Data extraction from One Piece Fandom wiki
│   ├── src/          # Main scraper source code
│   ├── data/         # Raw and processed scraper data
│   ├── notebooks/    # Data exploration and cleaning
│   └── config.py     # Scraper configuration
├── pipeline/         # RDF conversion and knowledge graph ingestion
│   ├── entities_ingestion.py
│   ├── rdflib_basics.py
│   └── testing.py
├── ontology/         # OWL/RDF ontology and graph definitions
│   ├── onepiece-ontology.ttl
│   ├── OnePieceEntities-Base Model.ttl
│   └── one-piece-graph.ttl
├── data/             # Consolidated data files
│   ├── raw/          # Raw character and devil fruit data
│   └── processed/    # Cleaned and transformed data
└── index.html        # Ontology visualization
```
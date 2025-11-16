# Create High-Quality Knowledge Graphs

**Connected Data London 2025 Masterclass:**  
_Combining Data from Structured and Unstructured Sources to create High-Quality Knowledge Graphs_

Thu Nov 20, 2025  
09:30-11:30 GMT  
<https://2025.connected-data.london/talks/combining-data-from-structured-and-unstructured-sources-to-create-high-quality-knowledge-graphs/>

  * **Paco Nathan** and **Gurpinder Dhillon** @ [Senzing.com](https://senzing.com/)
  * slides: <https://derwen.ai/s/nrf8#0> or <https://drive.proton.me/urls/S7352D48GG#eGkDq6kWhLFs>


### Overview

Integrating structured and unstructured data sources into high-quality
knowledge graphs is an incredibly common need in production use
cases. Downstream there may be several patterns of usage for a
high-quality KG, such as graph analytics, dashboards, GraphRAG,
question/answer chat bots, agents, tools, memory, planners, and so on.

Throughout this masterclass, we will leverage insights from the
tutorial steps described below to identify patterns of _tradecraft_
within a graph, as a fraud analyst team at a bank would do.

Overall, we will show how to use open datasets with contemporary
[_entity resolution_](https://senzing.com/entity-resolution-generative-ai/)
to enhance AI applications for more trusted outcomes, streamlined
governance, better customer experiences, and accelerated innovation.

A tutorial in three parts:

  1. **Part 1**: Visualize fraud networks, using `Senzing`, `OpenSanctions`, `Open Ownership`, `Polars`, `Maplib`, `NetworkX`, `yWorks`
  2. **Part 2**: Entity embeddings in graphs: blend structured + unstructured data, using `Senzing`, `LanceDB`, `RDFlib`, `NetworkX`, `DSPy`, `Ollama`
  3. **Part 3**: How to become a money launderer

### Course Goals

Gain hands-on experience in Python using high-quality knowledge graphs
with _entity resolution_, _computable semantics_, _entity embeddings_,
_graph algorithms_, _interactive visualization_, plus _context
engineering_ to augment the graph and enhance downstream AI
applications.

### Target Audience

  * Data Scientists, Machine Learning Engineers
  * Data Engineers, MLOps
  * Financial Fraud Analysts
  * Team leads and managers for the roles above

### Prerequisites

  * Level: Beginner - Intermediate
  * Some experience coding in Python
  * Familiarity with popular packages such as Jupyter and Docker

**Important:**
You must have [Docker](https://docs.docker.com/get-docker/),
[Git](https://git-scm.com/install/),
and [Python 3.13+](https://www.python.org/downloads/release/python-3139/)
downloaded and installed to run this tutorial.

Before going to the conference, **download this container** onto your
laptop:

```bash
docker pull senzing/serve-grpc:latest
```

NB: due to sudden changes for `KùzuDB`, we've had to adjust the
content of this course, and unfortunately **Prashanth Rao** will not
be able to join.

We will include additional content using `LanceDB` and `DSPy` for
context engineering, plus a section on "how to become a money launderer"
-- leveraging graph analytics to examine `OCCRP` leaked data from the
"Azerbaijani Laundromat" case.


---

## Part 1: Visualize Fraud Networks

  * Duration: 55 minutes
  * GitHub repository: <https://github.com/DerwenAI/cdl-2025-masterclass>

We'll start with a brief intro lecture covering the background for
leveraging these technologies together with open data in an anti-fraud
use cases.

1. Download the Docker container for `Senzing` gRPC server (during the intro)
2. Launch the `Senzing` container and run it in the background for a gRPC server.
3. Initialize the Python environment on your laptop using `uv` to load the library dependencies.
4. Download slices of the `OpenSanctions` and `Open Ownership` datasets.
5. Run _entity resolution_ in `Senzing` to merge the datasets and generate graph "building blocks" in RDF, as a domain-specific thesaurus.
6. Review the _metadata application profile_ (MAP) for the SKOS taxonomy used, how it integrates with [NIEM](https://niem.github.io/), [FollowTheMoney](https://followthemoney.tech/), [BODS](https://bods-data.openownership.org/), and so on.
7. Also transform records from the datasets into `Polars` dataframes.
8. Use SPARQL queries in `Maplib` to transform the RDF into `Polars` dataframes.
9. Load tables into a graph database from the dataframes.
10. Leverage graph algorithms in `NetworkX`: partitioning to identify subgraphs as potential fraud rings within the graph, and betweenness centrality to rank individuals of interest within each subgraph.
11. Run visualizations using `yFiles` to examine the [2021 South London Papa Johns](https://www.newsshopper.co.uk/news/19164815.boss-bromley-catford-papa-johns-stores-jailed/) tax evasion case.
12. Q&A discussion.

Tutorial: [PART1 instructions](PART1.md)

### Links to components

  * <https://github.com/senzing-garage/sz-semantics>
  * <https://github.com/senzing-garage/serve-grpc>
  * <https://www.opensanctions.org/>
  * <https://www.openownership.org/>
  * <https://github.com/DataTreehouse/maplib>
  * <https://pola.rs/>
  * <https://networkx.org/>
  * <https://jupyter.org/>
  * <https://www.yworks.com/products/yfiles-graphs-for-jupyter>
  * <https://github.com/yWorks/yfiles-jupyter-graphs-for-kuzu>

---

## Part 2: Entity Embeddings in Graphs

  * Duration: 30 minutes
  * GitHub repository: <https://github.com/DerwenAI/strwythura>

Let's build on what we covered in **Part 1**, and examine how to use
_entity embeddings_ in graphs, to blend structured and unstructured
data, using `Senzing`, `LanceDB`, `RDFlib`, `NetworkX`, `DSPy`,
`Ollama` -- applying a more intentional approach to developing
"context" for _context engineering_.

This uses _entity resolution_ (ER) with _computable semantics_,
starting from a _taxonomy_ curated per use case, then generating a
_domain-specific thesaurus_ from structured data sources. In other
words, resolve identify information about people and organizations
along with relations among the entities, their synonyms, and so on,
and use this as a "backbone" for working with the graph.

During KG construction and updates, the domain-specific context
focuses the _named entity recognition_ (NER) and _entity linking_ to
extract entities from unstructured data sources and link these
contextually into the KG.

Given the thesaurus, we'll construct the following bundle of assets
from the unstructured sources:

  * _vector store_ with embeddings of text chunks, cross-linked with entities
  * _entity embedding_ model, built from sequences of lemmatized noun phrases
  * _lexical graph_ constructed from parsed text chunks using a _textgraph_ algorithm

This provides better afforandances for _human-in-the-loop_ (HITL)
curation of extracted entities (vs. resolved entities) before their
promotion into the KG, and also guides how to tranform RDF
representation (which allows for validation, relation range
constraints, etc.) into a property graph.

Working from these assets as a basis, we can promote graph elements
(entities, relations, properties) into the resulting KG, retaining the
cross-links with the vector store.

Downstream from the KG, during run-time use, the entity embeddings
enhance LLM integrations in multiple ways to enhance outcomes in AI
applications.

  * query the entity embedding model, as a more robust alternative to `Text2Cypher` (or complementary)
  * use _semantic expansion_ and _random walks_ so than entity reranking drives text chunk reranking
  * include text definitions for classes in the taxonomy into the reranked text chunks


We will this section begin with a brief introduction to the topics
plus overview of available (albeit less often discussed) technology
components.

Then we'll have a live demo and code walk-through in the
implementation:

  1. Run _entity resolution_ in `Senzing` to merge the datasets and generate graph "building blocks" in RDF, as a domain-specific _thesaurus_.
  2. Construct a "backbone" for a knowledge graph in `NetworkX` from the thesaurus.
  3. Crawl the related documents, chunking text from the unstructured content and loading chunks plus their embeddings into `LanceDB`.
  4. Parse the text in each chunk using `GLiNER` _zero-shot NER_ in a `spaCy` pipeline, based on semantic definitions from the thesaurus.
  5. Use a _textgraph_ algorithm to construct a lexical graph which links to the text chunks, plus ranking for the "most referenced" entities.
  6. Curate semantics for optimizing the AI app outcomes within a specific domain.
  7. Entity linking: promote entities extracted from the unstructured content into the KG, linked to ER results.
  8. Build _entity embeddings_ in `GenSim`, determining their neighborhoods semantic expansion.
  9. Use `NetworkX` for _semantic expansion_ and _semantic random walks_ to rerank text chunks in `LanceDB`.
  10. Implement a question/answer chat bot based on GraphRAG using `DSPy` and `Ollama`, running the `gemma3:12b` LLM locally.
  11. Q&A discussion.

Tutorial: [PART2 instructions](PART2.md)

### Links to components

  * <https://senzing.com/what-is-entity-resolution/>
  * <https://lancedb.com/>
  * <https://spacy.io/>
  * <https://github.com/urchade/GLiNER>
  * <https://networkx.org/>
  * <https://radimrehurek.com/gensim/models/word2vec.html>
  * <https://dspy.ai/>
  * <https://ollama.com/>
  * <https://huggingface.co/google/gemma-3-12b-it>
  * <https://pyinstrument.readthedocs.io/>

---

## Part 3: How to become a money launderer

  * Duration: 20 minutes
  * GitHub repository: <https://github.com/DerwenAI/cdl-2025-masterclass/>

Let's build on what we covered in **Part 1** and **Part 2** to develop
more sophisticated graph-based analysis for fraud tradecraft. Recall
from the general-case data model used for anti-fraud that the _event_
data is difficult to obtain, and we did not use it in **Part 1**.

So now we will introduce event data from whistleblower leaks, to
analyze a real-world case. Then let's examine how to use _leaked data_
to build simulations which generate _synthetic data_. This allows for
better evaluation of anti-fraud approaches, both in terms of scale and
diversity of patterns.

We'll start with a brief intro about the "Azerbaijani Laundromat"
incident (~$3B money laundering) with real-world examples of how graph
technologies empower anti-fraud investigations.

  1. Review _anti-money laundering_ points in summarized excerpts from the highly recommended [_The Dark Money Files_](https://www.thedarkmoneyfiles.com/) by **Graham Barrow** and **Ray Blake**.
  2. Demo of the notebook in the `kleptosyn` repo for forensic accounting, graph-based flow analysis, and interactive visualization of the Azerbaijani Laundromat leaked data from `OCCRP`.
  3. Demo of the AML notebook in this repo to show how synthetic data for wire transfer transactions can simulate patterns of criminal tradecraft among fraud networks represented in a graph.
  4. Review resources for how data practitioners can get involved: GraphGeeks community, learn more about AML, human trafficking certification, support whistleblowers, etc.
  5. Q&A discussion.

Tutorial: [PART3 instructions](PART3.md)

### Links to components

  * <https://www.thedarkmoneyfiles.com/>
  * <https://www.occrp.org/en/project/the-azerbaijani-laundromat/the-raw-data>
  * <https://github.com/DerwenAI/kleptosyn>
  * <https://networkx.org/>
  * <https://pyvis.readthedocs.io/>
  * <https://seaborn.pydata.org/>
  * <https://matplotlib.org/>
  * <https://youtu.be/Gtp7U0iq-2I?feature=shared>
  * <https://jupyter.org/>


---

Kudos to
[@prrao87](https://github.com/prrao87),
[@brianmacy](https://github.com/brianmacy),
[@jbutcher21](https://github.com/jbutcher21),
[@docktermj](https://github.com/docktermj),
[@cj2001](https://github.com/cj2001),
[@louisguitton](https://github.com/louisguitton),
[@jesstalisman-ia](https://github.com/jesstalisman-ia),
[@pudo](https://github.com/pudo),
[@StephenAbbott](https://github.com/StephenAbbott),
and the kind folks at [GraphGeeks](https://graphgeeks.org/) for their support.

# Create High-Quality Knowledge Graphs

**Connected Data London 2025 Masterclass:**  
_Combining Data from Structured and Unstructured Sources to create High-Quality Knowledge Graphs_

Thu Nov 20, 2025  
09:30-11:30 GMT  
<https://2025.connected-data.london/talks/combining-data-from-structured-and-unstructured-sources-to-create-high-quality-knowledge-graphs/>

  * **Paco Nathan** and **Gurpinder Dhillon** @ [Senzing.com](https://senzing.com/)
  * slides: <https://drive.proton.me/urls/S7352D48GG#eGkDq6kWhLFs>


### Overview

Integrating structured and unstructured data sources into high-quality
knowledge graphs is an incredibly common need in production use
cases. Downstream there may be several patterns of usage for a
high-quality KG, such as graph analytics, dashboards, GraphRAG,
question/answer chat bots, agents, tools, memory, planners, and so on.

Through this masterclass, we will leverage insights from the tutorial
steps described below to identify patterns of _tradecraft_ within a
graph, as a fraud analyst team at a bank would do.

Overall, we will show how to use open datasets with contemporary
[_entity resolution_](https://senzing.com/entity-resolution-generative-ai/)
to enhance AI applications for more trusted outcomes, streamlined
governance, better customer experiences, and accelerated innovation.

A tutorial in three parts:

  1. **Part 1**: Visualize fraud networks, using `Senzing`, `OpenSanctions`, `Open Ownership`, Maplib, `RyuGraph`, `yWorks`
  2. **Part 2**: Blending structured and unstructured data in KGs for context engineering using `Senzing`, `LanceDB`, `DSPy`, `Ollama`
  3. **Part 3**: How to become a money launderer

Note that due to sudden unforeseen changes for `KùzuDB`, we've had to
adjust the content of this course, and one of the original co-authors,
**Prashanth Rao**, will not be able to join. Now we'll use `RyuGraph`
instead, and also make loads of use of `NetworkX`, which can be scaled
and accelerated using `cuGraph` on NVIDIA GPUs.

We will also include additional content about using `LanceDB` and
`DSPy` for context engineering, plus a section on how to become a
money launderer -- leveraging graph analytics to examine the leaked
`OCCRP` data for the "Azerbaijani Laundromat" case.

### Course Goals

Gain hands-on experience with tools in Python using high-quality
knowledge graphs with entity resolution, graph algorithms, interactive
visualization, plus context engineering both to augment the graph and
enhance downstream AI applications.

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
You must have both [Docker](https://docs.docker.com/get-docker/)
and [Python 3.13+](https://www.python.org/downloads/release/python-3139/)
downloaded and installed to run this tutorial.

Before going to the conference, you need to have downloaded
**these two containers** onto your laptop:

```bash
docker pull senzing/serve-grpc:latest
docker pull ryugraphdb/explorer:latest
```

---

## Part 1: Visualize Fraud Networks

  * Duration: 55 minutes
  * GitHub repository: <https://github.com/DerwenAI/cdl-2025-masterclass>

We'll start with a brief intro lecture covering the background for
leveraging these technologies together with open data in an anti-fraud
use cases.

1. Download the Docker containers for `Senzing` gRPC server and `RyuGraph` Explorer (during the intro)
2. Initialize the Python environment on your laptop using `uv` to load the library dependencies.
3. Download slices of datasets from `OpenSanctions` and `Open Ownership`.
4. Launch the `Senzing` container and run it in the background for a gRPC server.
5. Run _entity resolution_ in `Senzing` to merge the datasets and generate graph "building blocks" in RDF, as a domain-specific thesaurus.
6. Review the _metadata application profile_ (MAP) for the SKOS taxonomy used, how it integrates with [NIEM](https://niem.github.io/), [FollowTheMoney](https://followthemoney.tech/), [BODS](https://bods-data.openownership.org/), and so on.
7. Use SPARQL queries in `Maplib` to transform the RDF into `Polars` dataframes.
8. Also transform records from the datasets into `Polars` dataframes.
9. Load tables into `RyuGraph` from the dataframes.
10. Leverage graph algorithms in `NetworkX`: partitioning to identify subgraphs as potential fraud rings within the graph, and betweenness centrality to rank individuals of interest within each subgraph.
11. Run visualizations using `yFiles` to examine the [2021 South London Papa Johns tax evasion case](https://www.newsshopper.co.uk/news/19164815.boss-bromley-catford-papa-johns-stores-jailed/)
12. Q&A discussion.

Tutorial: [PART1 instructions](PART1.md)

### Links to components

  * <https://github.com/senzing-garage/sz-semantics>
  * <https://github.com/senzing-garage/serve-grpc>
  * <https://www.opensanctions.org/>
  * <https://www.openownership.org/>
  * <https://ryugraph.io/>
  * <https://github.com/DataTreehouse/maplib>
  * <https://pola.rs/>
  * <https://networkx.org/>
  * <https://github.com/rapidsai/nx-cugraph>
  * <https://github.com/yWorks/yfiles-jupyter-graphs>

---

## Part 2: Unbundling the Graph in GraphRAG

  * Duration: 30 minutes
  * GitHub repository: <https://github.com/DerwenAI/strwythura>

Let's build on what we covered in **Part 1**, to show how to blend
structured and unstructured data in KGs for _context engineering_
based on `Senzing`, `LanceDB`, `DSPy`, `Ollama`.

This approach extends on much of what is published elsewhere by
several key points during graph+vector construction:

  * entity resolution (ER) on structured data, as a generative approach for graph elements
  * text chuning on paragraph boundaries, split into sentences which can be identified later
  * natural language parsing per sentence, using zero-shot NER with context from the SKOS taxonomy
  * entity linking of NER with ER results based on tagged, lemmatized noun phrases
  * textgraph algorithm used to contruct a lexical graph and rank entities based on usage
  * embedding model of co-occurring entities, with bi-directional links to text chunks
  * human-in-the-loop curation of extracted entities (vs. resolved entities) for promotion into the KG
  * tranform RDF representation (to allow for validation, range constraints, etc.) into a property graph

Then during integration with a large languge model (LLM), this
approach also extends typical practices with:

  * using entity embedding instead of `Text2Cypher` (could also be complementary)
  * leverage bi-direction links between entity and text chunk embeddings
  * semantic expansion based on the KG, which can be constrained by domain vocabularies
  * semantic random walk so that entity reranking drives text chunk reranking

In other words, leverage the graph structure from entity resolution,
plus the computable semantics and entity embeddings, to improve the
domain-specific context for downstream AI applications.

We'll start with a brief introduction covering why
["unbundling the graph in GraphRAG"](https://www.oreilly.com/radar/unbundling-the-graph-in-graphrag/)
allows more effective curation of semantics-driving-embeddings for
domain-specific context, improving downstream AI application
workflows.

Then we'll have a live demo and walk through the highlights of this
implementation in the code.

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

  1. Review the _anti-money laundering_ points in summarized excerpts from [_The Dark Money Files_](https://www.thedarkmoneyfiles.com/) by **Graham Barrow** and **Ray Blake**.
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

---

Kudos to
[@prrao87](https://github.com/prrao87),
[@brianmacy](https://github.com/brianmacy),
[@jbutcher21](https://github.com/jbutcher21),
[@docktermj](https://github.com/docktermj),
[@cj2001](https://github.com/cj2001),
[@jesstalisman-ia](https://github.com/jesstalisman-ia),
[@pudo](https://github.com/pudo),
[@StephenAbbott](https://github.com/StephenAbbott),
and the kind folks at [GraphGeeks](https://graphgeeks.org/) for their support.

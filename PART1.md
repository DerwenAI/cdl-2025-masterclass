# Create High-Quality Knowledge Graphs

**Connected Data London 2025 Masterclass:**  
_Combining Data from Structured and Unstructured Sources to create High-Quality Knowledge Graphs_

**Part 1**: Visualize fraud networks, using `Senzing`, `OpenSanctions`, `Open Ownership`, `Maplib`, `RyuGraph`, `yWorks`


## GitHub repository for the tutorial

First and foremost, use `Git` to clone the GitHub repository for this
course onto your laptop, then connect into that directory:

```bash
git clone https://github.com/kuzudb/cdl-2025-masterclass.git
cd cdl-2025-masterclass
```


## Docker container for the Senzing gRPC server

Assuming you've already downloaded the `serve-grpc` container onto
your laptop, prior to the start of the course since it takes several
minutes, depending on the WiFi quality ... though if not, here's the
command line for that:

```bash
docker pull senzing/serve-grpc:latest
```

Using another terminal window, launch the container and run it in the
background to provide a gRPC server, from which to call the Senzing
SDK from Python code running in JupyterLab notebooks.

```bash
docker run -it --publish 8261:8261 --rm senzing/serve-grpc
```


## Python library dependencies

This course uses `uv` to initialize a Python environment and manage
the library dependencies.  To install `uv` for your OS:
<https://docs.astral.sh/uv/getting-started/installation/>

Then use `uv` to install the required libraries:

```bash
uv sync
source .venv/bin/activate
```


## Senzing entity resolution

To get started on constructing our knowledge graph for visualizing
fraud networks, we need to download the datasets and run _entity
resolution_ (ER) to merge these. Then generate a _domain-specific
thesaurus_ from the ER results, used to generate "building blocks" for
constructing a graph. Launch JupyterLab and run the `1.run_er.ipynb`
notebook:

```bash
.venv/bin/jupyter-lab 1.run_er.ipynb
```

Let's look through the _metadata application profile_ (MAP) for the
SKOS taxonomy used by Senzing, to see how it integrates with
[NIEM](https://niem.github.io/),
[FollowTheMoney](https://followthemoney.tech/),
[BODS](https://bods-data.openownership.org/),
and so on.
In your browser, open
<https://github.com/senzing-garage/sz-semantics/wiki/ns>


## Polars dataframes for loading graph elements


We'll use SPARQL queries in `Maplib` to reform the RDF into _property graph_ elements in `Polars` dataframes which can then be loaded into RyuGraph.

---


8. Also transform records from the datasets into `Polars` dataframes.
9. Load tables into `RyuGraph` from the dataframes.
10. Leverage graph algorithms in `NetworkX`: partitioning to identify subgraphs as potential fraud rings within the graph, and betweenness centrality to rank individuals of interest within each subgraph.
11. Run visualizations using `yFiles` to examine the [2021 South London Papa Johns tax evasion case](https://www.newsshopper.co.uk/news/19164815.boss-bromley-catford-papa-johns-stores-jailed/)
12. Q&A discussion.

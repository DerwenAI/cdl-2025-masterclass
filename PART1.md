# Create High-Quality Knowledge Graphs

**Connected Data London 2025 Masterclass:**  
_Combining Data from Structured and Unstructured Sources to create High-Quality Knowledge Graphs_

**Part 1**: Visualize fraud networks, using `Senzing`, `OpenSanctions`, `Open Ownership`, `Polars`, `Maplib`, `NetworkX`, `yWorks`


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
SDK from Python code running in `JupyterLab` notebooks.

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
constructing a graph.

Launch `JupyterLab` and open the `1.run_er.ipynb` notebook:

```bash
./.venv/bin/jupyter-lab 1.run_er.ipynb
```

Let's look through the _metadata application profile_ (MAP) for the
SKOS taxonomy used by Senzing, to see how it integrates with
[NIEM](https://niem.github.io/),
[FollowTheMoney](https://followthemoney.tech/),
[BODS](https://bods-data.openownership.org/),
and so on.
In your browser, open
<https://github.com/senzing-garage/sz-semantics/wiki/ns>


## Transform data records into dataframes

Transform the source data records from the open datasets into `Polars` dataframes.
Then serialize these dataframes as CSV files for use later.

In `JupyterLab` open the `2.open_data.ipynb` notebook:

```bash
./.venv/bin/jupyter-lab 2.open_data.ipynb
```


## Reform RDF triples into a property graph

We'll use SPARQL queries in `Maplib` to reform the RDF into _property graph_ elements in `Polars` dataframes.
Then load nodes and edges from the dataframes into their corresponding tables in the graph database.

In `JupyterLab` open the `3.reform.ipynb` notebook:

```bash
./.venv/bin/jupyter-lab 3.reform.ipynb
```

## Graph analytics

Leverage graph algorithms in `NetworkX`: 

  - partitioning to _identify subgraphs_ as potential fraud rings within the graph
  - betweenness centrality to _rank individuals_ of interest within each subgraph

In `JupyterLab` open the `4.analytics.ipynb` notebook:

```bash
./.venv/bin/jupyter-lab 4.analytics.ipynb
```


## Interactive visualization

Let's complete the implementation of the **four-step design pattern** for graph analytics in anti-fraud, by running interactive visualizations using
[`yFiles`](https://www.yworks.com/products/yfiles-graphs-for-jupyter)
to examine a subgraph about the
[2021 South London Papa Johns](https://www.newsshopper.co.uk/news/19164815.boss-bromley-catford-papa-johns-stores-jailed/)
tax evasion case.

We'll develop a theme about leveraging AI applications to "refocus the lens" in complex problems (such as developing prosecutable evidence against criminal networks) to bring them back to human scale, and optimize for collaboration within and across teams.

In `JupyterLab` open the `5.kg_vis.ipynb` notebook:

```bash
./.venv/bin/jupyter-lab 5.kg_vis.ipynb
```


## Q&A discussion

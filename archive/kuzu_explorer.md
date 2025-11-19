## Graph visualization in Kuzu Explorer

To visualize the graph in Kuzu using its browser-based UI, Kuzu
Explorer, run the following commands from this root directory:

```bash
docker run -p 8000:8000 \
           -v db:/database \
           -e MODE=READ_WRITE \
           --rm kuzudb/explorer:latest
```

This will download and run the Kuzu Explorer image, and you can access
the UI at <http://localhost:8000>

Make sure that the path to the database directory is set to the name
of the Kuzu database directory in the code!

In the Explorer UI, enter the following Cypher query in the shell
editor to visualize the graph:

```cypher
MATCH (a:Entity)-[b*1..3]->(c)
RETURN *
LIMIT 100
```

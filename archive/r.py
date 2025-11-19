import ryu

db = ryu.Database("database.dir")
conn = ryu.Connection(db)

conn.execute("CREATE NODE TABLE User(name STRING PRIMARY KEY, age INT64)")
conn.execute("CREATE NODE TABLE City(name STRING PRIMARY KEY, population INT64)")
conn.execute("CREATE REL TABLE Follows(FROM User TO User, since INT64)")
conn.execute("CREATE REL TABLE LivesIn(FROM User TO City)")

conn.execute('COPY User FROM "./data/user.csv"')
conn.execute('COPY City FROM "./data/city.csv"')
conn.execute('COPY Follows FROM "./data/follows.csv"')
conn.execute('COPY LivesIn FROM "./data/lives-in.csv"')

response = conn.execute(
    """
    MATCH (a:User)-[f:Follows]->(b:User)
    RETURN a.name, b.name, f.since;
    """
)

for row in response:
    print(row)

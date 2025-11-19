# Create High-Quality Knowledge Graphs

**Connected Data London 2025 Masterclass:**  
_Combining Data from Structured and Unstructured Sources to create High-Quality Knowledge Graphs_

## Part 3: How to become a money launderer


## Money Laundering

First, take a look at the [AML.md](AML.md) file which describes some
of the heuristics used by fraud analysts to spot not-so-legit things
happening during financial transactions. These heuristics help assess
whether a bank account has been used for money laundering.

In other words, this is helpful info for someone who is new to
_anti-money laundering_ (AML) or, for that matter, anyone thinking
about **becoming a money launderer**.


## Forensic accounting on leaked data with graph algorithms in `NetworkX`

While it's possible to get open data which describes companies, their
ownership, sanctions risks -- i.e., the "risk" and "link" data in an
investigative graph -- it's difficult to obtain "event" data such as
financial transactions. Generally this class of data is much too
confidential; however, in some cases transactions for large-scale
fraud have been leaked.

[Howard Wilkinson](https://www.ft.com/content/32d47fd8-c18b-11e8-8d55-54197280d3f7)
was the whistleblower in a massive-scale money laundering case at
the Estonia branch of Danske Bank.
Wilkinson noticed bank transactions with a shell company named
"Lantana Trade" and the rest of the story became history.
This leak provided PDFs for 17K wire transfer records in the
[Azerbaijani Laundromat](https://www.occrp.org/en/project/the-azerbaijani-laundromat)
case.

This next section of this course is based on the
[`kleptosyn`](https://github.com/DerwenAI/kleptosyn)
repository on GitHub.

While you are very much welcomed to clone and run repo this yourself,
in the interest of time we'll run this as a brief demo. Let's examine
the `occrp.ipynb` notebook which implements several of the heuristics
mentioned above using graph algorithms for _flow analysis_ and
_forensice accounting_, developing means of classifying the roles of
shell companies.

This notebook also serves as a pretty good "cheat sheet" for how to
use `NetworkX` when you're just beginning to explore a new dataset as
a graph.


## What's missing?

Synthetic data.
But we have some bonus material, which we'll cover if we have time!

Recall that obtaining "event" data is difficult. We can't always count
on having brave whistleblowers leak data from banks involved in
sketchy business.

But we can sample from leaks, simulate the transactions of a fraud
network in operation using known patterns of criminal tradecraft, then
generate "event" data as _synthetic data_.

Simulation methods defined in the `aml.py` Python module use paramters
based on analysis from known money laundering cases, such as what was
discovered about the Azerbaijani Laundromat above:

```bash
python3 aml.py
```

Then in the next workflow we generate synthetic data to simulate money
laundering. We use shell companies which were part of some real-world
fraud network, then generate simulated transactions based on
statistical analysis of leaked bank data.

In `JupyterLab` open the `6.aml.ipynb` notebook:

```bash
./.venv/bin/jupyter-lab 6.aml.ipynb
```

BTW, for more examples of this kind of approach, see
<https://github.com/IBM/AMLSim>

This is a work in progress. We invite others to collaborate.

Stay tuned for more soon --
>same bat-time, same bat-channel!


## Q&A discussion

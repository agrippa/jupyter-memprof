# jupyter-memprof

## Background

When doing exploratory data analysis on a new dataset or project, it is common
to end up with an outrageously long Jupyter notebook containing hundreds of
cells worth of code and objects as a data scientist explores, learns, and
visualizes a dataset.

It is not uncommon for that exploratory analysis to come to an abrupt and
screeching halt when the data scientist is suddenly faced with a `MemoryError`
-- their Python instance has run out of memory.

Assuming the scientist in question has some background in Computer Science and
some understanding of Python's internal object model and garbage collection
(which is not always the case), they may try deleting some references to objects
while using `gc.collect()` to release memory.

However, it is rarely clear which objects to release or even how to release
them. The largest consumers of memory may have been created hundreds of code
cells ago. They may be referenced from multiple variables in the Jupyter
notebook, and identifying which may be difficult.

Fundamentally, this problem is caused by a mismatch between the Python garbage
collector and Jupyter notebooks. Python GC works well for procedural,
well-scoped code in which references to objects that are no longer needed are
automatically cleaned up as we leave local and functional scopes that contain
those references. However, Jupyter notebooks (particularly exploratory ones)
tend to be written entirely in a single, global scope -- preventing the Python
garbage collector from cleaning up any objects automatically.

Without the ability to identify and clean up some large, leftover objects the
data scientist is left with no other option but to restart their Jupyter kernel,
deleting all of the accumulated state in that notebook.

This repo aims to offer utilities and tools for addressing this problem. It will
likely start with small and relatively simple utilities, but I hope to expand it
over time. The sections below outline different utilities and examples included
in this repo.

## `jupyter_memprof.big_objs()`

The `big_objs` method can be used to list (by name) a set of live, large objects
in memory in the current Python instance.

`big_objs` uses the `guppy` package to iterate over objects in memory to pull
out and return a list of objects that the programmer should consider deleting.
In general, the Python `del` keyword can then be used to remove references to
these objects in the Jupyter notebook, and `gc.collect()` can be used to force
the re-collection of that memory.

An example of this API is included in `notebooks/sandbox_lib.ipynb`.

## Contact

Questions about this repo can be directed to Max Grossman (max@7pod.tech).

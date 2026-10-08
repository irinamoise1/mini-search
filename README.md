# Mini Search

A simple text search engine written in Python. It reads `.txt` files from a folder, builds an inverted index and returns the files that contain all the words you search for, ranked by relevance.

# How it works

1. **Tokenization** – each text is lowercased, punctuation is removed and the text is split into a list of words.
2. **Inverted index** – a dictionary that maps every word to the set of files where it appears (like the index at the end of a book).
3. **Search** – for a query with several words, the program finds the files that contain *all* of them by intersecting the sets of files of each word.
4. **Ranking** – the matching files are sorted by how many times the query words appear in them, so the most relevant file comes first.

# Project structure

    search.py        # the search engine and the command-line interface
    test_search.py   # unit tests (pytest)
    docs/            # sample text files (e.g. cat.txt, italy.txt)

# How to run

Put your `.txt` files in the `docs` folder, then run:

    python search.py

Type a word or a phrase to search, or `exit` to quit.

# Run the tests

    pip install pytest
    pytest

# What I learned

- How an inverted index works and why it makes searching fast.
- Working with dictionaries, sets and set intersection in Python.
- Writing unit tests with pytest.

# Possible improvements

- Better ranking, so that rare words count more than very common ones.
- Support searching for any of the words (OR), not only all of them (AND).
- Ignore very common words (stop words).

## Notes

The sample texts in `docs` are short excerpts from Wikipedia, used only for testing.

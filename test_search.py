from search import tokenize, build_index, search_all, rank

def test_tokenize_basic():
    assert tokenize("Cat sleeps!") == ["cat", "sleeps"]

def test_tokenize_newline():
    assert tokenize("cat\nsleeps") == ["cat", "sleeps"]

DOCS = {
    "cat.txt": ["cat", "is", "a", "domestic", "animal"],
    "italy.txt": ["italy", "is", "a", "country"],
}

def test_search_all_one_file():
    index = build_index(DOCS)
    assert search_all(index, "domestic cat") == {"cat.txt"}

def test_search_all_no_file():
    index = build_index(DOCS)
    assert search_all(index, "domestic italy") == set()

def test_search_all_diff_files():
    index = build_index(DOCS)
    assert search_all(index, "is") == {"cat.txt", "italy.txt"}
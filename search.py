import os

def tokenize(sentence: str):
    result=""
    for char in sentence:
        if char.isalpha() or char.isspace():
            result+=char.lower()

    return result.split()


def load_documents(folder):
    documents={}
    for name in os.listdir(folder): #parcurg numele fisierelor
        path=folder+"/"+name
        with open(path, encoding="utf-8") as f:
            text=f.read()
        words=tokenize(text)
        documents[name]=words
    return documents

def build_index(documents):
    index={}
    for name in documents:
        for word in documents[name]:
            if word not in index:
                index[word]=set()
            index[word].add(name)
    return index

def search(index, word):   
    return index.get(word.lower(),set())

def search_all(index, query):
    words=tokenize(query)
    if not words:
        return set()
    result=search(index, words[0])
    for word in words[1:]:
        result= result&search(index,word)
    return result

def rank(documents, index, query):
    words=tokenize(query)
    scores={}
    for name in search_all(index, query):
        score=0
        for word in words:
            score+=documents[name].count(word)
        scores[name]=score
    return sorted(scores, key=scores.get, reverse=True)

def main():
    
#print(search_all(index, "domestic cat")) #da cat.txt pentru ca acolo se regasesc ambele cuvinte
#print(search_all(index, "domestic italy")) #da set() pentru ca nu avem un fisier care sa le aiba pe amandoua
#print(search_all(index, "xyz")) #da set() pentru ca nu exista nicaieri

    docs=load_documents("docs")
    index=build_index(docs)

    while True:
        query=input("Search (or write 'exit' to leave): ")
        if query=="exit":
            break
        results=rank(docs, index, query)
        if not results:
            print(f"No result for: {query}")
        else:
            for number, name in enumerate(results, start=1):
                print(f"{number}. {name}")

if __name__=="__main__":
    main()
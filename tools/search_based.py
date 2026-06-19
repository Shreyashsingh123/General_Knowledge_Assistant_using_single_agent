from ..RAG.retreive import retreiver
def search(query:str) ->str:
    return retreiver(query)


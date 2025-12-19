def add_prefix(document:str, documents:tuple) ->tuple:
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    return documents + (new_doc,)

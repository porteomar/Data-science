def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    index_dict = {}
        
    if keywords == []:
        return index_dict
    else:
        for keyword in keywords:
            index_dict.update({keyword:[]})
    
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        cleaned = [token.rstrip('.,?!').lower() for token in tokens]
    
        for keyword in keywords:            
            if keyword.lower() in cleaned:
                index_dict[keyword].append(i)

    return index_dict
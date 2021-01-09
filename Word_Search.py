# Word Search
# takes in a word and a list of documens and returns a list of idx vals of the docs that contain the word

def word_search(doc_lst, word):
    index_lst = []

    for i, doc in enumerate(doc_lst):
        tokens = doc.split()
        cleaned = [token.rstrip('.,?!').lower() for token in tokens]
    
        if word.lower() in cleaned:
            index_lst.append(i)
            
    return index_lst

example_lst = ["My name is Omar.", "Hello!", "What is today?", "Omar, is hungry!"]
print(word_search(example_lst, 'Hello'))
print(word_search(example_lst, 'Omar'))
print(word_search(example_lst, 'is'))



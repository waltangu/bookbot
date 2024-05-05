def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_text = f.read()
    word_list = file_text.split()
    word_count = len(word_list)
    
    count_dict = {
        "a": 0, "b": 0, "c": 0,
        "d": 0, "e": 0, "f": 0,
        "g": 0, "h": 0, "i": 0,
        "j": 0, "k": 0, "l": 0,
        "m": 0, "n": 0, "o": 0, 
        "p": 0, "q": 0, "r": 0, 
        "s": 0, "t": 0, "u": 0, 
        "v": 0, "w": 0, "x": 0, 
        "y": 0, "z": 0
    }
    
    lowered_text = file_text.lower()
    for letter in lowered_text:
        if letter in count_dict:
            count_dict[letter] += 1
    
    dict_list = []
    for entry in count_dict:
        list_item = {"letter": entry, "count": count_dict[entry]}
        dict_list.append(list_item)
    from operator import itemgetter
    sorted_list = sorted(dict_list, key=itemgetter('count'), reverse=True)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for counter in sorted_list:
        for item in counter:
            l = counter["letter"]
            c = counter["count"]
        print(f"The {l} character was found {c} times")
    print("--- End report ---")



main()
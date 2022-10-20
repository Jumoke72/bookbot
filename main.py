def sort_on(d):
    return d["num"]

def get_num_words(text):
    words = text.split()
    return (len(words))

def get_chars_dict(text):
    chars = {}
    for c in text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return (chars)

def get_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
#   sorted_list.sort(reverse=True, key=lambda s: s["num"])
    sorted_list.sort(reverse=True, key=sort_on) #key takes a function as input
    return(sorted_list)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        chars_dict = get_chars_dict(file_contents)
        sorted_list = get_sorted_list(chars_dict)
                
        print ("--- Begin report of books/frankenstein.txt ---")
        print (f"{num_words} words found in the document")
        print()

        for item in sorted_list:
            if item["char"].isalpha():
                print(f"The '{item['char']}' character was found {item['num']} times")
        print("--- End report ---")

main()


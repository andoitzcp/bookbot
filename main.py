#!/usr/bin/env python3

def ft_countcharoccurrences(blob):
    blob = blob.lower()
    char_count = {}
    for char in blob:
        if (char not in char_count):
            char_count[char] = 0
        char_count[char] += 1
    return (char_count)

def ft_convdicttolist(dictry):
    list = []
    for k in dictry:
        char_entry = {"char": k, "q": dictry[k]}
        list.append(char_entry)
    return (list)

def ft_sorton(dict):
    return (dict["q"])

def ft_printreport(wc, char_ranking):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document\n")
    for entry in char_ranking:
        char = entry["char"]
        qty = entry["q"]
        if (char.isalpha()):
            print(f"The '{char}' character was found '{qty}' times")
    print("--- End report ---")


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    occurrence_dict = ft_countcharoccurrences(file_contents)
    occurrence_list = ft_convdicttolist(occurrence_dict)
    occurrence_list.sort(reverse=True, key=ft_sorton)
    ft_printreport(len(words), occurrence_list)

main()

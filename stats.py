def count_words(text):
    word_list = text.split()

    return len(word_list)


def count_letters(text):

    occurrence_dict = {}

    for char in text:
        char = char.lower()
        if char in occurrence_dict:
            occurrence_dict[char] += 1
        else:
            occurrence_dict[char] = 1

    return occurrence_dict


def sort_occurence_dict(my_dict):
    sorted_list = []

    for key, value in my_dict.items():
        sorted_list.append({"char": key, "num": value})
        
    sorted_list.sort(reverse=True, key=sort_on_num)
    return sorted_list

def sort_on_num(items):
    return items['num']

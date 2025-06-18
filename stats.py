
def get_num_words(file_contents):
    words = file_contents
    book_text = words.split()
    num_words = len(book_text)
    return num_words

def text_to_num(file_contents):
    num_char = {}
    for i in file_contents:
        lower_char = i.lower()
        if (lower_char in num_char):
            num_char[lower_char] = num_char[lower_char] + 1
        else:
            num_char[lower_char] = int(1)
    return num_char

def sort_on(dict):
    return dict["num"]

def count_char(num_char):
    report = []
    for i in num_char:
        num = num_char[i]
        char_dict = {"char": i, "num": num}
        report.append(char_dict)
    report.sort(reverse=True, key=sort_on)
    return report
        

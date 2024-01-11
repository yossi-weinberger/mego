# def letter_count(text):
#     letters = 0
#
#     file = open(text, 'r')
#     text = file.read()
#
#     for letter in text:
#         if letter.isalpha():
#             letters += 1
#     print(f"sum of letters: {letters}")
#
#     words_list = text.split()
#     print(f"sum of words: {len(words_list)}")
#
#     words_set = set(words_list)
#     print(f"sum of uniq words: {len(words_set)}")
#
#     words_dict = {}
#     for word in words_list:
#         words_dict.setdefault(word, 0)
#         words_dict[word] += 1
#     print(words_dict)
#
#     file.close()
#
#
# letter_count("lorem_ipsum.txt")
#
#

grade = 55

match grade:
    case 0:
        print("you failed")
    case 100:
        print("you you are the best")
    case _:
        print("something")

import pprint
import string

my_str = """It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
    However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.
    My dear Mr. Bennet,” said his lady to him one day, “have you heard that Netherfield Park is let at last?”
    Mr. Bennet replied that he had not.
    But it is,” returned she; “for Mrs. Long has just been here, and she told me all about it.”
    Mr. Bennet made no answer.
    Do you not want to know who has taken it?” cried his wife impatiently.
    You want to tell me, and I have no objection to hearing it.
    This was invitation enough.
    Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England.
    That he came down on Monday in a chaise and four to see the place, and was so much delighted with it that he agreed with Mr. Morris immediately.
    That he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week.
    What is his name?”
    Bingley.”
    Is he married or single?”
    Oh! single, my dear, to be sure!
    A single man of large fortune; four or five thousand a year.
    What a fine thing for our girls!
    How so? how can it affect them?”
    My dear Mr. Bennet,” replied his wife, “how can you be so tiresome!
    You must know that I am thinking of his marrying one of them.”
    Is that his design in settling here?”
    Design! nonsense, how can you talk so!
    But it is very likely that he may fall in love with one of them, and therefore you must visit him as soon as he comes.
    I see no occasion for that.
    You and the girls may go, or you may send them by themselves, which perhaps will be still better, for as you are as handsome as any of them, Mr. Bingley might like you the best of the party."""
"""
Muhammed EREN
"""

punctuation = string.punctuation  # you must import string module(library)
words = my_str.split()  # return a list separeted by default space

print(f""" Toplam kelime sayısı = {len(words)}""")

"""
mydic = {
key1: value1,
key2: value2,
key2: value3
}

mydic = {
key1: value1,
key2: value3
}
mydict[key1]

mydict[key1001]
"""
my_dictionary = {}

for x in words:
    my_clean_word = x.strip(punctuation)
    my_punctuation = x.replace(my_clean_word, "")

    if my_clean_word:  # x is not '':
        if my_clean_word in my_dictionary:  #
            my_dictionary[my_clean_word] += 1  # Bu kısmı yaparken chatgptden yardım aldım
        else:  # Değerleri 1 artırabilmek için
            my_dictionary[my_clean_word] = 1  #

    if my_punctuation:  # my_punctuation is not '':
        if my_punctuation in my_dictionary:  #
            my_dictionary[my_punctuation] += 1  # Bu kısmı yaparken chatgptden yardım aldım
        else:  # Değerleri 1 artırabilmek için
            my_dictionary[my_punctuation] = 1  #

pprint.pprint(my_dictionary)







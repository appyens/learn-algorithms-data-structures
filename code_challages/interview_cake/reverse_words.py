"""
You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake
Vault. The message has been mostly deciphered, but all the words are backward! Your colleagues have handed off the last step to you.

Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place. ↴

Why a list of characters instead of a string?

The goal of this question is to practice manipulating strings in place. Since we're modifying the message,
we need a mutable ↴ type like a list, instead of Python 3.6's immutable strings.

For example:

  message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))

Python 3.6
When writing your function, assume the message contains only letters and spaces, and all words are separated by one space.
"""

message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']


def reverse_words(word_list):
    result = ''
    current_word = ''
    for ch in word_list:
        if ch != ' ':
            current_word += ch
        else:
            result += ' ' + current_word

    print(result)


reverse_words(message)
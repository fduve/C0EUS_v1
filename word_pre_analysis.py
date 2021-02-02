import miscellaneous_features as mf
import os
import sys
import time
import string
import numpy as np
'''
Doc
'''

def concatenate_list_data(characters_list):
    result= ''
    for element in characters_list:
        result += str(element)
    return result

def read_file():
    file_name = input('File name w/extension, which is in this folder:\n')
    with open("./{}".format(file_name), 'r+') as init_file:
        file_content = init_file.read()
    time.sleep(1)
    #print(type(file_content))
    return(file_content)

def split_file_content(file_content):
    '''
    

    Parameters
    ----------
    file_content : string
        Full text, after is read by the function read_file().

    Returns
    -------
    splitted_file_content : list
        All the full text-to-string file  lines separated.

    '''

    splitted_file_content = file_content.splitlines()
    #print(type(splitted_file_content))
    return(splitted_file_content)

def singularizing_words(listed_lines):
    '''
    

    Parameters
    ----------
    listed_lines : list
        Contains one line per list block unit. Those are all the lines of the
        text file.

    Returns
    -------
    complete_word_list : list
        Contains all the words of the full text, but they are still not singularized.
        They can still be repeated between them.

    '''
    listed_lines = listed_lines
    complete_word_list = []

    for i in range(0, len(listed_lines)):
        current_line = listed_lines[i]
        current_line = current_line.split(" ")
        current_line_list_length = len(current_line)
        for j in range(0, current_line_list_length):
            complete_word_list.append(current_line[j])

    list_len = len(complete_word_list)

    print('There has been found {} words'.format(list_len))            
    return (complete_word_list)

def words_list_cleansing(words_list):
    '''
    

    Parameters
    ----------
    words_list : list
        Contains all the words on the corpus, repeated, not singularized.

    Returns
    -------
    words_list : list
        Same list that enters but except the useless punctuation and
        symbols.

    '''
    words_list = words_list 
    special_character_list = list(string.punctuation)
    for tmpi in range(0,10):
        to_add = str(tmpi)
        special_character_list.append(to_add)
    #print(len(words_list))

    for i in range(0, len(words_list)):
        current_word = words_list[i]
        current_word = current_word.lower()

        current_char_list = list(current_word)

        
        for j in range(0, len(current_char_list)):
            current_char = current_char_list[j]
            #print('working with: {}'.format(current_char))
            
            #print(current_char_list)
            for k in range(0, len(special_character_list)):
                banned_symbol = special_character_list[k]
                if (banned_symbol == current_char):
                    #print('found: {} in word: {}'.format(banned_symbol, current_word))
                    current_char = ''
            current_char_list[j] = current_char
            #print(current_char_list)
        words_list[i] = concatenate_list_data(current_char_list)
    #print(words_list) 
    print('There has been {} words cleansed of symbols and useless characters'.format(len(words_list)))
    return (words_list)

def remove_spaces_from_list(word_list):
    count = 0
    index = 0
    for word in word_list:
        if ((word == '' ) or (word == ' ')):
            word_list.pop(index)
            count = count+1
        index = index+1
    print('There has been founded {} blank spaces'.format(count))
    print('New total count is {} words'.format(len(word_list)))
    return(word_list)

def get_vocab(word_list):
    '''
    

    Parameters
    ----------
    word_list : list
        Contains all the words on the corpus, repeated, not singularized.

    Returns
    -------
    d_vocab : dict
        Contains a dict of unique elements (words) which appeared in the 
        corpus. This function also removes the spaces.

    '''
    vocab = set(word_list)
    vocab.remove('')
    ##vocab.remove(' ')
    
    idx = 0
    d_vocab = {}
    for word in vocab:
        d_value = word
        d_key = idx
        d_vocab[d_key] = d_value
        idx += 1   
    
    print('Vocabulary size: {}'.format(len(d_vocab)))
    return d_vocab


def clean_lines(listed_lines):
    '''
    

    Parameters
    ----------
    listed_lines : list
        The list that contains all the lines of the corpus.

    Returns
    -------
    clean_lines : list
        The same list that enters, except it now excludes useless
        punctuation and symbols.

    '''
    special_character_list = list(string.punctuation)
    for tmpi in range(0,10):
        to_add = str(tmpi)
        special_character_list.append(to_add)
        
    clean_lines = []
    
    for i in range(0, len(listed_lines)):
        current_line = listed_lines[i]
        #print(current_line)

        for banned_symbol in special_character_list:
            current_line = current_line.replace(banned_symbol, '')
            #print(current_line)
        clean_lines.append(current_line)
    
    return clean_lines


def words_frequency(vocab_set, cleansed_phrases):
    '''
    

    Parameters
    ----------
    vocab_set : set
        Contains the words of the corpus, singularized, which now are going to be counted.
    cleansed_phrases : list
        Contains the clean corpus.

    Returns
    -------
    None.

    '''
    
    vocab_set_len = len(vocab_set)
    cleansed_phrases_len = len(cleansed_phrases)
    
    print('2D array dimensions: ({},{})'.format(cleansed_phrases_len, vocab_set_len))
    freq_matrix = np.zeros((cleansed_phrases_len, vocab_set_len), dtype = int)
    
    #print(freq_matrix)
    print(type(freq_matrix))
    print(freq_matrix[1][4])
    
    return freq_matrix

#Part 1: Clean the data. Get words and phrases.
plain_text = read_file()
corpus = split_file_content(plain_text)
repeated_words = singularizing_words(corpus)
repeated_words = words_list_cleansing(repeated_words)
#five = remove_spaces_from_list(four)
vocab_set = get_vocab(repeated_words)
cleansed_phrases = clean_lines(corpus) 

#Part 2: Get frequencies.

words_frequency(vocab_set, cleansed_phrases)



'''
def main(): 
    return 0

if __name__ == '__main__':
    main()
'''




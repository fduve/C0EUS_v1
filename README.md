# words_preprocessing01
No specialized libraries used to get a text file, split it and get the words. For the next code's improvements, it is on mind that it will take the word's frequencies and perform some preliminar processing to get some first insights about the corpus to work.

version 0.01: After uploading the first version, noticed that forgot to delete the line for importing a custom library, so, in order for it to work,
just delete the custom import line.

version 0.02: Implements the use of pandas and numpy to get an array with frequencies, and optionally, the name of the word which is getting the frequency of.


The scripts works by selecting a text file, both in the same folder. If the text file fulfill the following requierement: (1) All lines are
separated from each other by a ('\n') or a jump line, then it is ready to work.
The script is going to ask you for a file's name, write it. Then it is going to work and pre-process the text inside.



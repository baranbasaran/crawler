import os
import re
import string
import sys

# import the Porter stemmer module
from porterStemmer import PorterStemmer


def preProcessing(file, outputFolder, stopwordFile):
    # initialize an empty list to store the processed words
    output = []
    # create a Porter stemmer object
    p = PorterStemmer()
    # open the stopword file and read its contents
    f = open(stopwordFile, "r")
    stopwordFile = f.read()
    # split the stopwords by newline characters
    stopwords = stopwordFile.split("\n")
    # close the file
    f.close()
    # open the input file and read its contents
    f = open(file, "r")
    inputs = f.read()
    # TOKENIZATION
    # lowercase the input text
    inputs = inputs.lower()
    # split the input text by newline or space characters
    inputs = re.split(r'[\n ]', inputs)
    # close the file
    f.close()
    # iterate through the list of input words
    for word in inputs:
        # PUNCTIATION
        # remove punctuation from the word
        word = word.translate(str.maketrans('', '', string.punctuation))
        # STEMMING
        # stem the word using the Porter stemmer
        word = p.stem(word, 0, len(word) - 1)
        # STOPWORD REMOVING
        # if the word is not a stopword, append it to the list of processed words
        if word not in stopwords:
            if len(word) > 0:
                output.append(word)
    # open the output file in write mode and write the processed words to it, separated by newlines
    with (open(outputFolder, "w", encoding="utf8") as w):
        w.write("\n".join(output))


if __name__ == "__main__":
    # get the input, output, and stopword directories from command line arguments
    infolder, outfolder, stopwordfile = sys.argv[1], sys.argv[2], sys.argv[3]
    # add a trailing slash to the input directory if it doesn't already have one
    infolder = infolder if infolder.endswith("/") else infolder + "/"
    # add a trailing slash to the output directory if it doesn't already have one
    outfolder = outfolder if outfolder.endswith("/") else outfolder + "/"
    # if the output directory doesn't exist, create it
    if not (os.path.exists(outfolder)):
        os.mkdir(outfolder)
    # if the input directory doesn't exist, print an error message
    if not (os.path.exists(infolder)):
        print("Input directory not exist")
    # if the input directory does exist, process all the files in it
    else:
        for file in os.listdir(infolder):
            print(infolder+file)
            preProcessing(infolder+file, outfolder+file, stopwordfile)

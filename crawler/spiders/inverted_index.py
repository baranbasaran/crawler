import os
import sys


def main():
    # get the input directory and output file path from command line arguments
    infolder, outfile = sys.argv[1], sys.argv[2]
    # initialize an empty dictionary to store the inverted index
    inverted_index = {}
    # iterate through all the files in the input directory
    for file in os.listdir(infolder):
        # get the full path of the file
        file_path = os.path.join(infolder, file)
        # if the file is a text file
        if file.endswith('.txt'):
            # open the file in read mode
            with open(file_path, 'r', encoding='utf8') as f:
                # iterate through the lines in the file
                for line in f:
                    # lowercase the line, remove newlines, and remove periods
                    line = line.lower().replace('\n', '').replace('.', '')
                    # split the line into words
                    words = line.split(' ')
                    # iterate through the words
                    for word in words:
                        # skip empty words
                        if word == '':
                            continue
                        # if the word is not in the inverted index, add it
                        if word not in inverted_index:
                            inverted_index[word] = {}
                        # if the file is in the inverted index for the word, increment the count
                        if file in inverted_index[word]:
                            inverted_index[word][file] += 1
                        # if the file is not in the inverted index for the word, add it with a count of 1
                        else:
                            inverted_index[word][file] = 1

    # open the output file in write mode
    with open(outfile + '.txt', 'w') as f:
        # iterate through the inverted index
        for word, values in inverted_index.items():
            # write the word to the file
            f.write(word + '\t')
            # sort the values (i.e., the file counts) in descending order
            sorted_values = sorted(
                values.items(), key=lambda x: x[1], reverse=True)
            # iterate through the sorted values
            for file, count in dict(sorted_values).items():
                # write the file name and count to the file, separated by brackets
                f.write(file.replace('.txt', '') +
                        '[' + str(count) + ']' + '\t')
            # write a newline character after each word
            f.write('\n')


# if the script is being run from the command line, call the main function
if __name__ == '__main__':
    main()

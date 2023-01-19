import math
import sys


def get_len_of_doc(document):
    filepath = "preprocess/" + document + ".txt"
    with open(filepath, "r") as f:
        lines = f.read()
        return len(lines.split())


def calculate_tf(count, document):
    """Calculate the term frequency (TF) for a word in a document."""
    return count / get_len_of_doc(document)


def calculate_idf(num_documents_with_word, number_of_documents):
    """Calculate the inverse document frequency (IDF) for a word."""
    return math.log(number_of_documents / num_documents_with_word)


def calculate_tfidf(tf, idf):
    """Calculate the TF-IDF score for a word in a document."""
    return round(tf * idf, 3)


def tf_idf(infile, outfile):
    # Read in the input file
    with open(infile) as indexing:
        lines = indexing.readlines()

        # Initialize variables
        N = 20  # total number of documents
        tfidf_values = {}

        for line in lines:
            parsingline = line.split("\t")
            word = parsingline[0]
            frequencies = parsingline[1:len(parsingline)-1]

            # Calculate the TF-IDF scores for the word in each document
            tfidf_values[word] = {}
            num_documents_with_word = len(frequencies)
            for frequency in frequencies:
                if not frequency == "":
                    # D20[1]
                    document, count = frequency.split("[")
                    # 1]
                    count = int(count[:-1])
                    tf = calculate_tf(count, document)
                    idf = calculate_idf(num_documents_with_word, N)
                    tfidf = calculate_tfidf(tf, idf)
                    tfidf_values[word][document] = tfidf

    # Write the output file
    with open(outfile + '.txt', 'w') as write_file:
        # Write the header row with the document names
        write_file.write("Docs \t")
        # columns
        write_file.write("\t".join(["D" + str(i+1) for i in range(N)]))
        write_file.write("\n")

        for word, values in tfidf_values.items():
            write_file.write(word + "\t")
            for i in range(N):
                document = "D" + str(i+1)
                if document in values:
                    # Write the value if it exists
                    write_file.write(str(values[document]) + "\t")
                else:
                    # Write 0 if the value does not exist
                    write_file.write("0.0\t")
            write_file.write("\n")


if __name__ == "__main__":
    file, outfile = sys.argv[1], sys.argv[2]
    tf_idf(file, outfile)

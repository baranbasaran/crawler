import os
import sys
from math import sqrt
from porterStemmer import PorterStemmer


def main():
    # Parse command line arguments
    input_folder = sys.argv[1]
    query = sys.argv[2]
    stopwords_file = sys.argv[3]

    # Read stopwords from file
    with open(stopwords_file, 'r') as f:
        stopwords = set(f.read().split())

    # Initialize stemmer
    stemmer = PorterStemmer()

    documents = {}
    word_and_frequency = {}

    # Read and preprocess documents in input folder
    def preprocess_document(document):
        # Read and lowercase document
        document = document.lower()
        # Remove stopwords
        # removing any words that are in the stopwords list, and then joining the remaining words back into a single string.
        document = ' '.join(
            [word for word in document.split() if word not in stopwords])
        # Stem words
        document = ' '.join([stemmer.stem(word, 0, len(word)-1)
                            for word in document.split()])
        return document

    def count_word_frequencies(word_and_frequency, document, filename):
        # Count frequency of words in document
        for word in document.split():
            if word not in word_and_frequency:
                word_and_frequency[word] = {filename: 1}
            elif filename not in word_and_frequency[word]:
                word_and_frequency[word][filename] = 1
            else:
                word_and_frequency[word][filename] += 1
        return word_and_frequency
    print(word_and_frequency)
    for filename in os.listdir(input_folder):
        with open(os.path.join(input_folder, filename), 'r') as f:
            # Read and preprocess document
            document = f.read()
            document = preprocess_document(document)
            documents[filename] = document
            # Count word frequencies
            word_and_frequency = count_word_frequencies(
                word_and_frequency, document, filename)

    # Preprocess query
    query = query.lower()
    query = ' '.join([word for word in query.split() if word not in stopwords])
    query = ' '.join([stemmer.stem(word, 0, len(word)-1)
                     for word in query.split()])

    # Create query vector
    query_vector = {word: 1 for word in query.split()}

    # Create document vectors
    document_vectors = {}

    def create_document_vector(document_vector, word_and_frequency, filename):
        """Create a document vector for a document by setting the value for each word to the word's frequency in the document."""
        for word, count in word_and_frequency.items():
            if filename in count:
                document_vector[word] = count[filename]
            else:
                document_vector[word] = 0
        return document_vector

    for filename, document in documents.items():
        document_vector = create_document_vector(
            {}, word_and_frequency, filename)
        document_vectors[filename] = document_vector

    # Compute cosine similarity scores
    scores = {}

# This function calculates the Euclidean length of a vector

# This function calculates the cosine similarity between two vectors
    def dot_product(query_vector, document_vector):
        dot_product = 0
        for word in query_vector:
            if word in document_vector:
                dot_product += query_vector[word] * document_vector[word]
        return dot_product

    def euclidean_length(vector):
        norm = 0
        for count in vector.values():
            norm += count ** 2
        return sqrt(norm)

    def compute_cosine_similarity(query_vector, document_vector):

        query_norm = euclidean_length(query_vector)
        document_norm = euclidean_length(document_vector)
        if query_norm * document_norm > 0:
            return dot_product(query_vector, document_vector) / (query_norm * document_norm)
        return 0
    for filename, document_vector in document_vectors.items():
        scores[filename] = compute_cosine_similarity(
            query_vector, document_vector)

    # Print top 20 scored documents
    for i in range(20):
        max_filename = max(scores, key=scores.get)
        print(f'{max_filename}: {scores[max_filename]}')
        del scores[max_filename]


if __name__ == "__main__":
    main()

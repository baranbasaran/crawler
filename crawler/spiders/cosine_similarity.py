import math
import sys

# This function takes a filename, and two document IDs (doc1 and doc2) as input, and returns
# the tf-idf values for the two documents


def extract_tfidf_values(filename, doc1, doc2):
    # Open the file in read mode
    with open(filename, 'r') as f:
        # Skip the first line (header)
        f.readline()
        # Read all the lines in the file
        lines = f.readlines()

        # Initialize empty lists to store the extracted values
        doc1_tfidf_values = []
        doc2_tfidf_values = []

        # Iterate over the lines in the file
        for line in lines:
            # Split the line by tab character and extract the word and values
            word, values = line.split("\t")[0], line.split("\t")[1:]

            # Iterate over the values
            for i, value in enumerate(values):
                # Split the value by ":" and extract the tf-idf value
                # Check if the value corresponds to doc1 or doc2 and append it to the appropriate list
                if doc1 == f"D{i + 1}":
                    doc1_tfidf_values.append(float(value))
                if doc2 == f"D{i + 1}":
                    doc2_tfidf_values.append(float(value))

        # Return the extracted values
        return doc1_tfidf_values, doc2_tfidf_values

# This function calculates the dot product of two vectors


def dot_product(vec1, vec2):
    # Initialize the dot product to 0.0
    dot_product = 0.0
    # Iterate over the elements of the vectors and calculate the dot product
    for i in range(len(vec1)):
        dot_product += vec1[i] * vec2[i]
    # Return the dot product
    return dot_product

# This function calculates the Euclidean length of a vector


def euclidean_length(vec):
    # Calculate the Euclidean length using the formula sqrt(sum(x^2))
    return math.sqrt(sum([x ** 2 for x in vec]))

# This function calculates the cosine similarity between two vectors


def cosine_similarity(vec1, vec2):
    # Calculate the dot product of the vectors
    dot = dot_product(vec1, vec2)
    # Calculate the Euclidean length of both vectors
    euclidean_length_vec1 = euclidean_length(vec1)
    euclidean_length_vec2 = euclidean_length(vec2)
    # Calculate the cosine similarity using the formula dot / (euclidean_length_vec1 * euclidean_length_vec2)
    try:
        return float(dot) / (euclidean_length_vec1 * euclidean_length_vec2)
    except ZeroDivisionError:
        return 0


if __name__ == "__main__":
    # Get the filename, doc1, and doc2 from the command line arguments
    filename, doc1, doc2 = sys.argv[1], sys.argv[2], sys.argv[3]

    # Extract the tf-idf values for doc1 and doc2
    doc1_tfidf_values, doc2_tfidf_values = extract_tfidf_values(
        filename, doc1, doc2)

    # Calculate the cosine similarity between the two vectors
    similarity = cosine_similarity(doc1_tfidf_values, doc2_tfidf_values)

    # Print the similarity
    print(similarity)

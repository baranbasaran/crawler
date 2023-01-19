Scripts
    This project includes the following scripts:

        scrapping.py: Scrapes data from a webpage
        preprocessing.py: Preprocesses the data from the scraping step
        inverted_index.py: Creates an inverted index from the preprocessed data
        TF-IDF.py: Calculates the TF-IDF values for the inverted index
        cosine_similarity.py: Calculates the cosine similarity between two documents
        IR.py: Implements a simple information retrieval system

System requirements
    Python 3
    Scrappy library (install using pip install scrappy)

Language and version
    All scripts are written in Python 3.

List of files
    In addition to the scripts, this project includes the following files:
        stopwords.txt: A list of stopwords to be used in the preprocessing step

Instructions to run
    To run the scripts in this project, follow these steps:

        Ensure that you have Python 3 and the Scrappy library installed on your machine.

            Open a terminal window and navigate to the directory where the scripts are located.

                Run the scripts in the following order:

                    python scrapping.py "doc"
                    python preprocessing.py "doc" "preprocess" "stopwords.txt"
                    python inverted_index.py "preprocess" "indexing"
                    python TF-IDF.py indexing.txt tfIdf
                    python cosine_similarity.py tfIdf.txt D3 D5
                    python IR.py doc "Griffith College Dublin IRWS course menu" "stopwords.txt"

                Each script performs a specific task in the overall process, and the output of each script is used as input for the next script. For example, the output of the scrapping.py script is used as input for the preprocessing.py script.

Input and output
    Input
        The input to each script varies, but generally includes file paths and data.

        scrapping.py: Takes a file path as input, indicating where the scraped data should be saved.
        preprocessing.py: Takes a file path for the input data and a file path for the output data, as well as a file path for a list of stopwords.
        inverted_index.py: Takes a file path for the input data and a file path for the output data.
        TF-IDF.py: Takes a file path for the input data and a file path for the output data.
        cosine_similarity.py: Takes a file path for the input data, and two document identifiers for the documents to compare.
        IR.py: Takes a file path for the input data, a query string, a file path for a list of stopwords.
    Output
        The output of each script is either a file or a calculation.

        scrapping.py: Outputs the scraped data to a file.
        preprocessing.py: Outputs the preprocessed data to a file.
        inverted_index.py: Outputs the inverted index to a file.
        TF_IDF.py: Outputs the calculated tf-idf values to a file.
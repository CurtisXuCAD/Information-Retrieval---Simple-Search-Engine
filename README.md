# Information-Retrieval---Simple-Search-Engine
This is a UCI CS 122A Information Retrieval Class Assignment

20 test quries:

                1.  cristina lopes
                2.  machine learning
                3.  ACM
                4.  master of software engineering 
                5.  informatics
                6.  neural network
                7.  Computer Science
                8.  department
                9.  research opportunity
                10. student id
                11. computer science and engineering
                12. computer game science
                13  Donald Bren School
                14. data science
                15. University of California
                16. human computer interaction
                17. irvine
                18. Software Evaluation
                19. University of California, San Diego
                20. career fair
                
                
tf: term frequency
The number of times a word appears in a document divded by the total number of words in the document.


idf: inverse document frequency
The log of the number of documents divided by the number of documents that contain the word w. Inverse data frequency determines the weight of rare words across all documents in the corpus.


Search interface
The response to search queries should be ≤ 300ms. Ideally it would be . 100ms,
but you won’t be penalized if it’s higher (as long as it’s kept ≤ 300ms).


Ranking: 
First, we precompute the tf and idf scores for every term, and we build the N length vector for each document, using the tf * idf of each term as the entries.
Then, we compute the query, and get a result set of matching documents (using previously described techniques).
After this, we compute the vector for the query, which is also of length N and uses the tf * idf as each of its entries.
Then, we calculate the similarity between the query and each document in the result set (using cosine similarity), and get a score for each document.
We sort the documents by this score, and return them, in order.

runtime performance:

execution time of code in milliseconds in Python



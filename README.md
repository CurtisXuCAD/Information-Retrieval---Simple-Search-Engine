# Information-Retrieval
This is a UCI CS 122A Information Retrieval Class Assignment


Assignment 3: Search engine


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
                
                
--Indexer.py--


    get_file_path:
          
       take a path-like string foldername as parameter and return all files' paths in that folder and its subfolders.   
          
    extract_content:
    
        extract the useful contents from the json files . 
        This function will return a list which are the url that the json file contains and important word list and regular word list. 
        We use beautiful soap findall function to get important words by catching their tags and get the html content. 
    
    process_index:
         
         call the extract_content function to get the contents that we need. 
         The function contains 3 global variables, which include a words_index dictionary that stores the words with their related docID 
         and frequency, a docUrls dicionary that include all the file paths, a words_set is the set that store all words information. 
         The keys of words_index are word, and the value is another dictionary that the keys are file paths, and values are frequency.

    store_index:
    
        words_index folder store all the index dict to files: files named by the first 2 char of the word 
        words_summary.json file has all words count and the all words that we stored from content.

--Search.py--


    get_file_path:
    
          take a query word as parameter and return its index file path in the file.
            
    extract_content:
          
          
    search_query:

              
    intersect:
          
          
    get_top_5_answer:
            
            
tf: term frequency
The number of times a word appears in a document divded by the total number of words in the document.


idf: inverse document frequency
The log of the number of documents divided by the number of documents that contain the word w. Inverse data frequency determines the weight of rare words across all documents in the corpus.


Search interface
The response to search queries should be ≤ 300ms. Ideally it would be . 100ms,
but you won’t be penalized if it’s higher (as long as it’s kept ≤ 300ms).


Ranking: 
First, we compute the tf and idf scores for every term, and tf * idf of each term.


Then, we compute the query, and get a result.


After this, we compute the vector for the query.


Then, we calculate the similarity between the query and each document in the result set (using cosine similarity), and get a score for each document.


We sort the documents by this score.



runtime performance:

execution time of code in milliseconds in Python



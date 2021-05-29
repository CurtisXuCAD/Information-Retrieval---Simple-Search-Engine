# Information-Retrieval
This is a UCI CS 122A Information Retrieval Class Assignment


Assignment 3: Search engine


20 test queries:

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
                21. aux
                
                
--Indexer.py--


    get_file_path:
          
       take a path-like string foldername as parameter and return all files' paths in that folder and its subfolders.   
          
    extract_content:
    
        extract the useful contents from the json files . 
        This function will return a list which are the url that the json file contains and important word list and regular word list. 
        We use beautiful soap findall function to get important words by catching their tags and get the html content. 
    
    process_index:
         
         call the extract_content function to get the contents that we need. 
         The function contains 3 global variables, which include a words_index dictionary that stores the words with their related 
         docID and frequency, a docUrls dicionary that include all the file paths, a words_set is the set that store all words information. 
         The keys of words_index are word, and the value is another dictionary that the keys are file paths, and values are frequency.

    store_index:
    
        words_index folder store all the index dict to files: files named by the first 2 char of the word 
        words_summary.json file has all words count and the all words that we stored from content.

--Search.py--


    get_file_path:
    
          take a query word as parameter and return its index file path in the file.
            
    extract_content:
          
          take a query word and json_file path as parameter and return the matrix of query word index.
          
    search_query:
          
          take a query as parameter and tokenize the query with stopwords and krovetz stemmer and return list of store word's index dictionary.
              
    intersect:
          
          merge the query(AND only) and get common to both of the initial lists and return them into answer dictionary.
          
    get_top_5_answer:
            
            print the top 5 URLs for each of the queries. 
            
            
tf: term frequency
The number of times a word appears in a document divded by the total number of words in the document.


idf: inverse document frequency
The log of the number of documents divided by the number of documents that contain the word w. Inverse data frequency determines the weight of rare words across all documents in the corpus.


Search interface
The response to search queries should be ≤ 300ms. Ideally it would be . 100ms,
but you won’t be penalized if it’s higher (as long as it’s kept ≤ 300ms).

---------conclusion--------


The most chanllenge part of this proejct is how to efficiently access larger collection of web pages and store and extract information. We came up with the idea. At first, we try to get the tfidf score for each term and make a words index folder based on the score. The folder contains list of folders with initial letter of the word. The folder of initial character has list of json files with their first two characters of the word and each file has related word index dictionary who starts with those two characters. Also, we have better idea for some of the query (ex: cristina lopes, career fair etc..) that test search engine ranking system. we try to increase important words frequency to have better score on the ranking system. Base on this storing strategy, we didn’t meet too many problems while ranking and searching, and the speed is acceptable. 

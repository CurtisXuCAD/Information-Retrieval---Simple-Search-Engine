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
                10. aux
                11. computer science and engineering
                12. computer game science
                13  Donald Bren School
                14. data science
                15. University of California
                16. human computer interaction
                17. irvine
                18. Software Evaluation
                19. University of California, San Diego
                20. a

For Query 10 -- **aux**, we choose **aux** since Windows operating system prohibits us to create **aux.json**. **aux.json** is reserved filename in windows. To avoid doing that, we choose the first two initial characters to make an index file. Also, we create an index file with the word itself for words have more than five characters.(ex: student --> student.json)

For Query 1,2,3,6, we at first doing poorly on ranking the result, so we justify the value of an important word (title, subtile, bold, ...) to make the result more acceptable. We try to increase important words frequency to have better score on the ranking system.

For Query 4,7,11,12,13,14,15,16,19, the efficient for these queries are poor and unstable at first since there are too many document having these words. We tested the time taken by each function one by one to find out which function takes the longest time. By doing so, we found that the efficient is poor since the index file is quite large and it is time consuming to load the file to python dict. Thus, we modify the indexer to make it create an index file with the word itself for words have more than five characters. This helps us make the query time reduce to less than 100ms for these queries.

For Query 20, we first end up having to answer since we removed all the stop words in query. Thus we and the tf-idf score since we know that the idf score can handle stop words (common words).

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

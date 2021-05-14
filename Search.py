import glob
import json
import time
import krovetz
from nltk.corpus import stopwords
from collections import defaultdict

ks = krovetz.PyKrovetzStemmer()
stop_words = set(stopwords.words('english'))

#   C:/Users/Owner/OneDrive/Desktop/CS121/Assignment3 M1/words_index\c
def get_file_path(query_word):
    """
    get_file_path() take a query word and its index file path
    """
    index_files_path = "D:\\OneDrive\\ICS\\CS 121\\CS121 Assignment\\Assignment3 M1\\words_index"
    query_index_path = ""
    if len(query_word) > 1:
        query_index_path = index_files_path + "\\" + query_word[0] + "\\" + query_word[:2] + ".json"
    else:
        query_index_path = index_files_path + "\\" + query_word[0] + query_word[0] + ".json"
    return query_index_path

def extract_content(json_file, query_word):
    query_index_dict = dict()
    with open(json_file,'r',encoding='utf-8') as file:        #  open json file   ex: cr file
        data = json.load(file)
        query_index_dict = data[query_word] #get the index matrix
    return query_index_dict                # return the matrix

#   1 cristina lopes, 2 machine learning, 3 ACM, 4 master of software engineering
def search_query(query):
    #   words = ['cristina', 'lopes'] etc..
    words = []
    query_indexes= [] # list to store word's index dict
    query = query.split()
    # tokenize the query
    for word in query:
        # if word not in stop_words: # remove stop words
            words.append(ks.stem(word))
    
    for w in words:
        query_index_path = get_file_path(w)
        
        try:
            #append query word's index dict
            query_indexes.append(extract_content(query_index_path, w))
                       
        except:
            #if file not found exception or can find word in matrix, it mean there is no indexed about this word
            print(f"Can't find anything about \"{w}\" !")
            query_indexes.append({})
    
    return query_indexes

# merge query
def intersect(query_indexes):
    answer = defaultdict(int)
    
    #
    intersections = query_indexes[0].keys()
    for i in query_indexes:
        intersections = intersections & i.keys()
    
    #calculate the total frequency
    for i in intersections:
        for qi in query_indexes:
            answer[i] += qi[i]
        
    return answer

# what makes top 5 URLs?

def get_top_5_answer(answer):
    sorted_answer = sorted(answer.keys(), key=lambda x: answer[x], reverse=True)
    i = 0
    while True:
        if i >= 5 or i >= len(sorted_answer):
            break
        print(sorted_answer[i])
        i += 1


# what does screenshot of your search interface in text?

if __name__ == '__main__':
    # file_paths = get_file_path("C:/Users/Owner/OneDrive/Desktop/CS121/Assignment3 M1/words_index")
    while True:
        query = input("\nPlease type in the key word: (Press ENTER directly to EXIT)\n")
        start = time.clock()
        if query == "":
            print("END")
            break
        print()
        answer = intersect(search_query(query))
        if len(answer) != 0:
            end = time.clock()
            print(f"Found {len(answer)} results ({format(end-start,'.3f')})seconds")
            print(f"Top {len(answer) if len(answer) < 5 else 5} results:")
            get_top_5_answer(answer)
        else:
            print(f"There are no results about \"{query}\" !")
        
        # end = time.clock()
        # print(end-start,"s")
    
    

import glob
import json
import time
import math
import krovetz
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.tokenize import word_tokenize

ks = krovetz.PyKrovetzStemmer()
stop_words = set(stopwords.words('english'))

#   C:/Users/Owner/OneDrive/Desktop/CS121/Assignment3 M1/words_index\c
def get_file_path(query_word):
    """
    get_file_path() take a query word and its index file path
    """
    # index_files_path = "D:\\OneDrive\\ICS\\CS 121\\CS121 Assignment\\Assignment3 M1\\words_index"
    index_files_path = "words_index"
    query_index_path = ""
    if len(query_word) > 1 and len(query_word) < 5:
        query_index_path = index_files_path + "\\" + query_word[0] + "\\" + query_word[:2] + ".json"
    else:
        query_index_path = index_files_path + "\\" + query_word[0] + "\\" + query_word + ".json"
    return query_index_path

def extract_content(json_file, query_word):
    query_index_dict = dict()
    with open(json_file,'r',encoding='utf-8') as file:        #  open json file   ex: cr file
        data = json.load(file)
        query_index_dict = data[query_word] #get the index matrix
    return query_index_dict                # return the matrix

#   1 cristina lopes, 2 machine learning, 3 ACM, 4 master of software engineering
def search_query(query):
    # start1 = time.clock()
    #   words = ['cristina', 'lopes'] etc..
    words = []
    query_indexes= [] # list to store word's index dict
    query = word_tokenize(query)
    # tokenize the query
    for word in query:
        # if word not in stop_words and len(query) > 1: # remove stop words
            if word.isalnum(): 
                words.append(ks.stem(word))
    
    for w in words:
        # start = time.clock()
        query_index_path = get_file_path(w)
        # end = time.clock()
        # print("get_file_path:",end-start)
        
        try:
            #append query word's index dict
            # start2 = time.clock()
            query_indexes.append(extract_content(query_index_path, w))
            # end2 = time.clock()
            # print("extract_content:",end2-start2)
                       
        except:
            #if file not found exception or can find word in matrix, it mean there is no indexed about this word
            print(f"Can't find anything about \"{w}\" !")
            # query_indexes.append({})
    # end1 = time.clock()
    # print("search query:",end1-start1)
    return query_indexes

# def query_prod(query):
#     d = {x:query.count(x) for x in query}
#     norm_vector = math.sqrt(sum((1+math.log(d[x]))**2 for x in d))
#     for word in d:
#         wt = 1+math.log(d[word])
#         d[word] = wt/norm_vector
#     return d


# merge query
def intersect(query_indexes):
    answer = defaultdict(int)
    #
    if len(query_indexes) == 0:
        return answer
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
    results = []
    while True:
        if i >= 5 or i >= len(sorted_answer):
            break
        # print(sorted_answer[i])
        with open("words_index\\doc_id_urls.json") as f:
            f.seek(0, 0)
            line = f.readline()
            for j in range(int(sorted_answer[i])):
                line = f.readline()
            line = "{" + line.rstrip(",\n") + "}"
            data = json.loads(line)
            print(data[sorted_answer[i]])
            results.append(data[sorted_answer[i]])
        i += 1
    return results

def run(query):
    results = []
    start = time.clock()
    answer = intersect(search_query(query))
    numOfResults = 0
    text = []
    if len(answer) != 0:
        end = time.clock()
        text.append(f"Found {len(answer)} results ({format(end-start,'.3f')})seconds")
        print(f"Found {len(answer)} results ({format(end-start,'.3f')})seconds")
        numOfResults = len(answer)
        text.append(f"Top {len(answer) if len(answer) < 5 else 5} results:")
        print(f"Top {len(answer) if len(answer) < 5 else 5} results:")
        results += get_top_5_answer(answer)
    else:
        print(f"There are no results about \"{query}\" !")   
        text.append(f"There are no results about \"{query}\" !")
    return text,results,format(end-start,'.3f'),numOfResults


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
    
    

import glob
import json
import time
import os

#   C:/Users/Owner/OneDrive/Desktop/CS121/Assignment3 M1/words_index\c
def get_file_path(folderName):
    """
    get_file_path() take a path-like string (foldername) and return all files' paths in that folder and its subfolders
    """
    file_paths = []  # list to store file paths
    folderName = folderName + "/*"

    for subfolder in glob.iglob(folderName):
        subfolder = subfolder
        #print(subfolder)
        for single_file_path in glob.iglob(subfolder):
            file_paths.append(single_file_path)
    return file_paths

def extract_content(json_file, query_word):
    query_list = []
    with open(json_file) as file:        #  open json file   ex: cr file
        json_data = json.load(file)
        for data in json_data.keys():
            if data == query_word:           #data word == query word
                query_list.append(json_data[query_word])     #save into list
    return set(query_list)                 # set of list urls for query_word

#   1 cristina lopes, 2 machine learning, 3 ACM, 4 master of software engineering
def search_query(query):
    #   words = ['cristina', 'lopes'] etc..
    words = []
    words_urls = []
    query = query.split()
    for word in query:
        words.append(word.lower())
    #   list of file_paths
    file_path = get_file_path("C:/Users/Owner/OneDrive/Desktop/CS121/Assignment3 M1/words_index")
    words_count = 0
    for paths in file_path:     #first path in list
        for word in words:    #first query in list
            if paths[-1] == word[0]:      #check last element path == first chart in query
                words_urls.append(extract_content(paths, word))   #append query word list
    return words_urls

# AND , merge query
def intersect(words_urls):
    answer = []
    if len(words_urls) <= 1:    # if one list in the url list return answer :  ex: acm
        return answer
        # url lists [{'cristina list'}, {'lopes list'}]
        # One-Liner to intersect a list of sets
    answer = words_urls[0].intersection(*words_urls)
    return answer

# what makes top 5 URLs?
# what does screenshot of your search interface in text?

if __name__ == '__main__':
   # file_paths = get_file_path("C:/Users/Owner/OneDrive/Desktop/CS121/Assignment3 M1/words_index")
    query = input("Please type in the key word: ")
    res = []
    words_urls = search_query(query)
    if len(words_urls) != 0:
        answer = intersect(words_urls)
    else:
        print("can't find any thing, please search again! ")

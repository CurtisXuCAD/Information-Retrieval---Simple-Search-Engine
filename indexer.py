import os
import json
import re
import glob
import string
import sys
import traceback
import time
from urllib.parse import urldefrag
# import bleach
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import krovetz

ks = krovetz.PyKrovetzStemmer()

words_set = set()
words_index = dict()
file_count = 0

def get_file_path(folderName):
    """
    get_file_path() take a path-like string (foldername) and return all files' paths in that folder and its subfolders
    """
    
    file_paths = [] # list to store file paths
    folderName = folderName + "\*"
    
    for subfolder in glob.iglob(folderName):
        subfolder = subfolder+"\*"
            # print(subfolder)
        for single_file_path in glob.iglob(subfolder):
            file_paths.append(single_file_path)
            
    return file_paths
    
    
def extract_content(file_path):
    
    global file_count

    important_words = []
    regular_words = []
    #for root, dirs, files in os.walk(dir):
        #for filename in files:
            #doc = os.path.join(root, filename)
    with open(file_path) as file_to_extract:
        json_data = json.load(file_to_extract)
        url = json_data['url']
        content = json_data['content']
        fragment = urldefrag(url)[1]
        
        soup = BeautifulSoup(content)
        
        #get regular text
        content_text = soup.get_text()
        
        if len(content_text) < 50000 and len(fragment) == 0:
        
            file_count += 1
            
            #get important html content (need further process)
            bold = soup.findAll('b')
            strong = soup.findAll('strong')
            h1 = soup.findAll('h1')
            h2 = soup.findAll('h2')
            h3 = soup.findAll('h3')
            title = soup.findAll('title')
            
            important_html_content = bold + strong + h1 + h2 + h3 + title
        
            #store important words
            important_word_tokens = word_tokenize(content_text)  
            for html_words in important_word_tokens:
                if html_words.isalnum():
                    important_words.append(ks.stem(html_words))
                
            #store regular words

            word_tokens = word_tokenize(content_text)      
            for word in word_tokens:
                if word.isalnum():
                    regular_words.append(ks.stem(word))
                # if word not in string.punctuation and word != "'s":
                # if word.isalpha():
                # if word not in string.punctuation and word != "'s":
                #     if word[0] not in string.punctuation:
                #         if len(word) > 1:
                #             if word[1] not in string.punctuation:
                #                 regular_words.append(ks.stem(word))
                #         else:
                #             regular_words.append(ks.stem(word))
    
    return (url, important_words, regular_words)

def process_index(file_path):
    
    # get the file path and build the index dict
    
    print("Processing: " + file_path)
    # make sure we have the correct folder to store the index
    content = extract_content(file_path)
    url = content[0]
    important_words = content[1]
    regular_words = content[2]
    if len(regular_words) != 0:
        for r_word in regular_words:
            
            # dict type: dict{ key:word, value: dict{ key:url, value: frequency}}            
            if r_word in words_index:
                if url in words_index[r_word]:
                    words_index[r_word][url] += 1
                else:
                    words_index[r_word][url] = 1
            else:
                words_index[r_word] = {url: 1}
                
            words_set.add(r_word)
        
        for r_word in important_words:
            # dict type: dict{ key:word, value: dict{ key:url, value: frequency}}            
            if r_word in words_index:
                if url in words_index[r_word]:
                    words_index[r_word][url] += 20
                else:
                    words_index[r_word][url] = 20
            else:
                words_index[r_word] = {url: 20}
                
            words_set.add(r_word)

def store_index():
    
    #store all the index dict to files: files named by the first 2 char of the word
    
    if os.path.exists("words_index") == False:
        os.mkdir("words_index")
    
    with open("words_summary.json","w",encoding='utf-8') as f:
        result = dict()
        # result["document number"] = doc_num
        result["words_count"] = len(words_set)
        result["words"] = list(words_set)
        json.dump(result,f,indent=4)
    
    for word,value in words_index.items():
        # print("Creating "+word+".json")
        try:
            if os.path.exists("words_index\\"+word[0]) == False:
                os.mkdir("words_index\\"+word[0])
            
            
            if len(word) > 1:
                
                r_word_path = "words_index\\"+word[0]+"\\"+word[:2]+".json"
                
                if os.path.exists(r_word_path):
                    print("Inserting " + r_word_path)
                    
                    # data = dict()
                    # with open(r_word_path, "r") as f:
                    #     data = json.load(f)
                    #     data.update({word: value})
                    with open(r_word_path, "a",encoding='utf-8') as f:
                        # json.dump(data, f)
                        f.write(f",\n   \"{word}\": ")
                        json.dump(value,f,indent= 8)
                        
                        
                else:
                    print("Creating " + r_word_path)
                    
                    # data = dict()
                    # data = {word: value}
                    with open(r_word_path, "w",encoding='utf-8') as f:
                        # json.dump(data, f)
                        f.write("{\n")
                        f.write(f"   \"{word}\": ")
                        json.dump(value,f,indent= 4)
                
            else:
                with open("words_index\\"+word[0]+"\\"+word+".json",'w',encoding='utf-8') as f:
                    print("Creating " + "words_index\\"+word[0]+"\\"+word+".json")
                    
                    # data = {word: value}
                    # json.dump(data , f, indent= 4)
                    f.write("{\n")
                    f.write(f"   \"{word}\": ")
                    json.dump(value,f,indent= 4)
                    
        except Exception as e:
            with open("error.log","a") as f:
                error_log = "Unexpected error:" + "\n"
                f.write(error_log)
                traceback.print_exc(file=f)
                f.write("\n")
    
    done_index_paths = get_file_path("words_index")
    for p in done_index_paths:
        with open(p,"a") as f:
            f.write("\n}") 


                    

if __name__ == '__main__':
    
    #timer
    start = time.clock()
    
    file_paths = get_file_path("DEV")
    for p in file_paths:
        process_index(p)
    store_index()
    print("OK")
    
    end = time.clock()
    
    print(end-start,"s")
    print(file_count)


#----------------------------------------------------------------------------------------------
# def process_index(file_path):
    
#     print("Processing: " + file_path)
    
#     # make sure we have the correct folder to store the index
#     if os.path.exists("words_index") == False:
#         os.mkdir("words_index")
    
#     if os.path.exists("words_summary.json") == False:
#         with open("words_summary.json","w") as f:
#             words_summary = {"words_count": 0, "words": []}
#             json.dump(words_summary, f)
    
#     content = extract_content(file_path)
#     url = content[0]
#     important_words = content[1]
#     regular_words = content[2]
#     if len(regular_words) != 0:
#         for r_word in regular_words:
            
#             # make a json file corresponding to this word
#             # json file stores: dict{ key:word, value: dict{ key:url, value: frequency}}
#             r_word_path = "words_index\\"+r_word+".json"
            
#             if r_word+".json" in os.listdir("words_index\\"):
#                 data = dict()
#                 with open(r_word_path, "r") as f:
#                     data = json.load(f)
#                     if url in data[r_word]:
#                         data[r_word][url] += 1
#                     else:
#                         data[r_word][url] = 1
#                 with open(r_word_path, "w") as f:
#                     json.dump(data, f)
#             else:
#                 data = dict()
#                 data[r_word] = {url: 1}
#                 with open(r_word_path, "w") as f:
#                     json.dump(data, f)
            
#             data = dict()        
#             with open("words_summary.json", "r") as f:
#                 data = json.load(f)
#                 if r_word in data["words"]:
#                     continue
#                 else:
#                     data["words_count"]+=1
#                     data["words"].append(r_word)
#             with open("words_summary.json", "w") as f:
#                 json.dump(data, f)
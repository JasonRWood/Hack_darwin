from bs4 import BeautifulSoup as bs
import lxml
import nltk
import os
import string

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def extract_info(filepath,words):
    
    dictionary_of_interest = {}
    
    with open(filepath,"r",encoding="utf8") as file:
            
        content = file.readlines()
        content = "".join(content)
        
        bs_content = bs(content, "lxml")
        
        unique_id = bs_content.find("tei").attrs["xml:id"]
        
        dictionary_of_interest["unique_id"] = unique_id
        
        letter_details = bs_content.find_all("correspaction")
        
        for deets in letter_details:
            
            if deets.attrs["type"] == "sent":
                
                if "when" in list(deets.date.attrs.keys()):
                    dictionary_of_interest["date"] = deets.date.attrs["when"]
                
                try:
                    dictionary_of_interest["sender"] = deets.persname.text
                except AttributeError:
                    dictionary_of_interest["reciever"] = deets.orgname.text
                
                try:
                    dictionary_of_interest["sender_bio"] = deets.persname.attrs["key"]
                except AttributeError:
                    dictionary_of_interest["sender_bio"] = "None Available"
                except KeyError:
                    dictionary_of_interest["sender_bio"] = "None Available"
                    
            if deets.attrs["type"] == "received":
                
                try:
                    dictionary_of_interest["reciever"] = deets.persname.text
                except AttributeError:
                    dictionary_of_interest["reciever"] = deets.orgname.text
                    
                try:
                    dictionary_of_interest["reciever_bio"] = deets.persname.attrs["key"]
                except AttributeError:
                    dictionary_of_interest["reciever_bio"] = "None Available"
                except KeyError:
                    dictionary_of_interest["reciever_bio"] = "None Available"
                    
        try:
            free_text = bs_content.find_all("div",{"type":"transcription"})[0].p.text
        except AttributeError:
#             print(bs_content) 
            free_text = ""
            

        # cleaning of the data
        dictionary_of_interest["body"] = (free_text.lower()).translate(str.maketrans('','',string.punctuation))
        text_tokens = word_tokenize(dictionary_of_interest["body"])
#         no_stop_words = [word for word in text_tokens] # if not word in stopwords.words()
        for word in text_tokens:
            words.append(word)
#         print(no_stop_words)

        file.close()
        
    return dictionary_of_interest

def generate_feature_data(free_text,feature_set):
    
    feature_bools = []
    
    for word in feature_set:
        feature_bools.append(1*(word in free_text))
        
    return feature_bools
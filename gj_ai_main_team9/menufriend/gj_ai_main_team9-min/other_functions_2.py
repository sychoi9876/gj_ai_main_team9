from other_functions_1 import cleanText,isNaN,nan_value, list_to_dict,ingre_to_counter,check_ingre
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import math 
import pandas as pd 
import ast
import re
import numpy as np

def mf_1500_function(file_path_):  # 전처리 완료된 1500개 데이터를 DataFrame 으로 반환.
    df = pd.read_csv(file_path_)
    df = df.iloc[:,1:]
    df = df.dropna(subset=['main_ingredients'])

    df['main_ingredients'] = df['main_ingredients'].str.replace(' ','')
    df['main_ingredients'] = df['main_ingredients'].str.replace('or',',')
    df['main_ingredients'] = df['main_ingredients'].str.replace('OR',',')
    df['main_ingredients'] = df['main_ingredients'].str.replace('\u200b','') 
    df['main_ingredients'] = df['main_ingredients'].apply(lambda x: ast.literal_eval(x)) #dict화
    df['main_ingredients'] = df['main_ingredients'].apply(lambda x : [y for y in x])
    df['main_ingredients'] = df['main_ingredients'].apply(lambda x : ','.join(x))
    df['main_ingredients'] = df['main_ingredients'].apply(cleanText)

    df['ingredients'] = df['ingredients'].str.replace(' ','')
    df['ingredients'] = df['ingredients'].str.replace('or',',')
    df['ingredients'] = df['ingredients'].str.replace('OR',',')
    df['ingredients'] = df['ingredients'].str.replace('\u200b','') 
    df['ingredients'] = df['ingredients'].apply(lambda x: ast.literal_eval(x)) #dict화
    df['ingredients'] = df['ingredients'].apply(lambda x : [y for y in x])
    df['ingredients'] = df['ingredients'].apply(lambda x : ','.join(x))
    df['ingredients'] = df['ingredients'].apply(cleanText)
    return df
    
def mf_33000_function(file_path_): # 모든 데이터 33000개를 DataFrame으로 
    df = pd.read_csv(file_path_)
    df = df.iloc[:,1:]
    df = df.fillna('')
    df['raw_ingre_sep'] = df['raw_ingre'].str.replace(' ','')
    df['raw_ingre_sep'] = df['raw_ingre_sep'].str.replace('or',',')
    df['raw_ingre_sep'] = df['raw_ingre_sep'].str.replace('OR',',')
    df['raw_ingre_sep'] = df['raw_ingre_sep'].str.replace('\u200b','')
    df['raw_ingre_sep'] = df['raw_ingre_sep'].apply(lambda x: ast.literal_eval(x)) #dict화
    df['raw_ingre_sep'] = df['raw_ingre_sep'].apply(lambda x : [y for y in x])
    df['raw_ingre_sep'] = df['raw_ingre_sep'].apply(lambda x : ','.join(x))
    df['raw_ingre_sep'] = df['raw_ingre_sep'].apply(cleanText)
    df['raw_ingre_sep'] = df['raw_ingre_sep'].apply(lambda x: x.split(','))
    df.main_ingredients = df.main_ingredients.apply(lambda x : ast.literal_eval(x) if not x == '' else x)
    df['main_ingredients'] = df['main_ingredients'].apply(lambda x : [y for y in x] if not x == '' else x )
    df['main_ingredients'] = df['main_ingredients'].apply(lambda x : ','.join(x))
    df['main_ingredients'] = df['main_ingredients'].replace('',np.nan)
    df.ingredients = df.ingredients.apply(lambda x : ast.literal_eval(x) if not x == '' else x)
    df['ingredients'] = df['ingredients'].apply(lambda x : [y for y in x] if not x == '' else x)
    df['ingredients'] = df['ingredients'].apply(lambda x : ','.join(x))
    df['raw_ingre_sep'] = df.raw_ingre_sep.apply(lambda x: check_ingre(x) if not isNaN(x) else x)
    df['raw_ingre_sep'] = df['raw_ingre_sep'].apply(lambda x : [y for y in x])
    df['raw_ingre_sep'] = df['raw_ingre_sep'].apply(lambda x : ','.join(x))
    return df

def find_ingre(pre_menu_idx): 
  if pre_menu_idx >= 0:
    df = mf_33000_function('./mfd.csv')
    i = df.loc[pre_menu_idx].raw_ingre_sep.split(',')
    return i
  return -1

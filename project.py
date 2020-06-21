#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:31:20 2020

@author: hanzhuo
"""


import numpy as np
import pandas as pd


ratings = pd.read_csv('rating.csv')
anime = pd.read_csv('anime.csv')

anime = anime.drop(['genre','type','episodes', 'members', 'rating'],axis=1)

ratings = pd.merge(anime,ratings, on='anime_id')
ratings.head()

ratings.groupby('name')['rating'].count().sort_values(ascending=False).head()

user_ratings = ratings.pivot_table(index='user_id',columns='name', values='rating')
user_ratings.head()

user_ratings = user_ratings.dropna(thresh=100,axis=1).fillna(0)
#print(user_ratings.head())


#item_similarity_df = user_ratings.corr(method='pearson')
#print(item_similarity_df.head())

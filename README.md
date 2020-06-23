# Anime Recommender System

This project is for COEN 140 final project. Will plan to expand on this project in the future

current approach: User-based, KNN

## DataSet:
Anime.csv content:
-anime_id - use to identifying the anime
-name - full name of anime
-genre - comma separated list of genres for this anime
-type - movie, TV, OVA or etc
-episodes - how many episodes in the anime
-rating - average rating out of 10
-members - number of community members that are in this anime

Rating.csv content:
-user_id - non identifiable randomly generated user id
-anime_id - the anime id that the user has rated
-rating - rating out of 10 this user has assigned(-1 if the user watched it but didn’t assign a rating)


Unable to upload the rating.csv file since is too big. Please use this link below to download the dataset:
https://www.kaggle.com/CooperUnion/anime-recommendations-database

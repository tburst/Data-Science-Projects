# Projects


## Cultural Heritage - Map-Visualization

Do certain architectural heritage categories occur more frequently in some regions than in others? The Hessian cultural heritage register DenkXWeb was scraped using BeautifulSoup and Selenium and the data stored in an SQL database. The descriptions for every object were then prepared and analyzed via pandas and scikit-learn and visualized in folium maps.

Alternative version [hier](http://nbviewer.jupyter.org/github/tburst/Projekte/blob/master/Denkmale%20Hessen%20-%20Map-Visualisierung/DenkmaleHessen_RegionaleUnterschiede.ipynb)

## Classification of Political Orientations

Can a machine learning model learn to assign texts to a political orientation only on the basis of the words used in those texts? Using a self-generated text corpus of Bundestag speeches from the election periods 14-18, an SVM model was trained to identify the political direction of the speaker based on uni and bigrams. Subsequently, the generalizability of the model is tested on election programs and newspaper articles.

[Link](https://github.com/tburst/Projekte/blob/master/Klassifikation%20politischer%20Sprache/Klassikfikation_politischer_Sprache.ipynb)

## Sentiment-Dict

Are there uniquely negative or positive words in political language? Through a Word2Vec model, words are mapped in terms of their meaning in the political context. Thanks to two lists of predefined sentiment words, an SVM model can learn to predict the sentiment of a word based on its word vector. The model is then used to find new positive/negative words in political language usage and to create its own sentiment lists. Finally, this new sentiment resource will be used to analyze the language in the German Bundestag.

[Link](https://github.com/tburst/Projekte/blob/master/Sentiment-Dict/Erstellung_eines_Sentiment_Dicts.ipynb)


# Projekte


## Denkmale Hessen - Map-Visualisierungen

Kommen bestimmte Denkmaltypen in manchen Regionen häufiger vor als in anderen? Das hessische Denkmalverzeichnis DenkXWeb wurde mittels BeautifulSoup und Selenium gescrapet und in eine SQL-Datenbank eingepflegt. Die Begründungstexte wurden dann durch pandas und scikit-learn analysierbar gemacht und in folium Karten visualisiert.

Falls die Karten nicht dargestellt werden findet sich eine alternative Version [hier] (http://nbviewer.jupyter.org/github/tburst/Projekte/blob/master/Denkmale%20Hessen%20-%20Map-Visualisierung/DenkmaleHessen_RegionaleUnterschiede.ipynb)

## Klassifikation politischer Sprache

Kann ein Machinelearning-Modell nur anhand der verwendeten Wörter lernen, Texte einer politischen Richtung zuzuordnen? Mittels eines selbsterstellten Textkorpus aus Bundestagsreden der Wahlperioden 14-18 wurde einem SVM-Modell anhand von Uni- und Bigrams beigebracht, die politische Richtung des Redners zu identifizieren. Im Anschluss daran wird die Generalisierbarkeit des Modells bei Wahlprogrammen und Zeitungsartikeln getestet.

## Sentiment-Dict

Gibt es eindeutig negative oder positive Wörter im politischen Sprachgebrauch? Durch ein Word2Vec-Modell


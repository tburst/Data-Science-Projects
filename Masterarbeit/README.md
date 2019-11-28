Replikationsdaten zur Masterarbeit *"Deutschlands Blick auf die Welt - westlich oder europäisch? Eine Messung von Länderwahrnehmungen im Deutschen Bundestag mittels Wortvektormodellen"*. Die Arbeit misst mittels Wortvektormodellen, wie der Deutsche Bundestag zwischen 1996 und 2016 über andere Länder gesprochen hat. Dabei zeigt sich in der Analyse: Die Verteilung der Wortvektoren entspricht ab 2003 immer weniger einer Zweiteilung in westliche und nicht-westliche Länder. Vielmehr entspricht die Nähe der Wortvektoren zunehmend einer Unterscheidung zwischen europäischen und nicht-europäischen Staaten. Europa scheint den Westen als zentrales Unterscheidungsmerkmal für Länder abzulösen.


## Wortvektordaten

Da alle Wortvektormodelle zusammen über 150GB groß sind, können die Word2vec-Modelle nicht zur Verfügung gestellt werden. Stattdessen wurden relevante Auszüge aus den Modellen in drei Ordner hochgeladen. Mit diesen Daten ist eine Replikation der Analyse möglich.

#### Country_Vectors

Enthält die Wortvektoren der Ländernamen aller genutzten Word2vec-Modelle als Csv-Dateien. Für jeden  Modellzeitraum stehen die Ländervektoren von 25 unterschiedlichen Bootstrapping-Durchläufen und von einem "fixed Model" (an originalem, nicht durch bootstrapping veränderten Datensatz trainiert) zur Verfügung. Die Wortvektoren wurden vor dem Abspeichern in den Csv-Dateien mittels des gensim Befehls "init_sims" L2-Normalisiert.

#### Country_Vectors_Similarity

Enthält die Kosinus-Ähnlichkeiten zwischen den Ländervektoren als Csv-Dateien.

#### Country_Vectors_Cluster

Enthält die für jedes Wortvektormodell gebildeten Cluster ähnlicher Ländervektoren. Als Grundlage für die Clusterung dienten die Kosinus-Ähnlichkeiten aus dem Ordner "Country_Vectors_Similarity". Zur Clusterung wurde auf <a href="https://python-louvain.readthedocs.io/en/latest/api.html" target="_blank">python-louvain</a> zurückgegriffen.


## Dateien

#### Country_Groups.csv

Enthält Informationen zu den einzelnen Ländern, wie bspw. zu welcher UN-Regionalgruppe sie gehören. Wird für einen Teil der Visualisierungen benötigt.

#### Country_Min5Freq.csv

Enthält die Namen aller Länder, die in jedem vierjährigen Modellzeitraum mindestens fünf mal in Bundestagsreden vorkamen. Nur sie werden in die Analyse mit einbezogen.

#### Ländernamen.csv

Enthält die Namen von 188 Ländern der Welt. Wird für die Bildung der Wortvektormodelle benötigt, u.a. um die Genitivformen der Länder zu korrigieren.


## Code

#### Output der Ländervektoren.ipynb

Generiert aus den fertig gebildeten Wortvektormodellen die drei Ordner "Country_Vectors", "Country_Vectors_Similarity" und "Country_Vectors_Cluster" mitsamt aller Csv-Dateien.

#### Replikation der Visualisierungen.ipynb

Code der verwendet wurde, um die Visualisierungen der Arbeit zu erstellen. Jede Grafik wird auf Basis der drei "Wortvektordaten" Ordner gebildet, die originalen Word2vec-Modelle sind nicht notwendig. Da in github teilweise Probleme mit der Darstellung von Grafiken auftauchen, wird empfohlen, das Notebook über den <a href="https://nbviewer.jupyter.org/github/tburst/Projekte/blob/master/Masterarbeit/Replikation%20der%20Visualisierungen.ipynb " target="_blank">nbviewer</a> aufzurufen

#### Bilden der Wortvektormodelle.ipynb

Code der verwendet wurde, um die Wortvektormodelle zu bilden.


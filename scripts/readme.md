# Projekt Analizator Wyników

## Opis projektu
Celem projektu jest stworzenie modelu predykcyjnego, który na podstawie dostarczonego zbioru danych przewiduje zmienną `score`. Projekt obejmuje eksplorację danych, inżynierię cech, trenowanie i ocenę modelu.
## Analiza danych
   ![Histogram](./images/histogram.png)

Histogramy dla zmiennych liczbowych w zbiorze danych wskazują na różnorodność w wartościach oraz potencjalne niejednorodności w rozkładzie niektórych zmiennych. Ogólnie, wiele zmiennych wydaje się mieć wartości skoncentrowane w dolnym zakresie. W związku z tym jako jeden z algorytmów zastosowałem Random forest, który jest mniej wrazliwy na odstające wartości.

Zbiór danych zawiera 15 kolumn.
Wszystkie kolumny zawierają 4739 non-null wartości, co oznacza, że nie ma brakujących danych (null) w żadnej z kolumn.

## Wybór algorytmu
Przetestowane zostały trzy algorytmy dla podanych danych
- **Regresja liniowa**
MSE: 0.6478110558382555
MAE: 0.6610828223195607
R²: 0.3532577798594442
- **Gradient boosting wraz z odpowiednimi parametrami**
Best MSE: 0.6521370585366623
Best MAE: 0.6659013881128322
Best R2: 0.3489389147146045
- **Random forest wraz z odpowiednimi parametrami**
Best MSE: 0.6375852449270155
Best MAE: 0.6460359759252305
Best R²: 0.3634667190121037

Na podstawie porównania wyników trzech modeli regresyjnych, najlepszym algorytmem okazał się Random Forest.

MSE (Średni Błąd Kwadratowy) dla Random Forest wynosi 0.6376, co jest najniższą wartością spośród wszystkich modeli.
MAE (Średni Błąd Bezwzględny) również osiągnął wartość 0.6460, co wskazuje na mniejsze odchylenia prognozowanych wartości od rzeczywistych.
R² (Współczynnik Determinacji) wynosi 0.3635, co oznacza, że model Random Forest dobrze potrafi wychwycić róznice w danych

## Statystyki
Data columns (total 15 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   rownames   4739 non-null   int64  
 1   gender     4739 non-null   object 
 2   ethnicity  4739 non-null   object 
 3   score      4739 non-null   float64
 4   fcollege   4739 non-null   object 
 5   mcollege   4739 non-null   object 
 6   home       4739 non-null   object 
 7   urban      4739 non-null   object 
 8   unemp      4739 non-null   float64
 9   wage       4739 non-null   float64
 10  distance   4739 non-null   float64
 11  tuition    4739 non-null   float64
 12  education  4739 non-null   int64  
 13  income     4739 non-null   object 
 14  region     4739 non-null   object 
dtypes: float64(5), int64(2), object(8)
memory usage: 555.5+ KB
None
           rownames        score        unemp         wage     distance      tuition    education
count   4739.000000  4739.000000  4739.000000  4739.000000  4739.000000  4739.000000  4739.000000
mean    3954.638953    50.889029     7.597215     9.500506     1.802870     0.814608    13.807765
std     5953.827761     8.701910     2.763581     1.343067     2.297128     0.339504     1.789107
min        1.000000    28.950001     1.400000     6.590000     0.000000     0.257510    12.000000
25%     1185.500000    43.924999     5.900000     8.850000     0.400000     0.484990    12.000000
50%     2370.000000    51.189999     7.100000     9.680000     1.000000     0.824480    13.000000
75%     3554.500000    57.769999     8.900000    10.150000     2.500000     1.127020    16.000000
max    37810.000000    72.809998    24.900000    12.960000    20.000000     1.404160    18.000000
rownames     0
gender       0
ethnicity    0
score        0
fcollege     0
mcollege     0
home         0
urban        0
unemp        0
wage         0
distance     0
tuition      0
education    0
income       0
region       0

import pandas as pd
import matplotlib.pyplot as plt

#
#zad. 1 Wczytaj dane do zmiennej data, w taki sposób, żeby nazwa Państwa była kluczem.
data=pd.read_csv("homework02/gapminder.csv",index_col=0)
print(data)

#zad. 2 Znajdź najbardziej i najmniej zaludnione państwa na świecie.
df= pd.DataFrame(data)

#max population
print(df[df.population == df.population.max()].population)

#min population
print(df[df.population == df.population.min()].population)

#zad. 3** W ilu państwach współczynnik `female_BMI` jest większy od `male_BMI`.

amount=(df[df.female_BMI >= df.male_BMI].female_BMI.count())
print("ilosc panstw gdzie BMI kobiet jest wieksze niz BMI mezczyzn = " + str(amount))


#zad. 4

#Zainstaluj bibliotekę pycountry_convert i zaimportuj ją.
#Dodaj do danych kolumnę continent, która będzie zawierać nazwę kontynentu,
#na którym jest położone dane państwo. Wykorzystaj bibliotekę pycountry_convert.
#Uwaga: trzeba najpierw uzystać kod państwa w fomacie ISO-2, następnie uzystkać kod kontynentu, a na końcu uzyskać nazwę kontynentu.

import pycountry_convert

conts = []
for name in data.index:
    country_code = pycountry_convert.convert_countries.country_name_to_country_alpha2(name)
    cont_code = pycountry_convert.convert_country_alpha2_to_continent_code.country_alpha2_to_continent_code(
        country_code)
    cont = pycountry_convert.convert_continent_code_to_continent_name(cont_code)
    conts.append(cont)

data['continent'] = conts
data['continent']


#zad. 5 Oblicz ile osób mieszka na każdym z kontynentów.


data.groupby('continent').sum().population

#zad. 6 Narysyj wykres słupkowy pokazujący ile państw leży na każdym z kontynentów.
data.continent.value_counts().plot('bar')


# zad. 7
#Kolumna gdp zawiera informacje o PKB na obywatela. Stwórz nową kolumnę gdp_total, która będzie informować o PKB danego kraju.
#Oblicz ile wynosi suma światowego PKB (kolumna gdp_total).
#Oblicz ile krajów jest odpowiedzialnych za wytworzenie 80% światego PKB.

#Kolumna gdp zawiera informacje o PKB na obywatela. Stwórz nową kolumnę gdp_total, która będzie informować o PKB danego kraju.
gdp_total = 0
for name in data.index:
    gdp_total = data.gdp*data.population

data['gdp_total'] = gdp_total

pd.set_option('display.max_rows', None)
data['gdp_total']

#Oblicz ile wynosi suma światowego PKB (kolumna gdp_total).
print('total_pkb=',data.gdp_total.sum())

#Oblicz ile krajów jest odpowiedzialnych za wytworzenie 80% światego PKB.
pkbSortedDesc = data.sort_values(['gdp_total'],ascending=False)
pkbSortedDesc

gdp_total_80_counter = 0
gdp_total_80_value = 0
total_pkb_100 = pkbSortedDesc.gdp_total.sum()
percantage = 0
temp1 = 0
for name in pkbSortedDesc.index:
    #print(pkbSortedDesc['gdp_total'].values)
   # gdp_total_80_value=gdp_total_80_value+pkbSortedDesc['gdp_total'].values
    gdp_total_80_value = gdp_total_80_value+ pkbSortedDesc.get_value(name,'gdp_total')
    #print(gdp_total_80_value)
    gdp_total_80_counter+=1
    percantage = (gdp_total_80_value/total_pkb_100)*100
    #print('procent=  ',percantage,' %')
    print(gdp_total_80_counter,'procent=  ',percantage,' %',)
    if((gdp_total_80_value/total_pkb_100)>0.8):
       break
print('Ilosc najbogatszych panstw wytwarzajacych ponad 80% pkb = ', gdp_total_80_counter)

# zad. 8 Wyświetl wszystkie europejskie państwa, w których oczekiwana długość życia wynosi conajmniej 80 lat.
df=pd.DataFrame(data,columns=['continent','life_expectancy'])
selected_countries = df.loc[(df['life_expectancy']>=80) & (df['continent']=="Europe")]
print(selected_countries)


#zad. 9 Znajdź państwo, które ma najbardziej zbliżone PKB do Polski. Spróbuj rozwiązać to zadanie w jednej linijce.

#max population
print(df[df.population == df.population.max()].population)    
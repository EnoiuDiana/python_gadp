import pandas as pd
import matplotlib.pyplot as plt

description = ('Country', [
    '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'
])

dataset = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ':']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ',
            '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ',
            '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ',
            '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57', '59 ', '64 ', '67 ',
            '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 ', ': ',
            '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ',
            '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ',
            '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ',
            '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ',
            '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ',
            '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ',
            '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ',
            '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ',
            '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ',
            '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ',
            '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ',
            '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ',
            '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ',
            '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ',
            '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ',
            '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ',
            '93 ', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 ', '79 ',
            '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ',
            '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ',
            '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ',
            '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ',
            '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ',
            '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ',
            '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 ', '68 ', '72 ', '76 ',
            '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ',
            '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 ', '95 ',
            '93 ', '96 ']),
    ('SI', ['73 ',
            '74 ', '76 ', '77 ', '78 ', '78 ', '82 ',
            '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ',
            '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ',
            '93 ', '94 ',
            '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ',
            '93 ']),
]
print("/////////////////// In clasa /////////////////////")
df = pd.DataFrame(dict(dataset))
df.to_csv("dataset.csv")
df.replace(': ', 0, inplace=True)
df.replace(':', 0, inplace=True)
print("Inlocuit date cu 0")
print(df)
print("Describe:")
for x in df:
    df[x] = df[x].astype(int)
print(df.describe())
print("Media pe fiecare tara in linia 9:")
df_mean = pd.DataFrame([df.mean()], columns=list(df))
df_with_mean = df.append(df_mean, ignore_index=True)
print(df_with_mean)
print("Media pe fiecare tara in intr-o noua coloana:")
df["Mean"] = df.mean(axis=1)
print(df)
print("Plot scatter primele 2 tari in functie de medie:")
df.plot(kind='scatter', x=["AL", "AT"], y=["Mean", "Mean"])
df.corr()
plt.show()
print(df.corr())
print("Histograma pentru Romania")
df.plot(kind='hist', y="RO")
df.corr()
plt.show()
print(df.corr())


print("/////////////////// Homework /////////////////////")


def get_df(dataset_param):
    df2 = pd.DataFrame(dict(dataset_param))
    df2.replace(': ', 0, inplace=True)
    df2.replace(':', 0, inplace=True)
    return df2


def get_year_data(dataset_param, year):
    df2 = get_df(dataset_param)
    year_index = None
    for index, year_itr in enumerate(description[1]):
        if year_itr is year:
            year_index = index
    list_get_year_data = [(country, df2[country][year_index]) for country in df2.keys()]
    return {year: list_get_year_data}


def get_country_data(dataset_param, country):
    df2 = get_df(dataset_param)
    list_get_country_data = [(description[1][index], value) for (index, value) in enumerate(df2[country])]
    return {country: list_get_country_data}


def get_country_data_explicit(country, df2):
    list_get_country_data = [{'year': description[1][index], 'coverage': value}
                             for (index, value) in enumerate(df2[country])]
    return list_get_country_data


def get_all_country_data():
    df2 = get_df(dataset)
    dict_country_data = {country: get_country_data_explicit(country, df2) for country in df2.keys()}
    return dict_country_data


def perform_average(country_data_param):
    mean = 0
    for dict_itr in country_data_param:
        mean = mean + int(dict_itr['coverage'])
    return mean / len(description[1])


print("1.")
print(get_year_data(dataset, '2019'))
print("2.")
print(get_country_data(dataset, "RO"))
print("3.")
country_data = get_all_country_data()
print(perform_average(country_data['RO']))

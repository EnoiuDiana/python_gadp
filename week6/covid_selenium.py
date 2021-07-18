from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")

# create a dictionary with all the counties as keys
counties_list = []
for i in range(2, 45):
    county = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr['
                                           + str(i) + ']/td[2]')
    counties_list.append(county.text)
dict_counties_covid_data = {key: [] for key in counties_list}

# find for 7 consecutive days data related to covid new cases in that day
for j in range(7):
    browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-' + str(20 + j) +
                '-ianuarie-ora-13-00/')
    try:
        for i in range(2, 45):
            # first get the counties in order from that page
            current_county = browser.find_element_by_xpath(
                '/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/'
                'tbody/tr[' + str(i) + ']/td[2]')
            # next find the corresponding new cases for that county
            cases = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody'
                                                  '/tr[' + str(i) + ']/td[4]')
            # add the new cases to the list of the corresponding county in the dictionary
            list_cases = dict_counties_covid_data.get(current_county.text)
            list_cases.append(cases.text)
    except NoSuchElementException:  # in case the page does not exists just add '-' in the list
        print('Page does not exists, completing with \'-\'')
        for key in dict_counties_covid_data.keys():
            list_cases = dict_counties_covid_data.get(key)
            list_cases.append('-')
print(dict_counties_covid_data)

df = pd.DataFrame(dict_counties_covid_data)  # transform to a data frame
for i in range(7):
    df.rename(index={i: 'ziua ' + str(i + 1)}, inplace=True)  # format the data frame
df.to_csv('Covid_pe_judete_7_zile.xls', encoding="utf-8-sig")  # export to csv
browser.close()

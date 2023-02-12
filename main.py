from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.spacex.com/launches/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

    launches_container = soup.select_one('#items')

    launches = launches_container.select('.item')

    with open('spacex-launches.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter=';')

        writer.writerow(['Launch date', 'Label'])

        for launch in launches:
            date_element = launch.select_one('.date')
            date = date_element.text

            label_element = launch.select_one('.label')
            label = label_element.text

            writer.writerow([date, label])
else:
    print('Something went wrong.')

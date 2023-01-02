from bs4 import BeautifulSoup
import requests

url = 'https://www.spacex.com/launches/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

    launches_container = soup.select_one('#items')

    launches = launches_container.select('.item')

    for launch in launches:
        date_element = launch.select_one('.date')
        date = date_element.text

        label_element = launch.select_one('.label')
        label = label_element.text

        print(f'Launch date: {date} Label: {label}')
else:
    print('Something went wrong.')

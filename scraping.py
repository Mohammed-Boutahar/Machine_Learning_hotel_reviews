import requests
from bs4 import BeautifulSoup as soup
import csv
import re


header = ["Review", "Rating"]

data = open(r'all_reviews.csv', 'w', encoding="utf-8", newline="")


writer = csv.writer(data, delimiter =';')
writer.writerow(header)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.65 Safari/537.36'}



def scrap_data(url):
    page = requests.get(url, headers=headers)
    soup1 = soup(page.content, "html.parser")
    soup2 = soup(soup1.prettify(), 'html.parser')

    list_data_reviews = soup2.findAll('div', {'class': 'YibKl MC R2 Gi z Z BB pBbQr'})

    for data_review in list_data_reviews:

        review = data_review.find('q', {'class': 'QewHA H4 _a'})
        rating = data_review.find('div', {'class': 'Hlmiy F1'})
        rating_value = rating.find('span').attrs['class'][1][7]
        row = [review.find('span').text.strip(), rating_value]
        writer.writerow(row)


def number_reviews(url):
    page = requests.get(url, headers=headers)
    soup1 = soup(page.content, "html.parser")
    soup2 = soup(soup1.prettify(), 'html.parser')

    list_data_reviews = soup2.findAll('div', {'class': 'YibKl MC R2 Gi z Z BB pBbQr'})
    return len(list_data_reviews)


def last_page(url):
    page = requests.get(url, headers=headers)
    soup1 = soup(page.content, "html.parser")
    soup2 = soup(soup1.prettify(), 'html.parser')
    pages = soup2.find('div', {'class':'pageNumbers'})
    current_page = pages.find('span', {'class':'pageNum current disabled'})
    current_page_num = int(current_page.text.strip())

    other_pages = pages.findAll('a',{'class':'pageNum'})
    list_other_pages = []
    for other_page in other_pages:
        list_other_pages.append(int(other_page.text.strip()))
    max_page = max(list_other_pages)

    if current_page_num < max_page :
        return False
    else :
        return True



<<<<<<< HEAD
url1 = "https://www.tripadvisor.com/Hotel_Review-g147273-d550565-Reviews-Club_Amigo_Carisol_Los_Corales-Santiago_de_Cuba_Santiago_de_Cuba_Province_Cuba.html"
url2 = "https://www.tripadvisor.com/Hotel_Review-g32655-d208191-Reviews-Four_Points_by_Sheraton_Los_Angeles_International_Airport-Los_Angeles_California.html"

#url4 = "https://www.tripadvisor.com/Hotel_Review-g60763-d93627-Reviews-West_Side_YMCA-New_York_City_New_York.html"
#url5 = "https://www.tripadvisor.com/Hotel_Review-g60763-d7182733-Reviews-The_Paul_Hotel_NYC-New_York_City_New_York.html"
#url6 = "https://www.tripadvisor.com/Hotel_Review-g60763-d671150-Reviews-The_Empire_Hotel-New_York_City_New_York.html"
#url7 = "https://www.tripadvisor.com/Hotel_Review-g60763-d142114-Reviews-Night_Hotel_Broadway-New_York_City_New_York.html"
#url8 = "https://www.tripadvisor.com/Hotel_Review-g293734-d1873436-Reviews-Riad_Kheirredine-Marrakech_Marrakech_Safi.html"

urls = [url1, url2]
=======
# url1 = "https://www.tripadvisor.com/Hotel_Review-g186338-d282814-Reviews-Abercorn_House-London_England.html"
# url2 = "https://www.tripadvisor.com/Hotel_Review-g60763-d1181739-Reviews-The_Jane_Hotel-New_York_City_New_York.html"
# url3 = "https://www.tripadvisor.com/Hotel_Review-g60763-d122005-Reviews-The_New_Yorker_A_Wyndham_Hotel-New_York_City_New_York.html"
# url4 = "https://www.tripadvisor.com/Hotel_Review-g60763-d93627-Reviews-West_Side_YMCA-New_York_City_New_York.html"
# url5 = "https://www.tripadvisor.com/Hotel_Review-g60763-d7182733-Reviews-The_Paul_Hotel_NYC-New_York_City_New_York.html"
# url6 = "https://www.tripadvisor.com/Hotel_Review-g60763-d671150-Reviews-The_Empire_Hotel-New_York_City_New_York.html"
# url7 = "https://www.tripadvisor.com/Hotel_Review-g60763-d142114-Reviews-Night_Hotel_Broadway-New_York_City_New_York.html"
# url8 = "https://www.tripadvisor.com/Hotel_Review-g293734-d1873436-Reviews-Riad_Kheirredine-Marrakech_Marrakech_Safi.html"
# url9 = "https://www.tripadvisor.com/Hotel_Review-g32655-d77237-Reviews-Hollywood_Hotel-Los_Angeles_California.html"
# url10 = "https://www.tripadvisor.com/Hotel_Review-g32655-d223049-Reviews-Hyatt_Regency_Los_Angeles_International_Airport-Los_Angeles_California.html"
# url11 = "https://www.tripadvisor.com/Hotel_Review-g32655-d78694-Reviews-Hilton_Los_Angeles_Universal_City-Los_Angeles_California.html"

#Bad reviews
url12 = "https://www.tripadvisor.com/Hotel_Review-g60763-d99443-Reviews-Park_West_Hotel-New_York_City_New_York.html"
url13 = "https://www.tripadvisor.com/Hotel_Review-g60763-d249710-Reviews-Morningside_Inn-New_York_City_New_York.html"
url14 = "https://www.tripadvisor.com/Hotel_Review-g60763-d6701149-Reviews-Midtown_West_Hotel-New_York_City_New_York.html"
url15 = "https://www.tripadvisor.com/Hotel_Review-g60763-d267182-Reviews-Windsor_Hotel-New_York_City_New_York.html"
url16 = "https://www.tripadvisor.com/Hotel_Review-g60763-d224229-Reviews-Hotel_Riverside_Studios-New_York_City_New_York.html"
url17 = "https://www.tripadvisor.com/Hotel_Review-g60763-d307945-Reviews-Woogo_Central_Park-New_York_City_New_York.html"

urls = [url12, url13, url14, url15, url16, url17]
>>>>>>> 437e9ee75bd29796fdf3afd2e9f50d1d36df3ec1

for url_origin in urls:
    
    url = url_origin
    scrap_data(url)
    cmp = 0
    while (not last_page(url) ):

        cmp += number_reviews(url)
        url = re.sub(r'(Reviews-)', "or" + str(cmp) + "-", url_origin)
        scrap_data(url)




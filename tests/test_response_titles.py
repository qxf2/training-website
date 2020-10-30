"""
A script to check the titles and response code of all pages our website.
We simply want to check that the pages:
a) do not 404 and show a 200
b) [NOT DONE] have the right titles
"""
import requests
import sys
import bs4


#Structure is [['endpoint','title'],['endpoint':'title']]
website_map = [['/','Home'],['/senior-qa-training-approach','Senior QA training approach'],['/senior-qa-trainees','Senior QA training audience'],['/why-join-senior-qa-training','Why join senior QA training'],['/why-not-join-senior-qa-training','Why NOT join senior QA training'],['/before-you-join','Senior QA Training: Before you join'],['/senior-qa-training-benefits','Senior QA Training Benefits'],['/senior-qa-training-plan','Senior QA Training Plan'],['/senior-qa-training-samples','Senior QA Training preview']]

def test_response_codes(base_url):
    "Test response code returned by each page"
    if base_url[-1]=='/':
        base_url = base_url[:-1]

    for page in website_map:
        response = requests.get(base_url+page[0])
        assert response.status_code == 200

def test_titles(base_url):
    "Test the titles of each page"
    if base_url[-1]=='/':
        base_url = base_url[:-1]
    
    for page in website_map:
        response = requests.get(base_url+page[0])
        html = bs4.BeautifulSoup(response.text,'lxml')
        assert html.title.text == page [1]


#----START OF SCRIPT
if __name__=='__main__':
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        base_url = 'http://localhost:6464/'
    test_response_codes(base_url)
    test_titles(base_url)
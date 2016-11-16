import re
import csv
import json
import glob

import requests
import urllib.request 
from bs4 import BeautifulSoup

def find_sites():
    'This bit does not work'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-US,en;q=0.8,en-GB;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.expireddomains.net',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }

    session = requests.Session()
    response = session.get('https://www.expireddomains.net/',headers=headers)
    print(response.text)

    search = 'test'
    domain_search_url = 'https://www.expireddomains.net/domainnamesearch/?q={}&position=tour'.format(search)
    response = session.get(domain_search_url,headers=headers)

    print('reponse',response.text) 
    print(response.request.headers)
    print(response.headers)   

def main():

    sites = []
    site_urls = ['LondonClassifieds.co.uk']

    for site_url in site_urls:
        site_details_url = 'https://moz.com/researchtools/ose/api/links?site={}&filter=&source=external&target=page&group=0&page=1&sort=page_authority'.format(site_url)

        response = requests.get(site_details_url).json()

        for item in response['data']:
            print('{target_url}\n\tPage Authority: {page_authority}\tDomain Links: {domain_links_to_domain}'.format(**item))
            sites.append({
                'target_url': item['target_url'],
                'page_authority': item['page_authority'],
                'domain_links_to_domain': item['domain_links_to_domain']
            })

    json.dump(sites,open('output/sites.json','w'),indent=4)

if (__name__ == "__main__"):
    main()
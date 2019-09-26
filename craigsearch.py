#!/usr/bin/env python
# scrape craigslist for sys admin jobs using keyword "linux"
# this was initially intended for use with beautifulsoup, but
# lxml turned out to be wayyyyy friggin better.
# nh

from lxml import html
import requests
#import argparse

'''
parser = argparse.ArgumentParser(description='Craigslist SysAdmin and TechSupport job listing scraper.')
parser.add_argument('-s','--search', help='Search parameter, i.e. "-s linux" ', required=True)
args = vars(parser.parse_args())

response = requests.get('http://sfbay.craigslist.org/search/sad?query=' + str(args))
response1 = requests.get('http://sfbay.craigslist.org/search/tch?query=' + str(args))
'''

response = requests.get('http://sfbay.craigslist.org/search/sad?query=linux')
response1 = requests.get('http://sfbay.craigslist.org/search/tch?query=linux')

if (response.status_code == 200) & (response1.status_code == 200):

    pagehtml = html.fromstring(response.text)
    pagehtml1 = html.fromstring(response1.text)

    link = (pagehtml.xpath('//p[@class="result-info"]/a/@href'))
    jobs = (pagehtml.xpath('//p[@class="result-info"]/a/text()'))
    link1 = (pagehtml1.xpath('//p[@class="result-info"]/a/@href'))
    jobs1 = (pagehtml1.xpath('//p[@class="result-info"]/a/text()'))

print("Systems Admin Jobs:")
x = 0
for i in jobs:
    if x < 25:
        print(jobs[x] + " --", end=" ")
        check_pay = requests.get(link[x])
        if (check_pay.status_code == 200):
            pay_rate = html.fromstring(check_pay.text)
            pay_offer = (pay_rate.xpath('//p[@class="attrgroup"]/span/b/text()')[0])
            print(link[x],  "PAY:", pay_offer)
            x += 1

print("\n")
print("Tech Support Jobs:")
y = 0
for i in jobs1:
    if y < 15:
        print(jobs1[y] + " --", end=" ")
        check_pay1 = requests.get(link1[y])
        if (check_pay1.status_code == 200):
            pay_rate1 = html.fromstring(check_pay1.text)
            pay_offer1 = (pay_rate1.xpath('//p[@class="attrgroup"]/span/b/text()')[0])
            print(link1[y],  "PAY:", pay_offer1)
            y += 1

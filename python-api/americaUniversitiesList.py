"""
Author: J. Smith
Date: June 2022
Description: A small python script to pull data from a public API
API: https://datausa.io/
"""

import warnings
import requests

# Turn off warnings
warnings.filterwarnings('ignore')

# Variables
new_list = []


# Get total of Universities
def universities_total():
    universities_response = requests.get('https://datausa.io/api/searchLegacy?limit=8000&dimension=University',
                                         verify=False)
    return str(len(universities_response.json()['results']))


# Get total of hierarchies within the Universities
def hierarchies_total(hierarchy_type, limit):
    hierarchy_url = 'https://datausa.io/api/searchLegacy?limit=' + str(limit) + '&dimension=University&hierarchy=' \
                    + hierarchy_type
    hierarchy_response = requests.get(hierarchy_url, verify=False)
    return str(len(hierarchy_response.json()['results']))


# Get the list of hierarchies within the Universities
def hierarchies_list(hierarchy_type, limit):
    hierarchy_url = 'https://datausa.io/api/searchLegacy?limit=' + str(limit) + '&hierarchy=' \
                    + hierarchy_type
    hierarchy_response = requests.get(hierarchy_url, verify=False)
    hierarchy_name = hierarchy_response.json()['results']
    return hierarchy_name


# Output
print('\nUniversities within USA')
print('-------------------------')

# Print out Parent Carnegies
print('Total parent carnegies:\t' + hierarchies_total('Carnegie Parent', 100))
num = 1
for parent_carnegies in hierarchies_list('Carnegie Parent', 100):
    print(str(num) + ' ' + parent_carnegies['name'])
    int(num)
    num += 1
print()

# Print out Carnegies
print('Total carnegies:\t\t' + hierarchies_total('Carnegie', 100))
num = 1
for carnegies in hierarchies_list('Carnegie', 100):
    print(str(num) + ' ' + carnegies['name'])
    int(num)
    num += 1
print()

# Print out Universities
print('Total universities:\t\t' + hierarchies_total('University', 8000))
num = 1
for universities in hierarchies_list('University', 8000):
    print(str(num) + ' ' + universities['name'])
    int(num)
    num += 1
print()

# Print out grand total of Universities
print('Grand total:\t\t\t' + universities_total())

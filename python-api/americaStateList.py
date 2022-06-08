"""
Author: J. Smith
Date: June 2022
Description: A small python script to pull data from a public API
API: https://datausa.io/
"""

import warnings
import requests

# Turn off warnings - DO NOT SEND TO PRODUCTION
warnings.filterwarnings('ignore')

# Variables
ordered_state_list = []
response = requests.get('https://datausa.io/api/searchLegacy/?limit=100&dimension=Geography&hierarchy=State&q=',
                        verify=False)


# Convert State key for ordering purposes
def convert_state_number(state_key):
    state_key_split = state_key.split('-')
    state_key_number = state_key_split[-1]
    state_key = state_key_number[-2:]
    return state_key


# Create a list of States to be ordered
for data in response.json()['results']:
    state_list = convert_state_number(data['key']) + "\t\t" + data['name']
    ordered_state_list.append(state_list)


# Order the state list
ordered_state_list.sort()

# Print the ordered state list
print('\nUSA State List:')
print('-----------------\n')
print('Key:\tState:')
print('----\t------')
for state in ordered_state_list:
    print(state)

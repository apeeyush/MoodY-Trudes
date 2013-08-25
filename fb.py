import requests
import json

# Aman's post time
AFTER = 1353233754
TOKEN =                                                                                                                                                                 'CAACEdEose0cBAAlvI5KoS02dmayLjXHVqf6i8K9KFg5Q4DTk77LwHOx7t8MzsZAeUvcF2CYY3uhM1ZBCaK54uqquN4ZCpFHm8l9hmPmz4PumYMGGWi0xZBIBK9FcbLxveokVEOnlZCZB4OFOPEz4DrO7ZBOukZAxGvkZD'

def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall
    between start and end time"""
    query = ("SELECT post_id, actor_id, message, updated_time FROM stream WHERE source_id = me() AND created_time > 1377397025 LIMIT 100")

    payload = {'q': query, 'access_token': TOKEN}

    r = requests.get('https://graph.facebook.com/fql', params=payload)
    print r
    result = json.loads(r.text)
    print result['data']


if __name__ == '__main__':
    get_posts()

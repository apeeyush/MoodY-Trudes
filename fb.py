import requests
import json

# Aman's post time
AFTER = 1353233754
TOKEN = 'CAACEdEose0cBAH05yQmArVVzmWOhHrB7NWgFLoInw9Rp4zMv1OZCzHZBZBcG6peBZAKZBQ7yiZAtwUKHR7Hor4mugoJJVZBQobuZCERhs4DBknmANpUMRGwFaPnRcSXZBxXPgnm4lbM8y7yOMIFjACd1xSQArfwCfi4QZD'

def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall
    between start and end time"""
    query = ("SELECT post_id, actor_id, message FROM stream WHERE source_id = me() AND created_time > 1377397025 LIMIT 100")

    payload = {'q': query, 'access_token': TOKEN}

    r = requests.get('https://graph.facebook.com/fql', params=payload)
    print r
    result = json.loads(r.text)
    print result['data']


if __name__ == '__main__':
    get_posts()

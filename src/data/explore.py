import json
import requests
from pprint import pprint

from client import authenticated_request
from constants import build_relative_path, USER_ID


def filter_keys(keys, dictionary):
    value = {}
    for key in keys:
        value[key] = dictionary[key]
    return value

def is_user_exists(current_user, graph=None):
    if graph is None:
        with open(build_relative_path('graph.json'), 'r') as graph_file:
            graph = json.load(graph_file)
    for user in graph:
        if current_user['user_id'] == user['user_id']:
            return True
    return False

def save_user(current_user):
    with open(build_relative_path('graph.json'), 'r') as graph_file:
        graph = json.load(graph_file)
    if is_user_exists(current_user, graph):
        for user in graph:
            if current_user['user_id'] == user['user_id']:
                user = current_user
                break
        return False
    graph.append(current_user)
    print(graph)
    with open(build_relative_path('graph.json'), 'w') as graph_file:
        json.dump(graph, graph_file, indent=2)
        graph_file.write('\n')
    return True

def explore_norminations(initial_user_id=USER_ID):
    next_id = initial_user_id

    while True:
        status, data = authenticated_request(requests.post, '/get_profile', {
            'user_id': next_id,
        })
        if (status != 200):
            break

        profile = data['user_profile']
        keys = ['user_id', 'name', 'username', 'photo_url']

        invited_by_user_profile = profile['invited_by_user_profile']
        next_id = invited_by_user_profile['user_id'] if invited_by_user_profile else None

        current_user = filter_keys(keys, profile)
        current_user['referrer'] = next_id

        pprint(current_user)
        if not save_user(current_user):
            break

        if next_id is None:
            break

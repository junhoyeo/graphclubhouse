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
    with open(build_relative_path('graph.json'), 'w') as graph_file:
        json.dump(graph, graph_file, indent=2)
        graph_file.write('\n')
    return True

def explore_norminations(initial_user_id=USER_ID):
    next_id = initial_user_id

    if is_user_exists({ 'user_id': next_id}):
        print(f'[!] User {next_id} already exists')
        return

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


def _get_pagination(route, user_id):
    status, data = authenticated_request(requests.post, route, {
        'user_id': user_id,
    })
    if (status != 200):
        return []

    # TODO: pagination
    print('pagination_next:', data['next'])

    return [user['user_id'] for user in data['users']]

def get_following(user_id=USER_ID):
    return _get_pagination('/get_following', user_id)


def get_followers(user_id=USER_ID):
    return _get_pagination('/get_followers', user_id)


def get_channels(user_id=USER_ID):
    return _get_pagination('/get_channels', user_id)


def join_channel(user_id=USER_ID):
    return _get_pagination('/join_channel', user_id)


def active_ping(user_id=USER_ID):
    return _get_pagination('/active_ping', user_id)


def refresh_token(user_id=USER_ID):
    return _get_pagination('/refresh_token', user_id)


def explore_follow_network(user_id=USER_ID):
    crawl_functions = [get_following, get_followers]
    for crawl in crawl_functions:
        users = crawl()

    for user_id in users:
        explore_norminations(user_id)

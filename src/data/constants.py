import os, os.path
from pathlib import Path
from dotenv import load_dotenv

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def build_relative_path(path):
    return os.path.join(__location__, path)

env_path = Path(build_relative_path('.env'))
load_dotenv(dotenv_path=env_path)

API_URL = os.getenv('API_URL')
UUID = os.getenv('UUID')
USER_ID = os.getenv('USER_ID')
HEADERS = {
    'User-Agent': 'clubhouse/269 (iPhone; iOS 14.1; Scale/3.00)',
    'CH-Languages': 'en-US',
    'CH-Locale': 'en_US',
    'CH-AppVersion': '0.2.15',
    'CH-AppBuild': '269',
    'CH-DeviceId': UUID.upper(),
}
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

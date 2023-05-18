import requests, os, natsort, gspread, json, string, re
from selenium import webdriver
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def parse_photos():
    """parse folder path"""
    list = os.listdir("reg/")
    split_key = lambda x: [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', x)]
    # sort the list of files using the lambda function and natsort
    sorted_files = natsort.natsorted(list, key=split_key)
    photos_path = f"reg\\{sorted_files[0]}"
    return photos_path

def df_to_gsheets(df, spreadsheet_name, worksheet_name):
    """Sending df to google sheets"""
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('res/erudite-stratum-316309-a2d8c45cadb8.json', scope)
    gc = gspread.authorize(credentials)
    # Open the Google Sheet
    spreadsheet = gc.open(spreadsheet_name)
    worksheet = spreadsheet.worksheet(worksheet_name)
    # Write the DataFrame to the Google Sheet
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

def parse_gmail(file):
    """Parse excel to get gmail account"""
    df = pd.read_excel(file)
    row = df.iloc[0]
    email, password, reserve = row

    parsed_df = df.iloc[1:]

    parsed_df.to_excel(file, index=False)
    return email, password, reserve

def parse_session(file):
    """parsing session excel"""
    df = pd.read_excel(file, dtype=str)
    row = df.iloc[0]
    session_name, name, proxy_host, proxy_port, proxy_type, proxy_username, proxy_password, latitude, longitude = row

    parsed_df = df.iloc[1:]

    parsed_df.to_excel(file, index=False)
    return session_name, name, proxy_host, proxy_port, proxy_type, proxy_username, proxy_password, latitude, longitude

def parse_proxy(file):
    df = pd.read_excel(file)
    row = df.iloc[0]
    email, password, reserve = row

    print(email)
    print(password)
    print(reserve)

    parsed_df = df.iloc[1:]

    parsed_df.to_excel(file, index=False)
    return email, password, reserve


def send_cmd(driver, cmd, params={}):
    """Deprecated*, used to send command to browser"""
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    return response.get('value')

def parse_line(file):
    """Deprecated*, used to parse first line of text file"""
    with open(file, "r", encoding="UTF-8") as f:
        list = f.readlines()
        line = list[0].strip()

    with open(file, "w", encoding="UTF-8") as f:
        new_list = list[1:]
        content = "".join(new_list)
        f.write(content)

    return line

def create_driver(session, port):
    """create driver"""
    mla_url = f'http://127.0.0.1:{port}/api/v1/profile/start?automation=true&profileId=' + session
    resp = requests.get(mla_url)
    json = resp.json()
    print(json)
    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--use-fake-device-for-media-stream")
    options.add_argument("--window-position=1920,0")
    driver = webdriver.Remote(command_executor=json['value'], options=options)
    return driver

def update_profile_proxy(profile_id, proxy_type, proxy_host, proxy_port, proxy_username, proxy_password, port):
    """update profile proxy"""
    url = f'http://localhost:{port}/api/v2/profile/' + profile_id
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "network": {
            "proxy": {
                "type": proxy_type,
                "host": proxy_host,
                "port": proxy_port,
                "username": proxy_username,
                "password": proxy_password
            }
        }
    }
    r = requests.post(url, json.dumps(data), headers=header)
    print(r.status_code)

def update_profile_group(profile_id, group_id, port):
    """Update profile group"""
    url = f'http://localhost:{port}/api/v2/profile/' + profile_id
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "group": group_id
    }
    r = requests.post(url, json.dumps(data), headers=header)
    print(r.status_code)

def update_profile_geo(profile_id, latitude, longitude, port):
    """update profile geo"""
    url = f'http://localhost:{port}/api/v2/profile/' + profile_id
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "geolocation": {
            "mode": "ALLOW",
            "fillBasedOnExternalIp": False,
            "lat": latitude,
            "lng": longitude,
            "accuracy": "100"
        },
        "mediaDevices": {
            "mode": "REAL"
        },
    }
    r = requests.post(url, json.dumps(data), headers=header)
    print(r.status_code)

def create_profile(session_name, port):
    """create profile"""
    x = {
        "name": f"{session_name}",
        "browser": "mimic",
        "os": "win",
        "enableLock": True,
        "startUrl": f"https://tinder.com/ru"
    }
    header = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    url = f"http://localhost:{port}/api/v2/profile"
    req = requests.post(url, data=json.dumps(x), headers=header)

    return json.loads(req.content).get("uuid")

def list_profiles(port):
    """list all profiles"""
    url = f"http://localhost:{port}/api/v2/profile"
    resp = requests.get(url)
    resp_json = json.loads(resp.content)
    return resp_json

def get_profile_group(session, port):
    """get profile group"""
    data = list_profiles(port)
    df = pd.DataFrame(data)
    locked = df.loc[df['uuid'] == session]
    group_id = locked["group"]
    print(group_id)
    return group_id

def get_profile_name(session, port):
    """get profile name"""
    data = list_profiles(port)
    df = pd.DataFrame(data)
    locked = df.loc[df['uuid'] == session]
    session_name = locked["name"]
    session_name = session_name.to_list()
    session_name = session_name[0]
    pattern = r'[' + string.punctuation + ']'
    session_name = re.sub(pattern, "", session_name)
    print(session_name)
    return session_name


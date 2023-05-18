import time
from info import create_driver
from info import parse_line
import traceback
from selenium.webdriver.common.by import By
import datetime, pyautogui
import os
import re
import string
from get_shadows import get_shadows
from info import update_profile_group


def screenshoter(port):
    if port == "35000":
        logged_out_group = "2531dc67-f8ec-491c-b9ac-21df98a7a322"
    else:
        logged_out_group = "6a48063f-d166-4d7e-80bc-630bb69ed143"
    if port == "35000":
        match_group = "5301e1bf-26d4-464d-be68-b6cd5da9e0c6"
    else:
        match_group = "30fff33f-bc4c-4318-ba63-52e4470d7091"
    now = datetime.datetime.now()
    get_shadows(port)
    parent_dir = "C:/Users/david/PycharmProjects/Tinder/screenshots/shadows"
    directory = now.strftime("%Y_%m_%d %H_%M_%S")
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    while True:
        try:
            session = parse_line("sessions").strip()
            session_name = parse_line("session_names").strip()
            driver = create_driver(session=session, port=port)
            pattern = r'[' + string.punctuation + ']'
            session_name = re.sub(pattern, "", session_name)
            driver.get("https://tinder.com")
            driver.execute_script('navigator.mediaDevices.getUserMedia({video: true})')
            time.sleep(2)
            pyautogui.click(248, 162)
            try:
                pg.click()
            except:
                pass
        except:
            pass
        finally:
            try:
                driver.quit()
            except:
                pass

screenshoter("34999")




def create_driver(session, port):
    """create driver"""
    mla_url = f'http://127.0.0.1:{port}/api/v1/profile/start?automation=true&profileId=' + session
    resp = requests.get(mla_url)
    json = resp.json()
    print(json)
    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--use-fake-device-for-media-stream")
    driver = webdriver.Remote(command_executor=json['value'], options=options)
    return driver

session = "b6775a1f-3dd9-43e4-a57b-42564b79b98f"
port = 35000

import requests
from selenium import webdriver
import pandas as pd
import re
import string
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import natsort

driver = create_driver(session, port)

import time, pyautogui


driver.get("https://tinder.com")
driver.execute_script('navigator.mediaDevices.getUserMedia({video: true})')
time.sleep(5)
pyautogui.click(316, 158)

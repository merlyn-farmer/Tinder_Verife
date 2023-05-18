import time, traceback, subprocess, pyautogui, os.path, os, configparser, random, pyvirtualcam, cv2, threading
from info import create_driver, update_profile_group, parse_line
from selenium.webdriver.common.by import By
from get_sessions import get_sessions
from get_pose import get_pose
from scan_id import scan_asset_id, group_id_list, camera_func
from virtual_camera import virtual_camera

config = configparser.ConfigParser()

config.read('config.ini')
port = config.get('Settings', 'port')
group_id = config.get('Settings', 'group')
group_fine = config.get('Settings', 'group_fine')

group = group_id_list(group_id, port)
g_fine = group_id_list(group_fine, port)

folder = ['011', '010', '012', '001', '014']

def verify(port, group, g_fine):
    get_sessions(port, group)
    with open("sessions") as f:
        list = f.readlines()
    for i in list:
        try:
            session = parse_line("sessions").strip()
            session_name = parse_line("session_names")
            driver = create_driver(session=session, port=port)
            rand_folder = random.choice(folder)
            driver.get("https://tinder.com")
            time.sleep(6)
            try:
                el1 = driver.find_element(By.XPATH, "(//*[name()='path'][@fill='url(#svg-fill-linear__selfie-verification-pending)'])[1]")
                update_profile_group(session, g_fine, port)
            except:

                """Authorization"""

                driver.execute_script('navigator.mediaDevices.getUserMedia({video: true})')
                time.sleep(2)
                pyautogui.click(248, 162)
                time.sleep(1)
                pyautogui.click(248, 162)

                try:
                    driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
                    time.sleep(3)
                except:
                    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/section[1]/button[1]").click()

                try:
                    driver.find_element(By.XPATH, "//button[1]//div[2]//div[2]").click()
                except:
                    driver.find_element(By.XPATH, "//div[contains(text(),'Next')]").click()
                time.sleep(3)
                pose_elem = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]")
                time.sleep(3)

                """Camera Segment 1"""
                pose = pose_elem.get_attribute("style")
                asset_id = scan_asset_id(session_name)
                driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/button[1]").click()
                time.sleep(1)
                """Создание паралельного потока"""
                def cam_1_process_1():
                    if os.path.isdir(f'assets/{asset_id}'):
                        asset_path = f"assets/{asset_id}/"
                        asset1 = asset_path + get_pose(pose) + ".jpg"
                        virtual_camera(asset1)
                    else:
                        asset_path = f"assets/{rand_folder}/"
                        asset1 = asset_path + get_pose(pose) + ".jpg"
                        virtual_camera(asset1)
                three1 = threading.Thread(target=cam_1_process_1)
                three1.start()
                time.sleep(11)
                driver.find_element(By.XPATH, "//button[@aria-label='Take a picture']").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/button[2]").click()
                time.sleep(7)
                three1.join()

                """Camera Segment 2"""
                pose_elem = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]")
                pose = pose_elem.get_attribute("style")
                time.sleep(3)
                asset_id = scan_asset_id(session_name)
                driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/div[1]/div[1]/button[1]").click()
                time.sleep(1)
                def cam_2_process_1():
                    if os.path.isdir(f'assets/{asset_id}'):
                        asset_path = f"assets/{asset_id}/"
                        asset1 = asset_path + get_pose(pose) + ".jpg"
                        virtual_camera(asset1)
                    else:
                        asset_path = f"assets/{rand_folder}/"
                        asset1 = asset_path + get_pose(pose) + ".jpg"
                        virtual_camera(asset1)
                three2 = threading.Thread(target=cam_2_process_1)
                three2.start()
                time.sleep(11)
                driver.find_element(By.XPATH, "//button[@aria-label='Take a picture']").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/button[2]").click()
                time.sleep(3)
                three2.join()
                update_profile_group(session, g_fine, port)

        except:
            traceback.print_exc()
        finally:
            try:
                driver.quit()
            except:
                pass

verify(port, group, g_fine)



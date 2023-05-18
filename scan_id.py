import re, os, subprocess
from get_pose import get_pose


def scan_asset_id(session_name):
    result = re.search(r'R(\d{3})', session_name)
    if result:
        asset_id = result.group(1)
        return asset_id

def group_id_list(group_id, port):
    match (group_id, port):

        case ("verif", "34999"):
           g_id = "39510937-6d3d-473f-b3ce-0ca96e3cf9cd"
        case ("verif", "35000"):
           g_id = "8549b7a5-0b13-4b3d-80d8-a23e200e34dd"

        case ("very_fine", "34999"):
           g_id = "ef2d7ef6-11c9-4b7a-9ef6-9bc3c5b7fecb"
        case ("very_fine", "35000"):
           g_id = "b199b3da-67b6-44fd-89e7-6c6b855fd217"


    return g_id

def camera_func(pose, asset_id):
    if os.path.isdir(f'assets/{asset_id}'):
        asset_path = f"assets/{asset_id}/"
        asset1 = asset_path + get_pose(pose) + ".jpg"
        virtual_cam = subprocess.Popen(["python", "-c",
                                        f"import pyvirtualcam;import cv2; from virtual_camera import virtual_camera;virtual_camera(f'{asset1}')"])
    else:
        asset_path = "assets/011/"
        asset1 = asset_path + get_pose(pose) + ".jpg"
        virtual_cam = subprocess.Popen(["python", "-c",
                                        f"import pyvirtualcam;import cv2; from virtual_camera import virtual_camera;virtual_camera(f'{asset1}')"])
    return virtual_cam
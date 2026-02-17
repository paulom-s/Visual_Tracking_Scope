import gphoto2 as gp2
import os
import time

os.system('pkill -f gvfsd-gphoto2')

context = gp2.Context()
cam = gp2.Camera()
cam.init()

def set(param, value):
    config = cam.get_config()
    child = config.get_child_by_name(param)
    child.set_value(value)
    cam.set_config(config)

def capture_LV(cam):
    cam_preview = cam.capture_preview()
    cam_preview.save('data/Camera_Output/preview.jpg')

#capture_LV(cam)
#set('iso', '800')

cam.exit()
import os
from time import strftime
class ConfigManger(object):
    '''
    添加截图目录和截图文件的配置
    '''
    @property
    def screen_path(self):
        basepath = os.path.abspath(os.path.dirname(__file__))
        screenshot_dir = os.path.join(basepath,'screen_capture')
        if not os.path.exists(screenshot_dir):
            os.mkdirs(screenshot_dir)
        now_time = strftime("%Y%m%d%H%M%S")
        screen_file = os.path.join(screenshot_dir,"{}.png".format(now_time))
        return now_time,screen_file
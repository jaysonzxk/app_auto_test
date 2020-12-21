import os
import time

import yaml
from appium import webdriver
from common.baseLog import Log as log


# 项目根目录路径，即android-ui-autotest文件夹的路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# capabilities配置文件desired_caps.py路径
DESIRED_CAPS_YAML_PATH = BASE_PATH + '\\config\\desired_caps'


def android_driver():
    # desired_caps = {}
    # 从desired_caps.yaml读取driver配置数据
    with open(DESIRED_CAPS_YAML_PATH, 'r') as f:
        f = f.read()
        desired_caps = yaml.load(f)
    # stream = open("../config/desired_caps", "r")
    # data = yaml.load(stream, Loader=yaml.FullLoader)
    #
    # desired_caps["platformName"] = data["platformName"].replace('()', ''),
    # desired_caps["platformVersion"] = data["platformVersion"],
    # desired_caps["deviceName"] = data["deviceName"],
    # desired_caps["appPackage"] = data["appPackage"],
    # desired_caps["appActivity"] = data["appActivity"],
    # desired_caps["unicodeKeyboard"] = data["unicodeKeyboard"],
    # desired_caps["resetKeyboard"] = data["resetKeyboard"],
    # desired_caps["noReset"] = data["noReset"],
    # desired_caps["automationName"] = data["automationName"]
    # Log().info('{}'.format(desired_caps))

    # 启动app
    try:
        driver = webdriver.Remote('http://' + str(desired_caps['ip']) + ':' + str(desired_caps['port']) + '/wd/hub', desired_caps)
        log().info("APP启动成功...")
        driver.implicitly_wait(8)
        time.sleep(2)
        return driver
    except Exception as e:
        log().error("APP启动失败，原因是：{}".format(e))


if __name__ == '__main__':
    android_driver()

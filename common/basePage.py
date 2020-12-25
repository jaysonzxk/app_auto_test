import os
import time
from datetime import datetime
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By
from common.baseLog import Log as log
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_to_be_visible(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        等待元素可见
        :param locator:元素定位的XPATH元组表达式
        :param img_doc:截图说明
        :param timeout:等待的超时时间
        :param frequency:轮询频率
        :return:
        """
        try:
            log().info('---' * 20)
            log().info('开始等待页面元素<{}>是否可见'.format(locator))
            log().info('---' * 20)
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            log().error('页面元素<{}>等待可见失败'.format(locator))
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            log().info('页面元素<{}>等待可见，等待时间：{}秒'.format(locator, round(end_time-start_time, 2)))

    def wait_element_to_be_click(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        等待元素可点击
        :param locator:元素定位的XPATH元组表达式
        :param img_doc:截图说明
        :param timeout:等待的超时时间
        :param frequency:轮询频率
        :return:
        """
        try:
            log().info('---' * 20)
            log().info('开始等待页面元素<{}>是否可点击!'.format(locator))
            log().info('---' * 20)
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            log().error('页面元素<{}>等待可点击失败!'.format(locator))
            # self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            log().info('页面元素<{}>等待可点击，等待时间：{}秒'.format(locator, round(end_time-start_time, 2)))

    def wait_element_to_be_exist(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        等待元素存在
        :param locator:元素定位的XPATH元组表达式
        :param img_doc:截图说明
        :param timeout:等待的超时时间
        :param frequency:轮询频率
        :return:
        """
        try:
            log().info('---' * 20)
            log().info('开始等待页面元素<{}>是否存在!'.format(locator))
            log().info('---' * 20)
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            log().error('页面元素<{}>等待存在失败!'.format(locator))
            # self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            log().info('页面元素<{}>等待存在，等待时间：{}秒'.format(locator, round(end_time-start_time, 2)))

    def save_screenshot(self, img_doc):
        """
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        """
        f_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        file_name = f_path + '\\screenshot\\{}_{}.png'.format(datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'), img_doc)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        # allure.attach(file, img_doc, allure.attachment_type.PNG)
        log().info('页面截图文件保存在：{}'.format(file_name))

    def get_element(self, locator, img_doc):
        """
        获取页面中的元素
        :param locator:元素定位的XPATH元组表达式
        :param img_doc:截图说明
        :return:WebElement对象
        """
        log().info('---' * 20)
        log().info('在{}中查找元素<{}>'.format(img_doc, locator))
        log().info('---' * 20)
        try:
            ele = self.driver.find_element(*locator)
        except Exception as e:
            log().error('在{}中查找元素<{}>失败!'.format(img_doc, locator))
            self.save_screenshot(img_doc)
            raise e
        else:
            return ele

    def get_elements(self, locator, img_doc):
        """
        获取页面中所有元素
        :param locator: 元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :return: WebElement对象
        """
        log().info('在{}中查找所有元素<{}>'.format(img_doc, locator))
        try:
            ele = self.driver.find_elements(*locator)
        except Exception as e:
            log().error('在{}中查找所有元素<{}>失败'.format(img_doc, locator))
            self.save_screenshot(img_doc)
            raise e
        else:
            return ele

    def input_text(self, text, locator, img_doc, timeout=20, frequency=0.5):
        """
        输入框输入文本内容
        :param text:输入的文本内容
        :param locator:元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency:轮询频率
        :return:
        """
        try:
            log().info('---' * 20)
            log().info('在{}中输入元素<{}>的内容为{}'.format(img_doc, locator, text))
            log().info('---' * 20)
            self.wait_element_to_be_visible(locator, img_doc, timeout, frequency)
            self.clear_text(locator, img_doc)
            self.get_element(locator, img_doc).send_keys(text)
        except Exception as e:
            log().error('在元素<{}>中输入内容{}失败'.format(locator, text))
            self.save_screenshot(img_doc)
            raise e

    def clear_text(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        清除文本框内容
        :param locator:元素定位的XPATH元组表达式
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        """
        try:
            log().info('---' * 20)
            log().info('在{}中清除元素<{}>的文本内容'.format(img_doc, locator))
            log().info('---' * 20)
            self.wait_element_to_be_click(locator, img_doc, timeout, frequency)
            self.get_element(locator, img_doc).clear()
        except Exception as e:
            log().error('在{}中清除元素<{}>的文本内容失败'.format(img_doc, locator))
            self.save_screenshot(img_doc)
            raise e

    def click_button(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        点击按钮
        :param locator:元素定位的XPATH元组表达式
        :param img_doc:截图说明
        :param timeout:等待的超时时间
        :param frequency:轮询频率
        :return:
        """
        try:
            log().info('---' * 20)
            log().info('在{}中点击元素<{}>'.format(img_doc, locator))
            log().info('---' * 20)
            self.wait_element_to_be_click(locator, img_doc, timeout, frequency)
            self.get_element(locator, img_doc).click()
            # time.sleep(2)
        except Exception as e:
            log().error('在{}中点击元素<{}>失败'.format(img_doc, locator))
            self.save_screenshot(img_doc)
            raise e

    def get_element_text(self, locator, img_doc, timeout=60, frequency=0.5):
        """
        获取WebElement对象的文本值
        :param locator:元素定位的XPATH元组表达式
        :param img_doc:截图说明
        :param timeout:等待的超时时间
        :param frequency:轮询频率
        :return:
        """
        try:
            log().info('---'*20)
            log().info('在{}中获取元素<{}>的文本值'.format(img_doc, locator))
            log().info('---' * 20)
            self.wait_element_to_be_visible(locator, img_doc, timeout, frequency)
            text = self.get_element(locator, img_doc).text
        except Exception as e:
            log().error('在{}中获取元素<{}>的文本值失败'.format(img_doc, locator))
            self.save_screenshot(img_doc)
            raise e
        else:
            log().info('获取到的元素文本值为：{}'.format(text))
            return text

    def get_elements_text(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        获取WebElement对象的所有文本值
        :param locator:元素定位的XPATH元组表达式
        :param img_doc:截图说明
        :param timeout:等待的超时时间
        :param frequency:轮询频率
        :return:
        """
        try:
            log().info("在{}中获取元素<{}>的所有文本值".format(img_doc, locator))
            self.wait_element_to_be_visible(locator, img_doc, timeout, frequency)
            all_text = self.get_elements(locator, img_doc)
            text_list = []
            for one_text in all_text:
                text_list.append(one_text.text)
        except Exception as e:
            log().error("在{}中获取元素<{}>的所有文本值失败！".format(img_doc, locator))
            self.save_screenshot(img_doc)
            raise e
        else:
            log().info("获取到的元素文本值列表为：{}".format(text_list))
            return text_list

    def get_element_attr(self, attr_name, locator, img_doc, timeout=20, frequency=0.5):
        """
        获取WebElement对象的属性值
        :param attr_name:属性名称
        :param locator:元素定位的XPATH元组表达式
        :param img_doc:截图说明
        :param timeout:等待的超时时间
        :param frequency:轮询频率
        :return: WebElement对象的属性值
        """
        try:
            log().info("在{}中获取元素<{}>的属性{}的值".format(img_doc, locator, attr_name))
            self.wait_element_to_be_exist(locator, img_doc, timeout, frequency)
            value = self.get_element(locator, img_doc).get_attribute(attr_name)
        except Exception as e:
            log().error("在{}中获取元素<{}>的属性{}的值失败！".format(img_doc, locator, attr_name))
            self.save_screenshot(img_doc)
            raise e
        else:
            log().info("获取到的元素属性{}的值为{}".format(attr_name, value))
            return value

    def sliding_screen(self, direction, img_doc):
        """
        滑屏操作
        :param direction: 滑屏方向：上-up；下-down；左-left；右-right
        :param img_doc: 截图说明
        :param n: 滑动次数
        :return:
        """
        size = self.driver.get_window_size()
        try:
            log().info("开始向{}方向滑动了".format(direction))
            if direction.lower() == 'up_big':
                time.sleep(1)
                self.driver.swipe(start_x=size['width'] * 0.5,
                                  start_y=size['height'] * 0.9,
                                  end_x=size['width'] * 0.5,
                                  end_y=size['height'] * 0.1,
                                  duration=200)
            elif direction.lower() == 'up_small':
                time.sleep(1)
                self.driver.swipe(
                    start_x=size['width'] * 0.5,
                    start_y=size['height'] * 0.5,
                    end_x=size['width'] * 0.5,
                    end_y=size['height'] * 0.3,
                    duration=200
                )
            elif direction.lower() == 'down':
                time.sleep(1)
                self.driver.swipe(start_x=size['width'] * 0.5,
                                  start_y=size['height'] * 0.1,
                                  end_x=size['width'] * 0.5,
                                  end_y=size['height'] * 0.9,
                                  duration=200)
            elif direction.lower() == 'left':
                time.sleep(1)
                self.driver.swipe(start_x=size['width'] * 0.9,
                                  start_y=size['height'] * 0.5,
                                  end_x=size['width'] * 0.1,
                                  end_y=size['height'] * 0.5,
                                  duration=200)
            elif direction.lower() == 'right':
                time.sleep(1)
                self.driver.swipe(start_x=size['width'] * 0.1,
                                  start_y=size['height'] * 0.5,
                                  end_x=size['width'] * 0.9,
                                  end_y=size['height'] * 0.5,
                                  duration=200)
            else:
                log().error("方向选择错误！")
        except Exception as e:
            log().error("向{}方向滑动屏幕失败！".format(direction))
            self.save_screenshot(img_doc)
            raise e

    def get_toast_msg(self, partial_text, img_doc):
        """
        获取toast文本信息
        :param partial_text: 不完整文本
        :param img_doc: 截图说明
        :return: toast文本
        """
        locator = (By.XPATH, '//*[contains(@text,"{}")]'.format(partial_text))
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located(locator))
            msg = self.driver.find_element(*locator).text
            print("toast出现了！！！")
            return msg
        except Exception as e:
            print("好可惜，toast没找到！！")
            log().error("获取toast文本失败！")
            self.save_screenshot(img_doc)
            raise e

    def switch_to_webview(self, locator, img_doc, timeout=20, frequency=0.5):
        """
        切换到webview页面
        :param locator: webview页面的元素
        :param img_doc: 截图说明
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        """
        try:
            log().info("等待元素{}可见，并进行webview切换".format(locator))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(locator))
            cons = self.driver.contexts
            log().info("开始切换到webview：{}".format(cons[-1]))
            self.driver.switch_to.context(cons[-1])
        except Exception as e:
            log().error("切换webview失败！")
            self.save_screenshot(img_doc)
            raise e
        else:
            end_time = time.time()
            log().info("切换到webview：{}成功，等待时间：{}秒".format(cons[-1], round(end_time - start_time, 2)))

    def switch_to_native_app(self, img_doc):
        """
        切换到app原生页面
        :param img_doc: 截图说明
        :return:
        """
        try:
            log().info("切换到app原生页面")
            self.driver.switch_to.context('NATIVE_APP')
        except Exception as e:
            log().error("切换到app原生页面失败！")
            self.save_screenshot(img_doc)
            raise e

    def application_switching(self, package_name, activity_name, img_doc):
        """
        应用切换
        :param package_name: 包名
        :param activity_name: 欢迎页面名
        :param img_doc: 截图说明
        :return:
        """
        try:
            log().info("切换应用到{}".format(package_name))
            self.driver.start_activity(app_package=package_name, app_activity=activity_name)
        except Exception as e:
            log().error("切换应用到{}失败！".format(package_name))
            self.save_screenshot(img_doc)
            raise e

    def center_coordinate(self, img_doc):
        """
        获取中心点坐标
        :param img_doc:
        :return:
        """
        try:
            log().info('获取屏幕中心坐标')
            size = self.driver.get_window_size()
            touch = TouchAction(self.driver)
            x = size['width'] * 0.5
            y = size['height'] * 0.5
            attribute_value = touch.tap(x=x, y=y).perform()
            # res = self.driver.tap([(x, y)]).find_elements(By.XPATH, '')
            # print(res)
            return attribute_value
        except Exception as e:
            log().error('获取屏幕中心坐标失败')
            self.save_screenshot(img_doc)
            raise e

    def is_element_exist(self, element):
        """
        判断当前页面元素属性是否存在
        :param element: 页面元素
        :return:
        """
        source = self.driver.page_source
        if element in source:
            return 'True'
        else:
            return 'False'



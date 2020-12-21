import time
import unittest
from common.baseDriver import android_driver


class StartEnd(unittest.TestCase):
    def setUp(self) -> None:
        print('----------测试开始---------')

    def tearDown(self) -> None:
        print('----------测试结束----------')

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = android_driver()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     time.sleep(2)
    #     cls.driver.close_app()
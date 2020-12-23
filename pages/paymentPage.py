from common.baseLog import Log
from common.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class PaymentPage(BasePage):
    # =====付款=====
    # 点击进入农户采购
    purchaseApp = (By.ID, 'com.yonghui.cloud.freshstore:id/typePurchase')  # 农户采购入口
    # 获取申请单状态
    applyStatus = (By.ID, 'com.yonghui.cloud.freshstore:id/apply_desc_tv')

    purchaseBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/batching_tv')  # 制单按钮
    purchaseTextBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/text_state')  # 采购信息填写按钮
    # 采购信息-采购组织页面元素
    purchaseChooseBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_purchase_choose')  # 选择采购组织按钮
    purchaseInputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/et_search')  # 采购组织输入搜索框
    purchaseName = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_content')  # 采购组织名称
    # 采购信息-需求地点页面元素
    requireAreaChooseBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_area_choose')  # 选择需求地点按钮
    areaInputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/et_search')  # 需求地点输入搜索框
    areaName = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_content')  # 地点名称
    # 采购信息-供应商页面元素
    supplierChooseBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_supplier_choose')  # 选择供应商按钮
    supplierInputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/et_search')  # 供应商输入搜索框
    supplierName = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_content')  # 供应商名称
    # 采购信息-付款类型
    payTypeChooseBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_pay_type_choose')  # 付款类型选择按钮
    payTypeSubmitBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/btnSubmit')  # 付款类型确认按钮

    purchaseInfoConfirmBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/baseTopRightBtLayout')  # 采购信息页面确认按钮
    # 商品-商品名称页面元素
    addBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/img_add')  # 新增商品按钮
    productBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/et_product')  # 选择商品按钮
    productInputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/et_search')  # 商品输入搜索框
    productName = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_content')  # 商品名称
    # 商品-商品采购价页面元素
    priceInputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/et_price')  # 采购价输入框
    numInputBox = (By.ID, 'com.yonghui.cloud.freshstore:id/et_num')  # 采购数量输入框
    productConfirmBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/baseTopRightBtLayout')  # 商品录入页面确认按钮
    # 申请按钮
    applyBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_send_apply')  # 采购申请按钮
    # 查看详情
    detailsBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_cancel')  # 查看制单详情
    # 制单申请完成--文本断言
    # assertionText1 = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_title')  # text: 申请完成
    assertionText1 = (By.ID, 'com.yonghui.cloud.freshstore:id/status_type_tv')  # text: 待付款
    assertionText2 = (By.ID, 'com.yonghui.cloud.freshstore:id/cancel_order_tv')  # text: 作废
    assertionText3 = (By.ID, 'com.yonghui.cloud.freshstore:id/sure_pay_order_tv')  # text: 确认付款

    # =====付款=====
    payConfirmBtn = (By.ID, 'com.yonghui.cloud.freshstore:id/tv_confirm')

    def payment_action(self):
        """
        制单
        :param purchase_org: 采购组织
        :param area_code: 需求地点
        :param supplier_code: 供应商编码
        :param product_code: 商品编码
        :param price: 采购价格
        :param num: 采购数量
        :return:
        """
        # 农户采购入口
        self.click_button(self.purchaseApp, '农户采购入口')
        # 向左滑动到待付款页面
        self.sliding_screen('left', '申请列表-全部列表页向左滑动到待付款列表页')
        # 获取页面所有的申请单状态文本
        # source = self.driver.page_source
        # print(source)
        while 1:
            text = self.get_element_text(self.applyStatus, '获取申请单状态')
            if text == '待付款' or text == '支付失败':
                self.click_button(self.applyStatus, '点击进入申请单详情页')
                break
            else:
                self.sliding_screen('up_small', '向上滑动一格')
                continue

    def get_assertion_ele(self):
        """
        断言元素
        :return:
        """
        assertionEle1 = (By.ID, self.assertionText1[1])
        assertionEle2 = (By.ID, self.assertionText2[1])
        assertionEle3 = (By.ID, self.assertionText3[1])
        return assertionEle1, assertionEle2, assertionEle3



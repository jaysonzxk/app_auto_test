from common.baseLog import Log
from common.basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class PurchasePage(BasePage):
    # =====制单=====
    # 点击进入农户采购
    purchaseApp = (By.ID, 'com.yonghui.cloud.freshstore:id/typePurchase')  # 农户采购入口
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

    def purchase_action(self, purchase_org, area_code, supplier_code, product_code, price, num):
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
        # 采购信息
        self.click_button(self.purchaseBtn, '制单按钮')
        self.click_button(self.purchaseTextBtn, '填写采购信息按钮')
        # 采购信息-采购组织
        self.click_button(self.purchaseChooseBtn, '点击采购组织选择按钮')
        Log().info('输入搜索的采购组织:{}'.format(purchase_org))
        self.input_text(purchase_org, self.purchaseInputBox, '采购组织')
        self.click_button(self.purchaseName, '点击选择查询出来的采购组织')
        # 采购信息-需求地点
        self.click_button(self.requireAreaChooseBtn, '点击需求选择地点')
        Log().info('输入搜索的需求地点:{}'.format(area_code))
        self.input_text(area_code, self.areaInputBox, '需求地点')
        self.click_button(self.areaName, '点击选择查询出来的需求地点')
        # 采购信息-供应商
        self.click_button(self.supplierChooseBtn, '点击供应商选择按钮')
        Log().info('输入搜索的供应商为:{}'.format(supplier_code))
        self.input_text(supplier_code, self.supplierInputBox, '供应商')
        self.click_button(self.supplierName, '点击选择查询出来的供应商')
        # 采购信息-付款类型
        self.click_button(self.payTypeChooseBtn, '付款类型选择按钮')
        # 采购信息-确认按钮
        self.click_button(self.payTypeSubmitBtn, '付款类型确认按钮')
        self.click_button(self.purchaseInfoConfirmBtn, '确认按钮')
        # 商品
        self.click_button(self.addBtn, '新增商品按钮')
        # 商品-商品名称
        self.click_button(self.productBtn, '选择商品按钮')
        Log().info('输入搜索的商品为:{}'.format(product_code))
        self.input_text(product_code, self.productInputBox, '商品')
        self.click_button(self.productName, '点击选择查询出来的商品')
        # 商品-采购价
        Log().info('输入采购价为:{}'.format(price))
        self.input_text(price, self.priceInputBox, '采购价格')
        # 商品-采购数量
        Log().info('输入采购数量为:{}'.format(num))
        self.input_text(num, self.numInputBox, '采购价格')
        self.click_button(self.productConfirmBtn, '确认按钮')
        # 申请按钮
        self.click_button(self.applyBtn, '采购申请按钮')
        # 制单详情按钮
        self.click_button(self.detailsBtn, '申请单详情')

    def get_assertion_ele(self):
        """
        断言元素
        :return:
        """
        assertionEle1 = (By.ID, self.assertionText1[1])
        assertionEle2 = (By.ID, self.assertionText2[1])
        assertionEle3 = (By.ID, self.assertionText3[1])
        return assertionEle1, assertionEle2, assertionEle3



import unittest
import os
import time
import HTMLTestRunner
# from TestRunner import HTMLTestRunner

# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.abspath(__file__))


def add_case(rule='test*'):
    """
    第一步：加载所有的测试用例
    :param rule:测试用例文件命令规则
    :return:
    """
    f_path = os.path.dirname(os.path.abspath(__file__))

    # 动态获取被测项目
    # for root, dirs, files in os.walk(f_path):
    #     if product in root and root.endswith(module):
    #         case_path = root  # 需要执行用例文件夹

    case_path = os.path.join(f_path, 'testcase')
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover


def run_case(allCase, reportName='report'):
    """
    第二步：执行所有的用例，并把结果写入HTML测试报告
    :param allCase:
    :param reportName:
    :return:
    """
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    reportPath = os.path.join(cur_path, reportName)  # 报告文件夹
    # 如果不存在就创建
    if not os.path.exists(reportPath):
        os.mkdir(reportPath)
    f_path = os.path.dirname(os.path.abspath(__file__))
    if 'app' in str(f_path) or 'web' in str(f_path):
        title = '{}测试报告'.format(f_path[8:11])
    else:
        title = 'api测试报告'
    report_abspath = os.path.join(reportPath, now+"result.html")
    # fp = open(report_abspath, "wb")
    # runner = HTMLTestRunner(stream=fp, title=title, description="用例执行情况")
    #
    # # 调用add_case返回值
    # runner.run(all_case)  # discover
    # fp.close()
    with open(report_abspath, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title, description="用例执行情况")
        runner.run(all_case)  # discover


def get_report_file(reportPath):
    """
    第三步：获取最新的测试报告
    :param reportPath: 测试报告路径
    :return:
    """
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path, fn)))
    print("最新测试报告: "+lists[-1])
    # 找到最新生成的测试报告
    reportfile = os.path.join(report_path, lists[-1])
    return reportfile


if __name__ == "__main__":
    all_case = add_case()   # 1 加载用例
    # 生成测试报告路径
    run_case(all_case)      # 2 执行用例
    report_path = os.path.join(cur_path, "report")   # 用例文件
    report_file = get_report_file(report_path)    # 3 获取最新测试报告

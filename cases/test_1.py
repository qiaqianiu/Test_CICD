from lib.main import *
import allure


def setup_module():
    print('\n *** 模块-初始化  ***')
    print('执行初始化代码')
def teardown_module():
    print('\n *** 模块-清除  ***')
    print('执行模块清除代码')
class Test_demo:
    @classmethod
    def setup_class(cls):
        print('\n === 初始化-类 ===')

    @classmethod
    def teardown_class(cls):
        print('\n === 清除 - 类 ===')

    def setup_method(self):
        print('\n --- 初始化-方法  ---')

    def teardown_method(self):
        print('\n --- 清除  -方法 ---')

    # 使用allure装饰器添加测试特性
    @allure.feature("百度搜索")
    @allure.story("基础功能测试")
    def test_demo_001(self):
        print('-----执行用例demo_001-----')
        wd.get('https://www.baidu.com/')
        # wd.find_element(By.ID, 'kw').send_keys('自动化测试')
        # wd.find_element(By.ID, 'su').click()
        # 添加Allure步骤日志
        allure.attach(wd.title, "页面标题", allure.attachment_type.TEXT)
        assert "百度" in wd.title, "页面标题验证失败"



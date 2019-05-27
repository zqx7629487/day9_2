import pytest
import allure


class TestOne:

    @allure.step(title="测试一下")
    def test_01(self):
        allure.attach("测试下","一下")
        print("ok")
        assert True

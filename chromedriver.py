from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    # 创建WebDriver对象，指定Chrome浏览器驱动程序的路径
    driver = webdriver.Chrome('/Users/bytedance/code/jktools/chromedriver/chromedriver_mac64/chromedriver')

    # 打开网页
    driver.get('https://dreamit.blog.csdn.net/article/details/113706328')

    # 关闭浏览器
    # driver.close()

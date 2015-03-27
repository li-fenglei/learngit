#coding=utf-8
#! /usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,sys,unittest
reload(sys)
sys.setdefaultencoding('utf-8')

#Firefox_driver=r"F:\program install\firefox.exe"
#os.environ['webdriver.Firefox.driver']=Firefox_driver
class company_submit():
    def __init__(self,**kwargs):
	#self.driver=webdriver.Firefox(Firefox_driver)
        self.driver=webdriver
	#self.driver.implicitly_wait(20)
	self.verificationErrors=[]
	self.accept_next_alert=True
	self.kwargs=kwargs

		

    def submit(self):
	values_dict={}
	kwargs_dict=self.kwargs
	for key in kwargs_dict:
		print kwargs_dict[key]
		#values_dict[key]=eval("u'"+kwargs_dict[key].decode('utf-8')+"'")
                values_dict[key]=kwargs_dict[key]
		print values_dict[key]
	driver=self.driver
	driver=webdriver.Firefox()
        driver.get("https://mp.dianhua.cn/bizctr/pc.php")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/a[3]").click()
        time.sleep(3)

        #登录
        user_elm=driver.find_element_by_id("user")
        pwd_elm=driver.find_element_by_id("pwd")
        user_elm.clear()
        user_elm.send_keys("ifly21@126.com")
        pwd_elm.clear()
        pwd_elm.send_keys("892671472")
        driver.find_element_by_id("login").click()
        time.sleep(3)
        #进入商家信息填写页面
        driver.find_element_by_id("addComms").click()
        time.sleep(2)
        #上传logo
        
        driver.find_element_by_id("logo_100").click()
        time.sleep(2)
        driver.switch_to_frame("Openbox")
        driver.find_element_by_xpath("//form[@id='fileinput']").click() #send_keys(values_dict["logo"])
        driver.find_element_by_id("triggerSubmit").click()
        time.sleep(3)
        driver.switch_to_default_content()
        
        #输入企业名称
        driver.find_element_by_name("name").send_keys(values_dict["name"])
        #上传企业形象
        driver.find_element_by_id("logo_1080").click()
        time.sleep(2)
        driver.switch_to_frame("Openbox")
        driver.find_element_by_name("file").send_keys(values_dict["form"])
        driver.find_element_by_id("triggerSubmit").click()
        time.sleep(3)
        driver.switch_to_default_content()
        #输入显示名称
        driver.find_element_by_name("show_name").send_keys(values_dict["show_name"])
        #办公时间
        driver.find_element_by_name("official_hours").send_keys(values_dict["official_hours"])
        #所属分类
        driver.find_element_by_link_text(u"选择分类").click()
        driver.switch_to_frame("OpenCategory")
        menu_eat=driver.find_element_by_link_text(u"吃喝玩乐购")
        webdriver.ActionChains(driver).move_to_element(menu_eat).perform()
        driver.find_element_by_link_text(u"购物服务").click()
        time.sleep(1)
        cat_box=driver.find_element_by_class_name("cat_box")
        cat_box.find_element_by_link_text(u"个体门店/柜台").click()
        driver.switch_to_default_content()
        #添加号码
        driver.find_element_by_link_text(u"添加号码").click()
        time.sleep(2)
        tel_type=driver.find_element_by_name("tel_type")
        tel_type.find_element_by_xpath("//option[@value='短信']").click()
        driver.find_element_by_name("tel").send_keys(values_dict["tel"])
        driver.find_element_by_name("tel_des").send_keys(values_dict["tel_des"])
        driver.find_element_by_link_text(u"确定").click()
        #简介
        driver.find_element_by_name("intro").send_keys(values_dict["intro"])
        #办公地点
        province_elm=driver.find_element_by_id("province")
        province_elm.find_element_by_xpath("//*[@id=\'province\']/option[@value=\'15\']").click()
        time.sleep(1)
        city_elm=driver.find_element_by_id("city")
        city_elm.find_element_by_xpath("//*[@id=\'city\']/option[@value=\'18\']").click()
        time.sleep(1)
        district_elm=driver.find_element_by_id("district")
        district_elm.find_element_by_xpath("//*[@id=\'district\']/option[@value=\'20\']").click()
        driver.find_element_by_name("address").send_keys(values_dict["address"])
        time.sleep(2)
        #添加坐标
        current_window=driver.current_window_handledriver
        driver.find_element_by_link_text(u"添加坐标").click()
        time.sleep(5)
        windows=driver.window_handles
        for each_window in windows:
	        if each_window!=current_window:
		        driver.switch_to_window(each_window)
		        time.sleep(1)
		        map_select=driver.find_element_by_xpath("//*[@id='base']/img[13]")
		        webdriver.ActionChains(driver).move_to_element(map_select).context_click().perform()
		        time.sleep(1)
		        driver.find_element_by_xpath("//*[@id='map']/div[1]/div[2]/div[1]/div[5]/ul/li[1]").click()
		        time.sleep(1)
		        driver.find_element_by_xpath("//*[@id='toolbar']/input[1]").click()
		        driver.switch_to_alert().accept()
        driver.switch_to_window(current_window)
        #营业执照
        driver.find_element_by_id("license").click()
        time.sleep(1)
        driver.switch_to_frame("Openbox")
        driver.find_element_by_name("file").send_keys(values_dict["license"])
        driver.find_element_by_name("triggerSubmit").click()
        driver.switch_to_default_content()
        #其他认证
        #官方网站
        driver.find_element_by_name("official_url").send_keys(values_dict["official_url"])
        #同意电话邦协议

submit=company_submit(logo="H:\\test\\image\\test.jpg",form="H:\\test\\image\\test.jpg",name="测试名称",show_name="显示测试名称",official_hours="24",tel="13126486719",tel_des="测试",intro="认证中心测试",address="静安中心",license="H:\\test\\image\\test.jpg",official_url="www.dianhua.cn")
submit.submit()
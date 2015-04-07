#coding=utf-8
#! /usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,sys,unittest,xlrd,xlutils
#reload(sys)
#sys.setdefaultencoding('utf-8')


#path='H:\\test\\pizctr\\keys.xlsx'

def rdexcel():
    #
    driver=webdriver.Firefox()
    driver.get("https://mp.dianhua.cn/bizctr/pc.php")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/a[3]").click()
    time.sleep(2)

    #登录
    user_elm=driver.find_element_by_id("user")
    pwd_elm=driver.find_element_by_id("pwd")
    user_elm.clear()
    user_elm.send_keys("ifly21@126.com")
    pwd_elm.clear()
    pwd_elm.send_keys("892671472")
    driver.find_element_by_id("login").click()
    time.sleep(3)

    #添加商企，进入商家信息填写页面
    driver.find_element_by_id("addComms").click()
    time.sleep(2)

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

    #办公地点
    province_elm=driver.find_element_by_id("province")
    province_elm.find_element_by_xpath("//*[@id=\'province\']/option[@value=\'3\']").click()
    time.sleep(1)
    city_elm=driver.find_element_by_id("city")
    city_elm.find_element_by_xpath("//*[@id=\'city\']/option[@value=\'57\']").click()
    time.sleep(1)
    district_elm=driver.find_element_by_id("district")
    district_elm.find_element_by_xpath("//*[@id=\'district\']/option[@value=\'24568\']").click()

    #添加坐标
    current_window=driver.current_window_handle
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

    #上传营业执照
    driver.find_element_by_id("license").click()
    time.sleep(1)
    driver.switch_to_frame("Openbox")
    driver.find_element_by_name("file").send_keys("H:\\test\\image\\test.jpg")
    driver.find_element_by_name("triggerSubmit").click()
    driver.switch_to_default_content()

    #读取excel文件
    list_data=[]        
    excel_file=xlrd.open_workbook('H:\\test\\pizctr\\keys.xlsx')        
    table=excel_file.sheet_by_name(u'Sheet1')        
    for i in range(table.nrows):        
        list_data.append(table.row_values(i))            
        #print list_data
    for j in range(1,3):
        name=list_data[j][0]
        show_name=list_data[j][1]
        official_hours=str(list_data[j][2])
        tel=str(list_data[j][3])
        tel_des=list_data[j][4]
        intro=list_data[j][5]
        address=list_data[j][6]
        official_url=list_data[j][7]
        #print official_url

        #输入企业名称
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(name)
        driver.find_element_by_name("show_name").clear()
        name_tip_elm=driver.find_element_by_class_name("name_tip")
        name_tip = name_tip_elm.text
        name_tip=name_tip.encode('utf-8')
        #print name_tip
        #table.write(j,8,name_tip)

        #输入显示名称
        driver.find_element_by_name("show_name").send_keys(show_name)
        driver.find_element_by_name("official_hours").clear()
        show_name_tip_elm=driver.find_element_by_class_name("show_name_tip")
        show_name_tip=show_name_tip_elm.text
        show_name_tip=show_name_tip.encode('utf-8')
        #print show_name_tip
        #table.write(j,9,show_name_tip)

        #办公时间
        driver.find_element_by_name("official_hours").send_keys(official_hours)
        driver.find_element_by_name("intro").clear()
        official_hours_tip_elm=driver.find_element_by_class_name("official_hours_tip")
        official_hours_tip=official_hours_tip_elm.text
        official_hours_tip=official_hours_tip.encode('utf-8')
        #print official_hours_tip
        #table.write(j,10,official_hours_tip)

        #添加号码
        driver.find_element_by_link_text(u"添加号码").click()
        time.sleep(2)
        tel_type=driver.find_element_by_name("tel_type")
        tel_type.find_element_by_xpath(u"//option[@value='短信']").click()
        driver.find_element_by_name("tel").send_keys(tel)
        driver.find_element_by_name("tel_des").send_keys(tel_des)
        driver.find_element_by_link_text(u"确定").click()

        #简介
        driver.find_element_by_name("intro").send_keys(intro)

        #detail address
        driver.find_element_by_name("address").send_keys(address)
        time.sleep(2)

        #官方网站
        driver.find_element_by_name("official_url").send_keys(official_url)


        
rdexcel()
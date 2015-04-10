#coding=utf-8
#! /usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,sys,unittest,xlrd,xlutils
reload(sys)
sys.setdefaultencoding('utf-8')

def info_submit():
    
    #用Firefox打开认证中心首页
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
    try:        
        windows=driver.window_handles
        for each_window in windows:
            if each_window!=current_window:
                driver.switch_to_window(each_window)
                time.sleep(2)
                map_select=driver.find_element_by_xpath("//*[@id='base']/img[13]")
                webdriver.ActionChains(driver).move_to_element(map_select).context_click().perform()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='map']/div[1]/div[2]/div[1]/div[5]/ul/li[1]").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='toolbar']/input[1]").click()
                driver.switch_to_alert().accept()
        driver.switch_to_window(current_window)
    except:
        print 'some error occured'
        driver.switch_to_window(current_window)

    #上传营业执照
    driver.find_element_by_id("license").click()
    time.sleep(1)
    driver.switch_to_frame("Openbox")
    driver.find_element_by_name("file").send_keys("H:\\test\\image\\test.jpg")
    driver.find_element_by_name("triggerSubmit").click()
    driver.switch_to_default_content()
    
    #打开txt文件，写入返回信息
    f=open('H:\\test\\pizctr\\response.txt','w')        
    
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
        official_hours=list_data[j][2]
        tel=str(list_data[j][3])
        tel_des=list_data[j][4]
        intro=list_data[j][5]
        address=list_data[j][6]
        official_url=list_data[j][7]
        #print official_url
        
        #输入企业名称
        name_elm=driver.find_element_by_name("name")
        name_elm.click()
        name_elm.clear()
        name_elm.send_keys(name)
        
        #输入显示名称
        show_name_elm=driver.find_element_by_name("show_name")
        show_name_elm.click()
        time.sleep(2)
        show_name_elm.clear()
        show_name_elm.send_keys(show_name)
        
        #办公时间
        official_hours_elm=driver.find_element_by_name("official_hours")
        official_hours_elm.click()
        time.sleep(2)
        official_hours_elm.clear()
        official_hours_elm.send_keys(official_hours)        
        
        #简介
        intro_elm=driver.find_element_by_name("intro")
        intro_elm.click()
        time.sleep(2)
        intro_elm.clear()
        intro_elm.send_keys(intro)
        
        #详细地址
        address_elm=driver.find_element_by_name("address")
        address_elm.click()
        time.sleep(2)
        address_elm.clear()
        address_elm.send_keys(address)        
               
        #官方网站
        official_url_elm=driver.find_element_by_name("official_url")
        official_url_elm.click()
        time.sleep(2)
        official_url_elm.clear()
        official_url_elm.send_keys(official_url)       
        
        name_elm.click()
        time.sleep(2)
               
        #企业名称response        
        name_tip_elm=driver.find_element_by_class_name("name_tip")               
        name_tip=name_tip_elm.text.encode('gbk')
        if name_tip=='':
            print 'pass'
            f.write('pass'+'\n')
        else:
            print name_tip
            f.write(name_tip+'\n')
                              
        #显示名称response        
        show_name_tip_elm=driver.find_element_by_class_name("show_name_tip")        
        show_name_tip=show_name_tip_elm.text.encode('gbk')
        if show_name_tip=='':
            print 'pass'
            f.write('pass'+'\n')
        else:
            print show_name_tip
            f.write(show_name_tip+'\n')
            
        #办公时间response    
        official_hours_tip_elm=driver.find_element_by_class_name("official_hours_tip")
        official_hours_tip= official_hours_tip_elm.text.encode('gbk')
        if official_hours_tip=='':
            print 'pass'
            f.write('pass'+'\n')
        else:
            print official_hours_tip
            f.write(official_hours_tip+'\n')
            
        #简介response
        intro_tip_elm=driver.find_element_by_class_name("intro_tip")
        intro_tip=intro_tip_elm.text.encode('gbk')
        if intro_tip=='':
            print 'pass'
            f.write('pass'+'\n')
        else:
            print intro_tip
            f.write(intro_tip+'\n')
            
        #详细地址response
        error_address_tip_elm=driver.find_element_by_class_name("error_address_tip")
        error_address_tip=error_address_tip_elm.text.encode('gbk')
        if error_address_tip=='':
            print 'pass'
            f.write('pass'+'\n')
        else:
            print error_address_tip
            f.write(error_address_tip+'\n')
            
        #官方网站 response
        official_url_tip_elm=driver.find_element_by_class_name("official_url_tip")
        official_url_tip=official_url_tip_elm.text.encode('gbk')
        if official_url_tip=='':
            print 'pass'
            f.write('pass'+'\n')
        else:
            print official_url_tip
            f.write(official_url_tip+'\n')
            
        time.sleep(3)       
        
        #添加号码
        driver.find_element_by_link_text(u"添加号码").click()
        time.sleep(2)
        tel_type=driver.find_element_by_name("tel_type")
        
        tel_elm=driver.find_element_by_name("tel")
        tel_des_elm=driver.find_element_by_name("tel_des")
        tel_elm.clear()
        tel_des_elm.clear()
        tel_elm.send_keys(tel)        
        tel_type.find_element_by_xpath(u"//option[@value='电话']").click()
        time.sleep(2)
        tel_tip_elm=driver.find_element_by_class_name("tip")
        tel_tip=tel_tip_elm.text.encode('gbk')
        if tel_tip=='':
            print 'pass'
            tel_des_elm.send_keys(tel_des) 
            driver.find_element_by_link_text(u"确定").click()            
            time.sleep(3)
            f.write('pass'+'\n')
            f.write('\n')
        else:
            print tel_tip
            driver.find_element_by_link_text(u"取消").click()            
            time.sleep(2)
            f.write(tel_tip+'\n')
            f.write('\n')
        time.sleep(4)
    f.close()
    
if __name__=='__main__':
    info_submit()

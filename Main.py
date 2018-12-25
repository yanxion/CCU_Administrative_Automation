# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime, date
import json
import time
import os
import calendar
import random

class Log_Manage:
    def __init__(self):
        chrome_path = os.path.abspath(".\chromedriver.exe")
        self.plan_num = ''
        self.acc = ''
        self.pwd = ''
        self.set_yy = ''
        self.set_mm = ''
        self.set_dd = []
        self.set_hrs = []
        self.set_workin = ''
        self.web = webdriver.Chrome(chrome_path)

    def main(self):
        self.load_json()
        self.login()
        self.add_log()
        self.make_log_number()

    def make_log_number(self):
        self.web.get('https://miswww1.ccu.edu.tw/pt_proj/print_sel.php')

        ele = Select(self.web.find_element_by_name('unit_cd1'))
        ele.select_by_value(self.plan_num)
        ele = self.web.find_element_by_name('sy')
        ele.clear()
        ele.send_keys(self.set_yy)
        ele = self.web.find_element_by_name('sm')
        ele.clear()
        ele.send_keys(self.set_mm)
        ele = self.web.find_element_by_name('sd')
        ele.clear()
        ele.send_keys(1)
        ele = self.web.find_element_by_name('ey')
        ele.clear()
        ele.send_keys(self.set_yy)
        ele = self.web.find_element_by_name('em')
        ele.clear()
        ele.send_keys(self.set_mm)
        ele = self.web.find_element_by_name('ed')
        ele.clear()
        ele.send_keys(calendar.monthrange(int(self.set_yy), int(self.set_mm))[1])
        self.web.find_element_by_xpath('/html/body/form/center/input').click()
        self.web.find_element_by_name('chka').click()


    def add_log(self):
        self.web.get('https://miswww1.ccu.edu.tw/pt_proj/control2.php')
        for i in range(len(self.set_dd)):
            self.add_log_detailed(i)
        self.web.switch_to.frame("main")
        self.web.find_element_by_xpath('/html/body/form/center/input[2]').click()
        time.sleep(0.5)
        self.web.find_element_by_xpath('/html/body/center/input').click()
        try:
            ele = self.web.switch_to.alert
            ele.accept()
        except:
            pass
        
        
    def load_json(self):
        file = open(os.path.abspath('.\default_set.json'), encoding='utf8')
        ftxt = str(file.read()).encode('utf-8')
        fjson = json.loads(ftxt)
        self.plan_num = fjson['plan_num']
        self.acc = fjson['acc']
        self.pwd = fjson['pwd']
        self.set_yy = fjson['set_yy']
        self.set_mm = fjson['set_mm']
        if (fjson['set_hrs'][0] > 4) and (len(fjson['set_hrs']) == 1) :
            self.set_hrs = self.auto_make_hrs(fjson['set_hrs'][0])
        else:
            self.set_hrs = fjson['set_hrs']
        if fjson['set_dd'][0] == 0:
            self.set_dd = self.auto_make_dd(fjson['set_yy'], fjson['set_mm'], self.set_hrs)
        else:
            self.set_dd = fjson['set_dd']
        self.set_workin = fjson['set_workin']

    def auto_make_hrs(self, hrs):
        arr_hrs = []
        while(hrs > 0):
            if hrs > 4:
                hrs -= 4
                arr_hrs.append(4)
            else:
                arr_hrs.append(hrs)
                break
        return arr_hrs

    def auto_make_dd(self, yy, mm, hrs):
        # print (yy, mm, hrs)
        # print(datetime.now().weekday())
        dd = 1
        dt = datetime.now()
        datetime_o = datetime.strptime('{0} {1} {2}'.format((1911 + int(yy)), mm, dd), '%Y %m %d')
        # if datetime_o.weekday
        if int(mm) == int(dt.month):
            days_in_month = dt.day - 1
        else:
            days_in_month = calendar.monthrange(int(yy), int(mm))[1]
        arr_normal_day = []

        for i in range(1, days_in_month + 1, +1):
            dd = i
            datetime_o = datetime.strptime('{0} {1} {2}'.format((1911 + int(yy)), mm, dd), '%Y %m %d')
            if datetime_o.weekday() in [0,1,2,3,4]:
                arr_normal_day.append(i)
        # print(arr_normal_day)
        arr_dd = random.sample(arr_normal_day, len(hrs))
        return arr_dd

    def login(self):
        self.web.get('https://miswww1.ccu.edu.tw/pt_proj/index.php')
        ele = self.web.find_element_by_name('staff_cd')
        ele.send_keys(self.acc)
        ele = self.web.find_element_by_name('passwd')
        ele.send_keys(self.pwd)
        ele = Select(self.web.find_element_by_name('proj_type'))
        ele.select_by_value("3")
        self.web.find_element_by_xpath('/html/body/center/form/input').click()
        try:
            ele = self.web.switch_to.alert
            ele.accept()
        except:
            pass

    def add_log_detailed(self, cnt):
        self.web.switch_to.frame("main")
        ele = Select(self.web.find_element_by_name('type'))
        ele.select_by_value(self.plan_num)
        ele = self.web.find_element_by_name('yy')
        ele.clear()
        ele.send_keys(self.set_yy)
        ele = self.web.find_element_by_name('mm')
        ele.clear()
        ele.send_keys(self.set_mm)
        ele = self.web.find_element_by_name('dd')
        ele.clear()
        ele.send_keys(self.set_dd[cnt])
        ele = self.web.find_element_by_name('hrs')
        ele.clear()
        ele.send_keys(self.set_hrs[cnt])
        ele = self.web.find_element_by_name('workin')
        ele.clear()
        ele.send_keys(self.set_workin)
        self.web.find_element_by_xpath('/html/body/form/center/input').click()


if __name__ == '__main__':
    log_mag = Log_Manage()
    log_mag.main()
    # web.close()

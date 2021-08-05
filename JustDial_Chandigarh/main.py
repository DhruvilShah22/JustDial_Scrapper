import time
import csv
from fake_useragent import UserAgent
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
PATH = "msedgedriver.exe"
options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
links=['https://www.justdial.com/Chandigarh/Ayurvedic-Doctors/nct-10029616','https://www.justdial.com/Chandigarh/Orthopaedic-Doctors/nct-10345039','https://www.justdial.com/Chandigarh/Cardiologists/nct-10080172','https://www.justdial.com/Chandigarh/Pulmonologists-Doctors/nct-10941605','https://www.justdial.com/Chandigarh/Paediatricians/nct-10348959','https://www.justdial.com/Chandigarh/Cosmetic-Surgeon-Doctors/nct-10934151','https://www.justdial.com/Chandigarh/Dentists/nct-10156331','https://www.justdial.com/Chandigarh/Dermatologists/nct-10156786','https://www.justdial.com/Chandigarh/Diabetologist-Doctors/nct-10892682','https://www.justdial.com/Chandigarh/Dietitians/nct-10161884','https://www.justdial.com/Chandigarh/ENT-Doctors/nct-10189442','https://www.justdial.com/Chandigarh/Ophthalmologists/nct-10343851','https://www.justdial.com/Chandigarh/Gastroenterologists/nct-10226406','https://www.justdial.com/Chandigarh/General-Physician-Doctors/nct-10892680','https://www.justdial.com/Chandigarh/Gynaecologist-Obstetrician-Doctors/nct-10551087','https://www.justdial.com/Chandigarh/Homeopathic-Doctors/nct-10251574','https://www.justdial.com/Chandigarh/Neonatologist-Doctors/nct-10892808','https://www.justdial.com/Chandigarh/Neurologists/nct-10336895','https://www.justdial.com/Chandigarh/Neurosurgeons/nct-10336901','https://www.justdial.com/Chandigarh/Oncologists/nct-10343365','https://www.justdial.com/Chandigarh/Ophthalmologists/nct-10343851','https://www.justdial.com/Chandigarh/Orthopaedic-Doctors/nct-10345039','https://www.justdial.com/Chandigarh/Paediatricians/nct-10348959','https://www.justdial.com/Chandigarh/Physiotherapists/nct-10365744','https://www.justdial.com/Chandigarh/Psychiatrists/nct-10393442','https://www.justdial.com/Chandigarh/Psychologist-Doctors/nct-10941606','https://www.justdial.com/Chandigarh/Sexologist-Doctors/nct-10892404','https://www.justdial.com/Chandigarh/Trichologist-Doctors/nct-11005171','https://www.justdial.com/Chandigarh/Thyroid-Doctors/nct-10480621','https://www.justdial.com/Chandigarh/Urologist-Doctors/nct-10892687']
for g in range(len(links)):
    print('Link ' + str(g + 1))
    print(links[g])
    driver = webdriver.Edge(executable_path=PATH)
    driver.get(links[g])
    driver.maximize_window()
    i=0
    count=0
    while(i<90):
        try:
            anc=driver.find_element_by_css_selector('#bcard'+str(i)+' > div.col-md-12.col-xs-12.colsp > section > div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0 > p.newrtings > a')
            name=anc.get_attribute('title')
            rating=driver.find_element_by_css_selector('#bcard'+str(i)+' > div.col-md-12.col-xs-12.colsp > section > div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0 > p.newrtings > a > span.green-box')
            noofvotes=driver.find_element_by_css_selector('#bcard'+str(i)+' > div.col-md-12.col-xs-12.colsp > section > div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0 > p.newrtings > a > span.rt_count.lng_vote')
            availability=driver.find_element_by_css_selector('#bcard'+str(i)+' > div.col-md-12.col-xs-12.colsp > section > div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0 > div.attr_clss > span.distnctxt.rsrtopn-1')
            tc=driver.find_element_by_css_selector('#bcard'+str(i)+' > div.col-md-12.col-xs-12.colsp > section > div.col-sm-5.col-xs-8.store-details.sp-detail.paddingR0 > p.address-info.adinfoex > span > a:nth-child(1)')
            typeofdoc=tc.get_attribute('title')
            count += 1
        except:
            driver.execute_script("window.scrollTo(0, 3*document.body.scrollHeight)/4;")
            time.sleep(5)
        name=name[12:]
        print('Name' + ' ' + str(i+1) + ': ' + name)
        print('Rating' + ' ' + str(i+1) + ': ' + rating.text)
        print('No. of votes' + ' ' + str(i+1) + ': ' + noofvotes.text)
        print('Availability' + ' ' + str(i+1) + ': ' + availability.text)
        print('Type of doctor' + ' ' + str(i+1) + ': ' + typeofdoc)
        i=i+1
    print(count)
    driver.close()

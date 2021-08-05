import time
from selenium import webdriver
PATH = "msedgedriver.exe"
links=['https://www.justdial.com/Ahmedabad/Ayurvedic-Doctors/nct-10029616','https://www.justdial.com/Ahmedabad/Orthopaedic-Doctors/nct-10345039','https://www.justdial.com/Ahmedabad/Cardiologists/nct-10080172','https://www.justdial.com/Ahmedabad/Pulmonologists-Doctors/nct-10941605','https://www.justdial.com/Ahmedabad/Paediatricians/nct-10348959','https://www.justdial.com/Ahmedabad/Cosmetic-Surgeon-Doctors/nct-10934151','https://www.justdial.com/Ahmedabad/Dentists/nct-10156331','https://www.justdial.com/Ahmedabad/Dermatologists/nct-10156786','https://www.justdial.com/Ahmedabad/Diabetologist-Doctors/nct-10892682','https://www.justdial.com/Ahmedabad/Dietitians/nct-10161884','https://www.justdial.com/Ahmedabad/ENT-Doctors/nct-10189442','https://www.justdial.com/Ahmedabad/Ophthalmologists/nct-10343851','https://www.justdial.com/Ahmedabad/Gastroenterologists/nct-10226406','https://www.justdial.com/Ahmedabad/General-Physician-Doctors/nct-10892680','https://www.justdial.com/Ahmedabad/Gynaecologist-Obstetrician-Doctors/nct-10551087','https://www.justdial.com/Ahmedabad/Homeopathic-Doctors/nct-10251574','https://www.justdial.com/Ahmedabad/Neonatologist-Doctors/nct-10892808','https://www.justdial.com/Ahmedabad/Neurologists/nct-10336895','https://www.justdial.com/Ahmedabad/Neurosurgeons/nct-10336901','https://www.justdial.com/Ahmedabad/Oncologists/nct-10343365','https://www.justdial.com/Ahmedabad/Ophthalmologists/nct-10343851','https://www.justdial.com/Ahmedabad/Orthopaedic-Doctors/nct-10345039','https://www.justdial.com/Ahmedabad/Paediatricians/nct-10348959','https://www.justdial.com/Ahmedabad/Physiotherapists/nct-10365744','https://www.justdial.com/Ahmedabad/Psychiatrists/nct-10393442','https://www.justdial.com/Ahmedabad/Psychologist-Doctors/nct-10941606','https://www.justdial.com/Ahmedabad/Sexologist-Doctors/nct-10892404','https://www.justdial.com/Ahmedabad/Trichologist-Doctors/nct-11005171','https://www.justdial.com/Ahmedabad/Thyroid-Doctors/nct-10480621','https://www.justdial.com/Ahmedabad/Urologist-Doctors/nct-10892687']
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

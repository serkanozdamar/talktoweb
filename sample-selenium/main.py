#setup chrome webdriver
from selenium import webdriver

driver = webdriver.Chrome()

#load the web page
driver.get('https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+menu/istatistikler/doviz+kurlari/saat+basi+belirlenen+doviz+kurlari+ve+altin+fiyatlari')

# print page source
print(driver.page_source)

# close the drive

driver.quit()
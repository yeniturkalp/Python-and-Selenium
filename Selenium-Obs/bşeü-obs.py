from selenium import webdriver #projeye selenium dahil edilir
import time #sayfalarda ne kadar sürede kalacağımızı belirlemek için dahil edilir


browser = webdriver.Firefox() #açılacak olan tarayıcıyı seçiyoruz

browser.get("https://obs.bilecik.edu.tr/login.aspx?ReturnUrl=/default.aspx") #gitmek istediğimiz link

time.sleep(3) # 3 saniye giriş sayfasında duracağız

kullanici_no = browser.find_element("xpath","//*[@id='txtLoginKullaniciAdi']")
#öğrenci no yazacağımız yerin HTML alanının xpath kodu
kullanici_sifresi = browser.find_element("xpath","//*[@id='txtLoginSifre']")
#öğrenci şifresini yazacağımız yerin HTML alanının xpath kodu

#dosyadan alınan öğrencino ve şifresini gerekli alanlara yazar
kullanici_no.send_keys(#kendi bilgilerinizi giriceksiniz)
kullanici_sifresi.send_keys(#kendi bilgilerinizi giriceksiniz)

time.sleep(3) # 3 saniye saniye giriş alanında da bekleriz
#giriş yap butonu olan yerin xpath kodu
login = browser.find_element("xpath","//*[@id='btnGiris']")
login.click()#butona tıklar
time.sleep(5) #obs içerisinde 5 saniye bekler

#açılan bildirim kutusunu kapatır
mesaj_kutusu = browser.find_element("xpath","//*[@id='AcilanPencere']/div/div[1]/button")
mesaj_kutusu.click()
time.sleep(3)
browser.back() #daha sonra tekrardan giriş sayfasına döner
time.sleep(3) # 3 saniye bekler 
browser.close() #tarayıcıyı kapatır 



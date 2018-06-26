from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import re
from bs4 import BeautifulSoup
import sqlite3


def get_kreis_stored_in_database():
    conn = sqlite3.connect(r"C:\Users\burst\Dropbox\Topographie_Analytics\Denkmale_new.db")
    cursor = conn.execute("SELECT Kreis FROM Denkmale GROUP BY Kreis")
    stored_kreis = []
    for row in cursor:
        stored_kreis.append(row[0])
    conn.close()
    return stored_kreis
        
        
    

def get_kreis_values():
    url = "http://denkxweb.denkmalpflege-hessen.de/filter/"
    chrome_options = Options()
    browser = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe",chrome_options=chrome_options)
    browser.get(url)
    #Get Kreise
    select_box = browser.find_element_by_name("kreise")
    options = [x for x in select_box.find_elements_by_tag_name("option")]
    kreis_dict = {}
    for element in options:
        kreis_dict[element.get_attribute("value")] =  element.get_attribute("text")
    return kreis_dict





def get_html_single_kreis(kreis_option):
    url = "http://denkxweb.denkmalpflege-hessen.de/filter/"
    chrome_options = Options()
    browser = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe",chrome_options=chrome_options)
    browser.get(url)
    #Select Einzeldenkmal
    select = Select(browser.find_element_by_name('denkmaltyp'))
    select.select_by_value('KD')
    #Select Kreis
    select = Select(browser.find_element_by_name('kreise'))
    select.select_by_value(kreis_option)
    #close dialog Box
    browser.find_element_by_css_selector('.modal-header > button[data-dismiss="modal"]').click()
    browser.find_element_by_css_selector('.modal-footer > button[data-dismiss="modal"]').click()
    time.sleep(5)
    browser.find_element_by_id('searchbtn').click()
    return browser.page_source

    
    
    
def change_encoding_errors(text):
    soup = BeautifulSoup(text,'html.parser')
    text = soup.text.replace("\\u00fc","ü")
    text = text.replace("\\u00df","ß")
    text = text.replace("\\u00f6","ö")
    text =text.replace("\\u00e4","ä")
    text =text.replace("\\u00dc","Ü")
    text =text.replace("\\u00e9","é")
    text =text.replace("\\u00d6","Ö")
    text =text.replace("\\u00c4","Ä")
    text =text.replace("\\u00e1","á")
    text =text.replace("\\u2026","…")
    text =text.replace("\\u2013","–")
    text =text.replace("\\u2020","†")
    text =text.replace("\\u00b4","´")
    text =text.replace("\\u00bd","½")
    text =text.replace("\\u00a7","§")
    text =text.replace("\\u00e2","â")
    text =text.replace("\\u201c",'"')
    text =text.replace("\\u201e",'"')
    text =text.replace('\xa0', ' ').strip()
    soup = BeautifulSoup(text,'html.parser')
    text = soup.text
    return text
    
    


def get_heritagedata_from_html(html_source):
    denkmal_list = re.search("bootstrapTable\('load',(\[.+])",html_source)
    single_dm_list = re.findall("{.+?}",denkmal_list.group(1))
    denkmal_dict = {}
    for entry in single_dm_list:
        denkmal = change_encoding_errors(entry)
        id_number = int(re.search('\"id\":\s(.*?),', denkmal).group(1))
        kdname = re.search('\"kdname\":\s\"(.*?)\"', denkmal)
        ort = re.search('\"ort\":\s\"(.*?)\"', denkmal)
        denkmalwert = re.search('\"denkmalwert\":\s\"(.*?)\"', denkmal)
        ortsteil = re.search('\"ortsteil\":\s\"(.*?)\"', denkmal)
        strassenname = re.search('\"strassenname\":\s\"(.*?)\"', denkmal)
        datierungen = re.search('\"datierungen\":\s\[(.*?)\]', denkmal)
        kreis = re.search('\"kreis\":\s\"(.*?)\"', denkmal)
        flur = re.search('\"flur\":\s\"(.*?)\"', denkmal)
        flurstk = re.search('\"flurstk\":\s\"(.*?)\"', denkmal)
        begruendung = re.search('\"begruendung\":\s\"(.*?)", "', denkmal)
        #Writing in dict
        if begruendung:
            denkmal_dict[id_number] = {}
            denkmal_dict[id_number]["kdname"] = kdname.group(1)
            denkmal_dict[id_number]["Ort"] = ort.group(1).strip()
            denkmal_dict[id_number]["Denkmalwert"] = denkmalwert.group(1)
            denkmal_dict[id_number]["Ortsteil"] = ortsteil.group(1).strip()
            denkmal_dict[id_number]["Strassenname"] = strassenname.group(1).strip()
            if datierungen:
                denkmal_dict[id_number]["Datierungen"] = datierungen.group(1)
            denkmal_dict[id_number]["Kreis"] = kreis.group(1).strip()
            denkmal_dict[id_number]["Flur"] = flur.group(1)
            denkmal_dict[id_number]["Flurstk"] = flurstk.group(1)
            denkmal_dict[id_number]["Begründung"] = begruendung.group(1)
    return denkmal_dict



def write_dict_to_sql(denkmal_dict):
    conn = sqlite3.connect(r"C:\Users\burst\Dropbox\Topographie_Analytics\Denkmale_new.db")
    for denkmal_id in denkmal_dict:
        ort = denkmal_dict[denkmal_id]["Ort"]
        ortteil = denkmal_dict[denkmal_id]["Ortsteil"]
        kreis = denkmal_dict[denkmal_id]["Kreis"]
        flur = denkmal_dict[denkmal_id]["Flur"]
        flurstk = denkmal_dict[denkmal_id]["Flurstk"]
        strasse = denkmal_dict[denkmal_id]["Strassenname"]
        begruendung = denkmal_dict[denkmal_id]["Begründung"]
        conn.execute("INSERT OR REPLACE INTO Denkmale (Id,Ort,Ortsteil,Strasse,Kreis,Flur,Flurstk,Begründung) VALUES(?,?,?,?,?,?,?,?)", (denkmal_id,ort,ortteil,strasse,kreis,flur,flurstk,begruendung))
        if "Datierungen" in denkmal_dict[denkmal_id]:
            for date in denkmal_dict[denkmal_id]["Datierungen"]:
                conn.execute("INSERT OR REPLACE INTO Datierungen (Id,Datierung) VALUES(?,?)", (denkmal_id,date))
        for wert in denkmal_dict[denkmal_id]["Denkmalwert"]:
            conn.execute("INSERT OR REPLACE INTO Denkmalwert (Id,Wert) VALUES(?,?)", (denkmal_id,wert))
    conn.commit()
    conn.close()



kreis_dict = get_kreis_values()
stored_kreis = get_kreis_stored_in_database()
print(kreis_dict)
print(stored_kreis)
for kreis in kreis_dict:
    if kreis_dict[kreis] not in stored_kreis and kreis:
        print("Scraping Kreis {}".format(kreis_dict[kreis]))
        html_source = get_html_single_kreis(kreis)
        denkmal_dict = get_heritagedata_from_html(html_source)
        if denkmal_dict:
            write_dict_to_sql(denkmal_dict)
        time.sleep(10)
    







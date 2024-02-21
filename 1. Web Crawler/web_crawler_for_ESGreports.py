
# check chrome與chrome driver相同版本
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.google.com')
# 能夠正常運行即為正常版本
# chrome要先更新到最新版本
# https://sites.google.com/chromium.org/driver/home?authuser=0
###################################################################
# 設定路徑
import os

os.chdir(r"C:\Users\ASUS\Desktop\ESG_analysis")  # 切換目錄
# os.listdir()  # 看目錄內有什麼

#####################################################################
# 要下載的 PDF 網址列表
# 上市、上櫃在不同頁面
# 匯入excel檔--找110有哪幾間公司
import pandas as pd
companys_df = pd.read_excel('ESG report_outline\ESG_report_companys.xlsx')

# 找110年有哪幾間公司有ESG報告
companys = []  # 有ESG報告的公司代碼
for i, id in enumerate(companys_df['公司代號']):
  if companys_df.loc[i, '110年'] == "V":
    companys.append(id)

print(companys)
print(len(companys))

###############################################################
# 開始爬蟲

import time
from selenium import webdriver

# 設定下載資料夾路徑
download_path = r"C:\Users\ASUS\Desktop\ESG_analysis\ESG_report_110"  # 想要的下載資料夾路徑

# 設定 Chrome 的選項以設定下載資料夾
chrome_option = webdriver.ChromeOptions()
setting = {"download.default_directory": download_path}
chrome_option.add_experimental_option("prefs", setting)

# 初始化 Chrome 瀏覽器並使用設定的選項
driver = webdriver.Chrome(options=chrome_option)

#####################################################################
# 遍歷網址列表

for id in companys[125:]:
    url = 'https://mops.twse.com.tw/server-java/FileDownLoad?step=9&filePath=/home/html/nas/protect/t100/&fileName=t100sa11_' + str(id) + '_110_E.pdf'
    # 前往 PDF 網址
    driver.get(url)

    # 等待 30 秒
    time.sleep(10)

# 關閉瀏覽器
driver.quit()



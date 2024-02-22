# Tone of Sustainability Report
Written by JamCourage                    

**主題類別**            
Text Mining, Data Preprocess, Large Language Model, FinBERT, ESG reports, Sentiment Classification         

**分析工具**      
Python(selenium, pandas, pdfplumber, regex, FinBERT, nltk)

**主要目標**      
計算台灣上市櫃公司英文永續報告書的揭露語調分數(Tone)，並搭配ESG主題分類           
其中，**語調分數(Tone)** 介於-1~1，有三種情緒，分別為**中立** 、**正向** 、**負向** 。
愈接近0為愈中立，愈接近1為愈正向，愈接近-1則為愈負向。     

**兩大步驟**            
1. [Part 1:蒐集台灣上市櫃公司的英文永續報告書--使用python爬蟲](1.%20Web%20Crawler)      
	(1) 將有揭露英文永續報告書的公司股票代碼存入list中      
	(2) 設定並初始化Chrome     
	(3) 使用for迴圈，迭代每一公司，依序從公開資訊觀測站，下載其英文永續報告書      
	【程式碼】            
	程式碼可參考[web_crawler_for_ESGreports.py](1.%20Web%20Crawler/web_crawler_for_ESGreports.py)，以下載110年永續報告書為例       
   
2. [Part 2:分別計算各永續報告書的語調分數(Tone)--使用FinBERT情緒分類模型 & FinBERT主題分類模型](2.%20FinBERT_calculate%20tone)        
	(1) 整理公司股票代碼：將代碼都存在list中      
	(2) 安裝FinBERT兩大模型、nltk tokenizer      
	(3) 逐一擷取PDF文字(使用pdfplumber)       
	(4) 文字前處理：使用regex套件，保留英文字母大小寫、正常標點符號，其他以空白取代           
	(5) nltk斷句        
	(6) FinBERT：同時檢查不得超過512張量，超過者斷成兩句       
		(6-1) FinBERT情緒分類模型：將文本分類為**中立** 、**正向** 、**負向**           
		(6-2) FinBERT主題分類模型：將文本分類為**環境(E)** 、**社會(S)** 、**治理(G)** 、 **非ESG**     	   
	(7) 紀錄結果：使用pandas套件，將結果存成dataframe格式。                
   【程式碼】            
   程式碼可參考：           
   (a) 迭代各公司，計算各公司永續報告書語調分數 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JamCourage/Tone-of-Sustainability-Report/blob/main/2.%20FinBERT_calculate%20tone/crawler_finbert.ipynb)                             
   (b) 記錄一家公司每一句的語調與分類  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JamCourage/Tone-of-Sustainability-Report/blob/main/2.%20FinBERT_calculate%20tone/crawler_finbert_for_one.ipynb)     
                       
   【輸出結果】              
   107年至110年之各公司永續報告書語調分數(Tone)結果，可參考[Tone_breakdown.xlsx](2.%20FinBERT_calculate%20tone/Tone_breakdown.xlsx)                       
   
   共有12種分類結果(情緒分類3種 x 主題分類4種)，欄位說明如下：             
   company_id：公司股票代碼       
   E_neutral：環境面中立情緒(句數)         
   E_positive：環境面正向情緒(句數)              
   E_negative：環境面負向情緒(句數)              
   S_neutral：社會面中立情緒(句數)               
   S_positive：社會面正向情緒(句數)                
   S_negative：社會面負向情緒(句數)                
   G_neutral：治理面中立情緒(句數)                
   G_positive：治理面正向情緒(句數)                 
   G_negative：治理面負向情緒(句數)                 
   non_neutral：非ESG中立情緒(句數)                 
   non_positive：非ESG正向情緒(句數)                  
   non_negative：非ESG負向情緒(句數)                 


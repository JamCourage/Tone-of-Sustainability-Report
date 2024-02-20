# Tone of Sustainability Report
**主要目標**      
計算台灣上市櫃公司英文永續報告書的揭露語調分數(Tone)           
其中，**語調分數(Tone)** 介於-1~1，有三種情緒，分別為**中立** 、**正向** 、**負向** 。
愈接近0為愈中立，愈接近1為愈正向，愈接近-1則為愈負向。     

**兩大步驟**            

1. **蒐集台灣上市櫃公司的英文永續報告書--使用python爬蟲**      
   (1) 將有揭露英文永續報告書的公司股票代碼存入list中      
   (2) 設定並初始化Chrome     
   (3) 使用for迴圈，迭代每一公司，依序從公開資訊觀測站，下載其英文永續報告書      
   程式碼可參考[web_crawer_for_ESGreports.py](web_crawer_for_ESGreports.py)，以下載110年永續報告書為例       
   
2. **分別計算各永續報告書的語調分數(Tone)--使用FinBERT情緒分類模型 & FinBERT主題分類模型**        
   (1) 整理公司股票代碼：將代碼都存在list中      
   (2) 安裝FinBERT兩大模型、nltk tokenizer      
   (3) 逐一擷取PDF文字       
   (4) 文字前處理：保留英文字母大小寫、正常標點符號，其他以空白取代           
   (5) nltk斷句        
   (6) FinBERT：同時檢查不得超過512張量，超過者斷成兩句             
   (7) 紀錄結果：使用pandas套件，將結果存成dataframe格式                
   程式碼可參考           
   107年至110年之各公司永續報告書語調分數(Tone)結果，可參考[Tone_breakdown.xlsx](Tone_breakdown.xlsx)


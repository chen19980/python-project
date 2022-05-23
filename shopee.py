from selenium import webdriver
import json
import requests

chromedriver = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome("chromedriver")
driver.get("https://www.trivago.com.tw/zh-Hant-TW/srl/%E9%A3%AF%E5%BA%97-%E6%BE%8E%E6%B9%96-%E5%8F%B0%E7%81%A3?search=200-389188;dr-20220429-20220430")
driver.maximize_window()


payload = json.loads('{"operationName":"accommodationSearchQuery","variables":{"shouldIncludeFreeWiFiStatus":false,"shouldIncludeBudgetFriendlyBadge":false,"shouldIncludeForwarderClickoutUrl":false,"pollData":null,"params":{"uiv":[{"nsid":{"ns":200,"id":389188}}],"priceRateAttributes":[],"tid":"207e7faae5498a5d3010f6a0d1","stayPeriod":{"arrival":"2022-04-25","departure":"2022-04-26"},"language":"zh-Hant-TW","platform":"tw","limit":25,"dealsLimit":3,"offset":0,"rooms":[{"adults":2,"children":[]}],"sorting":[{"type":0}],"currency":"TWD","applicationGroup":"MAIN_WARP","minPricePerNight":0,"priceTypeRestrictions":[1],"includePriceHistogram":true,"channel":{"branded":{"isStandardDate":false,"stayPeriodSource":{"value":40}}},"deviceType":"DESKTOP_CHROME"},"priceSliderParams":{"currency":"TWD","priceHistogramAlgorithmType":"EXPONENTIAL"}},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"f2b01e56079b32eca578927e3167c4524948402df3b01ea37b7b022cac8e0ba7"}}}')
res=requests.post("https://www.trivago.com.tw/graphql?accommodationSearchQuery",json = payload)


jd=json.loads(res.content.decode(encoding='utf8'))
print(jd)

# for x in range(10):
#     a = jd["data"]["accommodationSearchResponse"]["accommodations"][x] #商品名稱
#     # b = float(jd["data"]["items"][x]["discount"]) #折扣
#     # c = int((jd["data"]["items"][x]["price_before_discount"])/100000)
#     # d = int((c*b)/10)
#     # print(f"{a},{b},{c},{d}")
#     print(a)
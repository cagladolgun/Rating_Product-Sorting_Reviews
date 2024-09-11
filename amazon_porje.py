# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:51:09 2024

@author: oem
"""

import pandas as pd
pd.set_option("display.max_columns", None)
df = pd.read_csv("C:/Users/oem/Desktop/amazon_review.csv")
# Ürünün ortalama puanını hesaplayınız
df["overall"].mean()
df.head()
df.describe().T
# Tarihe göre ağırlıklı puan ortalamasını hesaplayınız
df.loc[df["day_diff"] <= df["day_diff"].quantile(0.25), "overall"].mean() #4.695
df.loc[(df["day_diff"] > df["day_diff"].quantile(0.25)) & (df["day_diff"] <= df["day_diff"].quantile(0.50)) , "overall"].mean() #4.636
df.loc[(df["day_diff"] > df["day_diff"].quantile(0.50)) & (df["day_diff"] <= df["day_diff"].quantile(0.75)) , "overall"].mean() #4.571
df.loc[df["day_diff"] > df["day_diff"].quantile(0.75), "overall"].mean() #4.446
df.head()
#Ağırlıklandırılmış puanlamada her bir zaman diliminin ortalamasını karşılaştırıp yorumlayınız
def time_based_weighted_average(dataframe, w1=28, w2=26, w3=24, w4=22):
    return dataframe.loc[dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.25), "overall"].mean() * w1 / 100 + \
           dataframe.loc[(dataframe["day_diff"] > dataframe["day_diff"].quantile(0.25)) & (dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.50)), "overall"].mean() * w2 / 100 + \
           dataframe.loc[(dataframe["day_diff"] > dataframe["day_diff"].quantile(0.50)) & (dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.75)), "overall"].mean() * w3 / 100 + \
           dataframe.loc[(dataframe["day_diff"] > dataframe["day_diff"].quantile(0.75)), "overall"].mean() * w4 / 100
time_based_weighted_average(df, w1=28, w2=26, w3=24, w4=22)  #4.595 
df["overall"].mean() #4.587
#helpful_no değişkenini üretiniz.
# Not:
# total_vote bir yoruma verilen toplam up-down sayısıdır.
# up, helpful demektir.
# veri setinde helpful_no değişkeni yoktur, var olan değişkenler üzerinden üretilmesi gerekmektedir.
df["helpful_no"] = df["total_vote"] - df["helpful_yes"]
df = df[["reviewerName", "overall", "summary", "helpful_yes", "helpful_no", "total_vote", "reviewTime"]]
df.head()
#score_pos_neg_diff, score_average_rating ve wilson_lower_bound Skorlarını Hesaplayıp Veriye Ekleyiniz
def wilson_lower_bound(up, down, confidence=0.95):
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)
def score_up_down_diff(up, down):
    return up - down
def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)

df["score_pos_neg_diff"] = df.apply(lambda x: score_up_down_diff(x["helpful_yes"], x["helpful_no"]), axis=1)
df.sort_values("score_pos_neg_diff", ascending=False).head(20)

# score_average_rating
df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)
df.sort_values("score_average_rating", ascending=False).head(20)

# wilson_lower_bound
df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)
df.sort_values("wilson_lower_bound", ascending=False).head(20)

##################################################
# Adım 3. 20 Yorumu Belirleyiniz ve Sonuçları Yorumlayınız.
###################################################

df.sort_values("wilson_lower_bound", ascending=False).head(20) 



# -*- coding: utf-8 -*-
"""
Created on Thu May 14 06:14:30 2020

@author: dell
"""

class stock_market_simulator:
    def __init__(self):
        self.positions = []
        self.holdings = []
    
    
    
    def get_cp(shares):
        #return current price of shares passed
        return None
    
    def fetch_news(self,sim=True):
        #fetch the news from source and return
        if sim:
            #Send some randomly generated news or from a corpus
            news = []
            return news
        
    def get_predictions(self,news_list):
        #Does some calculation and tell which share are gonna go up, which will go 
        #down and which will not affect with some level of confidence
        predictions = []
        return predictions
                
        
    def buy_or_sell(self,pred):
        #This function should sell the losing shares if in positon and invest in 
        #shares with more confidence of rising keeping in mind that loss is not 
        #taken or certain amount of loss is taken which either should be passed as
        # threshold or would be calculated from the confidence
        return None
    
    
    
def __main__():
    session1 = stock_market_simulator()
    while True:
        news_list = session1.fetch_news()
        pred = session1.get_predictions(news_list) 
        #Now use this pred to buy or sell stocks
        session1.buy_or_sell(pred)
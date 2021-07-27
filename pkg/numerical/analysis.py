from datetime import datetime, timedelta
from movingAvg import MovingAvg

'''
NumAnalysis class provides methods to analyze a specific stock using historical data. 
'''
class NumAnalysis:
    def __init__(self,api):
        self.api = api
    
    def IsBuy(self,stockSym):
        # default to check half a year of historical data
        return self.isStockABuy(stockSym,timedelta(6 * 30))


    def IsActive(self) -> str:
        return self.api.get_account().status


    def isStockABuy(self,stockSym,duration):
        today = datetime.today().strftime('%Y-%m-%d')
        fromDate = (datetime.today() - duration).strftime('%Y-%m-%d')
        halfYear = self.api.get_aggs(stockSym,1,"day",fromDate,today).df
        
        return MovingAvg(halfYear.close).WindowSize(30).NeverDropBy(10)
import datetime as dt

'''
현재시간 구하고 
현재시간 10분 이전 시간 
'''
def gettime_gap():
    m_dt = dt.datetime.now()
    gap_dt = dt.timedelta(minutes=10)
    result_dt = m_dt - gap_dt
    strtime = result_dt.strftime("%Y-%m-%d %H:%M:%S")
    print(strtime)
  

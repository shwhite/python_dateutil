import datetime as dt
import datetime

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

#
# Timestamp Convert DateFormat 
#
def timestamp_to_dateformat(timest=1546824863):
    #m_time = datetime.datetime.fromtimestamp(m_time).isoformat()
    # output - 2019-01-07T10:34:23
    m_time = datetime.datetime.fromtimesstamp(timest)
    m_date = m_time.strftime("%Y-%m-%d %H:%M:%S")    
    # output : 2019-01-07 10:34:23

#For retrieving information from google calendar api (구글 캘린더 api 정보 수집을 위해)
from Google import Create_Service
from pprint import pprint


#Authentication Process (인증 과정)
CLIENT_SECRET_FILE='credentials.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar','https://www.googleapis.com/auth/calendar.events.readonly','https://www.googleapis.com/auth/calendar.events']

service= Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)



#구글 캘린더에 있는 모든 일정 사전형으로 반환
def GetEvents(CalendarID): 
    
    # 일정 정보 수집
    events=service.events().list(calendarId=CalendarID).execute()['items']
    
    # 일정이 저장될 사전 생성
    EntireSchedule={}

    
    # 날짜형식에 맞춰 사전에 저장
    for i in events:
        
        try:   #'일정이 date형일때
            
            # 동일한 날짜에 다른 일정이 있을시 일정을 추가해라
            if (i['start']['date'][:10]) in EntireSchedule:
                EntireSchedule[i['start']['date'][:10]].append(i['summary'])
            
            
            # 날짜가 사전에 존재하지 않을시 날짜와 일정을 추가해라 
            else:
                EntireSchedule[i['start']['date'][:10]]=[]
                EntireSchedule[i['start']['date'][:10]].append(i['summary'])

        
        except:  #일정이 'dateTime'형일때

            # 동일한 날짜에 다른 일정이 있을시 일정을 추가해라
            if (i['start']['dateTime'][:10]) in EntireSchedule:
                EntireSchedule[i['start']['dateTime'][:10]].append(i['summary'])
                
            
            # 날짜가 사전에 존재하지 않을시 날짜와 일정을 추가해라 
            else:
                EntireSchedule[i['start']['dateTime'][:10]]=[]
                EntireSchedule[i['start']['dateTime'][:10]].append(i['summary'])
    
    #사전형 일정 반환
    return EntireSchedule



print(GetEvents("primary"))



#반복되는 일정 확인
def CheckRecurrence(schedule):
        try:
            if ("MONTHLY" in schedule['recurrence'][0][10:]):
                return "MONTHLY"
                
            elif ("YEARLY" in schedule['recurrence'][0][10:]):
                return "YEARLY" 
            
            elif ("DAILY" in schedule['recurrence'][0][10:]):
                return "DAILY" 
            
            
        except (KeyError):
            pass
        
        


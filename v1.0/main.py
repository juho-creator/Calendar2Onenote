#구글 캘린더 정보 수집
from OAuth import *

#프로그램 자동으로 열기
from subprocess import *


# 키보드&미우스 자동화
import pyautogui
import pyperclip


#시간 지연
import time




# 달력 알고리즘을 위한 월&요일 기본설정
months={'Jan': 1, 'Feb': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'Aug': 8, 'Sept': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
DaysInWeek={'Sun': 0, 'Mon': 1, 'Tues': 2, 'Wed': 3, 'Thurs': 4,'Fri': 5,'Sat': 6}






# '일' 형식을 맞추기 위해 (예 : 1->01, 12->12)
def AddZero(day):
    day=str(day)
    if len(day)==1:
        return f"0{day}"
    else:
        return day

#년월일 형식 반환 (예 :'2022-12-01')
def GetDates(year,month,day):
    return str(year)+"-"+AddZero(month)+"-"+AddZero(day)

#Get Key of an item in dict
def get_key(val):
    for key, value in DaysInWeek.items():
        if val == value:
            return key
 
    return "key doesn't exist"





#윤년 확인  
def IsLeapYear(year):
    return(((year%4==0)&(year%100!=0)) or (year%400==0))

#한 달의 첫 요일 확인
def FirstDayOfMonth(year,month):
    
    weekday=DaysInWeek['Mon']
    
    for i in range(1900,year):
        weekday=(weekday+365)%7
        if (IsLeapYear(i)):
            weekday=(weekday+1)%7

    for i in range(1,month):  
        weekday=(weekday+MonthDays(year,i))%7
        
    if weekday==7:
        weekday=0
    
    return get_key(weekday)


#한 달의 총 날짜 수 계산
def MonthDays(year,month):
    L=[4,6,9,11]
    if(month==2):
        if(IsLeapYear(year)):
            return 29
        return 28
    
    elif(month in L):
        return 30
    
    else:
        return 31




#CONTENT
def WriteOnPage(contents):
    pyautogui.press(['down','down'])
    for content in contents:
        pyautogui.hotkey('ctrl','1')
        pyperclip.copy(content)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('down')



#월 생성    
def CreateMonth(month):
    pyautogui.hotkey('ctrl','t')
    pyperclip.copy(month)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('Enter')



#날짜 생성
def CreateDates(FirstDay,DaysInMonths,year,month):
    
    #특정 달에 있는 모든 요일
    dates=[str(i) for i in range(1,DaysInMonths+1)]
    default=DaysInWeek[FirstDay]

    #날짜&요일 복붙
    for date in dates:
        if (date[-1]=='1'):
            pyperclip.copy(f"{date}st")
            pyautogui.hotkey('ctrl','v')


        elif (date[-1]=='2'):
            pyperclip.copy(f"{date}nd")
            pyautogui.hotkey('ctrl','v')


        elif (date[-1]=='3'):
            pyperclip.copy(f"{date}rd")
            pyautogui.hotkey('ctrl','v')


        else:
            pyperclip.copy(f"{date}th")
            pyautogui.hotkey('ctrl','v')
        
        AddDays(default)  
        if (default==6):
            default=0

        else:
            default+=1
        
        try:
            WriteOnPage(event[GetDates(year,month,date)])        
        except(KeyError):
            pass
        
        pyautogui.hotkey('ctrl','n')

#요일 생성   
def AddDays(default):
        pyperclip.copy(f" ({get_key(default)})")
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('Enter')



#스케쥴 생성
def CreateSchedule(year):
    
    for month in months:
        
        FirstDay=FirstDayOfMonth(year,months[month])
        DaysInMonths=MonthDays(year,months[month])
        
        CreateMonth(month)
        CreateDates(FirstDay,DaysInMonths,year,months[month])






#일정정보 가져오기
event=GetEvents("primary")

# OneNote 열기
Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE")

time.sleep(2)

#Schedule 생성
CreateSchedule(2021)


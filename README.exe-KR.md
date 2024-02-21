[![English](https://img.shields.io/badge/lang-English-blue.svg)](https://github.com/juho-creator/OneNoteSyncScheduler/blob/main/README.exe.md)
</br>
# 원노트 스케줄러

**개요:** OneNote Scheduler는 Google Calendar 일정을 OneNote노트로 생성하는 프로그램입니다.
<br><br>

## 시연 영상
[![시연 영상 시청하기](https://img.youtube.com/vi/kQ-CY51pwEo/0.jpg)](https://www.youtube.com/watch?v=kQ-CY51pwEo)

<!-- 적용 가능한 경우 여기에 데모 콘텐츠 추가 -->
<br><br>

## 사용법

### 처음 사용했을때

1. **다운로드**: [다운로드 링크](https://github.com/juho-creator/OneNoteSyncScheduler/releases)에서 OneNoteScheduler.exe와 Credentials.json를 다운한 후 동일한 폴더에 넣습니다.

2. **실행**: OneNoteScheduler.exe를 두 번 클릭하여 실행합니다.

3. **Microsoft 로그인**: 마이크로소프트 인증 창이 뜨면 자동으로 복사된 코드를 붙여넣고 Microsoft 계정으로 로그인합니다.

4. **OneNote 동기화**: OneNote에 대한 액세스 권한을 부여합니다.

5. **Google 로그인**: 구글 인증 창이 뜨면 Google 계정에 로그인합니다.

6. **Google 캘린더 동기화**: Google 캘린더 이벤트를 가져오기 위한 액세스 권한을 부여합니다.

7. **스케줄 생성**: 원노트로 변환할 년도를 터미널에 입력하여 12개의 월별 섹션으로 구성된 OneNote 노트북을 생성합니다. 이 작업은 5~10분이 소요됩니다.
<br>

### 후속 사용 (이미 로그인한 경우)

1. **실행**: OneNoteScheduler 실행 파일을 두 번 클릭합니다.

2. **스케줄 생성**: 목표 연도를 입력하여 12개의 월별 섹션으로 구성된 OneNote 노트북을 만듭니다. 이벤트는 각 섹션에 날짜별로 자동으로 구성됩니다.
<br><br>


## 인증 및 API 작동원리
### 단계 1. Google OAuth2.0 및 Google Calendar API (G_OAuth.py)
- **문서**: [Google OAuth2.0 문서](https://developers.google.com/workspace/guides/auth-overview?hl=ko), [Google Calendar API 문서](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
<br>![Google OAuth2.0 플로우 다이어그램](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/26717732-7e98-4da7-b845-eebff57423e6)

- **과정**:
  - Google OAuth2.0은 사용자 자격 증명 없이 Google 계정 사용자를 인증합니다. (**token.json** 사용)
  - 사용자가 Google Calendar 일정 액세스를 허용하면 OneNoteScheduler는 Google Calendar API를 이용해 구글 캘린더 일정을 가져올 수 있습니다. <br><br><br><br>






### 단계 2. Microsoft OAuth2.0 및 Microsoft Graph API (M_OAuth.py, OneNote.py)
- **문서**: [Microsoft 계정 인증 및 Microsoft Graph API 문서](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-authentication-flows)
<br>![Microsoft 계정 인증 및 Microsoft Graph API 플로우 다이어그램](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/e1df5d9b-e7e4-4e8f-8bba-fb4b8e718fab)

- **과정**:
  - Microsoft OAuth2.0인증을 통해 사용자 아이디 및 비밀번호를 OneNoteScheduler에 유출하지 않고 Microsoft(Onenote) 계정을 인증합니다. (**api_token_access.json** 사용)
  - 사용자가 Onenote 액세스를 허용하면 OneNoteScheduler는 Onenote 노트북을 만들 수 있는 권한이 부여됩니다.
  - OneNoteScheduler는 Microsoft Graph API를 이용해 OneNote를 생성할 권한이 부여됩니다.<br><br><br><br>
    


### 단계 3. OneNote API 개발 스택 <br>
- **문서**: [OneNote REST API 문서](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0) <br>
![이미지](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/df597c54-752f-44ed-9967-abe356bb24c2)
- 인증 및 권한 부여를 한 후 OneNoteScheduler는 Microsoft Graph API의 일부인 Onenote API를 사용하여 구글 캘린더 일정을 OneNote 노트북으로 생성합니다. <br>
<br><br>

## 사용된 기술
  
- **Google Calendar API**: 
  - **문서**: [Google Calendar API](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
  - **모듈**: `G_OAuth.py`
  - **기능**: 사용자 캘린더 이벤트를 가져오기 위해 Google 계정을 인증합니다.
  
- **Microsoft Authentication Library (MSAL)**: 
  - **문서**: [Microsoft Authentication Library (MSAL)](https://github.com/AzureAD/microsoft-authentication-library-for-python)
  - **모듈**: `M_OAuth.py`
  - **기능**: Onenote 사용을 위해 Microsoft 계정을 인증합니다.


  
- **Microsoft Graph API**: 
  - **튜토리얼**: [Microsoft Graph API](https://www.youtube.com/watch?v=AjOfAQCZsJU&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx&index=2)
  - **모듈**: `OneNote.py`
  - **기능**: Google 캘린더 이벤트를 OneNote 노트북으로 생성합니다.

<br><br>
## 참고문헌

### Google API 시작하기
- 비디오 튜토리얼: [여기에서 시청](https://www.youtube.com/watch?v=I5ili_1G0Vk)

### Google Calendar API
- 튜토리얼 시리즈: [여기에서 시청](https://www.youtube.com/watch?v=1JkKtGFnua8&list=PL3JVwFmb_BnTO_sppfTh3VkPhfDWRY5on)
- 문서: [여기에서 읽기](https://developers.google.com/calendar/api/quickstart/python)

### Microsoft Azure
- 튜토리얼 시리즈: [여기에서 시청](https://www.youtube.com/watch?v=BErur8WwAsg&list=PL3JVwFmb_BnQ8zwvN4OmP-fYpwJXg47Z6)

### Microsoft Graph API
- 튜토리얼 시리즈: [여기에서 시청](https://www.youtube.com/watch?v=7ywUs54eGBo&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx)

### Microsoft Graph Explorer를 사용한 Onenote API 테스트
- 튜토리얼: [여기에서 시청](https://www.youtube.com/watch?v=VXd4OeQU1ek)

### Onenote API 문서
- [자세히 알아보기](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0)

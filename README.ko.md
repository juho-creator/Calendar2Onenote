# OneNote 스케줄러

**개요:** OneNote 스케줄러는 Google 캘린더 이벤트를 기반으로 OneNote에서 일정을 생성하는 프로그램입니다.
<br><br>

## 데모

[데모 비디오](https://www.youtube.com/watch?v=uWZCjEYZeM4)
<!-- 해당되는 경우 여기에 데모 콘텐츠 추가 -->
<br>

## 사용법

### 처음 사용할 때 설정

1. **다운로드**: [다운로드 링크](https://github.com/juho-creator/OneNoteSyncScheduler/releases)에서 OneNoteScheduler와 Credentials.json을 가져와 동일한 폴더에 넣습니다.

2. **실행**: 다운로드 후, OneNoteScheduler 애플리케이션을 더블 클릭하여 실행합니다.

3. **Microsoft 로그인**: 자동으로 복사된 코드를 붙여넣고 Microsoft 계정으로 로그인합니다.

4. **OneNote 동기화**: OneNote에 대한 액세스를 승인합니다.

5. **Google 로그인**: Google 계정에 로그인합니다.

6. **Google 캘린더 동기화**: Google 캘린더 이벤트를 가져오기 위한 액세스를 승인합니다.

7. **스케줄러 생성**: 목표 연도를 터미널에 입력하여 OneNote 노트북을 생성하고, 이벤트를 날짜별로 자동으로 정리합니다. 이 과정은 5~10분이 소요될 수 있습니다.
<br>

### 다음 사용 (로그인한 경우)

1. **실행**: OneNoteScheduler 실행 파일을 더블 클릭합니다.

2. **스케줄러 생성**: 목표 연도를 입력하여 OneNote 노트북을 12개의 월별 섹션과 함께 생성합니다. 이벤트는 각 섹션 내에서 날짜별로 자동으로 정리됩니다.
<br>

## 인증 및 API 흐름 다이어그램

### Google OAuth2.0 및 Google 캘린더 API (G_OAuth.py)
- **문서**: [Google OAuth2.0 문서](https://developers.google.com/workspace/guides/auth-overview?hl=ko), [Google 캘린더 API 문서](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
<br>![Google OAuth2.0 흐름 다이어그램](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/26717732-7e98-4da7-b845-eebff57423e6)

- **프로세스**:
  - Google OAuth2.0은 사용자가 사용자 자격 증명을 필요로하지 않고 Google 계정 사용자를 인증합니다.
  - 사용자가 Google 캘린더 이벤트에 액세스를 승인하면 OneNoteScheduler(3rd-party 앱)은 Google 캘린더 API를 사용하여 사용자 캘린더 이벤트를 가져올 수 있습니다. <br>

### Microsoft OAuth2.0 및 Microsoft Graph API (M_OAuth.py, OneNote.py)
- **문서**: [Microsoft 계정 인증 및 Microsoft Graph API 문서](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-authentication-flows)
<br>![Microsoft 계정 인증 및 Microsoft Graph API 흐름 다이어그램](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/e1df5d9b-e7e4-4e8f-8bba-fb4b8e718fab)

- **프로세스**:
  - Microsoft OAuth2.0은 사용자가 사용자 자격 증명을 필요로하지 않고 Microsoft(OneNote) 계정 사용자를 인증합니다.
  - 사용자가 OneNote에 액세스를 승인하면 OneNoteScheduler(3rd-party 앱)은 OneNote 노트북을 생성할 수 있습니다. <br>
    
### OneNote API 개발 스택 <br>
- **문서**: [OneNote REST API 문서](https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0) <br>
![이미지](https://github.com/juho-creator/OneNoteSyncScheduler/assets/72856990/df597c54-752f-44ed-9967-abe356bb24c2)
- 인증 및 승인 프로세스 이후에 OneNoteScheduler는 Microsoft Graph API를 통해 OneNote API를 포함한 모든 Google 캘린더 이벤트로 OneNote 페이지를 생성할 준비가 됩니다. <br>

## 사용된 기술

- **Google 캘린더 API**: 
  - **문서**: [Google 캘린더 API](https://developers.google.com/calendar/api/quickstart/python?hl=ko)
  - **모듈**: `G_OAuth.py`
  - **기능**: Google 계정을 인증하고 캘린더 이벤트를 가져옵니다.
  
- **Microsoft Authentication Library (MSAL)**: 
  - **문서**: [Microsoft Authentication Library (MSAL)](https://github.com/AzureAD/microsoft-authentication-library-for-python)
  - **모듈**: `M_OAuth.py`
  - **기능**: Microsoft 계정을 인증합니다.
  
- **Microsoft Graph API**: 
  - **문서**: [Microsoft Graph API](https://www.youtube.com/watch?v=AjOfAQCZsJU&list=PL3JVwFmb_BnT9Ti0MMRj5nPF7XoN-4MQx&index=2)
  - **모듈**: `OneNote.py`
  - **기능**: 캘린더 이벤트와 함께 OneNote 노트북을 생성합니다.
  
  
## 참고

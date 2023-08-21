1학년때 작성한 코드를 2학년이 된 지금 보니 코드 스멜이 너무 많다. 

코드를 아래와 같이 개선을 해봤다: 
1. google_apis.py 제거
2. google.py & oauth.py에서 중복된 코드 제거, 코드를 전반적으로 간결하게 수정함.
3. main.py에 있는 함수를 typer.py에 전부 옮김
4. typer.py 파일에 있는 함수에 모두 주석처리함


코드 사용법을 정리하면 이렇다 :
1. credentials.json 파일을 다운한다
2. OAuth.py를 실행하여 계정인증한.
3. main.py를 실행하여 Onenote파일에 Google Calendar일정을 자동 작성한다.

설명 영상
https://clipchamp.com/watch/TmGLkVQDkGJ

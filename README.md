- venv 설정 내보내기
    ```bash
    $ pip freeze > requirements.txt
    ```
- venv 설정 설치하기
    ```bash
    $ pip install -r requirements.txt
    ```
- 가상환경 활성화
    ```bash
    $ source venv/Scripts/activate
    OR
    $ source venv/bin/activate
    ```
- 가상환경 비활성화
    ```bash
    $ deactivate
    ```
- 로컬 서버 실행
    ```bash
    $ uvicorn app.main:app --reload
    ```
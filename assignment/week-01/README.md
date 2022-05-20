# 1주차 과제


## 과제 설명
1주차 과제는 app.py 파일에 다음 기능을 추가하여서 배포해주세요.
- st.snow()
- https://docs.streamlit.io/library/api-reference/status/st.snow
## 제출 방법
### 1. 로컬환경에서 수정 후 GCP Compute Engine에 배포
- 로컬 환경에서 (학번폴더 안에 있는 상태)
    ```
    git pull
    <수정작업>
    git add .
    git commit -m "Submit assignment 1"ㄴ
    git push origin main
    ```
- 서버에서 (학번폴더 안에 있는 상태)
    ```
    tmux new-session -s server
    git pull
    . venv/bin/activate
    cd assignment/week-01
    streamlit run app.py
    #ctrl+b d로 빠져나오기
    ```


## 질문
### 1. 본인의 Compute Engine 퍼블릭 아이피를 알려주세요
예 : 55.55.55.55:8501

### 2. 기타 코멘트
여기에 작성

## 피드백
이 부분은 강사가 작성하는 부분입니다.
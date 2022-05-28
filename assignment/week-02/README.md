# 2주차 과제


## 과제 설명
2주차 과제는 app.py 파일에 다음 기능을 추가하여서 배포해주세요.
- 현재는 얼굴 인식하는 코드가 들어가 있는 상태입니다. 노트북을 잘 참조하여, 모자이크 처리하는 코드로 바꿔주세요!
- 얼굴이 있는 사진을 넣으면 모자이크 처리를 해서 반환

## 제출 방법
### 1. 로컬환경에서 수정 후 GCP Compute Engine에 배포
- 로컬 환경에서 (학번폴더 안에 있는 상태)
    ```
    git pull
    <수정작업>
    git add .
    git commit -m "Submit assignment 2"
    git push origin main
    ```
- 서버에서 (학번폴더 안에 있는 상태)
    ```
    tmux new-session -s faceapp
    git pull
    . venv/bin/activate
    pip install opencv-python matplotlib
    sudo apt-get install ffmpeg libsm6 libxext6  -y
    cd assignment/week-02
    streamlit run app.py
    #ctrl+b d로 빠져나오기
    ```
    아래 두 명령어는 관련된 패키지를 설치하기 위함입니다. 최초 한번만 실행해주세요!
    ```
    pip install opencv-python
    sudo apt-get install ffmpeg libsm6 libxext6  -y
    ```


## 질문
### 1. 본인의 Compute Engine 퍼블릭 아이피를 알려주세요
예 : 55.55.55.55:8501

### 2. 기타 코멘트
여기에 작성

## 피드백
이 부분은 강사가 작성하는 부분입니다.

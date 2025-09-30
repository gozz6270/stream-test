import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit 요소 예시 페이지")  # 페이지 제목

st.header("기본 텍스트 요소")  # 텍스트 관련 요소
st.write("이것은 일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**마크다운**을 지원합니다.")  # 마크다운 텍스트
st.code("print('Hello, Streamlit!')", language='python')  # 코드 블록

st.header("입력 위젯")  # 입력 관련 요소
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의하십니까?")  # 체크박스
color = st.radio("좋아하는 색상은?", ["빨강", "파랑", "초록"])  # 라디오 버튼
hobby = st.selectbox("취미를 선택하세요", ["독서", "운동", "게임"])  # 셀렉트박스
multi_hobby = st.multiselect("여러 취미를 선택하세요", ["독서", "운동", "게임"])  # 멀티셀렉트
date = st.date_input("날짜를 선택하세요")  # 날짜 입력
time = st.time_input("시간을 선택하세요")  # 시간 입력
file = st.file_uploader("파일을 업로드하세요")  # 파일 업로더
st.button("버튼 클릭")  # 버튼

st.header("슬라이더와 폼")  # 슬라이더 및 폼
value = st.slider("값을 선택하세요", 0, 100, 50)  # 슬라이더
with st.form("my_form"):
    st.write("폼 내부 요소")
    form_text = st.text_input("폼 텍스트 입력")
    submitted = st.form_submit_button("폼 제출")
    if submitted:
        st.write("폼이 제출되었습니다.")

st.header("데이터 표시")  # 데이터프레임 및 테이블
df = pd.DataFrame({
    'A': np.random.randn(5),
    'B': np.random.randn(5)
})
st.dataframe(df)  # 데이터프레임 표시
st.table(df)  # 테이블 표시
st.json({"name": "홍길동", "age": 30})  # JSON 표시

st.header("차트와 시각화")  # 차트 및 그래프
st.line_chart(df)  # 라인 차트
st.bar_chart(df)  # 바 차트
st.area_chart(df)  # 에어리어 차트

st.header("미디어 요소")  # 이미지, 오디오, 비디오
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")  # 이미지
st.audio(np.random.randn(44100), format='audio/wav')  # 오디오 (예시)
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오

st.header("상태 및 알림")  # 상태 표시 및 알림
st.success("성공 메시지입니다!")  # 성공 메시지
st.info("정보 메시지입니다.")  # 정보 메시지
st.warning("경고 메시지입니다.")  # 경고 메시지
st.error("에러 메시지입니다.")  # 에러 메시지
st.exception(Exception("예외 메시지입니다."))  # 예외 메시지

st.header("진행률 및 스피너")  # 진행률 및 스피너
import time
with st.spinner("잠시 기다려주세요..."):
    time.sleep(1)
st.progress(70)  # 진행률 바

st.header("사이드바")  # 사이드바 요소
st.sidebar.title("사이드바 제목")
st.sidebar.write("사이드바에 표시되는 텍스트")
st.sidebar.selectbox("사이드바 셀렉트박스", ["옵션1", "옵션2"])

# 각주: matplotlib을 제거하고 Streamlit 기본 차트 및 시각화 도구만 사용했습니다.

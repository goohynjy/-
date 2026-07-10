import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="환경설계(CPTED) 치안 분석 앱", page_icon="✨", layout="wide")

st.title("✨ 데이터 기반 환경설계(CPTED) 효과 분석 시스템")
st.markdown("---")

st.markdown("""
### 📌 프로젝트 개요
본 애플리케이션은 **국가 통계 데이터(`processed_crime_data.csv`)**를 기반으로, 각 지자체(지역)별 범죄 발생 현황을 진단하고, 
도시의 **방범 시설(CCTV 등)** 및 **조경 면적(녹지 지표)**이 실제 범죄 예방에 미치는 환경설계(CPTED) 효과를 다각도로 분석합니다.

### 📊 분석 데이터 가이드
왼쪽 사이드바의 메뉴를 통해 원하는 분석 페이지로 이동할 수 있습니다.
1. **📌 지역별 범죄 현황 (1_국가별MBTI.py)**: 선택한 지자체의 연도별 범죄 발생 건수 및 인구 10만 명당 범죄율 추이를 시각화합니다.
2. **🌳 환경설계(CPTED) 효과 분석 (2_MBTI비교.py)**: 특정 지역의 조경 면적 및 방범 시설 인프라 수준을 범죄율과 비교하여 환경설계의 실효성을 검증합니다.
""")

st.markdown("---")
st.subheader("📂 원본 데이터 셋 원격 미리보기 (`processed_crime_data.csv`)")

try:
    df = pd.read_csv("processed_crime_data.csv")
    st.dataframe(df.head(10), use_container_width=True)
    st.success("데이터 로드 성공! 왼쪽 메뉴에서 세부 분석을 진행해 보세요.")
except Exception as e:
    st.error(f"데이터 파일을 찾을 수 없거나 오류가 발생했습니다: {e}")

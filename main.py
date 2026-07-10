import streamlit as st
import pandas as pd

st.set_page_config(page_title="CPTED 환경설계 분석 시스템", page_icon="🌳", layout="wide")

st.title("🌳 CPTED 기반 방범시설·조경면적과 범죄율의 상관관계 분석")
st.markdown("---")

st.markdown("""
### 🎯 설정 가설
> **"도시 내 방범용 CCTV 설치 수와 정비된 조경 면적이 많은 지역일수록 인구 대비 범죄율(인구 10만 명당 범죄율)이 낮게 나타날 것이다."**

### 📁 분석 데이터 정보
본 앱은 전처리 단계에서 결합된 `조경면적과 시설이 범죄율이 미치는 상관관계 분석.csv` 공인 공공데이터를 기반으로 작동합니다.
* **인구_10만명당_범죄율**: 지역 간 인구 편차를 제거하여 객관화한 비교 지표
* **CCTV_설치수**: 물리적 감시 장치의 확충 수준
* **조경면적_m2**: 가시성 및 자연적 감시 환경을 반영하는 녹지 환경 지표
""")

st.markdown("---")
st.subheader("📋 통합 데이터셋 원본 확인 (`조경면적과 시설이 범죄율이 미치는 상관관계 분석.csv`)")

try:
    df = pd.read_csv("조경면적과 시설이 범죄율이 미치는 상관관계 분석.csv")
    st.dataframe(df, use_container_width=True)
    st.success(f"🎯 총 {len(df)}개의 지역 데이터셋이 성공적으로 연결되었습니다. 왼쪽 메뉴로 이동해 가설을 검증해 보세요!")
except Exception as e:
    st.error(f"데이터 파일을 읽는 도중 오류가 발생했습니다. 파일명과 경로를 확인해 주세요: {e}")

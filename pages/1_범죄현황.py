import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 깨짐 방지 설정 (안전한 설정)
plt.rcParams['font.family'] = 'Malgun Gothic' # 윈도우 기준 (맥은 AppleGothic)
plt.rcParams['axes.unicode_minus'] = False

st.title("📌 지역별 범죄 발생 및 치안 현황 조회")
st.markdown("---")

try:
    df = pd.read_csv("processed_crime_data.csv")
    
    # 지역 선택 사이드바/셀렉트박스
    available_regions = sorted(df['지역'].unique())
    selected_region = st.selectbox("조회할 지역(지자체)을 선택하세요:", available_regions)
    
    # 선택된 지역 데이터 필터링
    region_df = df[df['지역'] == selected_region].sort_values('연도')
    
    st.subheader(f"📊 {selected_region} 지역 범죄 데이터 상세 현황")
    st.dataframe(region_df, use_container_width=True)
    
    # 시각화 차트 영역
    st.markdown("### 📈 연도별 범죄 추이 차트")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**인구 10만 명당 범죄 발생 건수 추이**")
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.lineplot(data=region_df, x='연도', y='A/Bⅹ100,000 (건/10만명)', marker='o', color='crimson', ax=ax1)
        ax1.set_title(f"{selected_region} 인구 대비 범죄율 변화")
        st.pyplot(fig1)
        
    with col2:
        st.write("**전체 범죄 발생 총건수 추이**")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.barplot(data=region_df, x='연도', y='범죄발생총건수(A) (건)', color='skyblue', ax=ax2)
        ax2.set_title(f"{selected_region} 총 범죄 발생량 변화")
        st.pyplot(fig2)

except Exception as e:
    st.error(f"데이터 로드 중 오류 발생: {e}")

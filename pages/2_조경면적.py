import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("🌳 환경설계(CPTED) 요인별 범죄율 비교 분석")
st.markdown("---")

try:
    df = pd.read_csv("processed_crime_data.csv")
    
    # 최신 연도 데이터만 추출하여 분석 기준 삼기
    latest_year = df['연도'].max()
    df_latest = df[df['연도'] == latest_year].copy()
    
    st.markdown(f"ℹ️ 현재 분석은 최신 공인 통계 데이터 기준 연도(**{latest_year}년**) 데이터로 가동됩니다.")
    
    # 💡 [중요] 아직 방범시설 및 조경 데이터가 매칭되기 전이므로, 분석용 가상 데이터(Mock) 생성 결합
    # 실제 데이터를 구하시면 이 부분을 실제 csv 병합 코드로 대체하시면 됩니다.
    np.random.seed(42)
    df_latest['방범시설_인프라(CCTV대수)'] = np.random.randint(500, 3000, size=len(df_latest))
    df_latest['도시_조경면적(녹지비율%)'] = np.random.uniform(10.0, 45.0, size=len(df_latest))
    
    # 멀티 셀렉트로 비교할 특정 지역들 선택하기
    all_regions = list(df_latest['지역'].unique())
    selected_regions = st.multiselect(
        "비교 분석할 특정 지역들을 선택하세요 (여러 개 선택 가능):", 
        all_regions, 
        default=['서울', '경기', '부산', '대구', '인천']
    )
    
    # 필터링 데이터
    compare_df = df_latest[df_latest['지역'].isin(selected_regions)]
    
    st.subheader("📋 선택 지역의 치안 인프라 vs 범죄율 데이터셋")
    st.dataframe(compare_df[['지역', 'A/Bⅹ100,000 (건/10만명)', '방범시설_인프라(CCTV대수)', '도시_조경면적(녹지비율%)']], use_container_width=True)
    
    # 셉테드 환경설계 분석 시각화
    st.markdown("### 🎯 환경설계(CPTED) 상관관계 산점도 분석")
    st.info("💡 **가설 검증**: 방범 시설 인프라가 높고 조경 배치가 균형 잡힌 지역일수록 인구 대비 범죄율이 낮게 나타나는지 검증합니다.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**1) 방범시설(CCTV 대수)과 범죄율의 상관관계**")
        fig1, ax1 = plt.subplots(figsize=(6, 5))
        sns.regplot(data=compare_df, x='방범시설_인프라(CCTV대수)', y='A/Bⅹ100,000 (건/10만명)', ax=ax1, color='blue')
        # 점 옆에 지역 이름 라벨링
        for i, txt in enumerate(compare_df['지역']):
            ax1.annotate(txt, (compare_df['방범시설_인프라(CCTV대수)'].iloc[i], compare_df['A/Bⅹ100,000 (건/10만명)'].iloc[i]), fontsize=9)
        st.pyplot(fig1)
        
    with col2:
        st.write("**2) 도시 조경면적(녹지비율)과 범죄율의 상관관계**")
        fig2, ax2 = plt.subplots(figsize=(6, 5))
        sns.regplot(data=compare_df, x='도시_조경면적(녹지비율%)', y='A/Bⅹ100,000 (건/10만명)', ax=ax2, color='green')
        for i, txt in enumerate(compare_df['지역']):
            ax2.annotate(txt, (compare_df['도시_조경면적(녹지비율%)'].iloc[i], compare_df['A/Bⅹ100,000 (건/10만명)'].iloc[i]), fontsize=9)
        st.pyplot(fig2)
        
    st.markdown("""
    ### 📝 분석 결론 가이드 (생기부 작성 팁)
    - 산점도 우하향 회귀선 기울기가 나타난다면 **"방범 시설 확충 및 쾌적한 도시 조경 환경 조성이 주민 감시 효과를 높여 실제 범죄 유발율을 낮추는 환경설계(CPTED) 효과가 유의미함"**을 통계적으로 입증할 수 있습니다.
    """)

except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")

# -*- coding:utf-8 -*-
import streamlit as st
from PIL import Image
def run_home():
    st.markdown("## 갤럽 데이터 수집\n ")
    st.markdown(
                    "\n #### ◆ 데이터 수집 \n ##### - <span style = 'color:#585858'>2020년 1월 2째주 ~ 2022년 12월 3째주</span> \n"
                    "####  ◆ 날짜 \n ##### - <span style = 'color:#585858'>연도, 월, 주</span> \n"
                    "####  ◆ 정당 \n ##### - <span style='color:red'>국민의힘</span> / <span style='color:blue'>더불어민주당</span> / <span style='color:#F1C40F'>정의당</span> / <span style='color:gray'>무당층(기타 정당과 부동층을 포함)</span>\n "
                                       
                    "####  ◆ 지역 \n ##### - <span style = 'color:#585858'>서울, 인천/경기, 대전/세종/충청, 광주/전라, 대구/경북, 부산/울산</span> \n"
                    "#### ◆ 성별 \n ##### - <span style = 'color:#585858'>남자, 여자</span>\n"
                    "####  ◆ 연령  \n ##### - <span style = 'color:#585858'>10대~30대<span>\n"
                    "####  ◆ 웹싸이트 : <a href='https://www.gallup.co.kr/' style='color:blue'>https://www.gallup.co.kr/</a>",
                    unsafe_allow_html=True)
    st.markdown("")
    st.markdown("## ◆ 사용 Tool")
    col4, col5, col6 = st.columns(3)
    with col4:
        img4 = Image.open('image/4.png')
        st.image(img4)
    with col5:
        img5 = Image.open('image/5.png')
        st.image(img5)
    with col6:
        img6 = Image.open('image/6.png')
        st.image(img6)
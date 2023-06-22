# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu

import matplotlib.pyplot as plt
from gallup import run_gallup
from election import run_election
from PIL import Image

import base64
from pathlib import Path
from home import run_home
from home1 import run_home1


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' width='50' height='50'>".format(
      img_to_bytes(img_path)
    )
    return img_html

def main():
    with st.sidebar:
        selected = option_menu("대시보드 메뉴", ['홈', '갤럽여론조사', '20대 대통령선거'],
                               icons=['house', 'file-bar-graph', 'graph-up-arrow'], menu_icon="cast", default_index=0)
    if selected == "홈":
        # st.markdown("<h1 style='text-align: left; color: black;'>대통령 선거 데이터 분석</h1>", unsafe_allow_html=True)
        #
        # st.markdown("<h2 style='text-align: left; color: gray;'>10-30대는 어떻게 움직였는가? </h2>"
        #             "<p style='text-align: left; color: grey;'>"+img_to_html('img/figure01.png')+"</p>",
        #             unsafe_allow_html=True)
        # st.markdown(
        #     "Member|Skills|GitHub & Blog \n |:--:|:--:|:--:| \n | 김미나 |분석 & 기획|  https://github.com/180pp   \n |권용석|분석 & 대시보드| https://github.com/MaestroYongseok  | \n |주강희|대시보드& PPT|  https://blog.naver.com/wnrkdgml10|")
        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     img1 = Image.open('image/1.jpg').resize((150,120))
        #     st.image(img1)
        # with col2:
        #     img2 = Image.open('image/2.jpg').resize((150,120))
        #     st.image(img2)
        #
        # with col3:
        #     img3 = Image.open('image/3.jpg').resize((150,120))
        #     st.image(img3)
        # st.write('')
        # st.write('')
        #
        # st.write('')
        # st.write('')


        run_home1()


    elif selected == "갤럽여론조사":
        run_gallup()
    elif selected == "20대 대통령선거":
        run_election()
    else:
        print("error...")

if __name__ == "__main__":
    main()
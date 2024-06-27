import streamlit as st
import pandas as pd
import numpy as np
import graphviz
import pydeck as pdk

with st.sidebar:
    st.header('main menu')
# 代码块
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')



df = pd.read_csv('data/test.csv')
# 表格
# st.table(df)
edited_df = st.data_editor(df)
favorite_command = edited_df.loc[edited_df["green_gen_actual"].idxmax()]["target_datetime"]
st.markdown(f"Max green_gen_actual is **{favorite_command}** ")
# 折线图
st.line_chart(edited_df, x='target_datetime', y='green_gen_actual')

# 地图
df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 35.74,
    "col2": np.random.randn(1000) / 50 + 139.67,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
})

st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [35.74, 139.67],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=35.74,
        longitude=139.67,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

st.graphviz_chart('''
    digraph {
        开始->问候并提示使用菜单或直接提问->提问
        提问->回答并询问是否有帮助
        回答并询问是否有帮助->是
        回答并询问是否有帮助->否
        是->询问接下来做什么提示返回菜单且可以继续提问->提问
        否->表达歉意并提示联系支持菜单且可以继续提问->提问
    }
''')



video_file = open('data/star.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


import streamlit as st
import os
from PIL import Image
import pytesseract

def image_to_words(image_path):
    image = Image.open(image_path)
    words = pytesseract.image_to_string(image, 'chi_sim')
    return words

def save_words(save_path, words):
    f = open(save_path, 'w')
    f.write(words)
    f.close()

# 输入图像路径的交互组件
image_path = st.text_input("请输入图像路径：")

# 输入保存路径的交互组件
save_path = st.text_input("请输入保存路径：")

if st.button("转换并保存"):
    words = image_to_words(image_path)
    st.write(words)  # 在这里添加直接显示识别的结果

st.write("转换完成！")

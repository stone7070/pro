import streamlit as st
import re

st.title("AI 글 판별기 (베타)")

text = st.text_area("아래에 판별하고 싶은 글을 붙여넣어 주세요:")

if st.button("판별하기"):
    if len(text) < 100:
        st.warning("글자 수가 너무 적습니다. 더 긴 문장을 입력해 주세요.")
    else:
        ai_pattern = ["as an AI", "I am an AI", "my training data", "as a language model"]
        score = sum(1 for p in ai_pattern if p.lower() in text.lower())
        
        words = re.findall(r'\w+', text.lower())
        word_repeats = len(words) - len(set(words))
        
        if score > 0 or word_repeats > len(words) * 0.3:
            st.error("AI가 작성했을 가능성이 높습니다.")
        else:
            st.success("사람이 쓴 글일 가능성이 높습니다.")

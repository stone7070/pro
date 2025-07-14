import streamlit as st
import re

st.title("AI 글 판별기 (한글/영어 지원 베타)")

text = st.text_area("아래에 판별하고 싶은 글을 붙여넣어 주세요:")

if st.button("판별하기"):
    if len(text) < 100:
        st.warning("글자 수가 너무 적습니다. 더 긴 글을 입력해 주세요.")
    else:
        score = 0  # 점수 누적

        # ✅ 영어 AI 특징 문구
        ai_phrases_en = ["as an AI", "I am an AI", "my training data", "as a language model"]
        if any(p.lower() in text.lower() for p in ai_phrases_en):
            score += 1

        # ✅ 한글 AI 스타일 문구 (AI가 자주 쓰는 표현)
        ai_phrases_kr = [
            "따라서", "이러한", "그러한", "본 프로젝트는", "의의가 있습니다",
            "점점 중요해지고 있습니다", "다양한 분야에서 활용되고 있습니다"
        ]
        if any(p in text for p in ai_phrases_kr):
            score += 1

        # ✅ 문장 길이 (AI는 길고 딱딱한 문장 선호)
        sentences = re.split(r'[.!?。？！\n]', text)
        valid_sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
        avg_len = sum(len(s.split()) for s in valid_sentences) / len(valid_sentences)
        if avg_len > 20:
            score += 1

        # ✅ 단어 반복률
        words = re.findall(r'\w+', text.lower())
        word_repeats = len(words) - len(set(words))
        if word_repeats > len(words) * 0.3:
            score += 1

        # ✅ 최종 판별
        if score >= 2:
            st.error("⚠️ AI가 작성했을 가능성이 높습니다.")
        elif score == 1:
            st.warning("🤔 AI일 수도 있고, 아닐 수도 있습니다.")
        else:
            st.success("✅ 사람이 쓴 글일 가능성이 높습니다.")

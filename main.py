
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Fanpage Growth Assistant",
    page_icon="📈",
    layout="wide"
)

st.title("📈 FANPAGE GROWTH ASSISTANT")
st.caption("Công cụ quản lý và tăng trưởng Fanpage Facebook")

# Sidebar
st.sidebar.header("⚙️ Quản lý Fanpage")
page_name = st.sidebar.text_input(
    "Tên Fanpage",
    "Fanpage của tôi"
)

# Dashboard
st.subheader("📊 Tổng quan Fanpage")

col1, col2, col3 = st.columns(3)

with col1:
    likes = st.number_input(
        "Tổng lượt thích",
        min_value=0,
        value=1000
    )

with col2:
    followers = st.number_input(
        "Người theo dõi",
        min_value=0,
        value=1200
    )

with col3:
    posts = st.number_input(
        "Số bài đăng",
        min_value=0,
        value=50
    )

st.divider()

# Lưu dữ liệu
st.subheader("📈 Theo dõi tăng trưởng")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Lưu thống kê hôm nay"):
    st.session_state.history.append({
        "Ngày": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "Likes": likes,
        "Followers": followers,
        "Posts": posts
    })
    st.success("Đã lưu thống kê!")

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.line_chart(
        df.set_index("Ngày")[["Likes", "Followers"]]
    )
    st.dataframe(df, use_container_width=True)

st.divider()

# Gợi ý nội dung
st.subheader("💡 Gợi ý bài viết")

topic = st.text_input(
    "Nhập chủ đề muốn đăng bài"
)

if st.button("Tạo ý tưởng bài viết"):
    if topic:
        st.success(
            f"Ý tưởng: Chia sẻ 3 điều hữu ích về {topic}, "
            "kèm hình ảnh hấp dẫn và câu hỏi cuối bài "
            "để khuyến khích người đọc bình luận."
        )
    else:
        st.warning("Bạn hãy nhập chủ đề trước!")

st.divider()

# Link Fanpage
st.subheader("🔗 Fanpage của bạn")

url = st.text_input(
    "Link Fanpage Facebook"
)

if st.button("Mở Fanpage"):
    if url.startswith("https://"):
        st.link_button("Truy cập Fanpage", url)
    else:
        st.error("Vui lòng nhập link hợp lệ!")

st.caption("Fanpage Growth Assistant | Version 1.0")

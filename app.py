import streamlit as st

# Cấu hình trang web app
st.set_page_config(page_title="App Tính Thuế TNCN", page_icon="💰", layout="centered")

st.title("💰 Ứng dụng Tính Thuế TNCN")
st.write("Áp dụng biểu thuế lũy tiến từng phần mới nhất tại Việt Nam.")
st.markdown("---")

# Hàm tính thuế
def tinh_thue_tncn(thu_nhap, so_nguoi_pt=0, bao_hiem=0):
    # Giảm trừ bản thân (11tr) và người phụ thuộc (4.4tr/người)
    tntt = thu_nhap - 11000000 - (so_nguoi_pt * 4400000) - bao_hiem
    if tntt <= 0: 
        return 0, 0
    
    # Tính thuế rút gọn
    if tntt <= 5000000:   thue = tntt * 0.05
    elif tntt <= 10000000:  thue = tntt * 0.10 - 250000
    elif tntt <= 18000000:  thue = tntt * 0.15 - 750000
    elif tntt <= 32000000:  thue = tntt * 0.20 - 1650000
    elif tntt <= 52000000:  thue = tntt * 0.25 - 3250000
    elif tntt <= 80000000:  thue = tntt * 0.30 - 5850000
    else:                  thue = tntt * 0.35 - 9850000
    return tntt, round(thue)

# Giao diện nhập liệu trên App
thu_nhap = st.number_input("Tổng thu nhập tháng (VND):", min_value=0, value=25000000, step=1000000)
so_nguoi_pt = st.number_input("Số người phụ thuộc:", min_value=0, value=0, step=1)
bao_hiem = st.number_input("Tiền bảo hiểm bắt buộc (VND) - nếu có:", min_value=0, value=0, step=100000)

st.markdown("---")

# Nút tính toán và xuất kết quả
if st.button("Tính Thuế Ngay", type="primary"):
    tntt, thue_nop = tinh_thue_tncn(thu_nhap, so_nguoi_pt, bao_hiem)
    
    # Hiển thị kết quả dạng thẻ (Card) trực quan
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Thu nhập tính thuế", value=f"{tntt:,.0f} VND")
    with col2:
        if thue_nop > 0:
            st.metric(label="Thuế TNCN phải nộp", value=f"{thue_nop:,.0f} VND", delta="- Thuế", delta_color="inverse")
        else:
            st.success("Bạn không phải nộp thuế TNCN!")

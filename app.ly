import streamlit as st

# 1. Cấu hình tiêu đề ứng dụng (như trong ảnh Screenshot_2026-06-20-06-07-27-12_cd9f342f505fc08af23d5639700d5c03.jpg)
st.title("💵 Ứng dụng tính Thuế Thu nhập cá nhân - Trinh")

# 2. Tạo các ô nhập liệu bằng số (number_input)
thu_nhap = st.number_input(
    "Nhập thu nhập hàng tháng (triệu đồng)", min_value=0.0, value=20.0, step=0.5
)
nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc", min_value=0, value=0, step=1
)

# Hàm logic tính thuế TNCN căn bản


def tinh_thue_tncn(thu_nhap_trieu, so_nguoi_pt):
    # Quy đổi ra đồng để tính cho chuẩn
    thu_nhap_dong = thu_nhap_trieu * 1_000_000
    giam_tru_ban_than = 11_000_000
    giam_tru_phu_thuoc = so_nguoi_pt * 4_400_000

    # Thu nhập tính thuế
    tn_tinh_thue = thu_nhap_dong - giam_tru_ban_than - giam_tru_phu_thuoc

    if tn_tinh_thue <= 0:
        return 0

    # Tính thuế theo lũy tiến từng phần
    thue = 0
    if tn_tinh_thue <= 5_000_000:
        thue = tn_tinh_thue * 0.05
    elif tn_tinh_thue <= 10_000_000:
        thue = tn_tinh_thue * 0.1 - 250_000
    elif tn_tinh_thue <= 18_000_000:
        thue = tn_tinh_thue * 0.15 - 750_000
    elif tn_tinh_thue <= 32_000_000:
        thue = tn_tinh_thue * 0.2 - 1_650_000
    elif tn_tinh_thue <= 52_000_000:
        thue = tn_tinh_thue * 0.25 - 3_250_000
    elif tn_tinh_thue <= 80_000_000:
        thue = tn_tinh_thue * 0.3 - 5_850_000
    else:
        thue = tn_tinh_thue * 0.35 - 9_850_000

    return thue / 1_000_000  # Trả về đơn vị triệu đồng


# 3. Tạo nút bấm "Tính thuế"
if st.button("Tính thuế"):
    thue_phai_nop = tinh_thue_tncn(thu_nhap, nguoi_phu_thuoc)
    st.success(f"Số thuế TNCN dự kiến phải nộp: {thue_phai_nop:.3f} triệu đồng")
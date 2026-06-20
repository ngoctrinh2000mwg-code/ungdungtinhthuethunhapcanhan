def tinh_thue_tncn(thu_nhap, so_nguoi_pt=0, bao_hiem=0):
    # Tính thu nhập tính thuế sau khi giảm trừ bản thân (11tr) và người phụ thuộc (4.4tr/người)
    tntt = thu_nhap - 11000000 - (so_nguoi_pt * 4400000) - bao_hiem
    if tntt <= 0: return 0
    
    # Tính thuế lũy tiến theo công thức rút gọn của Tổng cục Thuế
    if tntt <= 5000000:   return tntt * 0.05
    if tntt <= 10000000:  return tntt * 0.10 - 250000
    if tntt <= 18000000:  return tntt * 0.15 - 750000
    if tntt <= 32000000:  return tntt * 0.20 - 1650000
    if tntt <= 52000000:  return tntt * 0.25 - 3250000
    if tntt <= 80000000:  return tntt * 0.30 - 5850000
    return tntt * 0.35 - 9850000

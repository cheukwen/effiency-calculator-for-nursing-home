import streamlit as st
from efficiency import calculate_bed_efficiency, calculate_area_efficiency, calculate_staff_efficiency

# 页面标题
st.title("Nursing Home Efficiency Calculator")

# 输入框和计算按钮
bed_area = st.number_input("Enter the total bed area (m²):", min_value=1)
bed_count = st.number_input("Enter the number of beds:", min_value=1)
staff_count = st.number_input("Enter the number of staff:", min_value=1)

if st.button("Calculate"):
    bed_eff = calculate_bed_efficiency(bed_area, bed_count)
    area_eff = calculate_area_efficiency(bed_area, bed_count)
    staff_eff = calculate_staff_efficiency(bed_area, staff_count)

    # 显示结果
    st.write(f"Bed Efficiency: {bed_eff}元/床")
    st.write(f"Area Efficiency: {area_eff}元/㎡")
    st.write(f"Staff Efficiency: {staff_eff}元/人")

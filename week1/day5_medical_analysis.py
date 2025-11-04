#!/usr/bin/env python3
"""
医学数据分析工具
循环与列表应用
"""

# 样本医疗数据
blood_pressures_systolic = [120, 135, 110, 145, 130, 125]  # 收缩压
blood_pressures_diastolic = [80, 85, 75, 95, 82, 78]       # 舒张压

def analyze_blood_pressure():
    """分析血压数据"""
    print("=== 血压数据分析 ===")
    
    high_bp_count = 0
    normal_bp_count = 0
    
    for i in range(len(blood_pressures_systolic)):
        systolic = blood_pressures_systolic[i]
        diastolic = blood_pressures_diastolic[i]
        
        print(f"样本{i+1}: {systolic}/{diastolic} mmHg", end=" - ")
        
        if systolic > 140 or diastolic > 90:
            print("高血压")
            high_bp_count += 1
        else:
            print("正常")
            normal_bp_count += 1
    
    print(f"\n统计结果:")
    print(f"高血压样本: {high_bp_count}个")
    print(f"正常血压样本: {normal_bp_count}个")
    print(f"高血压比例: {high_bp_count/len(blood_pressures_systolic)*100:.1f}%")

def calculate_averages():
    """计算平均值"""
    avg_systolic = sum(blood_pressures_systolic) / len(blood_pressures_systolic)
    avg_diastolic = sum(blood_pressures_diastolic) / len(blood_pressures_diastolic)
    
    print(f"\n平均血压: {avg_systolic:.1f}/{avg_diastolic:.1f} mmHg")

# 运行分析
analyze_blood_pressure()
calculate_averages()

# 额外练习：药物剂量计算
print("\n=== 药物剂量计算 ===")
medicines = ["阿莫西林", "布洛芬", "维生素C"]
doses_per_kg = [25, 10, 5]  # 每公斤剂量(mg)

patient_weight = 60  # 患者体重

for i in range(len(medicines)):
    total_dose = patient_weight * doses_per_kg[i]
    print(f"{medicines[i]}: {total_dose}mg")
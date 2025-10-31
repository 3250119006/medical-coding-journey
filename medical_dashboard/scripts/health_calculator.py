#!/usr/bin/env python3
"""
医学健康计算器
医学生综合练习项目
"""

def calculate_bmi(weight, height):
    """计算BMI指数"""
    bmi = weight / (height ** 2)
    return bmi

def analyze_bmi(bmi):
    """分析BMI分类"""
    if bmi < 18.5:
        return "体重过轻"
    elif bmi < 24:
        return "体重正常"
    elif bmi < 28:
        return "体重超重"
    else:
        return "肥胖"

def main():
    print("=== 医学健康计算器 ===")
    
    # 输入患者数据
    height = float(input("请输入身高(m): "))
    weight = float(input("请输入体重(kg): "))
    
    # 计算BMI
    bmi = calculate_bmi(weight, height)
    category = analyze_bmi(bmi)
    
    # 输出结果
    print(f"\n=== 分析结果 ===")
    print(f"BMI指数: {bmi:.2f}")
    print(f"体重分类: {category}")

if __name__ == "__main__":
    main()
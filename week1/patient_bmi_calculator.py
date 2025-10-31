#!/usr/bin/env python3
"""患者BMI计算器"""

def calculate_bmi(weight, height):
    """计算BMI: weight(kg) / height(m)^2"""
    return weight / (height ** 2)

def main():
    print("=== BMI计算器 ===")
    weight = float(input("体重(kg): "))
    height = float(input("身高(m): "))
    bmi = calculate_bmi(weight, height)
    print(f"您的BMI: {bmi:.1f}")

if __name__ == "__main__":
    main()

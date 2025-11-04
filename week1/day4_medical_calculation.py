#!/usr/bin/env python3
"""
医学计算综合练习
"""

print("=== 医学计算工具箱 ===")

# 1. BMI计算
print("\n1. BMI计算")
weight = float(input("体重(kg): "))
height = float(input("身高(m): "))
bmi = weight / (height ** 2)
print(f"BMI: {bmi:.2f}")

# 2. 药物剂量计算
print("\n2. 药物剂量计算")
patient_weight = float(input("患者体重(kg): "))
dose_per_kg = float(input("每公斤剂量(mg): "))
total_dose = patient_weight * dose_per_kg
print(f"总剂量: {total_dose}mg")

# 3. 液体需要量计算（4-2-1法则）
print("\n3. 每日液体需要量计算")
weight_kg = float(input("患者体重(kg): "))
daily_fluid = 0

if weight_kg <= 10:
    daily_fluid = weight_kg * 100
elif weight_kg <= 20:
    daily_fluid = 1000 + (weight_kg - 10) * 50
else:
    daily_fluid = 1500 + (weight_kg - 20) * 20

print(f"每日液体需要量: {daily_fluid}ml")
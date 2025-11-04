"""
输入输出练习
患者信息收集系统
"""

print("===患者信息登记系统===")
# 基础信息收集
name = input("请输入患者姓名：")
age = input("请输入患者年龄：")
# 医学信息收集
print("\n===生命体征记录===")
temperature = input("请输入体温（℃）:")
heart_rate = input("请输入心率（次/分）：")
# 显示收集信息
print("\n" + "="*30)
print("患者信息汇总：")
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"体温：{temperature}℃")
print(f"心率：{heart_rate}次/分")
print("="*30)
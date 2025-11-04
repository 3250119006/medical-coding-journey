# 这仅仅是一个例子
patient_records= ["张三", 35, 36.8, "A血型"]
medicines = ["阿莫西林", "布洛芬", "维生素C"]
# 今天的基础练习
print("\n" + "="*40)
#创建医疗方案列表
patients = ["张三", "李四", "王五"]
temperatures = [36.5, 37.2, 38.1]
blood_pressures = ["120/80", "130/85", "140/90"]
print(f"第一个患者温度:{patients[0]}")
print(f"李四的体温：{temperatures[1]}")
patients.append("赵六")
temperatures[1] = 36.8
#for循环————自动化处理
#第一次测试
patients = ["张三", "李四", "王五", "赵六"]
print("=== 今日查房名单 ===")
for patient in patients:
    print(f"正在检查:{patient}")
"""
for i in patients:
    print(f"正在检查:{i}")
#第一次创新成功，这个等价于上面那串代码    
"""
#第二次测试
patients = ["张三", "李四", "王五"]
temperatures = [36.5, 37.8, 38.2]
print("=== 体温检测报道 ===")
for i in range(len(patients)):
    print(f"{patients[i]}的体温：{temperatures[i]}℃")
print("\n"+"="*100)
"""
患者数据管理系统
第五天综合练习
"""

# 患者数据库
patients = ["张三", "李四", "王五"]
ages = [25, 34, 42]
bmis = [22.1, 24.5, 26.8]

def print_patient_report():
    """打印所有患者报告"""
    print("=== 患者健康报告 ===")
    print("=" * 30)
    
    for i in range(len(patients)):
        print(f"患者: {patients[i]}")
        print(f"年龄: {ages[i]}岁")
        print(f"BMI: {bmis[i]}")
        
        # BMI分类
        if bmis[i] < 18.5:
            status = "体重过轻"
        elif bmis[i] < 24:
            status = "体重正常"
        elif bmis[i] < 28:
            status = "体重超重"
        else:
            status = "肥胖"
            
        print(f"状态: {status}")
        print("-" * 20)

def add_new_patient():
    """添加新患者"""
    print("\n=== 添加新患者 ===")
    name = input("姓名: ")
    age = int(input("年龄: "))
    weight = float(input("体重(kg): "))
    height = float(input("身高(m): "))
    
    bmi = weight / (height ** 2)
    
    patients.append(name)
    ages.append(age)
    bmis.append(bmi)
    
    print(f"成功添加患者: {name}")

# 主程序
while True:
    print("\n=== 患者管理系统 ===")
    print("1. 查看所有患者报告")
    print("2. 添加新患者")
    print("3. 退出系统")
    
    choice = input("请选择操作 (1-3): ")
    
    if choice == "1":
        print_patient_report()
    elif choice == "2":
        add_new_patient()
    elif choice == "3":
        print("系统退出，再见！")
        break
    else:
        print("输入错误，请重新选择！")
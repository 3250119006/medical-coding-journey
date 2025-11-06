#!/usr/bin/env python3
"""
智能医疗助手 v1.0
第一周综合实践项目
医学生编程入门成果展示
"""

def bmi_calculator():
    """BMI计算器"""
    print("\n=== BMI 计算器 ===")
    try:
        height = float(input("请输入身高(m): "))
        weight = float(input("请输入体重(kg): "))
        
        bmi = weight / (height ** 2)
        
        print(f"\n计算结果:")
        print(f"身高: {height}m")
        print(f"体重: {weight}kg") 
        print(f"BMI: {bmi:.2f}")
        
        # BMI分类
        if bmi < 18.5:
            category = "体重过轻"
            advice = "建议增加营养摄入，适当增重"
        elif bmi < 24:
            category = "体重正常" 
            advice = "保持良好生活习惯"
        elif bmi < 28:
            category = "体重超重"
            advice = "建议控制饮食，适当运动"
        else:
            category = "肥胖"
            advice = "建议咨询专业医生制定减重计划"
            
        print(f"分类: {category}")
        print(f"建议: {advice}")
        
    except ValueError:
        print("❌ 输入错误！请确保输入数字")

def medicine_calculator():
    """药物剂量计算器"""
    print("\n=== 药物剂量计算器 ===")
    try:
        patient_weight = float(input("患者体重(kg): "))
        dose_per_kg = float(input("每公斤剂量(mg/kg): "))
        
        total_dose = patient_weight * dose_per_kg
        
        print(f"\n计算结果:")
        print(f"患者体重: {patient_weight}kg")
        print(f"每公斤剂量: {dose_per_kg}mg/kg")
        print(f"总剂量: {total_dose:.1f}mg")
        
    except ValueError:
        print("❌ 输入错误！请确保输入数字")

def patient_recorder():
    """患者信息记录系统"""
    print("\n=== 患者信息记录 ===")
    
    # 收集患者信息
    patients = []
    
    while True:
        print(f"\n当前已记录 {len(patients)} 名患者")
        print("1. 添加新患者")
        print("2. 查看所有患者")
        print("3. 返回主菜单")
        
        choice = input("请选择: ")
        
        if choice == "1":
            name = input("患者姓名: ")
            age = input("年龄: ")
            temperature = input("体温(℃): ")
            symptoms = input("主要症状: ")
            
            patient = {
                "姓名": name,
                "年龄": age,
                "体温": temperature,
                "症状": symptoms
            }
            
            patients.append(patient)
            print(f"✅ 已记录患者: {name}")
            
        elif choice == "2":
            if not patients:
                print("暂无患者记录")
            else:
                print("\n=== 患者列表 ===")
                for i, patient in enumerate(patients, 1):
                    print(f"\n患者 {i}:")
                    for key, value in patient.items():
                        print(f"  {key}: {value}")
                        
        elif choice == "3":
            break
        else:
            print("❌ 请输入1-3之间的数字")

def health_advisor():
    """健康建议生成器"""
    print("\n=== 健康建议生成器 ===")
    
    symptoms = input("请输入主要症状: ").lower()
    
    advice_library = {
        "头痛": "建议休息，多喝水，避免强光刺激",
        "发热": "建议测量体温，多休息，必要时服用退烧药",
        "咳嗽": "建议多喝温水，避免刺激性食物，保持空气湿润",
        "胃痛": "建议清淡饮食，避免辛辣油腻，规律进食"
    }
    
    found_advice = False
    for symptom, advice in advice_library.items():
        if symptom in symptoms:
            print(f"\n针对 '{symptom}' 的建议:")
            print(f"💡 {advice}")
            found_advice = True
    
    if not found_advice:
        print("\n💡 建议多休息，观察症状变化，如有需要请及时就医")

def main():
    """主程序"""
    print("=" * 50)
    print("       智能医疗助手 v1.0")
    print("       第一周学习成果展示")
    print("=" * 50)
    
    while True:
        print("\n请选择功能:")
        print("1. BMI 计算器")
        print("2. 药物剂量计算器") 
        print("3. 患者信息记录")
        print("4. 健康建议生成器")
        print("5. 退出系统")
        
        choice = input("\n请输入选择 (1-5): ")
        
        if choice == "1":
            bmi_calculator()
        elif choice == "2":
            medicine_calculator()
        elif choice == "3":
            patient_recorder()
        elif choice == "4":
            health_advisor()
        elif choice == "5":
            print("\n👋 感谢使用智能医疗助手！")
            print("🎉 恭喜完成第一周学习！")
            break
        else:
            print("❌ 请输入1-5之间的数字")

if __name__ == "__main__":
    main()
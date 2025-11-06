"""
第一周知识点总结
医学生编程入门
"""


#1.Linux命令总结
linux_commands = {
    "导航":["pwd", "cd", "ls"],
    "文件操作":["mkdir", "touch", "cp", "mv", "rm"],
    "权限管理":["chmod", "sudo"],
    "系统信息":["whoami", "uname -a"]
}

#python基础总结
python_basics = {
    "变量": "数据的容器，如 patient——name = '张三'",
    "数据类型": "int(整数),float(小数), str(文字), bool(真假), list(列表)",
    "输入输出": "input()获取输入, print()显示输出" ,
    "字符串格式化": "f-string: f'姓名:{name}'"
}

#git工作总结
git_workflow = [
    "git add . → 添加文件到暂存区",
    "git commit -m'描述' → 提交更改",
    "git push origin main → 推送到github",
    "git status → 查看状态"
]

print("=== 第一周学习总结 ===")
print("\n1. linux命令掌握:")
for category, commands in linux_commands.items():
    print(f"    {category}: {', '.join(commands)}")

print("\n2. python基础理解:")
for concept, explanation in python_basics.items():
    print(f"    {concept}: {explanation}")

print("\n3.git版本控制:")
for step in git_workflow:
    print(f"   · {step}")
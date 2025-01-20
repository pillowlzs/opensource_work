import os
import libcst as cst

# 定义一个自定义访问者来分析 Python 文件中的函数和类
class CodeAnalyzer(cst.CSTVisitor):
    def __init__(self):
        self.functions = 0
        self.classes = 0
        self.function_details = []
        self.class_details = []

    def visit_FunctionDef(self, node):
        self.functions += 1
        # 收集函数信息：函数名称、文档字符串（如果有）
        function_name = node.name.value
        docstring = self.extract_docstring(node)
        self.function_details.append((function_name, docstring))

    def visit_ClassDef(self, node):
        self.classes += 1
        # 收集类信息：类名称
        class_name = node.name.value
        self.class_details.append(class_name)

    # 提取文档字符串的方法
    def extract_docstring(self, node):
        if node.body:
            first_statement = node.body.body[0]  # 获取第一个语句
            if isinstance(first_statement, cst.Expr):
                value = first_statement.value
                if isinstance(value, cst.SimpleString):
                    return value.value.strip('"\'')  # 去掉引号
        return None

# 定义一个分析单个文件的函数
def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
            tree = cst.parse_module(code)
    except UnicodeDecodeError:
        print(f"无法读取文件 {file_path}，可能是编码问题")
        return 0, 0, [], []
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return 0, 0, [], []

    analyzer = CodeAnalyzer()
    tree.visit(analyzer)

    return analyzer.functions, analyzer.classes, analyzer.function_details, analyzer.class_details

# 定义一个分析整个项目的函数
def analyze_project(directory_path):
    total_functions = 0
    total_classes = 0
    file_count = 0
    function_details = []
    class_details = []

    # 遍历项目目录中的所有 Python 文件
    for root, dirs, files in os.walk(directory_path):
        # 排除不需要的目录，比如 .git, .venv 等
        dirs[:] = [d for d in dirs if d not in ['.git', '.venv']]

        for file in files:
            if file.endswith('.py'):  # 只分析 Python 文件
                file_path = os.path.join(root, file)
                functions, classes, funcs_details, classes_details = analyze_file(file_path)
                total_functions += functions
                total_classes += classes
                file_count += 1
                function_details.extend(funcs_details)
                class_details.extend(classes_details)

    return total_functions, total_classes, file_count, function_details, class_details

# 输入你的项目路径（假设是 'plotly' 项目）
project_path = r'E:\04college\opensource\plotly.py-6.0.0rc0'

# 分析整个项目
functions, classes, files, function_details, class_details = analyze_project(project_path)

# 输出分析结果
print(f"Total Python files analyzed: {files}")
print(f"Total functions found: {functions}")
print(f"Total classes found: {classes}")

# 显示一些有用的信息
print("\nSome function details (name and docstring):")
for func_name, docstring in function_details[:10]:  # 显示前 10 个函数
    print(f"Function: {func_name}, Docstring: {docstring or 'No docstring'}")

print("\nSome class details:")
for class_name in class_details[:10]:  # 显示前 10 个类
    print(f"Class: {class_name}")

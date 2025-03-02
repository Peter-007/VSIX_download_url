# VSCode扩展下载URL生成器

一个简单的Python工具，用于生成Visual Studio Code扩展包（VSIX文件）的下载URL。

## 功能特点

- 根据扩展标识符和版本号生成下载URL
- 严格的输入验证和错误处理
- 支持标准的VSCode扩展格式
- 提供清晰的错误提示

## 安装要求

- Python 3.6+

## 使用方法
直接使用Python运行：
```python
from generate_vsix_url import generate_vsix_url

vsix_info = """
Identifier
ms-python.python
Version
2025.0.0
"""

try:
    url = generate_vsix_url(vsix_info)
    print(f"下载URL为: {url}")
except ValueError as e:
    print(f"错误: {str(e)}")
```

## 输入格式

输入字符串必须遵循以下格式：
```
Identifier
[publisher].[extension-name]
Version
[version-number]
```

例如：
```
Identifier
ms-python.python
Version
2025.0.0
```

## 返回值

成功时返回格式如下的URL字符串：
```
https://marketplace.visualstudio.com/_apis/public/gallery/publishers/[publisher]/vsextensions/[extension-name]/[version]/vspackage
```

## 错误处理

该工具会在以下情况抛出 `ValueError`：
- 输入为空或不是字符串
- 输入格式不正确
- 找不到必要的标识符或版本信息
- 标识符格式不符合 `发布者.插件名称` 的要求
- 版本号格式不正确

## 示例

```python
# 成功示例
vsix_info = """
Identifier
ms-python.python
Version
2025.0.0
"""
url = generate_vsix_url(vsix_info)
# 输出: https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/python/2025.0.0/vspackage

# 错误示例
invalid_info = """
Identifier
invalid-format
Version
2025.0.0
"""
# 将抛出 ValueError: 插件标识符格式不正确，应为'发布者.插件名称'格式
```

## 注意事项

- 确保输入格式严格遵循要求
- 标识符必须使用点号(.)分隔发布者和插件名称
- 版本号必须由数字和点号组成

## 贡献

欢迎提交问题和改进建议！

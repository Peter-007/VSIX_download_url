def generate_vsix_url(vsix_info: str) -> str:
    """
    生成VSIX文件的下载URL
    
    参数:
        vsix_info (str): 包含插件标识符和版本的字符串，格式如下:
            Identifier
            publisher.name
            Version
            x.x.x
    
    返回:
        str: 生成的VSIX文件下载URL
        
    异常:
        ValueError: 当输入格式不正确时抛出
    
    示例:
        >>> vsix_info = '''
        ... Identifier
        ... ms-python.python
        ... Version
        ... 2025.0.0
        ... '''
        >>> generate_vsix_url(vsix_info)
        'https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/python/2025.0.0/vspackage'
    """
    
    if not vsix_info or not isinstance(vsix_info, str):
        raise ValueError("输入必须是非空字符串")

    # 扩展市场的基本URL
    extension_gallery_url = "https://marketplace.visualstudio.com/_apis/public/gallery"
    
    # 解析vsix_info
    lines = [line.strip() for line in vsix_info.strip().split('\n') if line.strip()]
    
    if len(lines) < 4:
        raise ValueError("输入格式不正确，需要包含Identifier和Version信息")
        
    try:
        identifier_index = lines.index("Identifier")
        version_index = lines.index("Version")
        identifier = lines[identifier_index + 1]
        version = lines[version_index + 1]
    except (ValueError, IndexError):
        raise ValueError("无法找到Identifier或Version信息，请检查输入格式")

    # 提取发布者和插件名称
    try:
        publisher, name = identifier.split('.')
    except ValueError:
        raise ValueError("插件标识符格式不正确，应为'发布者.插件名称'格式")
    
    # 验证版本号格式
    if not all(part.isdigit() for part in version.split('.')):
        raise ValueError("版本号格式不正确，应为数字和点号组成")
    
    # 生成URL
    url = f"{extension_gallery_url}/publishers/{publisher}/vsextensions/{name}/{version}/vspackage"
    return url

if __name__ == '__main__':
    # 从VSCode的扩展市场获取插件信息
    vsix_info = '''
    Identifier
    ms-python.python
    Version
    2025.0.0
    '''
    
    try:
        # 调用函数并打印生成的URL
        vsix_url = generate_vsix_url(vsix_info)
        print(f"生成的VSIX文件下载URL为:\n{vsix_url}")
    except ValueError as e:
        print(f"错误: {str(e)}")
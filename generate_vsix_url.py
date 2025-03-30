def generate_vscode_extension_url(raw_info: str, platform=None) -> str:
    """从原始文本生成VS Code扩展下载链接
    
    Args:
        raw_info: 包含identifier和version的原始文本
        
    Returns:
        下载URL
        
    Raises:
        ValueError: 当标识符格式错误或输入数据格式错误时
    """
    # 解析输入文本
    info_dict = dict(
        zip(
            map(str.lower, raw_info.strip().split('\n')[::2]),
            raw_info.strip().split('\n')[1::2]
        )
    )
    
    # 解析标识符
    try:
        publisher, name = info_dict['identifier'].split('.')
    except (KeyError, ValueError):
        raise ValueError("标识符格式错误，应为 'Publisher.Name'")
    
    # 获取版本号
    try:
        version = info_dict['version']
    except KeyError:
        raise ValueError("未找到版本号")
    
    # 生成下载URL
    base_url = "https://marketplace.visualstudio.com/_apis/public/gallery"
    download_url = f"{base_url}/publishers/{publisher}/vsextensions/{name}/{version}/vspackage"
    
    # 添加平台信息（如果指定了）
    # win32-x64: Windows 64-bit
    # win32-ia32: Windows 32-bit
    # win32-arm64: Windows ARM64
    # darwin-x64: macOS Intel
    # darwin-arm64: macOS Apple Silicon
    # linux-x64: Linux 64-bit
    # linux-arm64: Linux ARM64
    # alpine-x64: Alpine Linux
    if platform:
        download_url += f"?targetPlatform={platform}"

    return download_url

def main():
    raw_info = """
Identifier
ms-vscode.cpptools
Version
1.23.6
"""
    try:
        download_url = generate_vscode_extension_url(raw_info, "linux-x64")
        print(download_url)
    except ValueError as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main()

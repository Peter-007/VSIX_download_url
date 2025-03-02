def gen_vsix_url(vsix_info: str) -> str:
    """生成VSIX文件下载URL的简化版本"""
    lines = [line.strip() for line in vsix_info.strip().split('\n') if line.strip()]
    publisher, name = lines[lines.index("Identifier") + 1].split('.')
    version = lines[lines.index("Version") + 1]
    return f"https://marketplace.visualstudio.com/_apis/public/gallery/publishers/{publisher}/vsextensions/{name}/{version}/vspackage"

if __name__ == '__main__':
    vsix_info = '''
    Identifier
    vue.volar
    Version
    2.2.8
    '''
    print(f"VSIX URL: {gen_vsix_url(vsix_info)}")

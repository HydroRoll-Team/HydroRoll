import argparse
import curses

class Cli(object):
    parser = argparse.ArgumentParser(description="水系终端脚手架")

    def __init__(self):
        self.parser.add_argument("-i", "install", help="安装规则包、插件与模型", action="install_package")
        self.parser.add_argument("-T", "--template", help="选择模板快速创建Bot实例", action="build_template")
        self.parser.add_argument("-S", "search", help="在指定镜像源查找规则包、插件与模型", action="search_package")
        self.args = self.parser.parse_args()

    def get_args(self):
        return self.args
    
    def get_help(self):
        return self.parser.format_help()
    

cli = Cli()

print(cli.get_help())
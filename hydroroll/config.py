import argparse
import sys
import platform
from importlib.metadata import version
from iamai import Plugin
import os

# 创建全局 ArgumentParser 对象
global_parser = argparse.ArgumentParser(description='hydroroll[水系] 全局命令参数')

# 定义全局配置类
class GlobalConfig:
    _name = "hydroroll"
    _version = "0.1.0"
    _svn = "2"
    _author = "简律纯"
    _iamai_version = version('iamai')
    _python_ver = sys.version
    _python_ver_raw= '.'.join(map(str, platform.python_version_tuple()[:3]))
    _current_path = os.path.dirname(os.path.abspath('__file__'))
    _folders = {'config':{},'data':{},'logs':{},'models':{},'rules':{'rules_default'},'users':{},'web':{'frontend':{'static','js','css','public'},'backend':{'app','template'}}}
    
    # 定义系统组件
    class HydroSystem:
        def __init__(self):
            self.parser = argparse.ArgumentParser(description='hydroroll[水系].system 系统命令参数')
            self.subparsers = self.parser.add_subparsers()
            self.status_parser = self.subparsers.add_parser('status', aliases=['s'], help='系统状态')
            self.reload_parser = self.subparsers.add_parser('reload', aliases=['rld'], help='重新加载系统')
            self.restart_parser = self.subparsers.add_parser('restart', aliases=['rst'], help='重启系统')
            self.help = '\n'.join(self.parser.format_help().replace('\r\n', '\n').replace('\r', '').split('\n')[2:-3])
    class HydroBot:
        def __init__(self) -> None:
            self.parser = argparse.ArgumentParser(description="Bot命令")
        
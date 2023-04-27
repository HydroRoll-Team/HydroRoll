import argparse
import sys
import platform
from importlib.metadata import version
from iamai import Plugin
import os
import pickle
import threading


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
    current_path = os.path.dirname(os.path.abspath('__file__'))

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
        

class ConfigManager:
    def __init__(self, directory):
        self.directory = directory
        self.configs = {}
        self.locks = {}
    
    def get(self, filename, section, key, default=None):
        if not self._check_file_exists(filename):
            return default
        config = self._get_config(filename)
        if section not in config:
            return default
        return config[section].get(key, default)
    
    def set(self, filename, section, key, value):
        config = self._get_config(filename)
        if section not in config:
            config[section] = {}
        config[section][key] = value
        self._save_config(filename, config)
    
    def delete(self, filename, section, key):
        config = self._get_config(filename)
        if section not in config:
            return
        if key not in config[section]:
            return
        del config[section][key]
        self._save_config(filename, config)
    
    def sections(self, filename):
        if not self._check_file_exists(filename):
            return []
        config = self._get_config(filename)
        return list(config.keys())
    
    def section_items(self, filename, section):
        if not self._check_file_exists(filename):
            return []
        config = self._get_config(filename)
        if section not in config:
            return []
        return list(config[section].items())
    
    def files(self):
        return [filename for filename in os.listdir(self.directory) if filename.endswith('.dat')]

    def _get_lock(self, filename):
        if filename not in self.locks:
            self.locks[filename] = threading.Lock()
        return self.locks[filename]
    
    def _get_config(self, filename):
        with self._get_lock(filename):
            if filename not in self.configs:
                filepath = os.path.join(self.directory, filename)
                if os.path.exists(filepath):
                    try:
                        with open(filepath, 'rb') as f:
                            self.configs[filename] = pickle.load(f)
                    except:
                        pass
                if filename not in self.configs:
                    self.configs[filename] = {}
        return self.configs[filename]
    
    def _save_config(self, filename, config):
        with self._get_lock(filename):
            try:
                filepath = os.path.join(self.directory, filename)
                backuppath = os.path.join(self.directory, filename + '.bak')
                lockpath = os.path.join(self.directory, filename + '.lock')
                with open(lockpath, 'wb') as f:
                    pass
                if os.path.exists(filepath):
                    os.replace(filepath, backuppath)
                with open(filepath, 'wb') as f:
                    pickle.dump(config, f)
                os.remove(backuppath)
                os.remove(lockpath)
            except:
                pass
    
    def _check_file_exists(self, filename):
        filepath = os.path.join(self.directory, filename)
        return os.path.exists(filepath) and filename.endswith('.dat')

from iamai import Bot as _Bot
from typing import Optional, Dict, List, Type, Any, Union
from pathlib import Path
import os
# 获取当前目录路径
current_dir = Path.cwd()

# 获取当前脚本文件路径
script_file = current_dir.resolve() / __file__

# 获取当前脚本文件所在目录路径
script_dir = script_file.parent

__all__ = ["Bot"]

class Bot:
    def __init__(
        self,
        *,
        config_file: Optional[str] = "config.toml",
        config_dict: Optional[Dict] = None,
        hot_reload: bool = False,
    ) -> None:
        self.bot = _Bot(hot_reload=hot_reload,
                       config_file=config_file,
                       config_dict=config_dict
                       )
        self.bot.load_plugins_from_dirs(Path(f"{script_dir}/plugins"))
        self.create_folders()
        self.init_data()
        self.init_conf()
        self.init_webui()
    
    def run(self) -> None:
        self.bot.run()
    
    def restart(self) -> None:
        self.bot.restart()
        
    def create_folders(self):
            folder_path = os.path.dirname(os.path.abspath('__file__')) # 获取main.py所在文件夹路径
            if not os.path.isdir(os.path.join(folder_path, 'user')):
                os.mkdir(os.path.join(folder_path, 'user'))
            if not os.path.isdir(os.path.join(folder_path, 'data')):
                os.mkdir(os.path.join(folder_path, 'data'))
            if not os.path.isdir(os.path.join(folder_path, 'models')):
                os.mkdir(os.path.join(folder_path, 'models'))
            if not os.path.isdir(os.path.join(folder_path, 'web')):
                os.mkdir(os.path.join(folder_path, 'web'))
            if not os.path.isdir(os.path.join(folder_path, 'config')):
                os.mkdir(os.path.join(folder_path, 'config'))
            if not os.path.isdir(os.path.join(folder_path, 'logs')):
                os.mkdir(os.path.join(folder_path, 'logs'))
            if not os.path.isdir(os.path.join(folder_path, 'rules')):
                os.mkdir(os.path.join(folder_path, 'rules'))
    
    def init_data(self):
        ...
        
    def init_webui(self):
        ...
        
    def init_conf(self):
        ...
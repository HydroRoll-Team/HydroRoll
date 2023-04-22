from iamai import Bot as _Bot
from typing import Optional, Dict, List, Type, Any, Union
from pathlib import Path

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
    
    def run(self) -> None:
        self.bot.run()
    
    def restart(self) -> None:
        self.bot.restart()
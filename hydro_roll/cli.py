import argparse
import os
import aiohttp
import asyncio
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .typing import *

class Atien(object):
    parser = argparse.ArgumentParser(description="水系终端脚手架")

    def __init__(self):
        self.parser.add_argument(
            "-i",
            "--install",
            dest="command",
            help="安装规则包、插件与模型",
            action="store_const",
            const="install_package",
        )
        self.parser.add_argument(
            "-T",
            "--template",
            dest="command",
            help="选择模板快速创建Bot实例",
            action="store_const",
            const="build_template",
        )
        self.parser.add_argument(
            "-S",
            "--search",
            dest="command",
            help="在指定镜像源查找规则包、插件与模型",
            action="store_const",
            const="search_package",
        )
        self.parser.add_argument(
            "-c",
            "--config",
            dest="command",
            help="配置管理",
            action="store_const",
            const="config",
        )
        self.args = self.parser.parse_args()

    def get_args(self):
        return self.args

    def get_help(self):
        return self.parser.format_help()

    async def install_packages(self):
        package_name = input("请输入要安装的包名：")
        url = f"https://pypi.org/pypi/{package_name}/json"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    await self._extract_package(data, package_name)
                else:
                    print(f"找不到包：{package_name}")

    async def _extract_package(self, data, package_name):
        latest_version = data["info"]["version"]
        download_url = data["releases"][latest_version][0]["url"]

        plugins_dir = "plugins"
        if not os.path.exists(plugins_dir):
            os.mkdir(plugins_dir)

        file_name = download_url.split("/")[-1]
        file_path = os.path.join(plugins_dir, file_name)

        async with aiohttp.ClientSession() as session:
            async with session.get(download_url) as response:
                if response.status == 200:
                    with open(file_path, "wb") as file:
                        file.write(await response.read())
                    print(f"成功安装包：{package_name}")
                else:
                    print(f"下载包时出错：{package_name}")

    def build_template(self):
        template = input("请选择应用模板（输入数字）:\n" "1. 创建轻量应用\n" "2. 创建标准应用\n" "3. 创建开发应用\n")

        if template == "1":
            print("选择了轻量应用模板")
        elif template == "2":
            print("选择了标准应用模板")
        elif template == "3":
            print("选择了开发应用模板")
        else:
            print("无效的模板选择")

    async def search_package(self):
        search_term = input("请输入要搜索的包名关键字：")
        url = f"https://pypi.org/search/?q={search_term}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data: dict = response.json()  # type: ignore[dict]
                    packages = data.get("results", [])

                    for package in packages:
                        name = package["name"]
                        topics = package.get("topics", [])

                        if (
                            search_term.lower() in name.lower()
                            and "HydroRoll" in topics
                        ):
                            print(f"包名：{name}")
                else:
                    print("搜索失败")

    def config(self):
        config_dir = os.path.expanduser("~/.hydroroll")
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        config_file = os.path.join(config_dir, "config.json")

        subcommand = input("请输入子命令（add/delete）：")

        if subcommand == "add":
            key = input("请输入要添加的键名：")
            value = input("请输入要添加的键值：")

            with open(config_file, "r+") as file:
                try:
                    config_data = json.load(file)
                except json.JSONDecodeError:
                    config_data = {}

                config_data[key] = value
                self._extracted_from_config_21(file, config_data)
            print(f"成功添加配置项：{key}={value}")

        elif subcommand == "delete":
            key = input("请输入要删除的键名：")

            with open(config_file, "r+") as file:
                try:
                    config_data = json.load(file)
                except json.JSONDecodeError:
                    config_data = {}

                if key in config_data:
                    del config_data[key]
                    self._extracted_from_config_21(file, config_data)
                    print(f"成功删除配置项：{key}")
                else:
                    print(f"配置项不存在：{key}")

        else:
            print("无效的子命令选择")

    # TODO Rename this here and in `config`
    def _extracted_from_config_21(self, file, config_data):
        file.seek(0)
        json.dump(config_data, file, indent=4)
        file.truncate()


cli = Cli()

if cli.get_args().command == "install_package":
    asyncio.run(cli.install_packages())
elif cli.get_args().command == "build_template":
    cli.build_template()
elif cli.get_args().command == "search_package":
    asyncio.run(cli.search_package())
elif cli.get_args().command == "config":
    cli.config()
else:
    print(cli.get_help())

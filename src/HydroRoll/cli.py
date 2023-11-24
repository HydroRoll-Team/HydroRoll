import argparse
import os
import requests

class Cli(object):
    parser = argparse.ArgumentParser(description="水系终端脚手架")

    def __init__(self):
        self.parser.add_argument(
            "-i", "--install", dest="command", help="安装规则包、插件与模型", action="store_const", const="install_package"
        )
        self.parser.add_argument(
            "-T", "--template", dest="command", help="选择模板快速创建Bot实例", action="store_const", const="build_template"
        )
        self.parser.add_argument(
            "-S", "--search", dest="command", help="在指定镜像源查找规则包、插件与模型", action="store_const", const="search_package"
        )
        self.args = self.parser.parse_args()

    def get_args(self):
        return self.args

    def get_help(self):
        return self.parser.format_help()
    
    def install_packages(self):
        package_name = input("请输入要安装的包名：")
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url)

        if response.status_code == 200:
            self._extracted_from_install_packages_7(response, package_name)
        else:
            print(f"找不到包：{package_name}")

    # TODO Rename this here and in `install_packages`
    def _extracted_from_install_packages_7(self, response, package_name):
        data = response.json()
        latest_version = data["info"]["version"]
        download_url = data["releases"][latest_version][0]["url"]

        plugins_dir = "plugins"
        if not os.path.exists(plugins_dir):
            os.mkdir(plugins_dir)

        file_name = download_url.split("/")[-1]
        file_path = os.path.join(plugins_dir, file_name)

        with open(file_path, "wb") as file:
            file.write(requests.get(download_url).content)

        print(f"成功安装包：{package_name}")
    
    def build_template(self):
        template = input("请选择应用模板（输入数字）:\n"
                         "1. 创建轻量应用\n"
                         "2. 创建标准应用\n"
                         "3. 创建开发应用\n")
        
        if template == "1":
            print("选择了轻量应用模板")
        elif template == "2":
            print("选择了标准应用模板")
        elif template == "3":
            print("选择了开发应用模板")
        else:
            print("无效的模板选择")
    
    def search_package(self):
        search_term = input("请输入要搜索的包名关键字：")
        url = f"https://pypi.org/search/?q={search_term}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            packages = data["results"]
            
            for package in packages:
                name = package["name"]
                topics = package.get("topics", [])
                
                if search_term.lower() in name.lower() and "HydroRoll" in topics:
                    print(f"包名：{name}")
        else:
            print(f"搜索失败")


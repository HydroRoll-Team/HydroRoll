
<p align="center"><img width="300" src="image/readme/1681811270177.png"></p>

<h1 align="center">
  ChienDice
</h1>

<p align="center">
简系
</p>

## 📘 Introduction

一个新的骰系

## 🚀 Features

- 🎪 **Interactive [docs](https://iamai.retrofor.space) &amp; [demos](https://iamai.retrofor.space/demos)**
- 🕶 **Seamless migration**: Works for **both** [Rasa]() and [GPT]() and more...
- ⚡ **Fully tree shakeable**: Only take what you want, [bundle size](https://iamai.retrofor.space/export-size)
- 🔩 **Flexible**: Configurable event filters and targets
- 🔌 **Optional [Add-ons](https://iamai.retrofor.space/add-ons)**: [Apscheduler](https://iamai.retrofor.space/add-ons/apscheduler), etc.
- 👍 **Cross-platform**: [cqhttp](https://iamai.retrofor.space/guide/cqhttp-adapter.html), [dingtalk](https://iamai.retrofor.space/guide/dingtalk-adapter.html), [Mirai](https://iamai.retrofor.space/guide/mirai-adapter.html) etc.

## ⬇️ Install

### Docker

通过Docker直接部署。

### pip

通过pip下载后导入包部署

### Raw

下载源码直接部署。

## 🌈Site Preview

### 📌tutorial

- <https://chien.retrofor.space/> _(recommend)_
- <https://chien-dice.vercel.app/>

### 📌tools

- <https://play.chien.retrofor.space/>
- <https://envshare.chien.retrofor.space/>
- <https://flexirobo.retrofor.space/>
- <https://cyberdynamix.retrofor.space/>
  
## 👨‍🚀 Contributors

<a href="https://github.com/retrofor/ChienDice/graphs/contributors">
  <img width="50" src="https://contrib.rocks/image?repo=retrofor/ChienDice" />
</a>

## 📄 License

[MIT](https://github.com/retrofor/ChienDice/blob/main/LICENSE) © 2023-PRESENT [简律纯](https://github.com/HsiangNianian)






### 第一个娘

**pip部署**

命令行输入

``` shell
pip install ChienDice
```

**创建main.py**

``` py
from ChienDice import Bot
bot = Bot()

if __name__ == "__main__":
    bot.run()
```

**开启go-cqhttp**

``` shell
./go-cqhttp
```

**认主**

输入`.get married`

如此简单。


### 轻松入门

> 只需要记住两个命令即可轻松驾驭九只娘！

**入栈**

`.set` 用于设置一切！

**出栈**

`.get` 用于获取一切！

#### 快速举例

**认主**: `.get married`
**退群**: `.get lost`
**获取`jrrp`**: `.get jrrp`
**设置欢淫语**: `.set welcome [欢迎~] 可选添加 [{at}] [{nickname}] [{avatar}] [{id}]`

## 命令列表

> 还在为繁琐命令感到烦恼？使用简系，小学生都能记住的固定词组！

### get

**class `get`(self, *, config_file = 'config.toml', config_dict = None, hot_reload = False)**
Bases: `object`

读取并储存配置 `Config`，加载适配器 `Adapter` 和插件 `Plugin`，并进行事件分发。

Arguments

config_file (Optional[str]) - 配置文件，如不指定则使用默认的 config.toml。 若指定为 None，则不加载配置文件。

config_dict (Optional[Dict]) - 配置字典，默认为 None。 若指定字典，则会忽略 config_file 配置，不再读取配置文件。

hot_reload (bool) - 热重载。 启用后将自动检查 plugin_dir 中的插件文件更新，并在更新时自动重新加载。
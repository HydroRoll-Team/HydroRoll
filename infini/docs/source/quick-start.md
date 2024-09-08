# 快速开始

通过本文档，你可以快速开始学习如何使用 Infini 来构建一个规则包。请注意，如果你在查找如何使用 Infini，你可以前往 [Infini Adapters 文档](https://adapter.infini.hydroroll.team/)和[IPM 文档](https://ipm.hydroroll.team/)来获取更多信息。

## 预先准备

### Python 环境

```{important} 注意
我们强烈建议使用最新版 Python 分发。
```

请先确保你正确安装并配置了 Python 环境，如果你的计算机上还没有一个 Python 安装，请先前往[Python 官网](https://www.python.org/downloads/)下载和安装 Python。

```{tip} 提示
如果你的网络环境较差，你可以使用[淘宝镜像网站](https://registry.npmmirror.com/binary.html?path=python/)下载 Python，安装时请注意选择将 Python 加入环境变量。
```

安装完成后，你可以打开系统终端执行`python -V`以及`pip -V`来确保 Python 被正确安装。

### Infini 包管理器

我们强烈推荐使用 Infini 包管理器——**IPM**来构建一个 Python 规则包。

你可以通过执行终端指令来安装 IPM：

```bash
pip install ipdm
```

安装完成后，在终端中执行`ipm`确保 IPM 被正确安装。

## 创建项目

1. 使用 IPM 创建规则包

   你可以使用以下指令创建 Infini 规则包：

   ```bash
   ipm new yourpackage
   ```

   IPM 将为你初始化一个 Infini 规则包，你应该将`yourpackage`替换为你的包名。

   也可以在已有的文件夹内创建：

   ```bash
   cd exists_directory
   ipm init
   ```

   这两者是等效的。

   你可以前往[IPM 文档](https://ipm.hydroroll.team/)获得更多关于 IPM 使用的信息。

2. 手动创建规则包

   首先在一个目录中创建`infini.toml`，并写入以下内容：

   ```toml
   [infini]
   name = "yourpackage"
   version = "0.1.0"
   description = "规则包描述"
   license = "AGPLv3"

   [requirements]

   [dependencies]
   ```

   然后在同一个目录创建一个`src`文件夹，并在`src`中建立一个入口文件（`__init__.py`或`yourpackage.py`，这两者是等效的）。

## 正式开始

以上你已经成功建立了 Infini 开发环境，现在你可以开始学习如何构建一个你自己的规则包了。

Infini 2 规则包应当遵循规定的规则包标准，你可以前往阅读[通用规则包标准文档](grps/index)来进行下一步的学习。

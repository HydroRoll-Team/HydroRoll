# 社区贡献指引

## 文档

我们很高兴能有人一起维护 `infini` 在线文档。

在开始之前，请先了解以下内容：

1. `sphinx`，一个开源老牌 CMS。
2. `furo`，我们使用的 `sphinx` 文档主题。
3. `readthedocs`，我们的文档托管运行商。
4. `makefile`，可以极大简化开发与贡献步骤的指令管理器。

### 本地部署

sphinx 并不支持类似 hugo、hexo、jekyll 等直接生成网页并在线热重载的功能（这意味着当你做出文档更改以后，需要手动生成新的站点文件！）。

#### 依赖安装

1. 使用 `pdm` 管理器局部安装开发贡献在线文档所需的依赖。

```shell
pdm install -G docs
```

2. 或者如果你不习惯使用 `pdm`，可以参考全局安装方案:

```shell
cd docs
pip install -r requirements.txt
```

注意，首先你需要进入 `docs` 目录，之后的所有命令全部基于此目录，便不再赘述。

#### 站点生成

1. 使用 `make` 指令。

```shell
make html
make latex
make text
```

html 网页与 latex 源码以及 text 文本文档将会生成于 `docs/_build` 的 对应文件夹下。

2. 如果你没有 `makefile`，那么也可以直接使用 `sphinx-build` 命令生成文档:

```shell
pdm run sphinx-build source _build html
```

关于文档的写法并没有太多严格要求，同时，如果想知道更多 sphinx 的快速配置与 furo 的快捷语法，还请跳转到相应官网。

最后，你的工作环境可能或许会是这样的：

![workspace](https://infini.hydroroll.team/zh-cn/latest/_static/workspace.png)

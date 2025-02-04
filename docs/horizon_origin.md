# horizon的由来

该页面介绍了 treebl 开发的 ModPEScript（ModPE），到 Zhuowei Zhang 移植至安卓版的 BlockLauncher，再到 Zheka_Smirnov 基于 BlockLauncher 发布的 Core Engine，以及其后续发展成的独立 MOD 加载器 Inner Core，最后介绍了 Zheka_Smirnov 开发的多合一启动器 Horizon 的由来

注意：Minecraft: Bedrock Edition MOD加载器发展史是一个庞大的树形结构关系，以下是分支之一。按时间顺序。
## treebl（未知）
早期treebl开发了一款以js为编程语言的MOD加载器插件，插件名称为**ModPEScript**（简称 **ModPE**），它最初是为iOS设计的，后来因为作者的iPhone坏了（代码随之也丢了）而停止更新。
注意：这里的**ModPE**是作者给插件取名字，后来涉及更多涵义。
## Zhuowei Zhang（华人张卓伟）
ModPE在发布不久后很快被移植到了安卓版，软件名称为**BlockLauncher**（旧称**MCPELauncher**）。自2019年12月27日已停止更新，最新版本仅[基岩版1.14.1](https://minecraft.wiki/w/zh:%E5%9F%BA%E5%B2%A9%E7%89%881.14.1 "mcwiki:zh:基岩版1.14.1")。

## Zheka_Smirnov（俄罗斯开发者)
Zheka_Smirnov在2016年9月发布的基于**BlockLauncher**的Mod加载器，名称为**Core Engine**。
**CoreEngine** 的前身是 **Factorization** （非官方译作因式分解）。**Factorization**是**BlockLauncher**的代表MOD之一。在以自身 Mod 内容为主体的前提下，**Factorization** 允许导入基于自身 API 的拓展模组，在 **Factorization** 停止维护后，Zheka 将拓展 API 封装为单独的引擎，并更名为 **CoreEngine**。
后来Zheka_Smirnov把 **CoreEngine**做成了独立MOD加载器（不在依赖于**BlockLauncher**），名称为**Inner Core**。之后Zheka_Smirnov开发了一款多合一启动器**Horizon**。

---

参考文献：<br>

- [Horizon](https://wiki.mcbe-dev.net/p/Horizon)
- [Zheka_Smirnov](https://wiki.mcbe-dev.net/p/Zheka_Smirnov)
- [Inner_Core](https://wiki.mcbe-dev.net/p/Inner_Core)
- [CoreEngine](https://wiki.mcbe-dev.net/p/CoreEngine)
- [BlockLauncher](https://wiki.mcbe-dev.net/p/BlockLauncher)
- [ModPE](https://wiki.mcbe-dev.net/p/ModPE)
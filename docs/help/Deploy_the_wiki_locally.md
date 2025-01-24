# 在本地部署 Wiki

此页面仅对专业人士开放。如果你需要测试你的 Wiki 代码，你需要在本地部署本 Wiki。

1. 在开始部署之前你需要一个 GitHub 账号，如果没有可以在[Github 官网](https://github.com)注册一个。
2. 克隆[仓库](https://github.com/icmodtech/icmod-wiki)至本地。
3. 在控制台中运行如下命令以安装依赖：
```
pip install -r requirements.txt
```

4. 然后在控制台中使用`python mkdocs serve`命令即可在`http://127.0.0.1:8000`实时看到做出的更改。
5. 提交并推送更改后，可以在`https://wiki.icmod.tech`查看更改后的效果。
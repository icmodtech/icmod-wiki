"""
此插件功能如下：
1.添加social card
    你可以在https://opengraph.dev/上测试
2.为标签添加了元数据
    meta name="keywords"
3.文档发布状态
    ---
    title: 更多
    status: new
    publish: false
    ---
    如果publish: false则不发布该页面
"""

import mkdocs.plugins
from mkdocs.structure.pages import Page
from mkdocs.config.defaults import MkDocsConfig
from pathlib import Path
from mkdocs.structure.files import Files
from mkdocs.config import Config

#操作meta
class HTMLModifier:
    def __init__(self,meta):
        self.soup = meta
    @property
    def get(self):
        return self.soup
    def add_meta_property(self, name: str, value: str):
        self.soup=self.soup+[{ "property": name, "content": value }]
    def add_meta_keywords(self, value: list):
        self.soup=self.soup+[{ "name":"keywords", "content": ','.join(value) }]

#文档发布状态
#添加social card
def on_page_markdown(markdown, page:Page, config, files):



    #文档发布状态
    if page.meta.get('publish',True)==False:
            print('已移除：',page.title)
            files.remove(page.file)



    #添加social card
    title = page.meta.get('title')
    if title is not None:
        title =f"{config.site_name}" if title=='Home' else f"{title}-{config.site_name}"
    else:
        title = f"{config.site_name}"
    
    #获取描述
    description = page.meta.get('description', None)

    #获取图片
    image = page.meta.get('image', None)
    if image is not None:
        image = str(image)
        if image.startswith("../"):
            image = f"/{image.replace('../', '')}"
        if image.startswith("/"):
            image = image[1:]
        image_path = Path(config.docs_dir) / Path(image)
        if not image_path.exists():
            print('图片不存在')
        image = f'{config.site_url}{image.replace("//", "/")}'
    url = f"{config.site_url}{page.url}"
    site_name = config.site_name
    
    if title and description:
        html_modifier = HTMLModifier(page.meta.get("meta", []))
        #og
        html_modifier.add_meta_property(name="og:type", value="article")
        html_modifier.add_meta_property(name="og:title", value=title)
        html_modifier.add_meta_property(name="og:description", value=description)
        html_modifier.add_meta_property(name="og:site_name", value=site_name)
        html_modifier.add_meta_property(name="og:locale", value=url)
        html_modifier.add_meta_property(name="og:url", value=url)
        html_modifier.add_meta_property(name="og:image:width", value='1200')
        html_modifier.add_meta_property(name="og:image:height", value='6300')
        html_modifier.add_meta_property(name="og:image:type", value='image/png')
        #twitter
        card_type = "summary_large_image" if image else "summary"
        html_modifier.add_meta_property(name="twitter:card", value=card_type)
        html_modifier.add_meta_property(name="twitter:title", value=title)
        html_modifier.add_meta_property(name="twitter:description", value=description)
        html_modifier.add_meta_property(name="twitter:image:width", value='1200')
        html_modifier.add_meta_property(name="twitter:image:height", value='6300')
        #og&twitter
        if image is not None:
            html_modifier.add_meta_property(name="og:image", value=image)
            html_modifier.add_meta_property(name="twitter:image", value=image)
        #add
        page.meta["meta"]=html_modifier.get

#添加<meta name="keywords" content="HTML,CSS,XML,JavaScript">
def on_page_context(context, page, config, nav):
        if page.meta.get("tags"):
            html_modifier = HTMLModifier(page.meta.get("meta", []))
            html_modifier.add_meta_keywords(page.meta["tags"])
            page.meta["meta"]=html_modifier.get
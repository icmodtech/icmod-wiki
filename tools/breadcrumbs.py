"""
此插件功能如下：
1.添加面包屑
    首页> 电子产品 > 手机 
"""
import mkdocs.plugins
from mkdocs.structure.pages import Page
from mkdocs.config.defaults import MkDocsConfig

def on_post_page(output: str, *, page: Page, config: MkDocsConfig):
    path=page.url.split('/')
    del path[-2:]
    alink=['<li><a href="'+config.site_url+ '/'.join(path[:i+1]) +'">'+ path[i] +'</a></li>' for i in range(len(path))]
    output = output.replace('<article class="md-content__inner md-typeset">','<article class="md-content__inner md-typeset"><nav aria-label="面包屑导航"><ol><li><a href="'+ config.site_url +'"><span class="twemoji"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"></path></svg></span></a></li>'+''.join(alink)+'<li><a href="#">'+ page.title+'</a></li></ol></nav>')
    return output
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
    alink=['<a href="'+config.site_url+ '/'.join(path[:i+1]) +'">'+ path[i] +'&gt;</a>' for i in range(len(path))]
    output = output.replace('<article class="md-content__inner md-typeset">','<article class="md-content__inner md-typeset"><p><nav class=md-tags><a href="'+ config.site_url +'"><span class="twemoji"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"></path></svg></span>&gt;</a>'+''.join(alink)+'<a href="#">'+ page.title+'</a></nav></p>')
    return output
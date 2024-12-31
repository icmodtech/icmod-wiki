import yaml,re

#一个自定义的回调函数，用来忽略标签
def construct_ruby_object(loader,suffix,node):
    return loader.construct_yaml_str(node)
yaml.SafeLoader.add_multi_constructor('tag:yaml.org,2002:python/name:',construct_ruby_object)

title='计算机网络'
content_file_path=f'docs/{title}/目录.md'
mkdocsyaml='mkdocs.yml'
headline,sub_content=[],[]
with open(content_file_path,mode='r',encoding='utf-8') as file:
    file_content=file.read()
    title_split=re.split(r'#\s+.*[^\s]\s*',file_content)
    del title_split[0]
    headline=re.findall(r'#\s+(.*[^\s])\s*',file_content)
    sub_content=[[j for j in re.findall(r'-\s\[\[(.*)\]\]',i)] for i in title_split]
    for n,o in reversed(list(enumerate(headline))):
        if len(sub_content[n]):
            for u in range(len(sub_content[n])):
                sub_content[n][u]=f'{title}/'+o+'/'+sub_content[n][u]+'.md'
        else:
            del headline[n],sub_content[n]
with open(mkdocsyaml,mode='r',encoding='utf-8') as file:
    mkdocs=yaml.safe_load(file)
    for i in mkdocs['nav']:
        if isinstance(i,dict):
            if list(i.keys())[0]==title:
                i[title]=[{headline[d]:sub_content[d]} for d in range(len(headline))]
                break
    else:
        mkdocs["nav"].append({title:[{headline[d]:sub_content[d]} for d in range(len(headline))]})
with open('mkdocs.yml',mode='w',encoding='utf-8') as file:
    yaml.safe_dump(mkdocs,file,allow_unicode=True)

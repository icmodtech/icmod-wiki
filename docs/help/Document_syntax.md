# 文档语法

我们会告诉你如何从零编写Wiki页面。该页面总结了常用元素的使用方法，你可以在这里查看预期的效果。
## 内联元素

### 编辑标记([Critic](https://facelessuser.github.io/pymdown-extensions/extensions/critic/))

| 描述  | 语法               | 效果             |
| --- | ---------------- | -------------- |
| 删除  | <code>{\--删除我--}</code>      | {--内容--}       |
| 插入  | <code>{\++插入我++}</code>      | {++插入我++}      |
| 替换  | <code>{\~\~原来的\~>替换的\~\~}</code> | {~~原来的~>替换的~~} |
| 高亮  | <code>{\=\=高亮显示我==}</code>    | {==高亮显示我==}    |
| 注释  | <code>{\>>注释<<}</code>       | {>>注释<<}       |

### 插入符号([Caret](https://facelessuser.github.io/pymdown-extensions/extensions/caret/))

| 描述  | 语法        | 效果      |
| --- | --------- | ------- |
| 插入  | `^^插入我^^` | ^^插入我^^ |
| 上标  | `H^2^0`   | H^2^0   |

### 快捷键([Keys](https://facelessuser.github.io/pymdown-extensions/extensions/keys/))

| 描述   | 语法                    | 效果                  |
| ---- | --------------------- | ------------------- |
| 按键组合 | `++ctrl+alt+delete++` | ++ctrl+alt+delete++ |
| ...  | ...                   | ...                 |

### 马克笔([Mark](https://facelessuser.github.io/pymdown-extensions/extensions/mark/))

| 描述   | 语法       | 效果     |
| ---- | -------- | ------ |
| 马克标记 | `==标记==` | ==标记== |

### 波浪符号([Tilde](https://facelessuser.github.io/pymdown-extensions/extensions/tilde/))

| 描述  | 语法             | 效果           |
| --- | -------------- | ------------ |
| 删除  | `~~删除我~~`      | ~~删除我~~      |
| 下标  | `CH~3~CH~2~OH` | CH~3~CH~2~OH |

### ==表情==([Emoji](https://facelessuser.github.io/pymdown-extensions/extensions/emoji/))

| 描述  | 语法        | 效果      |
| --- | --------- | ------- |
| 微笑  | `:smile:` | :smile: |
| ... | ...       | ...     |

## 块级元素

### 详情([Details](https://facelessuser.github.io/pymdown-extensions/extensions/details/))



=== "预览1"

    ??? note

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

=== "语法"

    ```
    ??? note

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.
    ```


=== "预览2"

    ???+ note

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

=== "语法"

    ```
    ???+ note

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.
    ```


### ==标题==([Caption](https://facelessuser.github.io/pymdown-extensions/extensions/blocks/plugins/caption/))

为块级元素添加标题

=== "效果"

    Fruit      | Amount
    ---------- | ------
    Apple      | 20
    Peach      | 10
    Banana     | 3
    Watermelon | 1

    /// caption
    Fruit Count
    ///
    

=== "语法"

    ```
    Fruit      | Amount
    ---------- | ------
    Apple      | 20
    Peach      | 10
    Banana     | 3
    Watermelon | 1

    /// caption
    Fruit Count
    ///
    ```



## 其他元素

### ==友好的Markdown==([BetterEm](https://facelessuser.github.io/pymdown-extensions/extensions/betterem/))

| 描述     | 语法                                              | 效果                                            |
| ------ | ----------------------------------------------- | --------------------------------------------- |
| 连续的下划线 | `___A lot of underscores____________is okay___` | ___A lot of underscores____________is okay___ |
| ...    | ...                                             | ...                                           |

### ==算术公式==([Arithmatex](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/))

=== "Inline"

    ```
    $p(x|y) = \frac{p(y|x)p(x)}{p(y)}$
    ```
    
    $p(x|y) = \frac{p(y|x)p(x)}{p(y)}$

=== "Block"

    ```
    $$
    \cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
    $$
    ```

    $$
    \cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
    $$


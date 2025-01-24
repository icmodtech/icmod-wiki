---
title: 更多
status: new
publish: false
---

# 更多

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

```{.python .annotate}
print("Hello, World!") # 这是一个注释。(1)
```

1.  这是一个注解。

=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

<div class="grid" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>

??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

# 更多
| First Header | Second Header | Third Header |
| ------------ | ------------- | ------------ |
| Content Cell | Content Cell  | Content Cell |
| Content Cell | Content Cell  | Content Cell |

#table#

```python title="bubble_sort.py" linenums="1"
#[18，20]=18×20÷（18，20）=18×20÷2=180

#最小公倍数=积/最大公约数

#最大公约数=辗转相除法

def zd(value1,value2):

    sy=divmod(value1,value2)

    if sy[1]==0:

        return value2

    if sy[0]==0:

        return zd(value2,value1)

    else:

        return zd(value2,sy[1])

def zx(value1,value2):

    ji=value1*value2

    zd1=zd(value1,value2)

    return ji/zd1

print(zx(18,20))
```

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]


[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.


::spantable::

| Country      | Address                                                  |
| ------------ | -------------------------------------------------------- |
| France @span | 8 Rue St Ferréol - 92190 City: Meudon (Île-de-France)    |
|              | 50 boulevard Amiral Courbet - 94310 Orly (Île-de-France) |
|              | ...                                                      |
|              | ...                                                      |
| Italy @span  | Str. S. Maurizio, 12, 10072 Caselle torinese TO          |
|              | S.S. Torino-Asti - 10026 Santena (TO)                    |
|              | ...                                                      |
| Poland @span | al. Jana Pawła II 22, 00-133 Warszawa                    |
|              | plac Trzech Krzyży 4/6, 00-535 Warszawa                  |
|              | ...                                                      |
|              | ...                                                      |

::end-spantable::


::timeline::

[
    {
        "title": "Launch",
        "content": "First implementation.",
        "icon": ":fontawesome-rocket:",
        "sub_title": "2022-Q1"
    },
    {
        "title": "One",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "icon": ":octicons-sun-16:",
        "key": "cyan",
        "sub_title": "2022-Q2"
    },
    {
        "title": "Two",
        "content": "Lorem ipsum dolor sit amet.",
        "icon": ":material-github:",
        "sub_title": "2022-Q3"
    },
    {
        "title": "Three",
        "content": "Lorem ipsum dolor sit amet.",
        "key": "pink",
        "sub_title": "2022-Q4"
    }
]

::/timeline::
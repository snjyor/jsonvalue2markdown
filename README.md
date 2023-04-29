对任意json格式的数据，转换成markdown格式的文本
## 安装

```bash
pip install jsonvalue2markdown
```

## 用法示例

```python
from jsonvalue2markdown import JsonValueToMarkdown
json_value = {
        "title": "标题",
        "context": {
            "subtitle": "副标题",
            "context1": "内容1",
            "context2": "内容2",
            "context6": [
                "内容3",
                "内容4",
                {
                    "context7": "内容5",
                    "context8": "内容6",
                },
                {"context9": "内容10"}
            ],
            "context3": "内容7",
            "context4": "https://www.test.demo.jpg",
        },
    }

mapping_dict = {
        "title": "h1",
        "subtitle": "h2",
        "context1": "p",
        "context2": "li",
        "context7": "li",
        "context8": "li",
        "context3": "li",
        "context4": "img",
        "context9": "p",
    }

markdown = JsonValueToMarkdown(
        json_value=json_value,
        mapping_dict=mapping_dict,
        title_level=3,
    ).convert()
print(markdown)
```

## 参数说明
| 参数           | 说明                            |
|:-------------|:------------------------------|
| json_value   | 需要转换为markdown格式的json数据        |
| mapping_dict | json数据中的key与markdown中的标签的映射关系 |
| title_level  | 标题的级别，从1开始，最大为6               |

## 输出结果
```markdown
#标题
##副标题
内容1

  * 内容2
内容3

内容4

  * 内容5
  * 内容6
内容10

  * 内容7
![](https://www.test.demo.jpg)
```

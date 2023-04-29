"""
对任意json格式的数据，转换成markdown格式的文本
MIT License
Created by: snjyor
Created on: 2023/4/29
"""


class JsonValueToMarkdown:
    """
    可以对json的值进行转换成markdown格式的文本
    支持两种方式的转换：
    1. 通过json的层级来指定markdown的标题的层级
    2. 通过mapping_dict来指定json的key和markdown的标题的映射关系
    """

    def __init__(self, json_value, mapping_dict=None, title_level=2):
        self.json_value = json_value
        self.mapping_dict = mapping_dict
        self.markdown = ""
        self.title_level = title_level
        self.tab = "  "  # 缩进
        self.list_tag = '* '  # 列表标签
        self.htag = '#'  # 标题标签
        self.table_tag = "|"  # 表格分隔符
        self.link_tag = "[]"  # 链接标签
        self.imgtag = "!"  # 图片标签
        self.tag_funcs = {
            "p": self._p2markdown,
            "li": self._li2markdown,
            "img": self._img2markdown,
            "": self._p2markdown
        }

    def convert(self):
        """
        入口函数
        :return:
        """
        self._convert(self.json_value)
        return self.markdown

    def _convert(self, json_value):
        """
        对json的值进行转换成markdown格式的文本
        :param json_value:
        :return:
        """
        if self.mapping_dict:
            return self._convert_with_mapping(json_value)
        else:
            return self._convert_with_level(json_value)

    def _convert_with_mapping(self, json_value):
        """
        通过mapping_dict来指定json的key和markdown的标题的映射关系
        :param json_value:
        :return:
        """
        if isinstance(json_value, dict):
            return self._convert_dict_with_mapping(json_value)
        elif isinstance(json_value, list):
            return self._convert_list(json_value)

    def _convert_dict_with_mapping(self, json_value):
        """
        通过mapping_dict来指定json的key和markdown的标题的映射关系
        :param json_value:
        :return:
        """
        for key, value in json_value.items():
            if isinstance(value, dict):
                self._convert_with_mapping(value)
            elif isinstance(value, list):
                self._convert_list(value)
            elif isinstance(value, (str, float, int)):
                tag = self.mapping_dict.get(key, "")
                if tag:
                    if tag.startswith("h"):
                        self._h2markdown(tag, value)
                    else:
                        if func := self.tag_funcs.get(tag, ""):
                            func(value)
                        else:
                            self._p2markdown(value)

    def _convert_list(self, json_list, level=1):
        """
        通过json的层级来指定markdown的标题的层级
        :param json_list:
        :param level:
        :return:
        """
        for item in json_list:
            if isinstance(item, dict):
                if self.mapping_dict:
                    self._convert_dict_with_mapping(item)
                else:
                    self._convert_dict_with_level(item, level=level)
            elif isinstance(item, list):
                self._convert_list(item)
            elif isinstance(item, (str, float, int)):
                self._p2markdown(item)

    def _convert_with_level(self, json_value):
        """
        通过json的层级来指定markdown的标题的层级
        :param json_value:
        :return:
        """
        if isinstance(json_value, dict):
            self._convert_dict_with_level(json_value)
        elif isinstance(json_value, list):
            self._convert_list(json_value)

    def _convert_dict_with_level(self, json_dict, level=1):
        """
        通过json的层级来指定markdown的标题的层级
        :param json_dict:
        :param level:
        :return:
        """
        tags = list(json_dict.keys())
        for tag in tags:
            value = json_dict.get(tag)
            if isinstance(value, (str, float, int)):
                if level <= self.title_level:
                    self.markdown = f"{self.markdown}{self.htag * level}{value}\n"
                else:
                    self.markdown = f"{self.markdown}{value}\n\n"
            elif isinstance(value, dict):
                self._convert_dict_with_level(value, level+1)
            elif isinstance(value, list):
                self._convert_list(value, level+1)

    def _p2markdown(self, value):
        """
        段落转markdown
        :param item:
        :return:
        """
        self.markdown = f"{self.markdown}{value}\n\n"

    def _h2markdown(self, tag, value):
        """
        标题转markdown
        :param item:
        :return:
        """
        self.markdown = f"{self.markdown}{self.htag * int(tag[-1])}{value}\n"

    def _li2markdown(self, value):
        """
        列表转markdown
        :param value:
        :return:
        """
        self.markdown = f"{self.markdown}{self.tab}{self.list_tag}{value}\n"

    def _img2markdown(self, value):
        """
        图片转markdown
        :param value:
        :return:
        """
        self.markdown = f"{self.markdown}{self.imgtag}[]({value})\n\n"


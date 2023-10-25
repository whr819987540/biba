"""
    定义客体的类.
    没有定义任何方法, 定义了一个data属性, 来存放该客体的数据.
"""
from base import Base


class Object(Base):
    def __init__(self, name, msg: str, security_level, category):
        super().__init__(name, security_level, category)
        self.msg = msg

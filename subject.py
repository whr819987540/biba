"""
    定义主体的类.
    包括三个方法: 读客体, 写客体, 调用主体, 均返回该操作是否执行成功以及执行结果.
"""
from base import Base
from object import Object
class Subject(Base):
    def __init__(self, name,security_level, category):
        super().__init__(name, security_level, category)

    def read_object(self,object)->bool:
        assert type(object) is Object, "type error"
        if object.integrity_level.dom(self.integrity_level):
            return True, f"{self.name} reads from {object.name}: {object.msg}"
        else:
            return False,None

    def write_object(self,object,msg:str)->bool:
        assert type(object) is Object, "type error"
        if self.integrity_level.dom(object.integrity_level):
            object.msg += msg
            return True, f"{self.name} writes into {object.name}: {msg}"
        
    def call(self,subject)->bool:
        assert type(subject) is Subject, "type error"
        if self.integrity_level.dom(subject.integrity_level):
            return True
        else:
            return False
        
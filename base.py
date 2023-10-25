"""
    完整性级别用(密级,范畴)来描述.
        密级: 0-5的某个整数, 数值越大密级越高.
        范畴: 一个集合.
        在完整性级别中定义了一个名为dom的方法, 表示当前对象是否支配另一个对象(传入参数), 该方法将返回True/False.
    BIBA模型与SIP策略中, 主体与客体的基类是Base.
        name: 名称.
        integrity_level: 完整性级别.
"""


class IntegrityLevel:
    def __init__(self, security_level, category):
        assert type(security_level) is int, "type error"
        assert security_level >= 0 and security_level <= 5, "security_level should in 0-5."
        assert type(category) is list, "type error"
        self.security_level = security_level
        self.category = set(category)

    def dom(self, object):
        assert type(object) is IntegrityLevel, "type error"
        if self.security_level >= object.security_level:
            if object.category.issubset(self.category):
                return True
            else:
                return False
        else:
            return False


class Base:
    def __init__(self, name, security_level, category):
        self.name = name
        self.integrity_level = IntegrityLevel(security_level, category)

"""
    测试BIBA模型的SIP安全策略.
    1   定义两个主体: s1(3,{"SE","CS"}) s2(4,{"SE","CS","MA"})
        定义两个客体: o1(2,{"SE","CS"}) o2(5,{"SE","CS"})
    2   s1对o1进行写操作
        s1对o1进行读操作
        s1对o2进行写操作
        s1对o2进行读操作
        s1对s2进行调用操作
        s2对s1进行调用操作
        s2对o1进行写操作
        s2对o1进行读操作
        s2对o2进行写操作
        s2对o2进行读操作
    3   最后打印出o1与o2的数据
"""
from object import Object
from subject import Subject

if __name__ == "__main__":
    s1 = Subject("s1", 3, ["SE", "CS"])
    s2 = Subject("s2", 4, ["SE", "CS", "MA"])
    o1 = Object("o1", "This is o1.\n", 2, ["SE", "CS"])
    o2 = Object("o2", "This is o2.\n", 5, ["SE", "CS"])
    
    # s1对o1进行写操作
    msg = "s1 writes into o1.\n"
    flag = s1.write_object(o1, msg)
    if flag:
        print(f"s1 writes into o1 successed: {msg}")
    else:
        print("s1 writes into o1 failed.")

    # s1对o1进行读操作
    flag, ret = s1.read_object(o1)
    if flag:
        print(f"s1 reads from o1: {ret}")
    else:
        print("s1 reads from o1 failed.")

    # s1对o2进行写操作
    msg = "s1 writes into o2.\n"
    flag = s1.write_object(o2, msg)
    if flag:
        print(f"s1 writes into o2 successed: {msg}")
    else:
        print("s1 writes into o2 failed.")

    # s1对o2进行读操作
    flag, ret = s1.read_object(o2)
    if flag:
        print(f"s1 reads from o2: {ret}")
    else:
        print("s1 reads from o2 failed.")

    # s1对s2进行调用操作
    flag = s1.call(s2)
    if flag:
        print("s1 calls s2 success.")
    else:
        print("s1 calls s2 failed.")

    # s2对s1进行调用操作
    flag = s2.call(s1)
    if flag:
        print("s2 calls s1 success.")
    else:
        print("s2 calls s1 failed.")

    # s2对o1进行写操作
    msg = "s2 writes into o1.\n"
    flag = s2.write_object(o1, msg)
    if flag:
        print(f"s2 writes into o1 successed: {msg}")
    else:
        print("s2 writes into o1 failed.")
        
    # s2对o1进行读操作
    flag, ret = s2.read_object(o1)
    if flag:
        print(f"s2 reads from o1: {ret}")
    else:
        print("s2 reads from o1 failed.")
        
    # s2对o2进行写操作
    msg = "s2 writes into o2.\n"
    flag = s2.write_object(o2, msg)
    if flag:
        print(f"s2 writes into o2 successed: {msg}")
    else:
        print("s2 writes into o2 failed.")
        
    # s2对o2进行读操作
    flag, ret = s2.read_object(o2)
    if flag:
        print(f"s2 reads from o2: {ret}")
    else:
        print("s2 reads from o2 failed.")

    print(f"o1 msg: {o1.msg}")
    print(f"o2 msg: {o2.msg}")
    
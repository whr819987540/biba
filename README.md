# BIBA模型介绍
biba模型是为了保证数据完整性， 该模型有多种安全策略， 如SIP（Strict Integrity Policy， 严格完整性策略）、RP环策略（Ring Policy， 环策略）、LWMPS（Low Watermark Policy for Subjects，针对主体的下限标记策略）、LWMPO（Low Watermark Policy for Objects，针对客体的下限标记策略）.

下面主要介绍SIP。SIP中主体与客体均有一个完整性级别：对主体而言， 完整性级别越高， 其可信性与可靠性越高；对客体而言， 完整性级别越高， 其重要性与安全性越高。dom表示支配， 是安全级别之间的一种关系。完整性级别可以用二元组即密级（数字）与范畴（集合）来描述。SIP有以下几条规则:

- 主体s可以对客体o进行“读”访问， 当且仅当i(o) dom i(s).
- 主体s可以对客体o进行“写”访问， 当且仅当i(s) dom i(o).
- 主体s1可以调用（invoke）主体s2， 当且仅当i(s1) dom i(s2).

# 程序设计
在base.py中定义了IntegrityLevel、Base两个类。IntegrityLevel表示完整性级别，用(密级，范畴)来描述。其中，密级是0-5的某个整数，数值越大密级越高；范畴是一个集合。在IntegrityLevel中定义了一个名为dom的方法，表示当前对象是否支配另一个对象(传入参数)，该方法将返回True/False。BIBA模型与SIP策略中，主体与客体的基类是Base，包括name（名称）与integrity_level（完整性级别）两个属性。

在object.py中定义了Object类，该类继承自Base类，其中没有定义任何方法，定义了一个data属性，来存放该客体的数据。

在subject.py中定义了Subject，该类继承自Base类，该类包括三个方法: 读客体，写客体，调用主体，均返回该操作是否执行成功以及执行结果。

在main.py中定义了测试流程。

# 测试流程
测试BIBA模型的SIP安全策略.

1 定义两个主体: s1(3，{"SE"，"CS"}) s2(4，{"SE"，"CS"，"MA"})
  
  定义两个客体: o1(2，{"SE"，"CS"}) o2(5，{"SE"，"CS"})

2 s1对o1进行写操作

  s1对o1进行读操作
  
  s1对o2进行写操作
  
  s1对o2进行读操作
  
  s1对s2进行调用操作
  
  s2对s1进行调用操作
  
  s2对o1进行写操作
  
  s2对o1进行读操作
  
  s2对o2进行写操作
  
  s2对o2进行读操作
  
3 最后打印出o1与o2的数据

# 测试结果
![image.png](https://raw.githubusercontent.com/whr819987540/pic/main/20231025163716.png)

```bash
(base) whr-pc-ubuntu@whrpc:~/code/biba$ python main.py 
s1 writes into o1 successed: s1 writes into o1.

s1 reads from o1 failed.
s1 writes into o2 failed.
s1 reads from o2: s1 reads from o2: This is o2.

s1 calls s2 failed.
s2 calls s1 success.
s2 writes into o1 successed: s2 writes into o1.

s2 reads from o1 failed.
s2 writes into o2 failed.
s2 reads from o2 failed.
o1 msg: This is o1.
s1 writes into o1.
s2 writes into o1.

o2 msg: This is o2.
```

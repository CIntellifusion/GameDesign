## Demo 



## 类设计

### 环境类

n$\times$n的方格

环境类之下可以按照地形派生子类： 平原，河流，山地，雪地etc.



### 建筑类

建筑类之下可以派生：主城，防御建筑，生产建筑，资源建筑。 

每个类之下可以派生小类。 

建筑类的基本属性包括：血量，功能函数，占地面积和形状，建造花费，建造时间。

功能函数包括产生

### 人员类

人员类包括士兵，工人，科学家等职业。

人员类也可以派生出非生命但是可移动的单位。  

人口系统可以设计的很复杂。 

简单版本：给钱就造。 

中等版本:  机械的限制条件，例如住房，资源等限制

高级版本：模拟真实人口，对人口再生产进行数据模拟，实行动态的生育率。

### 时间线

离散时间粒度

更小的时间粒度可以带来更大的操作空间。



### 科技树

科技树怎么设计呢？



#### 玩家类（操作界面）

玩家类需要两个子类： AI类和玩家类

一个玩家类需要掌握的信息包括：

1. 地图上的部分信息
2. 自己的资源信息
3. 建造选项
4. 进攻选项



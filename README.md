# GameDesign
Temporal repo for a Game design 

- author: shiqi diluvio 
- time : 20230608



## 现有框架

即时战略游戏类 + 强化学习AI 
机制设计，数值平衡，强化学习环境，游戏前端开发



## 现有思路
### 参考游戏

- arena
- mindustry
- red alert
- the age of empire
- the civilization VI
- others



### 进度更新

- 20230720

经过多次友好交流和口腔体操

我们达成一致，可以用transformer进行序列预测的方式避开强化学习环境采样的消耗。

在我们的预测里，智能程度从高到低的排序应该是： 强化学习>序列预测>模式识别



然后我们会首先实现模式识别和序列预测的部分。 等到有钱了再训练强化学习。 



我们的key motivation是 **把现有的即时战略手游从即时策略的泥潭中抽出来**

AI对兵种进行战术上diversity的应用是我们的核心卖点

### 

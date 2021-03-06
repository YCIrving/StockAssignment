# StockAssignment

本仓库是课程大作业，用到了BigQuant平台进行回测，所以以BQ开头的文件都需要复制到BigQuant上运行。详细注释在Notebook中

**基于RNN和决策树的多因子选股策略**

1. 本代码包括两部分，第一部分为验证不同RNN模型与预测准确率的关系，第二部分为使用RNN模型与决策树来进行股票交易；

2. 计算用到的各支股票的数据均在“stockData”中；

3. 前缀为JN的代码表示在Jupyter Notebook中运行（运行的相关事宜在代码中均已介绍），前缀为BQ的代码表示需要BigQuant平台支持才能运行，但可以在Jupyter中进行查看；

4. 根据回测数据显示，我们的模型在时间区间为2018-01-01至2018-06-24的收益率为-1.24%，基准收益率为-10.47%。考虑到贸易战的影响，模型在区间2018-01-01至2018-04-30的收益率为10.94%，基准收益率为-6.8%。由此可见，我们的模型提供的选股策略能够显著提升用户的收益率，但在遇到国际突发事件时，可能无法保证用户收益率为正。

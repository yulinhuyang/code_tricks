

## 第 5.3 节 Socket
#### 一、I/O 模型
##### 阻塞式 I/O
##### 非阻塞式 I/O
##### I/O 复用
##### 信号驱动 I/O
##### 异步 I/O
##### 五大 I/O 模型比较
#### 二、I/O 复用
##### select
##### poll
##### 比较
###### 1. 功能
###### 2. 速度
###### 3. 可移植性
##### epoll
##### 工作模式
###### 1. LT 模式
###### 2. ET 模式
##### 应用场景
###### 1. select 应用场景
###### 2. poll 应用场景
###### 3. epoll 应用场景
#### 参考资料
# 第 6 章 操作系统
## 第 6.1 节 计算机操作系统
### 概述
#### 基本特征
##### 1. 并发
##### 2. 共享
##### 3. 虚拟
##### 4. 异步
#### 基本功能
##### 1. 进程管理
##### 2. 内存管理
##### 3. 文件管理
##### 4. 设备管理
#### 系统调用
#### 大内核和微内核
##### 1. 大内核
##### 2. 微内核
#### 中断分类
##### 1. 外中断
##### 2. 异常
##### 3. 陷入

### 进程管理
#### 进程与线程
##### 1. 进程
##### 2. 线程
##### 3. 区别
#### 进程状态的切换
#### 进程调度算法
##### 1. 批处理系统
##### 2. 交互式系统
##### 3. 实时系统
#### 进程同步
##### 1. 临界区
##### 2. 同步与互斥
##### 3. 信号量
##### 4. 管程
#### 经典同步问题
##### 1. 读者-写者问题
##### 2. 哲学家进餐问题
#### 进程通信
##### 1. 管道
##### 2. FIFO
##### 3. 消息队列
##### 4. 信号量
##### 5. 共享存储
##### 6. 套接字
### 死锁
#### 必要条件
#### 处理方法
#### 鸵鸟策略
#### 死锁检测与死锁恢复
##### 1. 每种类型一个资源的死锁检测
##### 2. 每种类型多个资源的死锁检测
##### 3. 死锁恢复
#### 死锁预防
##### 1. 破坏互斥条件
##### 2. 破坏占有和等待条件
##### 3. 破坏不可抢占条件
##### 4. 破坏环路等待
#### 死锁避免
##### 1. 安全状态
##### 2. 单个资源的银行家算法
##### 3. 多个资源的银行家算法
### 内存管理
#### 虚拟内存
#### 分页系统地址映射
#### 页面置换算法
##### 1. 最佳
##### 2. 最近最久未使用
##### 3. 最近未使用
##### 4. 先进先出
##### 5. 第二次机会算法
##### 6. 时钟
#### 分段
#### 段页式
#### 分页与分段的比较
### 设备管理
#### 磁盘结构
#### 磁盘调度算法
##### 1. 先来先服务
##### 2. 最短寻道时间优先
##### 3. 电梯算法
### 链接
#### 编译系统
- 预处理阶段：处理以 # 开头的预处理命令；
#### 静态链接
#### 目标文件
#### 动态链接
### 参考资料
## 第 6.2 节 Linux
### 一、常用操作以及概念
#### 快捷键
#### 求助
##### 1. --help
##### 2. man
##### 3. info
##### 4. doc
#### 关机
##### 1. who
##### 2. sync
##### 3. shutdown
##### shutdown [-krhc] 时间 [信息]
##### PATH
#### sudo
#### 包管理工具
#### 发行版
#### VIM 三个模式
#### GNU
#### 开源协议
### 二、磁盘
#### 磁盘接口
##### 1. IDE
##### 2. SATA
##### 3. SCSI
##### 4. SAS
#### 磁盘的文件名
### 三、分区
#### 分区表
##### 1. MBR
##### 2. GPT
#### 开机检测程序
##### 1. BIOS
##### 2. UEFI
### 四、文件系统
#### 分区与文件系统
#### 组成
#### 文件读取
#### 磁盘碎片
#### block
#### inode
#### 目录
#### 日志
#### 挂载
#### 目录配置
### 五、文件
#### 文件属性
#### 文件与目录的基本操作
##### 1. ls
ls [-aAdfFhilnrRSt] file|dir

##### 2. cd
##### 3. mkdir
mkdir [-mp] 目录名称

##### 4. rmdir
##### 5. touch
touch [-acdmt] filename

##### 6. cp
##### 7. rm
rm [-fir] 文件或目录

##### 8. mv
mv [-fiu] source destination

mv [options] source1 source2 source3 .... directory

#### 修改权限
chmod [-R] xyz dirname/filename

chmod 754 .bashrc

chmod [ugoa]  [+-=] [rwx] dirname/filename

chmod a+w .bashrc

#### 默认权限
#### 目录的权限
#### 链接
ln [-sf] source_filename dist_filename

##### 1. 实体链接
ln /etc/crontab .

ll -i /etc/crontab crontab

2. 符号链接

ll -i /etc/crontab /root/crontab2

#### 获取文件内容
##### 1. cat
cat [-AbEnTv] filename

##### 2. tac
##### 3. more
##### 4. less
##### 5. head
head [-n number] filename

##### 6. tail
##### 7. od
#### 指令与文件搜索
##### 1. which
which [-a] command

##### 2. whereis
whereis [-bmsu] dirname/filename

##### 3. locate
locate [-ir] keyword

##### 4. find
find [basedir] [option]

### 六、压缩与打包
#### 压缩文件名
#### 压缩指令
##### 1. gzip
-# ： # 为数字的意思，代表压缩等级，数字越大压缩比越高，默认为 6
-# ： # 为数字的意思，代表压缩等级，数字越大压缩比越高，默认为 6
##### 2. bzip2
##### 3. xz
#### 打包
### 七、Bash
#### 特性
#### 变量操作
#### 指令搜索顺序
#### 数据流重定向
### 八、管道指令
#### 提取指令
#### 排序指令
#### 双向输出重定向
#### 字符转换指令
#### 分区指令
### 九、正则表达式
#### grep
#### printf
#### awk
### 十、进程管理
#### 查看进程
##### 1. ps
*ps -l*

ps aux

ps aux | grep threadx

##### 2. pstree
pstree -A

##### 3. top
top -d 2

##### 4. netstat
netstat -anp | grep port

#### 进程状态
#### SIGCHLD
#### wait()
#### waitpid()
#### 孤儿进程
#### 僵尸进程
### 参考资料
###  
# 第 7 章 算法
## 第 7.1 节 剑指 Offer 题解
### 3. 数组中重复的数字
#### 题目描述
#### 解题思路
### 4. 二维数组中的查找
#### 题目描述
#### 解题思路
### 5. 替换空格
#### 题目描述
#### 解题思路
### 6. 从尾到头打印链表
#### 题目描述
#### 解题思路
##### 使用递归
##### 使用头插法
##### 使用栈
### 7. 重建二叉树
#### 题目描述
#### 解题思路
### 8. 二叉树的下一个结点
#### 题目描述
#### 解题思路
### 9. 用两个栈实现队列
#### 题目描述
#### 解题思路
###  
### 10.1 斐波那契数列
#### 题目描述
#### 解题思路
### 10.2 矩形覆盖
#### 题目描述
#### 解题思路
### 10.3 跳台阶
#### 题目描述
#### 解题思路
### 10.4 变态跳台阶
#### 题目描述
#### 解题思路
##### 动态规划
##### 数学推导
### 11. 旋转数组的最小数字
#### 题目描述
#### 解题思路
### 12. 矩阵中的路径
#### 题目描述
#### 解题思路
### 13. 机器人的运动范围
#### 题目描述
#### 解题思路
### 14. 剪绳子
#### 题目描述
#### 解题思路
##### 贪心
##### 动态规划
### 15. 二进制中 1 的个数
#### 题目描述
##### n&(n-1)
##### Integer.bitCount()
### 16. 数值的整数次方
#### 题目描述
#### 解题思路
### 17. 打印从 1 到最大的 n 位数
#### 题目描述
#### 解题思路
### 18.1 在 O(1) 时间内删除链表节点
#### 解题思路
### 18.2 删除链表中重复的结点
#### 题目描述
#### 解题描述
### 19. 正则表达式匹配
#### 题目描述
#### 解题思路
###  
### 20. 表示数值的字符串
#### 题目描述
#### 解题思路
### 21. 调整数组顺序使奇数位于偶数前面
#### 题目描述
#### 解题思路
### 22. 链表中倒数第 K 个结点
#### 解题思路
### 23. 链表中环的入口结点
#### 题目描述
#### 解题思路
### 24. 反转链表
#### 解题思路
##### 递归
##### 迭代
### 25. 合并两个排序的链表
#### 题目描述
#### 解题思路
##### 递归
##### 迭代
### 26. 树的子结构
#### 题目描述
#### 解题思路
### 27. 二叉树的镜像
#### 题目描述
#### 解题思路
### 28 对称的二叉树
#### 题目描述
#### 解题思路
### 29. 顺时针打印矩阵
#### 题目描述
#### 解题思路
###  
### 30. 包含 min 函数的栈
#### 题目描述
#### 解题思路
### 31. 栈的压入、弹出序列
#### 题目描述
#### 解题思路
### 32.1 从上往下打印二叉树
#### 题目描述
#### 解题思路
### 32.2 把二叉树打印成多行
#### 题目描述
#### 解题思路
### 32.3 按之字形顺序打印二叉树
#### 题目描述
#### 解题思路
### 33. 二叉搜索树的后序遍历序列
#### 题目描述
#### 解题思路
### 34. 二叉树中和为某一值的路径
#### 题目描述
#### 解题思路
### 35. 复杂链表的复制
#### 题目描述
#### 解题思路
### 36. 二叉搜索树与双向链表
#### 题目描述
#### 解题思路
### 37. 序列化二叉树
#### 题目描述
#### 解题思路
### 38. 字符串的排列
#### 题目描述
#### 解题思路
### 39. 数组中出现次数超过一半的数字
#### 解题思路
###  
### 40. 最小的 K 个数
#### 解题思路
##### 快速选择
##### 大小为 K 的最小堆
### 41.1 数据流中的中位数
#### 题目描述
#### 解题思路
### 41.2 字符流中第一个不重复的字符
#### 题目描述
#### 解题思路
### 42. 连续子数组的最大和
#### 题目描述
#### 解题思路
### 43. 从 1 到 n 整数中 1 出现的次数
#### 解题思路
### 44. 数字序列中的某一位数字
#### 题目描述
#### 解题思路
### 45. 把数组排成最小的数
#### 题目描述
#### 解题思路
### 46. 把数字翻译成字符串
#### 题目描述
#### 解题思路
### 47. 礼物的最大价值
#### 题目描述
#### 解题思路
### 48. 最长不含重复字符的子字符串
#### 题目描述
#### 解题思路
### 49. 丑数
#### 题目描述
#### 解题思路
###  
### 50. 第一个只出现一次的字符位置
#### 题目描述
#### 解题思路
### 51. 数组中的逆序对
#### 题目描述
#### 解题思路
### 52. 两个链表的第一个公共结点
#### 题目描述
#### 解题思路
### 53. 数字在排序数组中出现的次数
#### 题目描述
#### 解题思路
### 54. 二叉查找树的第 K 个结点
#### 解题思路
### 55.1 二叉树的深度
#### 题目描述
#### 解题思路
### 55.2 平衡二叉树
#### 题目描述
#### 解题思路
### 56. 数组中只出现一次的数字
#### 题目描述
#### 解题思路
### 57.1 和为 S 的两个数字
#### 题目描述
#### 解题思路
### 57.2 和为 S 的连续正数序列
#### 题目描述
#### 解题思路
### 58.1 翻转单词顺序列
#### 题目描述
#### 解题思路
### 58.2 左旋转字符串
#### 题目描述
#### 解题思路
### 59. 滑动窗口的最大值
#### 题目描述
#### 解题思路
###  
### 60. n 个骰子的点数
#### 题目描述
#### 解题思路
##### 动态规划
##### 动态规划 + 旋转数组
### 61. 扑克牌顺子
#### 题目描述
#### 解题思路
### 62. 圆圈中最后剩下的数
#### 题目描述
#### 解题思路
### 63. 股票的最大利润
#### 题目描述
#### 解题思路
### 64. 求 1+2+3+...+n
#### 题目描述
#### 解题思路
### 65. 不用加减乘除做加法
#### 题目描述
#### 解题思路
### 66. 构建乘积数组
#### 题目描述
#### 解题思路
### 67. 把字符串转换成整数
#### 题目描述
#### 解题思路
### 68. 树中两个节点的最低公共祖先
#### 解题思路
##### 二叉查找树
##### 普通二叉树
###  
### 参考文献
## 第 7.2 节 Leetcode 题解
### 双指针
#### 1. 有序数组的 Two Sum
#### 2. 两数平方和
#### 3. 反转字符串中的元音字符
#### 4. 回文字符串
#### 5. 归并两个有序数组
#### 6. 判断链表是否存在环
#### 7. 最长子序列
####  
### 排序
#### 快速选择
#### 堆
##### 1. Kth Element
#### 桶排序
##### 1. 出现频率最多的 k 个元素
##### 2. 按照字符出现次数对字符串排序
#### 荷兰国旗问题
##### 1. 按颜色进行排序
####  
### 贪心思想
#### 1. 分配饼干
#### 2. 不重叠的区间个数
#### 3. 投飞镖刺破气球
#### 4. 根据身高和序号重组队列
#### 5. 买卖股票最大的收益
#### 6. 买卖股票的最大收益 II
#### 7. 种植花朵
#### 8. 判断是否为子序列
#### 9. 修改一个数成为非递减数组
#### 10. 子数组最大的和
#### 11. 分隔字符串使同种字符出现在一起
####  
### 二分查找
#### 1. 求开方
#### 2. 大于给定元素的最小元素
#### 3. 有序数组的 Single Element
#### 4. 第一个错误的版本
#### 5. 旋转数组的最小数字
#### 6. 查找区间
####  
### 分治
#### 1. 给表达式加括号
#### 2. 不同的二叉搜索树
####  
### 搜索
#### BFS
##### 1. 计算在网格中从原点到特定点的最短路径长度
##### 2. 组成整数的最小平方数数量
##### 3. 最短单词路径
#### DFS
##### 1. 查找最大的连通面积
##### 2. 矩阵中的连通分量数目
##### 3. 好友关系的连通分量数目
##### 4. 填充封闭区域
##### 5. 能到达的太平洋和大西洋的区域
#### Backtracking
##### 1. 数字键盘组合
##### 2. IP 地址划分
##### 3. 在矩阵中寻找字符串
##### 4. 输出二叉树中所有从根到叶子的路径
##### 5. 排列
##### 6. 含有相同元素求排列
##### 7. 组合
##### 8. 组合求和
##### 9. 含有相同元素的组合求和
##### 10. 1-9 数字的组合求和
##### 11. 子集
##### 12. 含有相同元素求子集
##### 13. 分割字符串使得每个部分都是回文数
##### 14. 数独
##### 15. N 皇后
####  
### 动态规划
#### 斐波那契数列
##### 1. 爬楼梯
##### 2. 强盗抢劫
##### 3. 强盗在环形街区抢劫
##### 4. 信件错排
##### 5. 母牛生产
#### 矩阵路径
##### 1. 矩阵的最小路径和
##### 2. 矩阵的总路径数
#### 数组区间
##### 1. 数组区间和
##### 2. 数组中等差递增子区间的个数
#### 分割整数
##### 1. 分割整数的最大乘积
##### 2. 按平方数来分割整数
##### 3. 分割整数构成字母字符串
#### 最长递增子序列
##### 1. 最长递增子序列
##### 2. 一组整数对能够构成的最长链
##### 3. 最长摆动子序列
#### 最长公共子序列
#### 0-1 背包
##### 1. 划分数组为和相等的两部分
##### 2. 改变一组数的正负号使得它们的和为一给定数
##### 3. 01 字符构成最多的字符串
##### 4. 找零钱的最少硬币数
##### 5. 找零钱的硬币数组合
##### 6. 字符串按单词列表分割
##### 7. 组合总和
#### 股票交易
##### 1. 需要冷却期的股票交易
##### 2. 需要交易费用的股票交易
##### 3. 只能进行两次的股票交易
##### 4. 只能进行 k 次的股票交易
#### 字符串编辑
##### 1. 删除两个字符串的字符使它们相等
##### 2. 编辑距离
##### 3. 复制粘贴字符
####  
### 数学
#### 素数分解
#### 整除
#### 最大公约数最小公倍数
##### 1. 生成素数序列
##### 2. 最大公约数
##### 3. 使用位操作和减法求解最大公约数
#### 进制转换
##### 1. 7 进制
##### 2. 16 进制
##### 3. 26 进制
#### 阶乘
##### 1. 统计阶乘尾部有多少个 0
#### 字符串加法减法
##### 1. 二进制加法
##### 2. 字符串加法
#### 相遇问题
##### 1. 改变数组元素使所有的数组元素都相等
#### 多数投票问题
##### 1. 数组中出现次数多于 n / 2 的元素
#### 其它
##### 1. 平方数
##### 2. 3 的 n 次方
##### 3. 乘积数组
##### 4. 找出数组中的乘积最大的三个数
####  
### 链表
####  1. 找出两个链表的交点
####  2. 链表反转
####  3. 归并两个有序的链表
####  4. 从有序链表中删除重复节点
####  5. 删除链表的倒数第 n 个节点
####  6. 交换链表中的相邻结点
####  7. 链表求和
####  8. 回文链表
####  9. 分隔链表
####  10. 链表元素按奇偶聚集
####  
### 树
#### 递归
##### 1. 树的高度
##### 2. 平衡树
##### 3. 两节点的最长路径
##### 4. 翻转树
##### 5. 归并两棵树
##### 6. 判断路径和是否等于一个数
##### 7. 统计路径和等于一个数的路径数量
##### 8. 子树
##### 9. 树的对称
##### 10. 最小路径
##### 11. 统计左叶子节点的和
##### 12. 相同节点值的最大路径长度
##### 13. 间隔遍历
##### 14. 找出二叉树中第二小的节点
#### 层次遍历
##### 1. 一棵树每层节点的平均数
##### 2. 得到左下角的节点
#### 前中后序遍历
##### 1. 非递归实现二叉树的前序遍历
##### 2. 非递归实现二叉树的后序遍历
##### 3. 非递归实现二叉树的中序遍历
#### BST
##### 1. 修剪二叉查找树
##### 2. 寻找二叉查找树的第 k 个元素
##### 3. 把二叉查找树每个节点的值都加上比它大的节点的值
##### 4. 二叉查找树的最近公共祖先
##### 5. 二叉树的最近公共祖先
##### 6. 从有序数组中构造二叉查找树
##### 7. 根据有序链表构造平衡的二叉查找树
##### 8. 在二叉查找树中寻找两个节点，使它们的和为一个给定值
##### 9. 在二叉查找树中查找两个节点之差的最小绝对值
##### 10. 寻找二叉查找树中出现次数最多的值
#### Trie
##### 1. 实现一个 Trie
##### 2. 实现一个 Trie，用来求前缀和
####  
### 栈和队列
#### 1. 用栈实现队列
#### 2. 用队列实现栈
#### 3. 最小值栈
#### 4. 用栈实现括号匹配
#### 5. 数组中元素与下一个比它大的元素之间的距离
#### 6. 循环数组中比当前元素大的下一个元素
####  
### 哈希表
#### 1. 数组中两个数的和为给定值
#### 2. 判断数组是否含有重复元素
#### 3. 最长和谐序列
#### 4. 最长连续序列
####  
### 字符串
#### 1. 字符串循环移位包含
#### 2. 字符串循环移位
#### 3. 字符串中单词的翻转
#### 4. 两个字符串包含的字符是否完全相同
#### 5. 计算一组字符集合可以组成的回文字符串的最大长度
#### 6. 字符串同构
#### 7. 回文子字符串个数
#### 8. 判断一个整数是否是回文数
#### 9. 统计二进制字符串中连续 1 和连续 0 数量相同的子字符串个数
####  
### 数组与矩阵
#### 1. 把数组中的 0 移到末尾
#### 2. 改变矩阵维度
#### 3. 找出数组中最长的连续 1
#### 4. 有序矩阵查找
#### 5. 有序矩阵的 Kth Element
#### 6. 一个数组元素在 [1, n] 之间，其中一个数被替换为另一个数，找出重复的数和丢失的数
#### 7. 找出数组中重复的数，数组值在 [1, n] 之间
#### 8. 数组相邻差值的个数
#### 9. 数组的度
#### 10. 对角元素相等的矩阵
#### 11. 嵌套数组
#### 12. 分隔数组
####  
### 图
#### 二分图
##### 1. 判断是否为二分图
#### 拓扑排序
##### 1. 课程安排的合法性
##### 2. 课程安排的顺序
#### 并查集
##### 1. 冗余连接
####  
### 位运算
#### 1. 统计两个数的二进制表示有多少位不同
#### 2. 数组中唯一一个不重复的元素
#### 3. 找出数组中缺失的那个数
#### 4. 数组中不重复的两个元素
#### 5. 翻转一个数的比特位
#### 6. 不用额外变量交换两个整数
#### 7. 判断一个数是不是 2 的 n 次方
#### 8.  判断一个数是不是 4 的 n 次方
#### 9. 判断一个数的位级表示是否不会出现连续的 0 和 1
#### 10. 求一个数的补码
#### 11. 实现整数的加法
#### 12. 字符串数组最大乘积
#### 13. 统计从 0 \~ n 每个数的二进制表示中 1 的个数
####  
## 第 7.3 节 算法
### 算法分析
#### 数学模型
#####  1. 近似
#####  2. 增长数量级
#####  3. 内循环
#####  4. 成本模型
#### 注意事项
#####  1. 大常数
#####  2. 缓存
#####  3. 对最坏情况下的性能的保证
#####  4. 随机化算法
#####  5. 均摊分析
#### ThreeSum
#####  1. ThreeSumSlow
#####  2. ThreeSumBinarySearch
#####  3. ThreeSumTwoPointer
#### 倍率实验
####  
### 排序
#### 约定
#### 选择排序
#### 冒泡排序
#### 插入排序
#### 希尔排序
#### 归并排序
##### 1. 归并方法
##### 2. 自顶向下归并排序
##### 3. 自底向上归并排序
#### 快速排序
##### 1. 基本算法
##### 2. 切分
##### 3. 性能分析
##### 4. 算法改进
######  4.1 切换到插入排序
######  4.2 三数取中
######  4.3 三向切分
##### 5. 基于切分的快速选择算法
#### 堆排序
##### 1. 堆
##### 2. 上浮和下沉
##### 3. 插入元素
##### 4. 删除最大元素
##### 5. 堆排序
###### 5.1 构建堆
###### 5.2 交换堆顶元素与最后一个元素
##### 6. 分析
#### 小结
##### 1. 排序算法的比较
##### 2. Java 的排序算法实现
####  
### 并查集
#### 前言
#### Quick Find
#### Quick Union
#### 加权 Quick Union
#### 路径压缩的加权 Quick Union
#### 比较
####  
### 栈和队列
#### 栈
##### 1. 数组实现
##### 2. 链表实现
#### 队列
####  
### 符号表
#### 前言
#### 初级实现
##### 1. 链表实现无序符号表
##### 2. 二分查找实现有序符号表
#### 二叉查找树
##### 1. get()
##### 2. put()
##### 3. 分析
##### 4. floor()
##### 5. rank()
##### 6. min()
##### 7. deleteMin()
##### 8. delete()
##### 9. keys()
##### 10. 分析
#### 2-3 查找树
##### 1. 插入操作
##### 2. 性质
#### 红黑树
##### 1. 左旋转
##### 2. 右旋转
##### 3. 颜色转换
##### 4. 插入
##### 5. 分析
#### 散列表
##### 1. 散列函数
##### 2. 拉链法
##### 3. 线性探测法
###### 3.1 查找
###### 3.2 插入
###### 3.3 删除
###### 3.5 调整数组大小
#### 小结
##### 1. 符号表算法比较
##### 2. Java 的符号表实现
##### 3. 稀疏向量乘法
####  
### 其它
#### 汉诺塔
#### 哈夫曼编码
####  
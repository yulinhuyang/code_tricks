# 第 1 章 数据库
## 第 1.1 节 数据库系统原理
### 一、事务
#### 概念
#### ACID
##### 1. 原子性（Atomicity）
##### 2. 一致性（Consistency）
##### 3. 隔离性（Isolation）
##### 4. 持久性（Durability）
#### AUTOCOMMIT
### 二、并发一致性问题
#### 丢失修改
#### 读脏数据
#### 不可重复读
#### 幻影读
### 三、封锁
#### 封锁粒度
#### 封锁类型
##### 1. 读写锁
##### 2. 意向锁
#### 封锁协议
##### 1. 三级封锁协议
##### 2. 两段锁协议
#### MySQL 隐式与显示锁定
### 四、隔离级别
#### 未提交读（READ UNCOMMITTED）
#### 提交读（READ COMMITTED）
#### 可重复读（REPEATABLE READ）
#### 可串行化（SERIALIZABLE）
### 五、多版本并发控制
#### 版本号
#### 隐藏的列
#### Undo 日志
#### 实现过程
##### 1. SELECT
##### 2. INSERT
##### 3. DELETE
##### 4. UPDATE
#### 快照读与当前读
##### 1. 快照读
##### 2. 当前读
### 六、Next-Key Locks
#### Record Locks
#### Gap Locks
#### Next-Key Locks
### 七、关系数据库设计理论
#### 函数依赖
#### 异常
#### 范式
##### 1. 第一范式 (1NF)
##### 2. 第二范式 (2NF)
##### 3. 第三范式 (3NF)
### 八、ER 图
#### 实体的三种联系
#### 表示出现多次的关系
#### 联系的多向性
#### 表示子类
### 参考资料
## 第 1.2 节 SQL
### 一、基础
### 二、创建表
### 三、修改表
### 四、插入
### 五、更新
### 六、删除
### 七、查询
#### DISTINCT
#### LIMIT
### 八、排序
### 九、过滤
### 十、通配符
### 十一、计算字段
### 十二、函数
#### 汇总
#### 文本处理
#### 日期和时间处理
#### 数值处理
### 十三、分组
### 十四、子查询
### 十五、连接
#### 内连接
#### 自连接
#### 自然连接
#### 外连接
### 十六、组合查询
### 十七、视图
### 十八、存储过程
### 十九、游标
### 二十、触发器
### 二十一、事务管理
### 二十二、字符集
### 二十三、权限管理
### 参考资料
## 第 1.3 节 Leetcode-Database 题解
### 595. Big Countries
#### Description
#### SQL Schema
#### Solution
### 627. Swap Salary
#### Description
#### SQL Schema
#### Solution
### 620. Not Boring Movies
#### Description
#### SQL Schema
#### Solution
### 596. Classes More Than 5 Students
#### Description
#### SQL Schema
#### Solution
### 182. Duplicate Emails
#### Description
#### SQL Schema
#### Solution
### 196. Delete Duplicate Emails
#### Description
#### SQL Schema
#### Solution
### 175. Combine Two Tables
#### Description
#### SQL Schema
#### Solution
### 181. Employees Earning More Than Their Managers
#### Description
#### SQL Schema
#### Solution
### 183. Customers Who Never Order
#### Description
#### SQL Schema
#### Solution
### 184. Department Highest Salary
#### Description
#### SQL Schema
#### Solution
### 176. Second Highest Salary
#### Description
#### SQL Schema
#### Solution
### 177. Nth Highest Salary
#### Description
#### SQL Schema
#### Solution
### 178. Rank Scores
#### Description
#### SQL Schema
#### Solution
### 180. Consecutive Numbers
#### Description
#### SQL Schema
#### Solution
### 626. Exchange Seats
#### Description
#### SQL Schema
#### Solution
## 第 1.4 节 MySQL
### 一、索引
#### B+ Tree 原理
##### 1. 数据结构
##### 2. 操作
##### 3. 与红黑树的比较
#### MySQL 索引
##### 1. B+Tree 索引
##### 2. 哈希索引
##### 3. 全文索引
##### 4. 空间数据索引
#### 索引优化
##### 1. 独立的列
##### 2. 多列索引
##### 3. 索引列的顺序
##### 4. 前缀索引
##### 5. 覆盖索引
#### 索引的优点
#### 索引的使用条件
### 二、查询性能优化
#### 使用 Explain 进行分析
#### 优化数据访问
##### 1. 减少请求的数据量
##### 2. 减少服务器端扫描的行数
#### 重构查询方式
##### 1. 切分大查询
##### 2. 分解大连接查询
### 三、存储引擎
#### InnoDB
#### MyISAM
#### 比较
### 四、数据类型
#### 整型
#### 浮点数
#### 字符串
#### 时间和日期
##### 1. DATETIME
##### 2. TIMESTAMP
### 五、切分
#### 水平切分
#### 垂直切分
#### Sharding 策略
#### Sharding 存在的问题
##### 1. 事务问题
##### 2. 连接
##### 3. ID 唯一性
### 六、复制
#### 主从复制
#### 读写分离
### 参考资料
## 第 1.5 节 Redis
### 一、概述
### 二、数据类型
#### STRING
#### LIST
#### SET
#### HASH
#### ZSET
### 三、数据结构
#### 字典
#### 跳跃表
### 四、使用场景
#### 计数器
#### 缓存
#### 查找表
#### 消息队列
#### 会话缓存
#### 分布式锁实现
#### 其它
### 五、Redis 与 Memcached
#### 数据类型
#### 数据持久化
#### 分布式
#### 内存管理机制
### 六、键的过期时间
### 七、数据淘汰策略
### 八、持久化
#### RDB 持久化
#### AOF 持久化
### 九、事务
### 十、事件
#### 文件事件
#### 时间事件
#### 事件的调度与执行
### 十一、复制
#### 连接过程
#### 主从链
### 十二、Sentinel
### 十三、分片
### 十四、一个简单的论坛系统分析
#### 文章信息
#### 点赞功能
#### 对文章进行排序
### 参考资料

# 第 2 章 Java
## 第 2.1 节 Java 基础
### 一、数据类型
#### 基本类型
#### 包装类型
#### 缓存池
### 二、String
#### 概览
#### 不可变的好处
#### String, StringBuffer and StringBuilder
#### String Pool
#### new String("abc")
### 三、运算
#### 参数传递
#### float 与 double
#### 隐式类型转换
#### switch
### 四、继承
#### 访问权限
#### 抽象类与接口
#### super
#### 重写与重载
### 五、Object 通用方法
#### 概览
#### equals()
#### hashCode()
#### toString()
#### clone()
### 六、关键字
#### final
#### static
### 七、反射
### 八、异常
### 九、泛型
### 十、注解
### 十一、特性
#### Java 各版本的新特性
#### Java 与 C++ 的区别
#### JRE or JDK
### 参考资料
## 第 2.2 节 Java 容器
### 一、概览
#### Collection
##### 1. Set
##### 2. List
##### 3. Queue
#### Map
### 二、容器中的设计模式
#### 迭代器模式
#### 适配器模式
### 三、源码分析
#### ArrayList
##### 1. 概览
##### 2. 扩容
##### 3. 删除元素
##### 4. Fail-Fast
##### 5. 序列化
#### Vector
##### 1. 同步
##### 2. 与 ArrayList 的比较
##### 3. 替代方案
#### CopyOnWriteArrayList
##### 读写分离
##### 适用场景
#### LinkedList
##### 1. 概览
##### 2. 与 ArrayList 的比较
#### HashMap
##### 1. 存储结构
##### 2. 拉链法的工作原理
##### 3. put 操作
##### 4. 确定桶下标
##### 5. 扩容-基本原理
##### 6. 扩容-重新计算桶下标
##### 7. 计算数组容量
##### 8. 链表转红黑树
##### 9. 与 HashTable 的比较
#### ConcurrentHashMap
##### 1. 存储结构
##### 2. size 操作
##### 3. JDK 1.8 的改动
#### LinkedHashMap
##### 存储结构
##### afterNodeAccess()
##### afterNodeInsertion()
##### LRU 缓存
#### WeakHashMap
##### 存储结构
##### ConcurrentCache
### 参考资料
## 第 2.3 节 Java 并发
### 一、线程状态转换
#### 新建（New）
#### 可运行（Runnable）
#### 阻塞（Blocked）
#### 无限期等待（Waiting）
#### 限期等待（Timed Waiting）
#### 死亡（Terminated）
### 二、使用线程
#### 实现 Runnable 接口
#### 实现 Callable 接口
#### 继承 Thread 类
#### 实现接口 VS 继承 Thread
### 三、基础线程机制
#### Executor
#### Daemon
#### sleep()
#### yield()
### 四、中断
#### InterruptedException
#### interrupted()
#### Executor 的中断操作
### 五、互斥同步
#### synchronized
#### ReentrantLock
#### 比较
#### 使用选择
### 六、线程之间的协作
#### join()
#### wait() notify() notifyAll()
#### await() signal() signalAll()
### 七、J.U.C - AQS
#### CountDownLatch
#### CyclicBarrier
#### Semaphore
### 八、J.U.C - 其它组件
#### FutureTask
#### BlockingQueue
#### ForkJoin
### 九、线程不安全示例
### 十、Java 内存模型
#### 主内存与工作内存
#### 内存间交互操作
#### 内存模型三大特性
##### 1. 原子性
##### 2. 可见性
##### 3. 有序性
#### 先行发生原则
##### 1. 单一线程原则
##### 2. 管程锁定规则
##### 3. volatile 变量规则
##### 4. 线程启动规则
##### 5. 线程加入规则
##### 6. 线程中断规则
##### 7. 对象终结规则
##### 8. 传递性
### 十一、线程安全
#### 不可变
#### 互斥同步
#### 非阻塞同步
##### 1. CAS
##### 2. AtomicInteger
##### 3. ABA
#### 无同步方案
##### 1. 栈封闭
##### 2. 线程本地存储（Thread Local Storage）
##### 3. 可重入代码（Reentrant Code）
### 十二、锁优化
#### 自旋锁
#### 锁消除
#### 锁粗化
#### 轻量级锁
#### 偏向锁
### 十三、多线程开发良好的实践
### 参考资料
## 第 2.4 节 Java 虚拟机
### 一、运行时数据区域
#### 程序计数器
#### Java 虚拟机栈
#### 本地方法栈
#### 堆
#### 方法区
#### 运行时常量池
#### 直接内存
### 二、垃圾收集
#### 判断一个对象是否可被回收
##### 1. 引用计数算法
##### 2. 可达性分析算法
##### 3. 方法区的回收
##### 4. finalize()
#### 引用类型
##### 1. 强引用
##### 2. 软引用
##### 3. 弱引用
##### 4. 虚引用
#### 垃圾收集算法
##### 1. 标记 - 清除
##### 2. 标记 - 整理
##### 3. 复制
##### 4. 分代收集
#### 垃圾收集器
##### 1. Serial 收集器
##### 2. ParNew 收集器
##### 3. Parallel Scavenge 收集器
##### 4. Serial Old 收集器
##### 5. Parallel Old 收集器
##### 6. CMS 收集器
##### 7. G1 收集器
### 三、内存分配与回收策略
#### Minor GC 和 Full GC
#### 内存分配策略
##### 1. 对象优先在 Eden 分配
##### 2. 大对象直接进入老年代
##### 3. 长期存活的对象进入老年代
##### 4. 动态对象年龄判定
##### 5. 空间分配担保
#### Full GC 的触发条件
##### 1. 调用 System.gc()
##### 2. 老年代空间不足
##### 3. 空间分配担保失败
##### 4. JDK 1.7 及以前的永久代空间不足
##### 5. Concurrent Mode Failure
### 四、类加载机制
#### 类的生命周期
#### 类加载过程
##### 1. 加载
##### 2. 验证
##### 3. 准备
##### 4. 解析
##### 5. 初始化
#### 类初始化时机
##### 1. 主动引用
##### 2. 被动引用
#### 类与类加载器
#### 类加载器分类
#### 双亲委派模型
##### 1. 工作过程
##### 2. 好处
##### 3. 实现
#### 自定义类加载器实现
### 参考资料
## 第 2.5 节 Java IO
### 一、概览
### 二、磁盘操作
### 三、字节操作
#### 实现文件复制
#### 装饰者模式
### 四、字符操作
#### 编码与解码
#### String 的编码方式
#### Reader 与 Writer
#### 实现逐行输出文本文件的内容
### 五、对象操作
#### 序列化
#### Serializable
#### transient
### 六、网络操作
#### InetAddress
#### URL
#### Sockets
#### Datagram
### 七、NIO
#### 流与块
#### 通道与缓冲区
##### 1. 通道
##### 2. 缓冲区
#### 缓冲区状态变量
#### 文件 NIO 实例
#### 选择器
##### 1. 创建选择器
##### 2. 将通道注册到选择器上
##### 3. 监听事件
##### 4. 获取到达的事件
##### 5. 事件循环
#### 套接字 NIO 实例
#### 内存映射文件
#### 对比
### 八、参考资料
# 第 3 章 系统设计
## 第 3.1 节 系统设计基础
### 一、性能
#### 性能指标
##### 1. 响应时间
##### 2. 吞吐量
##### 3. 并发用户数
#### 性能优化
##### 1. 集群
##### 2. 缓存
##### 3. 异步
### 二、伸缩性
#### 伸缩性与性能
#### 实现伸缩性
### 三、扩展性
### 四、可用性
#### 冗余
#### 监控
#### 服务降级
### 五、安全性
### 参考资料
## 第 3.2 节 分布式
### 一、分布式锁
#### 数据库的唯一索引
#### Redis 的 SETNX 指令
#### Redis 的 RedLock 算法
#### Zookeeper 的有序节点
##### 1. Zookeeper 抽象模型
##### 2. 节点类型
##### 3. 监听器
##### 4. 分布式锁实现
##### 5. 会话超时
##### 6. 羊群效应
### 二、分布式事务
#### 2PC
##### 1. 运行过程
###### 1.1 准备阶段
###### 1.2 提交阶段
##### 2. 存在的问题
###### 2.1 同步阻塞
###### 2.2 单点问题
###### 2.3 数据不一致
###### 2.4 太过保守
#### 本地消息表
### 三、CAP
#### 一致性
#### 可用性
#### 分区容忍性
#### 权衡
### 四、BASE
#### 基本可用
#### 软状态
#### 最终一致性
### 五、Paxos
#### 执行过程
##### 1. Prepare 阶段
##### 2. Accept 阶段
##### 3. Learn 阶段
#### 约束条件
##### 1\. 正确性
##### 2\. 可终止性
### 六、Raft
#### 单个 Candidate 的竞选
#### 多个 Candidate 竞选
#### 数据同步
### 参考
## 第 3.3 节 集群
### 一、负载均衡
#### 负载均衡算法
##### 1. 轮询（Round Robin）
##### 2. 加权轮询（Weighted Round Robbin）
##### 3. 最少连接（least Connections）
##### 4. 加权最少连接（Weighted Least Connection）
##### 5. 随机算法（Random）
##### 6. 源地址哈希法 (IP Hash)
#### 转发实现
##### 1. HTTP 重定向
##### 2. DNS 域名解析
##### 3. 反向代理服务器
##### 4. 网络层
##### 5. 链路层
### 二、集群下的 Session 管理
#### Sticky Session
#### Session Replication
#### Session Server
## 第 3.4 节 攻击技术
### 一、跨站脚本攻击
#### 概念
#### 攻击原理
#### 危害
#### 防范手段
##### 1. 设置 Cookie 为 HttpOnly
##### 2. 过滤特殊字符
### 二、跨站请求伪造
#### 概念
#### 攻击原理
#### 防范手段
##### 1. 检查 Referer 首部字段
##### 2. 添加校验 Token
##### 3. 输入验证码
### 三、SQL 注入攻击
#### 概念
#### 攻击原理
#### 防范手段
##### 1. 使用参数化查询
##### 2. 单引号转换
### 四、拒绝服务攻击
### 参考资料
## 第 3.5 节 缓存
### 一、缓存特征
#### 命中率
#### 最大空间
#### 淘汰策略
### 二、LRU
### 三、缓存位置
#### 浏览器
#### ISP
#### 反向代理
#### 本地缓存
#### 分布式缓存
#### 数据库缓存
#### Java 内部的缓存
#### CPU 多级缓存
### 四、CDN
### 五、缓存问题
#### 缓存穿透
#### 缓存雪崩
#### 缓存一致性
#### 缓存 “无底洞” 现象
### 六、数据分布
#### 哈希分布
#### 顺序分布
### 七、一致性哈希
#### 基本原理
#### 虚拟节点
### 参考资料
## 第 3.6 节 消息队列
### 一、消息模型
#### 点对点
#### 发布/订阅
### 二、使用场景
#### 异步处理
#### 流量削锋
#### 应用解耦
### 三、可靠性
#### 发送端的可靠性
#### 接收端的可靠性
### 参考资料
# 第 4 章 面向对象
## 第 4.1 节 设计模式
### 一、概述
### 二、创建型
#### 1. 单例（Singleton）
##### Intent
##### Class Diagram
##### Implementation
###### Ⅰ 懒汉式-线程不安全
###### Ⅱ 饿汉式-线程安全
###### Ⅲ 懒汉式-线程安全
###### Ⅳ 双重校验锁-线程安全
###### Ⅴ 静态内部类实现
###### Ⅵ 枚举实现
##### Examples
##### JDK
#### 2. 简单工厂（Simple Factory）
##### Intent
##### Class Diagram
##### Implementation
#### 3. 工厂方法（Factory Method）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 4. 抽象工厂（Abstract Factory）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 5. 生成器（Builder）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 6. 原型模式（Prototype）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
### 三、行为型
#### 1. 责任链（Chain Of Responsibility）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 2. 命令（Command）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 3. 解释器（Interpreter）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 4. 迭代器（Iterator）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 5. 中介者（Mediator）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 6. 备忘录（Memento）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 7. 观察者（Observer）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 8. 状态（State）
##### Intent
##### Class Diagram
##### Implementation
#### 9. 策略（Strategy）
##### Intent
##### Class Diagram
##### 与状态模式的比较
##### Implementation
##### JDK
#### 10. 模板方法（Template Method）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 11. 访问者（Visitor）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 12. 空对象（Null）
##### Intent
##### Class Diagram
##### Implementation
### 四、结构型
#### 1. 适配器（Adapter）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 2. 桥接（Bridge）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 3. 组合（Composite）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 4. 装饰（Decorator）
##### Intent
##### Class Diagram
##### Implementation
##### 设计原则
##### JDK
#### 5. 外观（Facade）
##### Intent
##### Class Diagram
##### Implementation
##### 设计原则
#### 6. 享元（Flyweight）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
#### 7. 代理（Proxy）
##### Intent
##### Class Diagram
##### Implementation
##### JDK
### 参考资料
## 第 4.2 节 面向对象思想
### 一、三大特性
#### 封装
#### 继承
#### 多态
### 二、类图
#### 泛化关系 (Generalization)
#### 实现关系 (Realization)
#### 聚合关系 (Aggregation)
#### 组合关系 (Composition)
#### 关联关系 (Association)
#### 依赖关系 (Dependency)
### 三、设计原则
#### S.O.L.I.D
##### 1. 单一责任原则
##### 2. 开放封闭原则
##### 3. 里氏替换原则
##### 4. 接口分离原则
##### 5. 依赖倒置原则
#### 其他常见原则
##### 1. 迪米特法则
##### 2. 合成复用原则
##### 3. 共同封闭原则
##### 4. 稳定抽象原则
##### 5. 稳定依赖原则
### 参考资料
# 第 5 章 网络
## 第 5.1 节 计算机网络
### 概述
#### 网络的网络
#### ISP
#### 主机之间的通信方式
#### 电路交换与分组交换
##### 1. 电路交换
##### 2. 分组交换
#### 时延
##### 1. 排队时延
##### 2. 处理时延
##### 3. 传输时延
##### 4. 传播时延
#### 计算机网络体系结构
##### 1. 五层协议
##### 2. OSI
##### 3. TCP/IP
##### 4. 数据在各层之间的传递过程
### 物理层
#### 通信方式
#### 带通调制
### 链路层
#### 基本问题
##### 1. 封装成帧
##### 2. 透明传输
##### 3. 差错检测
#### 信道分类
##### 1. 广播信道
##### 2. 点对点信道
#### 信道复用技术
##### 1. 频分复用
##### 2. 时分复用
##### 3. 统计时分复用
##### 4. 波分复用
##### 5. 码分复用
#### CSMA/CD 协议
#### PPP 协议
#### MAC 地址
#### 局域网
#### 以太网
#### 交换机
#### 虚拟局域网
### 网络层
#### 概述
#### IP 数据报格式
#### IP 地址编址方式
##### 1. 分类
##### 2. 子网划分
##### 3. 无分类
#### 地址解析协议 ARP
#### 网际控制报文协议 ICMP
##### 1. Ping
##### 2. Traceroute
#### 虚拟专用网 VPN
#### 网络地址转换 NAT
#### 路由器的结构
#### 路由器分组转发流程
#### 路由选择协议
##### 1. 内部网关协议 RIP
##### 2. 内部网关协议 OSPF
##### 3. 外部网关协议 BGP
### 传输层
#### UDP 和 TCP 的特点
#### UDP 首部格式
#### TCP 首部格式
#### TCP 的三次握手
#### TCP 的四次挥手
#### TCP 可靠传输
#### TCP 滑动窗口
#### TCP 流量控制
#### TCP 拥塞控制
##### 1. 慢开始与拥塞避免
##### 2. 快重传与快恢复
### 应用层
#### 域名系统
#### 文件传送协议
#### 动态主机配置协议
#### 远程登录协议
#### 电子邮件协议
##### 1. SMTP
##### 2. POP3
##### 3. IMAP
#### 常用端口
#### Web 页面请求过程
##### 1. DHCP 配置主机信息
##### 2. ARP 解析 MAC 地址
##### 3. DNS 解析域名
##### 4. HTTP 请求页面
### 参考链接
## 第 5.2 节 HTTP
#### 一 、基础概念
##### URI
##### 请求和响应报文
###### 1. 请求报文
###### 2. 响应报文
#### 二、HTTP 方法
##### GET
##### HEAD
##### POST
##### PUT
##### PATCH
##### DELETE
##### OPTIONS
##### CONNECT
##### TRACE
#### 三、HTTP 状态码
##### 1XX 信息
##### 2XX 成功
##### 3XX 重定向
##### 4XX 客户端错误
##### 5XX 服务器错误
#### 四、HTTP 首部
##### 通用首部字段
##### 请求首部字段
##### 响应首部字段
##### 实体首部字段
#### 五、具体应用
##### 连接管理
###### 1. 短连接与长连接
###### 2. 流水线
##### Cookie
###### 1. 用途
###### 2. 创建过程
###### 3. 分类
###### 4. 作用域
###### 5. JavaScript
###### 6. HttpOnly
###### 7. Secure
###### 8. Session
###### 9. 浏览器禁用 Cookie
###### 10. Cookie 与 Session 选择
##### 缓存
###### 1. 优点
###### 2. 实现方法
###### 3. Cache-Control
###### 4. 缓存验证
##### 内容协商
###### 1. 类型
###### 2. Vary
##### 内容编码
##### 范围请求
###### 1. Range
###### 2. Accept-Ranges
###### 3. 响应状态码
##### 分块传输编码
##### 多部分对象集合
##### 虚拟主机
##### 通信数据转发
###### 1. 代理
###### 2. 网关
###### 3. 隧道
#### 六、HTTPS
##### 加密
###### 1. 对称密钥加密
###### 2.非对称密钥加密
###### 3. HTTPS 采用的加密方式
##### 认证
##### 完整性保护
##### HTTPS 的缺点
#### 七、HTTP/2.0
##### HTTP/1.x 缺陷
##### 二进制分帧层
##### 服务端推送
##### 首部压缩
#### 八、HTTP/1.1 新特性
#### 九、GET 和 POST 比较
##### 作用
##### 参数
##### 安全
##### 幂等性
##### 可缓存
##### XMLHttpRequest
#### 参考资料


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


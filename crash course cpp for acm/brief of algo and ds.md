# brief of algo and ds

## 前言

本教程以「速成有关算法思想」为目的，不关注代码实现，不会按照传统意义上的从易到难安排顺序，而是将逻辑先后关系强的一些算法、思想、数据结构安排在一起，也会出现一些为了介绍一些重要算法而先唐突地插入前置知识的情况。

## 前缀和

对于数组 $a$，定义其前缀和数组 $s$，使得

$$
s_i = \sum_{j = 1}^{i} a_j
$$

有以下性质：

$$
s_i = \sum_{j = 1}^{i} a_j = a_i + \sum_{j = 1}^{i - 1} a_j = a_i + s_{i - 1}
$$

故前缀和数组可被 $\mathcal{O}\left(n\right)$ 地预处理。

又有以下性质：
$$
\sum_{i = l}^{r} a_i = s_r - s_{l - 1}
$$

故在预处理后，可以 $\mathcal{O}\left(1\right)$ 地回答 $a$ 的区间和。这是前缀和这一技巧最常见的应用。

前缀和不仅可以用于加法。实际上，它可以用于所有满足可差分性质的运算（乘法、按位异或等）。

## 差分

对于数组 $a$，定义其差分数组 $d$，使得

$$
d_i = \begin{cases}
	a_i & i = 1 \\
	a_i - a_{i - 1} & i > 1
\end{cases}
$$

有如下性质：

$$
a_i = \sum_{j = 1}^{i} d_j
$$

即 $a$ 为 $d$ 的前缀和数组。由此可见，前缀和与差分互为逆运算。

由这种关系，我们可以得到：如果使 $d_i \gets d_i + k$，则在数组 $a$ 中，第 $i$ 个元素及其之后的所有元素都会被加上 $k$。

思考题：

1. [AT_awc0024_d Highlighting with a Fluorescent Pen](https://atcoder.jp/contests/awc0024/tasks/awc0024_d)

2. [P4552 IncDec Sequence](https://www.luogu.com.cn/problem/P4552)

## 树状数组

上面的两种技巧只支持预处理后回答询问，无法做到边修改边询问。

树状数组通过构建与二进制技巧有关的前缀和结构，实现了 $\mathcal{O}\left(\log n\right)$ 单点加与区间查询的功能。

思考题：

1. [Lutece3389 箭串](https://cdoj.site/d/lutece/p/Lutece3389)

## 离散化

其实跟前面内容关系不大，主要是为了引入下面的权值树状数组。

离散化是指这样一种操作：将一个值域很大（如 $10^9$）的而长度在正常范围内（如 $10^5$）的序列中的元素建立一一映射，使得最终映射后，每个元素的映射值都不超过序列的长度，且映射值仍然保持与原来元素相同的偏序关系。

即本质上，离散化就是一种哈希操作，且保留了元素之间的偏序性质。

如序列 $a = [1, 5, 2026, 43, 1145, 5]$ 在离散化之后可映射为 $[1, 2, 5, 3, 4, 2]$。

通过排序或 `std::map` 实现离散化操作，时间复杂度为 $\mathcal{O}\left(n \log n\right)$。

## 桶

其实跟前面内容关系不大，主要是为了引入下面的权值树状数组。

对于一个序列 $a$，其所对应的桶是一个序列 $b$，满足下表为 $i$ 的元素的值是 $i$ 在 $a$ 中出现的次数，即

$$
b_i = \sum_{j = 1}^n [a_j = i]
$$

## 权值树状数组

权值树状数组即为用树状数组维护的一个桶。如果维护的序列值域很大，我们需要先进行离散化。

思考题：

1. [P1908 逆序对](https://www.luogu.com.cn/problem/P1908)

2. [T403456 排序算法](https://www.luogu.com.cn/problem/T403456)

## 树上带权修改、询问

### 树的一些基本性质

1. 一棵有 $n$ 个结点的树有 $n - 1$ 条边，且无环。

2. 除根外的每个结点有且仅有一个父亲。

3. 推论 1：每个结点到根的路径唯一。

4. 推论 2：树上任意两点间的路径唯一，且必定经过这两点的最近公共祖先（Lowest Common Ancenstor，一般直接简称「LCA」）。

思考题：

1. [P2420 让我们异或吧](https://www.luogu.com.cn/problem/P2420)

### 求 LCA

LCA 有多种求法，其中最常用的是倍增法，在 $\mathcal{O}\left(n \log n\right)$ 的预处理后，可以 $\mathcal{O}\left(\log n\right)$ 在线询问。

思考题：

1. [P4281 紧急集合 / 聚会](https://www.luogu.com.cn/problem/P4281)

### 树上差分

差分与前缀和的技巧可以迁移到树上使用，我们通常会维护一个点到其根节点的路径上的和。

思考题：

1. [P3258 松鼠的新家](https://www.luogu.com.cn/problem/P3258)
2. [P10931 闇の連鎖](https://www.luogu.com.cn/problem/P10931)

### 树的序列化

在进行 DFS 的过程中，不难发现，如果我们按顺序将遍历到的结点依次加到一个序列的末尾，那么对于任意一个结点，以其为根的子树中的所有结点在这个序列中都是连续的。由此，我们可以方便地处理一类在子树上的修改操作。

思考题：

1. [DFS 序 1](https://loj.ac/p/144)

---

从下面开始是一条新的串联线。

## 双指针

有一类这样的问题：在一段序列上，有一些区间是符合题目所要求的条件的，而有些不符合，题目通常需要求出符合条件的区间的数量或长度的最大/最小值。如果枚举区间的左右端点，时间复杂度至少为 $\mathcal{O}\left(n^2\right)$。我们可以通过这种方法避免枚举：维护两个指针 $l, r$ 作为区间的左右端点，并在不断移动 $l, r$ 的过程中维护区间的信息，统计答案。由于每个指针最多移动 $n$ 次，这保证了外层的时间复杂度为 $\mathcal{O}\left(n\right)$。

思考题：

1. [P1147 连续正整数和](https://www.luogu.com.cn/problem/P1147)

2. [P1638 逛画展](https://www.luogu.com.cn/problem/P1638)

3. [P4085 Haybale Feast G](https://www.luogu.com.cn/problem/P4085)

## 二分

二分法通常用来解决这样一类问题：在一群备选答案中，有些符合题意，有些不符合题意。而由于题目本身的性质，使得对于一个符合题意的答案，所有大于（小于）它的答案也都是符合题意的（我们一般称这种特殊性质为**单调性**），这时，题目往往会要我们求出符合题意的最小（最大）答案。

那么，我们可以这样解决这类问题：我们先锁定答案在 $[l, r]$ 范围内，然后取 $mid = \lfloor\frac{l + r}{2}\rfloor$，判断 $mid$ 是否是符合题意的答案，根据判断结果，将 $l \gets mid$ 或 $r \gets mid$，并进行下一轮判断，直到答案最终确定。

这种解决问题的方法是二分思想的应用，通常被称为**二分答案**。

思考题：

1. [P1083 借教室](https://www.luogu.com.cn/problem/P1083)

2. [P10235 舞萌基本练习](https://www.luogu.com.cn/problem/P10235)

对于上面双指针部分的区间计数问题，如果区间内的信息满足单调性（即对于两个左端点相同的区间，如果短区间符合题意，则长区间必符合题意的性质），则还可以 $\mathcal{O}\left(n\right)$ 枚举左端点，而二分求出最近的右端点统计答案。

思考如何用二分解决其中的第 1 题和第 3 题.

其中，如果第 3 题使用二分法，则需要使用一种数据结构多次快速查询区间内的最小元素，这里给出一种名为 ST 表的数据结构。对于一个静态的数组，ST 表在经过 $\mathcal{O}\left(n \log n\right)$ 的预处理后，可以 $\mathcal{O}\left(1\right)$ 地回答每次询问。

## 分治

将一个大的问题递归成两个（或多个）性质相同，但是规模更小的问题，在解决小问题后，在将两个小问题的答案合并，从而解决大问题。

这样的递归层数只有 $\mathcal{O}\left(\log n\right)$，一般可以接受。

例子：归并排序

## 线段树

一种结合了二分与分治思想的数据结构，具有强大的功能与通用性。

线段树是一颗这样的树：根节点维护区间 $[1, n]$ 的信息，左子结点维护区间 $[1, \lfloor\frac{1 + n}{2}\rfloor]$ 的信息，右子结点维护区间 $[\lfloor\frac{1 + n}{2}\rfloor + 1, n]$ 的信息，并依次递归的树。

这样的递归层数只有 $\mathcal{O}\left(\log n\right)$，一般可以接受。

结合 lazy-tag 技术可以处理多种区间修改区间查询问题。

思考题：

1. [P3372 【模板】线段树 1](https://www.luogu.com.cn/problem/P3372)

2. [DFS 序 2](https://loj.ac/p/145)

3. [P1253 扶苏的问题](https://www.luogu.com.cn/problem/P1253)

4. [P3373 【模板】线段树 2](https://www.luogu.com.cn/problem/P3373)

5. [P1558 色板游戏](https://www.luogu.com.cn/problem/P1558)

6. [ABC223F Parenthesis Checking](https://www.luogu.com.cn/problem/AT_abc223_f)

7. [P6327 区间加区间 sin 和](https://www.luogu.com.cn/problem/P6327)

8. [CF474F Ant colony](https://www.luogu.com.cn/problem/CF474F)

9. [GSS3 - Can you answer these queries III](https://www.luogu.com.cn/problem/SP1716)

10. [P2572 [SCOI2010] 序列操作](https://www.luogu.com.cn/problem/P2572)

## 树链剖分

这里仅介绍重链剖分。

在前面的讨论中，我们遇到了子树上操作的问题（可以用一般的 DFS 序解决），还遇到了路径上操作的问题（对于满足差分性质的操作，可以用树上差分解决），但路径上操作的问题却不能在线维护。因此，我们考虑改进对树序列化的方法，使得得出的序列更适合于在线维护路径上操作。

先做如下定义，对于一个结点 $u$，我们称其子树内所有的结点（包括 $u$ 自身）个数为子树 $u$ 的大小，记为 $\operatorname{size}\left(u\right)$。对于 $u$ 的所有直接子结点 $\operatorname{child}\left(u\right)$，我们定义 $\operatorname{child}\left(u\right)$ 中子树大小最大的一个直接子结点为 $u$ 的重儿子，记为 $\operatorname{heavy}\left(u\right)$，其余的直接子结点为轻儿子。$u$ 与其重儿子之间的边称为重边，与其轻儿子之间的边称为轻边。

考虑 $u$ 的任意一个轻儿子 $v$，必有 $\operatorname{size}\left(v\right) \times 2 < \operatorname{size}\left(u\right)$。进一步可推知，从任意结点向根的方向走，经过的轻边数不超过 $\mathcal{O}\left(\log n\right)$。

我们可以预先求出所有结点的重儿子。在对这棵树序列化的过程中，我们在遍历到每个结点时，都先进入它的重儿子，再进入它的轻儿子。这种方法得到的序列中，不仅一个子树内的结点在序列中的位置是连续的，而且一串连续的重边（我们称之为一段重链）在序列中的位置也是连续的。

这样，如果我们再记录每个结点所属重链的链顶（我们记为 $\operatorname{top}\left(u\right)$），我们就可以快速维护路径操作。

以在 $u, v$ 两结点之间的路径上所有结点做区间加为例，由于 $u$ 和 $\operatorname{top}\left(u\right)$ 之间的所有节点都在同一条重链上，这些结点在序列化后也处在连续的位置上，那么用线段树就可以在序列上维护区间加操作。之后，令 $u \gets \operatorname{top}\left(u\right)$，重复以上操作，直到 $u$ 与 $\operatorname{lca}\left(u, v\right)$ 处于同一条重链上（即 $\operatorname{top}\left(u\right) = \operatorname{top}\left(\operatorname{lca}\left(u, v\right)\right)$）为止。对于结点 $v$，做同样的操作。这样，我们将 $u, v$ 之间的路径划分为了至多 $\mathcal{O}\left(\log n\right)$ 条重链，并在这 $\mathcal{O}\left(\log n\right)$ 个区间上做了 $\mathcal{O}\left(\log n\right)$ 次区间加操作，每次操作的时间复杂度为 $\mathcal{O}\left(\log n\right)$，总时间复杂度为 $\mathcal{O}\left(\log^2 n\right)$.

思考题：

1. [P1505 旅游](https://www.luogu.com.cn/problem/P1505)

2. [P4092 树](https://www.luogu.com.cn/problem/P4092)

---

下面是图论部分和一些必要的数据结构基础。

## 栈

本质上是一个线性表，满足先进入栈中的元素必须后被弹出。

思考题：

1. [P1241 括号序列](https://www.luogu.com.cn/problem/P1241)

2. [P2201 数列编辑器](https://www.luogu.com.cn/problem/P2201)

## 队列

本质上是一个线性表，满足先进入队列中的元素必须先被弹出。

思考题：

1. [P2058 海港](https://www.luogu.com.cn/problem/P2058)

## 堆

又称优先队列。每次从堆中弹出的元素总是堆中最小（大）的元素。

插入与弹出的时间复杂度均为 $\mathcal{O}\left(\log n\right)$。

思考题：

1. [P1090 合并果子](https://www.luogu.com.cn/problem/P1090)

2. [P1323 删数问题](https://www.luogu.com.cn/problem/P1323)

3. [P1168 中位数](https://www.luogu.com.cn/problem/P1168)

4. [P1631 序列合并](https://www.luogu.com.cn/problem/P1631)

## DFS

DFS 全称 Depth First Search（深度优先搜索），即在搜索时优先访问深处的结点，而不是与当前结点同一层的结点。

DFS 的实现是基于栈的，具体为将当前访问到的结点推入栈中，而当该结点所有的后继（包括直接和间接）都被访问后，该点才从栈中弹出。

DFS 一般应用于树上或其他暴力搜索，在一般图中应用较少。

## BFS

BFS 全称 Breadth First Search（广度优先搜索），即在搜索时优先按层扩展。

由于这种按层扩展的特性，在边权全为 $1$ 的图上，可以使用 BFS 求最短路。

BFS 的实现一般基于队列，具体为每次取队首结点为当前结点，而将该结点的尚未入队的邻居推入队尾。这样的入队流程也保证了结点是按层被访问的。

思考题：

1. [P1443 马的遍历](https://www.luogu.com.cn/problem/P1443)

2. [P10234 找机厅](https://www.luogu.com.cn/problem/P10234)

3. [P10289 小杨的旅游](https://www.luogu.com.cn/problem/P10289)

4. [P1135 奇怪的电梯](https://www.luogu.com.cn/problem/P1135)

5. [P4667 Switch the Lamp On](https://www.luogu.com.cn/problem/P4667)

## 最短路

这里仅讨论无负权值的图。

几个有关最短路的性质：

1. 最短路径必无环。

2. 在一条最短路径上，起点到中间点的路径也是最短的。

### Dijkstra 算法

Dijkstra 算法是一种单源最短路算法。（即只能求出一个点到其他任意点的最短路径长，而不能求出任意两点的最短路径长）

流程如下：

1. 记结点 $u$ 到源点 $s$ 的距离为 $d_u$，定义布尔数组 $f$，若一个结点 $u$ 到 源点 $s$ 的最短路长度已被确定，则 $f_u = 1$，否则 $f_u = 0$；

2. 置 $d_s = 0$，对于其他所有结点 $u$，置 $d_u = +\infty$；

3. 在所有的仍未确定最短路长度的结点 $u$（即 $f_u = 0$）中，取出 $d_u$ 最小的一个，将其标记为最短路长度已确定（即 $f_u \gets 1$）；

4. 对于被取出的结点 $u$，考虑所有与其相邻的且仍未确定最短路的结点 $v$，尝试通过 $u$ 去更新 $v$ 的最短路长度（即 $d_v \gets \min\{d_v, d_u + w_{u, v}\}$）；

5. 若所有的点都已确定最短路长度，则算法结束，否则转 3。

复杂度分析：记 $n$ 为结点数，$m$ 为边数。我们一共需要确定 $n$ 个点的最短路长度，每次确定一个结点时，需要 $\mathcal{O}\left(n\right)$ 地检查所有结点，而尝试更新操作的次数不超过 $2m$，故总时间复杂度为 $\mathcal{O}\left(n^2 + m\right)$。

每次确定新的结点的过程是可以优化的。我们可以用一个小根堆存储所有结点的 $d$ 值，每次直接从堆顶取出堆中最小元素即可。而在使用堆优化时，我们需要在流程 4 中的更新操作时，将更新成功的结果存入堆中，因此，总时间复杂度应为 $\mathcal{O}\left(\left(n + m\right) \log n\right)$。

我们总是会选择堆优化的版本。

有些题会考察对该流程的理解，见思考题；许多的题会让你看不出来这道题是最短路，甚至让你看不出来这是图论题，需要自己建立图论模型；还有一些题看似是简单，实际上需要结合题目自身的特殊性质做优化。

思考题：

1. [P1342 请柬](https://www.luogu.com.cn/problem/P1342)

2. [P1462 通往奥格瑞玛的道路](https://www.luogu.com.cn/problem/P1462)

3. [P3044 Relocation S](https://www.luogu.com.cn/problem/P3044)

4. [P1144 最短路计数](https://www.luogu.com.cn/problem/P1144)

5. [P2865 Roadblocks G](https://www.luogu.com.cn/problem/P2865)

6. [P5810 文本的输入](https://www.luogu.com.cn/problem/P5810)

7. [P4568 飞行路线](https://www.luogu.com.cn/problem/P4568)

8. [CF1915G Bicycles](https://www.luogu.com.cn/problem/CF1915G)

9. [CF1846G Rudolf and CodeVid-23](https://www.luogu.com.cn/problem/CF1846G)

10. [CF1051F The Shortest Statement](https://www.luogu.com.cn/problem/CF1051F)

### Floyd 算法

思考题：

Floyd 算法是一种全源最短路算法（即算法执行后，可以查询任意两点之间的最短路），且可以处理负权边，时间复杂度为 $\mathcal{O}\left(n^3\right)$。

C++ 代码如下：

```cpp
const int inf = 1'000'000'000;
std::vector<std::vector<int>> dis(n, std::vector<int>(n, inf));
for (int i = 0; i < n; ++i) {
	dis[i][i] = 0;
}
for (int i = 0, u, v, w; i < m; ++i) {
	std::cin >> u >> v >> w;
	dis[u][v] = w;
}

for (int k = 0; k < n; ++k) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			dis[i][j] = std::min(dis[i][j], dis[i][k] + dis[k][j]);
		}
	}
}
```

算法的基本思路为：使用一个中间点去尝试更新其他点对之间的最短路长度，当所有的 $n$ 个点都做过中间点后，算法结束。本质上，这是一个动态规划的过程。

思考题：

1. [B3611 传递闭包](https://www.luogu.com.cn/problem/B3611)

2. [P1119 灾后重建](https://www.luogu.com.cn/problem/P1119)

## 并查集

一种可以动态维护结点之间的连通性的数据结构，支持如下操作：

1. 将两个结点之间连一条边。

2. 查询两个结点是否连通。

其内部通过「代表结点」来代表一整个连通块。起初，每个结点的代表结点显然为它自己。

我们使每个连通块形成一棵树的结构，将「代表结点」视为连通块的根节点，我们维护每个结点的父亲，这样我们从一个结点不断向上跳就可以最终到达根节点，这就是查询一个结点所在连通块的「代表结点」的方法。

对于连边操作，只需在需要连边的两个结点各自的「代表结点」之间连边即可；对于查询操作，只需检查两个结点的「代表结点」是否相同即可。

但当一颗树的深度过大时，查询「代表结点」的时间消耗会变得不可承受（最差时间复杂度为 $\mathcal{O}\left(n\right)$）。

可以做如下优化：对于一个结点 $u$，在查询其「代表结点」后，可以在其与「代表结点」之间直接连边；进一步地，查询路径上的所有结点（也即 $u$ 的所有祖先）都可以与「代表结点」之间直接连边。

这样的优化被称为「路径压缩」。Robert Tarjan 证明了经过「路径压缩」优化的并查集的时间复杂度为 $\mathcal{O}\left(\log n\right)$。

C++ 代码如下：

```cpp
class Dsu {
private:
	std::vector<int> fa;
public:
	Dsu(const int n): fa(std::vector<int>(n)) { for (int i = 0; i < n; ++i) fa[i] = i; }
	int get(const int cur) { return fa[cur] == cur ? cur : fa[cur] = get(fa[cur]); }
	void merge(const int x, const int y) { fa[get(y)] = get(x); }
	bool connected(const int x, const int y) { return get(x) == get(y); }
};
```

如果我们将边带上权值，则可以维护更多信息，详见思考题。

思考题：

1. [P1536 村村通](https://www.luogu.com.cn/problem/P1536)

2. [P1892 团伙](https://www.luogu.com.cn/problem/P1892)

3. [P1525 关押罪犯](https://www.luogu.com.cn/problem/P1525)

4. [P1197 星球大战](https://www.luogu.com.cn/problem/P1197)

5. [P1196 银河英雄传说](https://www.luogu.com.cn/problem/P1196)

6. [CF1851G Vlad and the Mountains](https://www.luogu.com.cn/problem/CF1851G)

## 最小生成树

对于一个连通图而言，生成树是指由原图的 $n$ 个结点和 $n - 1$ 条边组成的树，其保持了原图的连通性。

最小生成树即为选取的边权值总和最小的生成树。

## Kruskal 算法

Kruskal 算法是最常用的最小生成树算法，流程如下：

1. 起初，没有任何一条边被选入生成树中，我们使用一个并查集动态维护当前结点的连通性；

2. 将所有的 $m$ 条边按边权从小到大排序；

3. 遍历这些边，设当前边连接的是结点 $u, v$，如果结点 $u, v$ 当前尚未连通，则将当前边加入最小生成树中，并在并查集中连接 $u, v$。

不难得出时间复杂度为 $\mathcal{O}\left(m \log m\right)$。

## Prim 算法

Prim 算法与 Dijkstra 算法思想类似，流程如下：

1. 先确定生成树的根 $r$（可以是任意的），记结点 $u$ 到生成树的最小距离为 $d_r$，定义布尔数组 $f$，若结点 $u$ 已经在生成树中，则 $f_u = 1$，否则 $f_u = 0$；

2. 置 $d_r = 0$，对于其他所有结点 $u$，置 $d_u = +\infty$；

3. 在所有的仍不在生成树中的结点 $u$（即 $f_u = 0$）中，取出 $d_u$ 最小的一个，将其加入生成树（即 $f_u \gets 1$）；

4. 对于被取出的结点 $u$，考虑所有与其相邻的且仍不在生成树中的结点 $v$，尝试通过 $u$ 去更新 $v$ 到生成树的最小距离（即 $d_v \gets \min\{d_v, w_{u, v}\}$）；

5. 若所有的点都已被加入生成树，则算法结束，否则转 3。

如果使用堆优化，则时间复杂度为 $\mathcal{O}\left(\left(n + m\right)\log n\right)$。

在一般情况下，这个时间复杂度是劣于 Kruskal 算法的。但在图特别稠密（即 $m$ 很大，最大可取到 $\frac{n\left(n - 1\right)}{2}$）的情况下，这个时间复杂度会略优于 Kruskal 算法。但又因为 Kruskal 大概率也可以 handle 这样的数据范围，所以在绝大多数的情况下我们都会选择 Kruskal 算法。

思考题：

1. [P1111 修复公路](https://www.luogu.com.cn/problem/P1111)

2. [P2323 公路修建问题](https://www.luogu.com.cn/problem/P2323)

3. [P4047 部落划分](https://www.luogu.com.cn/problem/P4047)

4. [AT_abc270_f Transportation](https://www.luogu.com.cn/problem/AT_abc270_f)

5. [P1967 货车运输](https://www.luogu.com.cn/problem/P1967)

6. [P14362 道路修复](https://www.luogu.com.cn/problem/P14362)

7. [P14080 最小生成树](https://www.luogu.com.cn/problem/P14080)

8. [CF1857G Counting Graphs](https://www.luogu.com.cn/problem/CF1857G)

9. [CF1687B Railway System](https://www.luogu.com.cn/problem/CF1687B)

## 拓扑排序

考虑这样一类实际问题：做一件事 $v$ 之前需要先完成其他的某些事情 $u$，而不会出现成环的先后顺序，求出一种可能的做事先后序列。

如果我们将事件视为结点，并从先做的事件向后做的事件连一条有向边，整张图就是一个有向无环图（Directed Acyclic Graph，DAG），拓扑排序算法可以求解一种可能的先后顺序。

具体流程如下：

1. 统计每个点的入度（即有多少条有向边指向该点），点 $u$ 的入度记为 $ind_u$；

2. 维护一个队列，起初，将所有入度为 $0$ 的点入队；

3. 取出队首 $u$，对于 $u$ 所指向的所有结点 $v$，执行 $ind_v \gets ind_v - 1$，如果在执行后有 $ind_v = 0$，则将 $v$ 入队；

4. 重复执行 3，直到队列为空，此时各结点出队的顺序记为一种可能顺序；

易知时间复杂度为 $\mathcal{O}\left(n + m\right)$。

我们可以按照拓扑序递推在结点间一些信息，如到达某节点的最短时间、到达某节点的路径数等。实际上，这就是一种动态规划（Dynamic Programming，DP）算法。

思考题：

1. [B3644 【模板】拓扑排序 / 家谱树](https://www.luogu.com.cn/problem/B3644)

2. [P2712 摄像头](https://www.luogu.com.cn/problem/P2712)

3. [P1807 最长路](https://www.luogu.com.cn/problem/P1807)

4. [P3183 食物链](https://www.luogu.com.cn/problem/P3183)

5. [P1347 排序](https://www.luogu.com.cn/problem/P1347)

6. [P1685 游览](https://www.luogu.com.cn/problem/P1685)

7. [CF1593E Gardener and Tree](https://www.luogu.com.cn/problem/CF1593E)

## e-DCC 与 v-DCC

暂略。

## SCC

暂略。

## 网络流

暂略。

---

## DP

### 引入

动态规划（Dynamic Programming，DP）通常用于解决最优化问题和计数问题，以及一些期望和概率问题。我们以求解斐波那契数列为例，引入记忆化搜索和 DP 的相关概念。

定义斐波那契数列：

$$
f_n = \begin{cases}
	1 & n \le 2 \\
	f_{n - 1} + f_{n - 2} & n > 2
\end{cases}
$$

不难根据定义写出递归求解代码：

```cpp
int f(const int n) {
	return n <= 2 ? 1 : f(n - 1) + f(n - 2);
}
```

求解的时间复杂度为 $\mathcal{O}\left(2^n\right)$。效率如此糟糕的原因是有许多求解过程是重复的，如求解 $f_n$ 时我们需要求解 $f_{n - 2}$，而求解 $f_{n - 1}$ 时我们也需要求解 $f_{n - 2}$，造成了重复计算。

我们可以通过记录下已经求解出的 $f_{n}$ 值，下一次需要使用时直接读取记录即可，避免了重复计算。

改进后的代码如下：

```cpp
const int max_n = 30;
int memory[max_n + 5];

int f(const int n) {
	if (n <= 2) {
		return 1;
	}
	if (memory[n] != 0) {
		return memory[n];
	}
	return memory[n] = f(n - 1) + f(n - 2);
}
```

时间复杂度为 $\mathcal{O}\left(n\right)$，而空间复杂度为 $\mathcal{O}\left(n\right)$。

上面这种方法就可以看作是动态规划的其中一种实现方法：「记忆化搜索」。

可以看出，动态规范通过使用额外的空间记录已经求出的答案，以方便在后续求解时直接取用，避免冗余的重复求解，其本质就是「以空间换时间」。

动态规划的第二种实现方法是递推。对于本例，递推代码如下。

```cpp
int n; std::cin >> n;
std::vector<int> f(n + 1);
f[1] = f[2] = 0;
for (int i = 3; i <= n; ++i) {
	f[i] = f[i - 1] + f[i - 2];
}
```

两种实现方式本质上是没有区别的。

动态规划问题有三个组成要素：**阶段**、**状态**、**决策**。下面以两道具体的例题讲解这三个组成要素的具体含义。

1. [AT_abc306_d Poisonous Full-Course](https://www.luogu.com.cn/problem/AT_abc306_d)

解析：菜是一道一道上的，吃或不吃都会被撤走，不会回来（我们一般称之为动态规划问题的「无后效性」），这自然地将用餐流程划分成了不同**阶段**；高桥的身体状况有好有坏，这可以作为动态规划算法设计的**状态**；对于每道菜，高桥都要做出吃或不吃的**决策**。

我们可以设 $dp_{i, j} \left(1 \le i \le n, j \in \{0, 1\}\right)$ 表示在对第 $i$ 道菜做出决策后，且高桥的身体状况为舒适（用 $1$ 表示）或不适（用 $0$ 表示）时，所品尝的菜肴的美味程度之和的最大值。

这里的第一维 $i$ 体现了阶段，第二维 $j$ 体现了状态，而决策则体现在我们对答案的递推转移中。请思考如何递推求出 $dp_{i, j}$。

2. [P1048 采药](https://www.luogu.com.cn/problem/P1048)

解析：这道题看起来不像上一题有阶段划分和状态区分，但我们依然可以人为地设计阶段和状态。

设 $dp_{i, j}$ 表示在考虑前 $i$ 种草药采或不采的决策后，且总花费的时间不超过 $j$，采到的草药的最大价值。

同样的，第一维 $i$ 体现了阶段，第二维 $j$ 体现了状态，决策体现在我们对答案的递推转移中。请思考如何递推求出 $dp_{i, j}$。

DP 题的 $80\%$ 的重点和难点都在设计状态上。在设计好一个合理、便于转移递推的状态后，后续的转移决策往往都比较简单。

### 线性状态 DP

引入部分的两道例题都是线性状态 DP，接下来继续讲解几道思考题以巩固。

思考题：

1. [AT_dp_b Frog 2](https://www.luogu.com.cn/problem/AT_dp_b)

2. [AT_dp_c Vacation](https://www.luogu.com.cn/problem/AT_dp_c)

3. [AT_dp_h Grid 1](https://www.luogu.com.cn/problem/AT_dp_h)

4. [P2758 编辑距离](https://www.luogu.com.cn/problem/P2758)

5. [AT_dp_m Candies](https://www.luogu.com.cn/problem/AT_dp_m)

6. [AT_dp_i Coins](https://www.luogu.com.cn/problem/AT_dp_i)

7. [AT_abc339_e Smooth Subsequence](https://www.luogu.com.cn/problem/AT_abc339_e)

### 区间 DP

一类以区间左右端点位置作为状态的 DP 问题。通常，这类问题以区间长度从小到大划分阶段。

思考题：

1. [P1775 石子合并（弱化版）](https://www.luogu.com.cn/problem/P1775)

2. [P10236 排卡](https://www.luogu.com.cn/problem/P10236)

3. [P1063 能量项链](https://www.luogu.com.cn/problem/P1063) 

### 树上 DP

树具有良好的递归结构，这实际上为动态规划做了极为自然的状态划分：$90\%$ 的树上 DP 都是以子树作为阶段划分，且从子结点点向父结点做递推转移。

例如求一棵子树的大小就是一种 DP 过程，其转移为：

$$
\operatorname{size}\left(u\right) = 1 + \sum_{v \in \operatorname{son}\left(u\right)} \operatorname{size}\left(v\right)
$$

又如求一棵树的直径（即最长链）的长度，我们可以设 $dp_{u, 0/1}$ 表示在结点 $u$ 子树内，不以结点 $u$ 为链头（用 $0$ 表示）或以结点 $u$ 为链头（用 $1$ 表示）的最长链长度。

以结点 $u$ 为链头的情况是容易转移的。

$$
dp_{u, 1} = \max_{v \in \operatorname{son}\left(u\right)} \{dp_{v, 1}\} + 1
$$

不以结点 $u$ 为链头的情况有两种决策：结点 $u$ 是最长链的中间结点或结点 $u$ 不在最长链上。

$$
dp_{u, 0} = \max\{\max_{s, t \in \operatorname{son}\left(u\right), s \neq t} \{dp_{s, 1} + dp_{t, 1}\} + 1, \max_{v \in \operatorname{son}\left(u\right)} \{dp_{v, 0}\}\}
$$

思考题：

1. [AT_dp_p Independent Set](https://www.luogu.com.cn/problem/AT_dp_p)

2. [AT_abc447_f Centipede Graph](https://www.luogu.com.cn/problem/AT_abc447_f)

3. [Lutece3385 另一道树上问题](https://cdoj.site/d/lutece/p/Lutece3385)

4. [P3478 STA-Station](https://www.luogu.com.cn/problem/P3478)

5. [CF1187E Tree Painting](https://www.luogu.com.cn/problem/CF1187E)

6. [P2986 Great Cow Gathering G](https://www.luogu.com.cn/problem/P2986)

7. [T403457 购买车券](https://www.luogu.com.cn/problem/T403457)

### DAG 上的 DP

见图论部分

### 状压 DP

有这样一类问题，我们需要以某样物品是否已经被选中作为状态。如果有 $n$ 样物品，则状态数为 $2^n$。

如果我们以二进制数表示状态，则可以通过数组操作轻松访问每个状态的答案，进行 DP。

思考题：

1. [P1171 售货员的难题](https://www.luogu.com.cn/problem/P1171)

2. [P3052 Cows in a Skyscraper G](https://www.luogu.com.cn/problem/P3052)

3. [P2915 Mixed Up Cows G](https://www.luogu.com.cn/problem/P2915)

4. [P1879 Corn Fields G](https://www.luogu.com.cn/problem/P1879)

5. [Lutece1805 矩阵](https://cdoj.site/d/lutece/p/Lutece1805)

6. [AT_abc187_f Close Group](https://www.luogu.com.cn/problem/AT_abc187_f)

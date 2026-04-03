$3$ 条有关同余的性质：

1. 如果 $a \equiv b \pmod p$，那么 $a \pm c \equiv b \pm c \pmod p$

2. 如果 $a \equiv b \pmod p$，那么 $a \times c \equiv b \times c \pmod p$

其中，$p$ 不要求为质数。

3. 当 $p$ 为质数时，有 $a^{p - 1} \equiv 1 \pmod p$（费马小定理，证明见《算法竞赛进阶指南》 P149）

那么，性质 $3$ 可用于在模意义下表示分数。具体地，我们一般认为

$$
\frac{a}{b} \equiv a \times b^{p - 2} \pmod p
$$

$3$ 个题目中常见的质数：$998,244,353$，$10^9 + 7$，$10^9 + 9$。

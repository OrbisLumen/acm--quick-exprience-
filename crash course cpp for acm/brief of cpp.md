# brief of cpp

## OOP

`struct` 与 `class` 都是 C++ 中定义类的方法，区别在与 `struct` 默认 `public`，`class` 默认 `private`（即封装）。

格式如下：

```cpp
class MyClass {
private: // defalut
	
	type private_val;
	type private_func();

public:

	type public_val;
	MyClass() {
		// init
	}
	type public_func() {
		// able to access private val.
	}

private:

	type private_val_1;
};

type MyClass::private_func() {

}
```

其中 `MyClass()` 是构造函数（即初始化函数），在对象的实例被创建时默认调用。

### 运算符重载

可以使运算符发挥自定义的作用，例子如下：

```cpp
int gcd(const int a, const int b) {
	return b ? gcd(b, a % b) : a;
}

struct Fraction {
	int top, bottom;
	Fraction(const int top, const int bottom): top(top), bottom(bottom) {}
};

Fraction operator+(const Fraction &a, const Fraction &b) {
	Fraction res(a.top * b.bottom + b.top * a.bottom, a.bottom * b.bottom);
	const int g = gcd(res.bottom, res.top);
	res.bottom /= g, res.top /= g;
	return res;
}

Fraction operator+(const Fraction &a, const int b) {
	return a + Fraction(b, 1);
}
```

### 泛型（template）

暂略。

## namespace（命名空间）

命名空间用于分隔同名变量、函数、对象等。

以下代码用于声明一个新的命名空间：

```cpp
namespace my_namespace {
	type val;

	type func(type prag);
	
	class ClassName {
		type val;
		type func(type prag);
	};
};
```

以下代码用于包含一个命名空间：

```cpp
using namespace my_namespace;
```

### std

是 C++ 自带的一个命名空间，包含 `std::max()` `std::min()` `std::swap()` `std::sort()` 等实用函数，STL 标准库容器也包含在其中。

## IO

### C 风格

同 C。

### std::cin 与 std::cout

`std::cin` 与 `std::cout` 均包含在命名空间 `std` 中。

前置知识：`<<` 与 `>>` 运算符，运算符重载。

`std::cout` 格式如下：

```cpp
std::cout << int << double << std::string << char;
```

`std::cin` 格式如下：

```cpp
std::cin >> int >> double >> std::string >> char;
```

使用 `std::cin` 对输出的小数保留指定位数的小数方法如下：

```cpp
int digits;
double value;
std::cout << std::fixed << std::setpresition(digits) << value << '\n';
```

注：需要导入 `<iomanip>` 库。

以下代码用于关闭输入输出同步流，从而加速 `std::cin` 与 `std::cout`，通常放在 `main()` 函数开头。

```cpp
std::ios::sync_with_stdio(false);
std::cin.tie(nullptr);
std::cout.tie(nullptr);
```

**注意：关闭输入输出同步流后，一份代码内不能同时使用 `std::cin`，`std::cout` 与 C 风格 IO（`scanf()` `printf()` `getchar()` `putchar()` 等函数）**

### 多测处理

在一类单个测试点内有多组测试数据而没有知名测试数据组数的题目中，可以使用以下方式输入：

```cpp
#include <iostream>

int main() {
	
	int n;
	// C style
	while (scnaf("%d", &n) != EOF) {
		// solve a single test case
	}

	// C++ style
	while (std::cin >> n) {
		// solve a single test case
	}

	return 0;
}
```

### std::string

略。

## STL（standard template lib）

是 C++ 提供的一类数据结构和函数。

### std::array

静态的数组，格式如下：

```cpp
std::array<double, 10> double_array;
std::array<int, 20> int_array;
```

### std::vector

动态的数组，格式如下：

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {

	// init
	std::vector<int> a(3); // a = { 0, 0, 0 };
	std::vector<int> b(3, 1); // b = { 1, 1, 1 };
	std::vector<int> c(a); // c = a;
	std::vector<std::vector<int>> adj(3); // adj = { {}, {}, {} };
	std::vector<std::vector<int>> matrix(2, std::vector<int>(2, 1)); // matrix = { {1, 1}, {1, 1} };

	// access elements
	std::cout << a[2] << '\n';

	// push and pop the elements in the end of the vector (O(1))
	b.push_back(4); // b = { 1, 1, 1, 4 };
	c.pop_back(); // c = { 1, 1 };
	matrix.push_back(std::vector<int>(6));

	// sort of vector
	std::sort(b.begin(), b.end()); // increase
	std::sort(c.begin(), c.end(), std::greater<int>()); // decrease

	// get the size of vector
	std::cout << adj.size() << '\n';

	return 0;
}
```

其中，最重要的是，`push_back()` 与 `pop_back()` 方法均为 $\mathcal{O}\left(1\right)$ 的。

### std::pair

将两种指定类型的数据进行绑定，示例代码如下：

```cpp
std::pair<char, int> my_pair = { 'A', 10 };

const int n = 6;
std::vector<std::pair<int, int>> a(n);
for (int i = 0; i < n; ++i) {
	std::cin >> a[i].first >> a[i].second;
}
```

其中，上半部分即为 `std::pair` 的初始化方式，下半部分即为访问被绑定元素的方法（即调用 `first` 与 `second` 属性）。

### std::set

`std::set` 顾名思义即为集合，特征如下：

- 有序性：这使得在 `std::set`（底层实现为平衡树）中增删元素均为 $\mathcal{O}\left(\log n\right)$ 的。当然与之相对的还有 `std::unordered_set`（底层实现为哈希表（散列表）），其增删元素均为 $\mathcal{O}\left(1\right)$ 的。

- 相异性：与之相对的同样有 `std::multiset`。

`std::set` 的初始化及增删方法如下：

```cpp
std::set<int> set; // init
set.insert(4); // O(log n)
set.insert(2); // set = { 2, 4 }
set.insert(3); // set = { 2, 3, 4 }
set.erase(4); // set = { 2, 3 }
set.erase(set.begin()) // set = { 3 }
```

自定义类型作为 `std::set` 的元素时，需重载小于号。

以下可以简单地将迭代器理解为指针。

`std::set` 的查找有关方法如下：

- `std::set<type>::iterator std::set<type>::find(type val)`，其返回值是一个迭代器，如果 `val` 存在于该 `set` 中，返回 `set` 中指向 `val` 位置的迭代器，否则返回 `set.end()`。

- `int std::set<type>::count(type val)`，返回 `val` 在 `set` 中出现的次数。

- `std::set<type>::iterator std::set<type>::lower_bound(type val)`，其返回值是一个迭代器，该迭代器指向 `set` 中第一个**大于等于** `val` 的元素。

- `std::set<type>::iterator std::set<type>::upper_bound(type val)`，其返回值是一个迭代器，该迭代器指向 `set` 中第一个**严格大于** `val` 的元素。

### std::map

建立 key 与 value 的一一映射，且内部按照 key 的大小排序。

`std::map` 的初始化及增删方法如下：

```cpp
std::map<int, int> map; // <key type, value type>
map[3] = 5; // map = { 3->5 }
map.insert({2, 8}); // map = { 2->8, 3->5 }
map.erase(3); // map = { 2->8 }
map[2] = 10; // map = { 2->10 }
++map[1]; // map = { 1->1, 2->10 }
```

`std::map` 的查找有关方法均同 `std::set`。

### STL 容器的遍历

#### 使用迭代器遍历

以遍历 `std::map` 为例：

```cpp
std::map<int, int> map;
for (auto it = map.begin(); it != map.end(); ++it) {
	const int key = it->first, value = it->second;
}
```

#### for auto 遍历

先以遍历 `std::vector` 为例，展示该遍历方式的基本形式：

```cpp
std::vector<int> a;
for (const auto &v : a) {
	std::cout << v << '\n';
}
```

这样的 `for` 循环同样可以使用 `continue` 与 `break` 语句进行循环控制。

其中 `auto` 关键字可以被替换为具体的类型名，在上例中为 `int`。

上例中，取引用符 `&` 用于指明 `v` 只是 `a` 中元素的引用，而非副本。当 `a` 的元素特别大时，这可以避免深拷贝带来的开销，如：

```cpp
std::vector<std::vector<int>> adj(n);
for (const auto &vec : adj) {
	for (const auto &v : vec) {
		// ...
	}
}
```

对 `vec` 取引用可以避免对整个 `std::vector<int>` 进行拷贝，省去不必要的时间花销。

以上几例中的 `const` 限定符使得在循环内**无法改变被遍历元素的值**，起到保护作用。

下面这个例子则说明，如果需要改变元素的值，则去掉 `const` 限定符。

```cpp
int n; std::cin >> n;
std::vector<int> a(n);
for (int &v : a)
	std::cin >> v;
```

如果没有对遍历的元素取引用（`&`），也没有加上 `const` 限定，则在循环中改变元素的值时，实际上只改变了被深拷贝的副本的值，**原数组的元素不会被改变**。

如下例：

```cpp
std::vector<int> a = { 0, 1, 2, 3, 4 };

for (int v : a)
	v = 1;
// a = { 0, 1, 2, 3, 4 }

for (int &v : a)
	v = 1;
// a = { 1, 1, 1, 1, 1 }

for (const int v : a)
	v = 1; // Compile Error

for (const int &v : a)
	v = 1; // Compile Error
```

如果遍历的元素为 `std::pair`，可以使用**结构化绑定**语法，格式如下：

```cpp
std::vector<std::pair<char, int>> a;

for (auto &[ch, v] : a)
	std::cin >> ch >> v;

/*
equals to
*/

for (auto &pi : a) {
	char &ch = pi.first;
	int &v = pi.second;
	std::cin >> ch >> v;
}

/*
or equals to
*/

for (auto &pi : a) {
	auto &[ch, v] = pi;
	std::cin >> ch >> v;
}
```

遍历的元素为 `std::map` 中的 key-value 映射时，也可以使用结构化绑定语法，格式基本相同，如下所示：

```cpp
std::map<int, int> map;

for (const auto &[key, value] : map) {
	// do sth
}

/*
equals to
*/

for (const auto &pair : map) {
	const char &key = pair.first;
	const int &value = pair.second;
	// do sth
}

for (const auto &pair : map) {
	const auto &[key, value] = pair;
	// do sth
}
```

**注：结构化绑定语法需要 C++17 及以上编译标准。**

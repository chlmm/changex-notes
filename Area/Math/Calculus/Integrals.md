# 积分公式

## 1. 基本积分

$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$ ($n \neq -1$)

$\int \frac{1}{x} \, dx = \ln |x| + C$

$\int e^x \, dx = e^x + C$

$\int a^x \, dx = \frac{a^x}{\ln a} + C$

## 2. 三角函数积分

$\int \sin x \, dx = -\cos x + C$

$\int \cos x \, dx = \sin x + C$

$\int \tan x \, dx = -\ln |\cos x| + C$

$\int \cot x \, dx = \ln |\sin x| + C$

$\int \sec x \, dx = \ln |\sec x + \tan x| + C$

$\int \csc x \, dx = \ln |\csc x - \cot x| + C$

$\int \sec^2 x \, dx = \tan x + C$

$\int \csc^2 x \, dx = -\cot x + C$

$\int \sec x \cdot \tan x \, dx = \sec x + C$

$\int \csc x \cdot \cot x \, dx = -\csc x + C$

## 3. 反三角函数相关积分

$\int \frac{dx}{\sqrt{1 - x^2}} = \arcsin x + C$

$\int \frac{dx}{1 + x^2} = \arctan x + C$

$\int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin \frac{x}{a} + C$

$\int \frac{dx}{a^2 + x^2} = \frac{1}{a} \arctan \frac{x}{a} + C$

$\int \frac{dx}{x^2 - a^2} = \frac{1}{2a} \ln \left| \frac{x - a}{x + a} \right| + C$

$\int \frac{dx}{a^2 - x^2} = \frac{1}{2a} \ln \left| \frac{a + x}{a - x} \right| + C$

$\int \frac{dx}{\sqrt{x^2 \pm a^2}} = \ln \left| x + \sqrt{x^2 \pm a^2} \right| + C$

## 4. 含根式的积分

$\int \sqrt{a^2 - x^2} \, dx = \frac{x}{2} \sqrt{a^2 - x^2} + \frac{a^2}{2} \arcsin \frac{x}{a} + C$

$\int \sqrt{x^2 + a^2} \, dx = \frac{x}{2} \sqrt{x^2 + a^2} + \frac{a^2}{2} \ln \left| x + \sqrt{x^2 + a^2} \right| + C$

$\int \sqrt{x^2 - a^2} \, dx = \frac{x}{2} \sqrt{x^2 - a^2} - \frac{a^2}{2} \ln \left| x + \sqrt{x^2 - a^2} \right| + C$

## 5. 双曲函数积分

$\int \sinh x \, dx = \cosh x + C$

$\int \cosh x \, dx = \sinh x + C$

$\int \tanh x \, dx = \ln \cosh x + C$

## 6. 积分方法

### 换元法
$\int f(g(x))g'(x) \, dx = \int f(u) \, du$ (令 $u = g(x)$)

### 分部积分法
$\int u \, dv = uv - \int v \, du$

**LIATE 法则** (选择 $u$ 的优先级): 对数函数 > 反三角函数 > 代数函数 > 三角函数 > 指数函数

### 有理函数积分
通过部分分式分解将复杂有理式化为简单分式之和

### 三角函数有理式积分
**万能代换**: 令 $u = \tan \frac{x}{2}$

$\sin x = \frac{2u}{1 + u^2}, \quad \cos x = \frac{1 - u^2}{1 + u^2}, \quad dx = \frac{2 \, du}{1 + u^2}$

### 三角换元
- $\sqrt{a^2 - x^2}$: 令 $x = a\sin t$
- $\sqrt{a^2 + x^2}$: 令 $x = a\tan t$
- $\sqrt{x^2 - a^2}$: 令 $x = a\sec t$

## 7. Wallis 公式

$I_n = \int_0^{\frac{\pi}{2}} \sin^n x \, dx = \int_0^{\frac{\pi}{2}} \cos^n x \, dx = \begin{cases} \frac{(n-1)!!}{n!!} \cdot \frac{\pi}{2}, & n \text{ 为偶数} \\ \frac{(n-1)!!}{n!!}, & n \text{ 为奇数} \end{cases}$

## 8. 定积分性质

$\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx$

$\int_a^a f(x) \, dx = 0$

$\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx$

**牛顿-莱布尼茨公式**: $\int_a^b f(x) \, dx = F(b) - F(a)$

**积分中值定理**: $\int_a^b f(x) \, dx = f(\xi)(b - a)$, 其中 $\xi \in [a, b]$

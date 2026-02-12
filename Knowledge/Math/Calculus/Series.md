# 级数

## 1. 常数项级数

### 基本性质

$\sum_{n=1}^{\infty} a_n$ 收敛 $\Rightarrow \lim_{n \to \infty} a_n = 0$

$\sum_{n=1}^{\infty} ca_n = c\sum_{n=1}^{\infty} a_n$

$\sum_{n=1}^{\infty} (a_n \pm b_n) = \sum_{n=1}^{\infty} a_n \pm \sum_{n=1}^{\infty} b_n$

### 常用级数

**几何级数**: $\sum_{n=0}^{\infty} ar^n = \frac{a}{1 - r}$ ($|r| < 1$)

**p-级数**: $\sum_{n=1}^{\infty} \frac{1}{n^p}$ 收敛当且仅当 $p > 1$

**调和级数**: $\sum_{n=1}^{\infty} \frac{1}{n}$ 发散

### 正项级数判别法

**比较判别法**: 若 $0 \leq a_n \leq b_n$，则
- $\sum b_n$ 收敛 $\Rightarrow \sum a_n$ 收敛
- $\sum a_n$ 发散 $\Rightarrow \sum b_n$ 发散

**比值判别法 (达朗贝尔)**: $\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = \rho$
- $\rho < 1$: 收敛
- $\rho > 1$: 发散
- $\rho = 1$: 不确定

**根值判别法 (柯西)**: $\lim_{n \to \infty} \sqrt[n]{a_n} = \rho$
- $\rho < 1$: 收敛
- $\rho > 1$: 发散
- $\rho = 1$: 不确定

**积分判别法**: 若 $f(x)$ 在 $[1, \infty)$ 上非负递减，则 $\sum_{n=1}^{\infty} f(n)$ 与 $\int_1^{\infty} f(x) \, dx$ 同敛散

### 交错级数

**莱布尼茨判别法**: 若 $a_n > 0$ 单调递减且 $\lim_{n \to \infty} a_n = 0$，则 $\sum_{n=1}^{\infty} (-1)^{n-1} a_n$ 收敛

### 绝对收敛与条件收敛

- **绝对收敛**: $\sum |a_n|$ 收敛
- **条件收敛**: $\sum a_n$ 收敛但 $\sum |a_n|$ 发散

绝对收敛 $\Rightarrow$ 收敛

## 2. 幂级数

$\sum_{n=0}^{\infty} a_n x^n$ 或 $\sum_{n=0}^{\infty} a_n (x - x_0)^n$

### 收敛半径

$R = \lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}} \right|$ 或 $R = \frac{1}{\lim_{n \to \infty} \sqrt[n]{|a_n|}}$

- $|x| < R$: 绝对收敛
- $|x| > R$: 发散
- $|x| = R$: 需单独判断

### 常用幂级数展开

$\frac{1}{1 - x} = \sum_{n=0}^{\infty} x^n$, $|x| < 1$

$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$, $x \in \mathbb{R}$

$\sin x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}$, $x \in \mathbb{R}$

$\cos x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!}$, $x \in \mathbb{R}$

$\ln(1 + x) = \sum_{n=1}^{\infty} (-1)^{n-1} \frac{x^n}{n}$, $-1 < x \leq 1$

$(1 + x)^\alpha = \sum_{n=0}^{\infty} C_\alpha^n x^n$, $|x| < 1$

$\arctan x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{2n+1}$, $|x| \leq 1$

### 幂级数运算

**逐项求导**: $\left(\sum_{n=0}^{\infty} a_n x^n\right)' = \sum_{n=1}^{\infty} na_n x^{n-1}$

**逐项积分**: $\int_0^x \sum_{n=0}^{\infty} a_n t^n \, dt = \sum_{n=0}^{\infty} \frac{a_n}{n+1} x^{n+1}$

## 3. 傅里叶级数

$f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} (a_n \cos nx + b_n \sin nx)$

其中

$a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos nx \, dx$, $n = 0, 1, 2, \ldots$

$b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin nx \, dx$, $n = 1, 2, 3, \ldots$

### 狄利克雷收敛定理

若 $f(x)$ 在 $[-\pi, \pi]$ 上分段光滑，则傅里叶级数收敛于

$\frac{f(x^+) + f(x^-)}{2}$

### 正弦级数与余弦级数

**奇函数**: $f(x) = \sum_{n=1}^{\infty} b_n \sin nx$

**偶函数**: $f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos nx$

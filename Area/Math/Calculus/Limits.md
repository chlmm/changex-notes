# 极限

## 1. 基本极限

$\lim_{x \to 0} \frac{\sin x}{x} = 1$

$\lim_{x \to 0} \frac{\tan x}{x} = 1$

$\lim_{x \to 0} \frac{\arcsin x}{x} = 1$

$\lim_{x \to 0} \frac{\arctan x}{x} = 1$

$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$

$\lim_{x \to 0} (1 + x)^{\frac{1}{x}} = e$

$\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e$

$\lim_{x \to 0} \frac{e^x - 1}{x} = 1$

$\lim_{x \to 0} \frac{\ln(1 + x)}{x} = 1$

$\lim_{x \to 0} \frac{a^x - 1}{x} = \ln a$

$\lim_{x \to 0} \frac{(1 + x)^\alpha - 1}{x} = \alpha$

## 2. 无穷小等价替换 (当 $x \to 0$)

$\sin x \sim x$

$\tan x \sim x$

$\arcsin x \sim x$

$\arctan x \sim x$

$e^x - 1 \sim x$

$\ln(1 + x) \sim x$

$(1 + x)^\alpha - 1 \sim \alpha x$

$1 - \cos x \sim \frac{x^2}{2}$

$a^x - 1 \sim x \ln a$

$\log_a(1 + x) \sim \frac{x}{\ln a}$

## 3. 洛必达法则

若 $\lim_{x \to a} \frac{f(x)}{g(x)}$ 为 $\frac{0}{0}$ 或 $\frac{\infty}{\infty}$ 型，则

$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$

(要求右侧极限存在或为无穷大)

## 4. 泰勒展开

$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + o(x^n)$

$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots + (-1)^n \frac{x^{2n+1}}{(2n+1)!} + o(x^{2n+2})$

$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots + (-1)^n \frac{x^{2n}}{(2n)!} + o(x^{2n+1})$

$\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots + (-1)^{n-1} \frac{x^n}{n} + o(x^n)$

$(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^2 + \cdots + o(x^n)$

$\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots + (-1)^n \frac{x^{2n+1}}{2n+1} + o(x^{2n+2})$

## 5. 夹逼定理

若 $g(x) \leq f(x) \leq h(x)$ 且 $\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$，则 $\lim_{x \to a} f(x) = L$

## 6. 单调有界收敛定理

单调递增有上界（或单调递减有下界）的数列必收敛

## 7. 重要数列极限

$\lim_{n \to \infty} \sqrt[n]{n} = 1$

$\lim_{n \to \infty} \sqrt[n]{a} = 1$ ($a > 0$)

$\lim_{n \to \infty} \frac{n!}{n^n} = 0$

$\lim_{n \to \infty} \frac{a^n}{n!} = 0$

$\lim_{n \to \infty} \frac{n^k}{a^n} = 0$ ($a > 1$, $k$ 为常数)

## 8. 柯西收敛准则

数列 $\{a_n\}$ 收敛 $\Leftrightarrow \forall \varepsilon > 0$, $\exists N$, 当 $m, n > N$ 时，$|a_m - a_n| < \varepsilon$

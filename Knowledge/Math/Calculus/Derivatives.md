# 导数公式

## 1. 基本初等函数

$(x^n)' = nx^{n-1}$

$(e^x)' = e^x$

$(a^x)' = a^x \ln a$

$(\ln x)' = \frac{1}{x}$

$(\log_a x)' = \frac{1}{x \ln a}$

## 2. 三角函数

$(\sin x)' = \cos x$

$(\cos x)' = -\sin x$

$(\tan x)' = \sec^2 x$

$(\cot x)' = -\csc^2 x$

$(\sec x)' = \sec x \cdot \tan x$

$(\csc x)' = -\csc x \cdot \cot x$

## 3. 反三角函数

$(\arcsin x)' = \frac{1}{\sqrt{1 - x^2}}$

$(\arccos x)' = -\frac{1}{\sqrt{1 - x^2}}$

$(\arctan x)' = \frac{1}{1 + x^2}$

$(\text{arccot } x)' = -\frac{1}{1 + x^2}$

$(\text{arcsec } x)' = \frac{1}{|x|\sqrt{x^2 - 1}}$

$(\text{arccsc } x)' = -\frac{1}{|x|\sqrt{x^2 - 1}}$

## 4. 双曲函数

**定义**:

$\sinh x = \frac{e^x - e^{-x}}{2}$

$\cosh x = \frac{e^x + e^{-x}}{2}$

$\tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$

**导数**:

$(\sinh x)' = \cosh x$

$(\cosh x)' = \sinh x$

$(\tanh x)' = \text{sech}^2 x$

**反双曲函数**:

$\text{arsinh } x = \ln(x + \sqrt{x^2 + 1})$

$\text{arcosh } x = \pm \ln(x + \sqrt{x^2 - 1})$ ($x \geq 1$)

$\text{artanh } x = \frac{1}{2} \ln \frac{1 + x}{1 - x}$ ($|x| < 1$)

## 5. 求导法则

**加法法则**: $(u \pm v)' = u' \pm v'$

**乘法法则**: $(uv)' = u'v + uv'$

**除法法则**: $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$

**链式法则**: $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$

**反函数求导**: $\frac{dx}{dy} = \frac{1}{\frac{dy}{dx}}$

**隐函数求导**: 对方程两边同时对 $x$ 求导

**参数方程求导**: $\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}$

**对数求导法**: 先取对数再求导

## 6. 高阶导数

$(\sin x)^{(n)} = \sin\left(x + \frac{n\pi}{2}\right)$

$(\cos x)^{(n)} = \cos\left(x + \frac{n\pi}{2}\right)$

$(e^x)^{(n)} = e^x$

$(x^n)^{(m)} = \frac{n!}{(n-m)!}x^{n-m}$ (当 $m \leq n$)

**莱布尼茨公式**: $(uv)^{(n)} = \sum_{k=0}^{n} C_n^k u^{(n-k)} v^{(k)}$

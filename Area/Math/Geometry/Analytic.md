# 解析几何

## 1. 平面直角坐标系

**两点距离**: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$

**定比分点**: $P\left(\frac{x_1 + \lambda x_2}{1 + \lambda}, \frac{y_1 + \lambda y_2}{1 + \lambda}\right)$

**中点**: $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$

**三角形面积**: $S = \frac{1}{2}|x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$

## 2. 直线

**斜率**: $k = \tan\alpha = \frac{y_2 - y_1}{x_2 - x_1}$

**方程形式**:
- 点斜式: $y - y_0 = k(x - x_0)$
- 斜截式: $y = kx + b$
- 两点式: $\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$
- 截距式: $\frac{x}{a} + \frac{y}{b} = 1$
- 一般式: $Ax + By + C = 0$

**两直线关系**:
- 平行: $k_1 = k_2$ 或 $\frac{A_1}{A_2} = \frac{B_1}{B_2} \neq \frac{C_1}{C_2}$
- 垂直: $k_1 k_2 = -1$ 或 $A_1 A_2 + B_1 B_2 = 0$
- 夹角: $\tan\theta = \left|\frac{k_2 - k_1}{1 + k_1 k_2}\right|$

**点到直线距离**: $d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$

## 3. 圆

**标准方程**: $(x - a)^2 + (y - b)^2 = r^2$

**一般方程**: $x^2 + y^2 + Dx + Ey + F = 0$

**参数方程**: $x = a + r\cos\theta$, $y = b + r\sin\theta$

**圆心**: $(a, b) = \left(-\frac{D}{2}, -\frac{E}{2}\right)$

**半径**: $r = \frac{1}{2}\sqrt{D^2 + E^2 - 4F}$

**切线方程**: $(x_0 - a)(x - a) + (y_0 - b)(y - b) = r^2$

## 4. 椭圆

**标准方程**: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ ($a > b > 0$)

**参数方程**: $x = a\cos\theta$, $y = b\sin\theta$

**焦点**: $(\pm c, 0)$，其中 $c^2 = a^2 - b^2$

**离心率**: $e = \frac{c}{a}$ ($0 < e < 1$)

**准线**: $x = \pm \frac{a^2}{c} = \pm \frac{a}{e}$

**焦半径**: $r = a \pm ex$

**面积**: $S = \pi ab$

## 5. 双曲线

**标准方程**: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$

**渐近线**: $y = \pm \frac{b}{a}x$

**焦点**: $(\pm c, 0)$，其中 $c^2 = a^2 + b^2$

**离心率**: $e = \frac{c}{a}$ ($e > 1$)

**准线**: $x = \pm \frac{a^2}{c} = \pm \frac{a}{e}$

**焦半径**: $r = |ex \pm a|$

**等轴双曲线**: $x^2 - y^2 = a^2$，渐近线 $y = \pm x$

## 6. 抛物线

**标准方程**: $y^2 = 2px$ ($p > 0$)

**焦点**: $\left(\frac{p}{2}, 0\right)$

**准线**: $x = -\frac{p}{2}$

**焦半径**: $r = x + \frac{p}{2}$

**通径**: $|AB| = 2p$

**其他形式**:
- $y^2 = -2px$: 开口向左
- $x^2 = 2py$: 开口向上
- $x^2 = -2py$: 开口向下

## 7. 空间直角坐标系

**两点距离**: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$

**方向余弦**: $\cos\alpha = \frac{x}{r}$, $\cos\beta = \frac{y}{r}$, $\cos\gamma = \frac{z}{r}$

**性质**: $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$

## 8. 空间曲面

**球面**: $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$

**柱面**:
- 圆柱面: $x^2 + y^2 = R^2$
- 抛物柱面: $y^2 = 2px$

**锥面**: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{z^2}{c^2}$

**旋转曲面**: 曲线 $f(y, z) = 0$ 绕 $z$ 轴旋转: $f(\sqrt{x^2 + y^2}, z) = 0$

**椭球面**: $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$

**单叶双曲面**: $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$

**双叶双曲面**: $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = -1$

**椭圆抛物面**: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 2z$

**双曲抛物面**: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 2z$

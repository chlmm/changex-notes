# 向量

## 1. 向量的基本概念

**向量**: 既有大小又有方向的量，记作 $\vec{a}$ 或 $\mathbf{a}$

**模**: $|\vec{a}| = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}$

**单位向量**: $|\vec{a}| = 1$，记作 $\hat{a} = \frac{\vec{a}}{|\vec{a}|}$

**零向量**: $\vec{0}$，模为 0，方向任意

## 2. 线性运算

**加法**: 平行四边形法则或三角形法则

$\vec{a} + \vec{b} = (a_1 + b_1, a_2 + b_2, \ldots, a_n + b_n)$

**数乘**: $k\vec{a} = (ka_1, ka_2, \ldots, ka_n)$

**性质**:
- 交换律: $\vec{a} + \vec{b} = \vec{b} + \vec{a}$
- 结合律: $(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c})$
- 分配律: $k(\vec{a} + \vec{b}) = k\vec{a} + k\vec{b}$

## 3. 数量积 (点积)

$\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos\theta = a_1b_1 + a_2b_2 + \cdots + a_nb_n$

**性质**:
- $\vec{a} \cdot \vec{a} = |\vec{a}|^2$
- $\vec{a} \perp \vec{b} \Leftrightarrow \vec{a} \cdot \vec{b} = 0$
- 交换律: $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$
- 分配律: $\vec{a} \cdot (\vec{b} + \vec{c}) = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}$

**投影**: $\text{proj}_{\vec{b}} \vec{a} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}$

## 4. 向量积 (叉积) - 三维

$\vec{a} \times \vec{b} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}$

**性质**:
- $|\vec{a} \times \vec{b}| = |\vec{a}| |\vec{b}| \sin\theta$ (平行四边形面积)
- 方向: 右手定则
- $\vec{a} \parallel \vec{b} \Leftrightarrow \vec{a} \times \vec{b} = \vec{0}$
- 反交换律: $\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$
- 分配律: $\vec{a} \times (\vec{b} + \vec{c}) = \vec{a} \times \vec{b} + \vec{a} \times \vec{c}$

## 5. 混合积

$(\vec{a}, \vec{b}, \vec{c}) = (\vec{a} \times \vec{b}) \cdot \vec{c} = \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix}$

**几何意义**: 平行六面体的有向体积

**性质**:
- 轮换对称: $(\vec{a}, \vec{b}, \vec{c}) = (\vec{b}, \vec{c}, \vec{a}) = (\vec{c}, \vec{a}, \vec{b})$
- 交换变号: $(\vec{a}, \vec{b}, \vec{c}) = -(\vec{b}, \vec{a}, \vec{c})$
- 三向量共面 $\Leftrightarrow (\vec{a}, \vec{b}, \vec{c}) = 0$

## 6. 向量的线性相关性

**线性组合**: $\vec{v} = k_1\vec{a}_1 + k_2\vec{a}_2 + \cdots + k_n\vec{a}_n$

**线性相关**: 存在不全为零的 $k_i$ 使 $k_1\vec{a}_1 + k_2\vec{a}_2 + \cdots + k_n\vec{a}_n = \vec{0}$

**线性无关**: 仅当所有 $k_i = 0$ 时上式成立

**判定**:
- 二维: 两向量线性相关 $\Leftrightarrow$ 共线
- 三维: 三向量线性相关 $\Leftrightarrow$ 共面
- $n$ 个 $n$ 维向量线性无关 $\Leftrightarrow$ 行列式不为零

## 7. 向量空间

**基**: 向量空间 $V$ 中一组线性无关的向量，能表示 $V$ 中任意向量

**维数**: 基中向量的个数

**坐标**: $\vec{v} = x_1\vec{e}_1 + x_2\vec{e}_2 + \cdots + x_n\vec{e}_n$，则 $(x_1, x_2, \ldots, x_n)$ 为 $\vec{v}$ 在基 $\{\vec{e}_i\}$ 下的坐标

**标准正交基**: 基向量两两正交且为单位向量

**施密特正交化**:

$\vec{\beta}_1 = \vec{\alpha}_1$

$\vec{\beta}_2 = \vec{\alpha}_2 - \frac{(\vec{\alpha}_2, \vec{\beta}_1)}{(\vec{\beta}_1, \vec{\beta}_1)}\vec{\beta}_1$

$\vec{\beta}_k = \vec{\alpha}_k - \sum_{i=1}^{k-1} \frac{(\vec{\alpha}_k, \vec{\beta}_i)}{(\vec{\beta}_i, \vec{\beta}_i)}\vec{\beta}_i$

单位化: $\vec{e}_i = \frac{\vec{\beta}_i}{|\vec{\beta}_i|}$

## 8. 空间直线与平面

**直线方程**:
- 点向式: $\frac{x - x_0}{m} = \frac{y - y_0}{n} = \frac{z - z_0}{p}$
- 参数式: $x = x_0 + mt$, $y = y_0 + nt$, $z = z_0 + pt$
- 一般式: 两平面交线

**平面方程**:
- 点法式: $A(x - x_0) + B(y - y_0) + C(z - z_0) = 0$
- 一般式: $Ax + By + Cz + D = 0$
- 截距式: $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$

**法向量**: $\vec{n} = (A, B, C)$

**点到平面距离**: $d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}$

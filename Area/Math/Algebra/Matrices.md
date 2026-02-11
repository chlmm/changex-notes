# 矩阵

## 1. 基本运算

**加法**: $(A + B)_{ij} = a_{ij} + b_{ij}$

**数乘**: $(kA)_{ij} = ka_{ij}$

**乘法**: $(AB)_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}$

**转置**: $(A^T)_{ij} = a_{ji}$

**共轭转置**: $(A^*)_{ij} = \overline{a_{ji}}$

## 2. 特殊矩阵

**单位矩阵**: $I = \text{diag}(1, 1, \ldots, 1)$

**对角矩阵**: $\text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$

**对称矩阵**: $A^T = A$

**反对称矩阵**: $A^T = -A$

**正交矩阵**: $A^T A = AA^T = I$

**厄米特矩阵**: $A^* = A$

**酉矩阵**: $A^* A = AA^* = I$

**幂等矩阵**: $A^2 = A$

**对合矩阵**: $A^2 = I$

**幂零矩阵**: $A^k = 0$ (对某个正整数 $k$)

## 3. 逆矩阵

$A^{-1}$ 存在 $\Leftrightarrow \det A \neq 0$

**伴随矩阵**: $A^* = (A_{ji})$，其中 $A_{ij}$ 是 $a_{ij}$ 的代数余子式

$A^{-1} = \frac{1}{\det A} A^*$

**性质**:
- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$
- $(kA)^{-1} = \frac{1}{k}A^{-1}$ ($k \neq 0$)

## 4. 行列式

**二阶**: $\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$

**三阶**: 按第一行展开

$\begin{vmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{vmatrix} = a_{11}A_{11} + a_{12}A_{12} + a_{13}A_{13}$

**性质**:
- $\det(AB) = \det A \cdot \det B$
- $\det(A^T) = \det A$
- $\det(A^{-1}) = \frac{1}{\det A}$
- $\det(kA) = k^n \det A$ ($n$ 阶矩阵)

## 5. 矩阵的秩

$\text{rank}(A)$ = 矩阵中非零子式的最高阶数

**性质**:
- $\text{rank}(A) = \text{rank}(A^T)$
- $\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))$
- $\text{rank}(A + B) \leq \text{rank}(A) + \text{rank}(B)$

## 6. 特征值与特征向量

$Ax = \lambda x$ ($x \neq 0$)

**特征多项式**: $f(\lambda) = \det(\lambda I - A)$

**性质**:
- $\sum_{i=1}^{n} \lambda_i = \text{tr}(A) = \sum_{i=1}^{n} a_{ii}$
- $\prod_{i=1}^{n} \lambda_i = \det A$
- 不同特征值对应的特征向量线性无关

## 7. 相似对角化

$A$ 相似于对角矩阵 $\Leftrightarrow$ $A$ 有 $n$ 个线性无关的特征向量

$P^{-1}AP = \Lambda = \text{diag}(\lambda_1, \lambda_2, \ldots, \lambda_n)$

其中 $P = (x_1, x_2, \ldots, x_n)$，$x_i$ 是对应 $\lambda_i$ 的特征向量

**实对称矩阵**: 必可正交相似对角化，即存在正交矩阵 $Q$ 使 $Q^T A Q = \Lambda$

## 8. 二次型

$f(x_1, x_2, \ldots, x_n) = x^T A x = \sum_{i,j} a_{ij} x_i x_j$

**标准形**: $f = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots + \lambda_n y_n^2$

**惯性定理**: 标准形中正、负系数的个数是唯一确定的

**正定性判别**:
- 所有特征值 $> 0$
- 所有顺序主子式 $> 0$
- 正惯性指数 $= n$

## 9. 矩阵分解

**LU 分解**: $A = LU$ ($L$ 下三角，$U$ 上三角)

**QR 分解**: $A = QR$ ($Q$ 正交，$R$ 上三角)

**奇异值分解 (SVD)**: $A = U\Sigma V^T$

**谱分解**: $A = \sum_{i} \lambda_i x_i x_i^T$

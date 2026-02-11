# 三角函数公式

## 1. 诱导公式

### 1.1 基本诱导公式表

| 角/函数 | $\sin$ | $\cos$ | $\tan$ | $\cot$ |
|:-------:|:------:|:------:|:------:|:------:|
| $-\alpha$ | $-\sin\alpha$ | $\cos\alpha$ | $-\tan\alpha$ | $-\cot\alpha$ |
| $90°-\alpha$ | $\cos\alpha$ | $\sin\alpha$ | $\cot\alpha$ | $\tan\alpha$ |
| $90°+\alpha$ | $\cos\alpha$ | $-\sin\alpha$ | $-\cot\alpha$ | $-\tan\alpha$ |
| $180°-\alpha$ | $\sin\alpha$ | $-\cos\alpha$ | $-\tan\alpha$ | $-\cot\alpha$ |
| $180°+\alpha$ | $-\sin\alpha$ | $-\cos\alpha$ | $\tan\alpha$ | $\cot\alpha$ |
| $270°-\alpha$ | $-\cos\alpha$ | $-\sin\alpha$ | $\cot\alpha$ | $\tan\alpha$ |
| $270°+\alpha$ | $-\cos\alpha$ | $\sin\alpha$ | $-\cot\alpha$ | $-\tan\alpha$ |
| $360°-\alpha$ | $-\sin\alpha$ | $\cos\alpha$ | $-\tan\alpha$ | $-\cot\alpha$ |
| $360°+\alpha$ | $\sin\alpha$ | $\cos\alpha$ | $\tan\alpha$ | $\cot\alpha$ |

### 1.2 记忆口诀

**"奇变偶不变，符号看象限"**

- **奇变偶不变**：当角度加减 $90°$ 的奇数倍时，函数名改变（$\sin \leftrightarrow \cos$，$\tan \leftrightarrow \cot$）；当角度加减 $90°$ 的偶数倍时，函数名不变。

- **符号看象限**：将 $\alpha$ 视为锐角，看原函数在相应象限的符号。

### 1.3 常用诱导公式

**负角公式**：
$$\sin(-\alpha) = -\sin\alpha$$
$$\cos(-\alpha) = \cos\alpha$$
$$\tan(-\alpha) = -\tan\alpha$$

**补角公式**：
$$\sin(180°-\alpha) = \sin\alpha$$
$$\cos(180°-\alpha) = -\cos\alpha$$

**余角公式**：
$$\sin(90°-\alpha) = \cos\alpha$$
$$\cos(90°-\alpha) = \sin\alpha$$

**周期公式**：
$$\sin(\alpha + 360°k) = \sin\alpha \quad (k \in \mathbb{Z})$$
$$\cos(\alpha + 360°k) = \cos\alpha \quad (k \in \mathbb{Z})$$

## 2. 基本恒等式

### 2.1 同角三角函数关系

**平方关系**：
$$\sin^2\alpha + \cos^2\alpha = 1$$
$$1 + \tan^2\alpha = \sec^2\alpha$$
$$1 + \cot^2\alpha = \csc^2\alpha$$

**倒数关系**：
$$\sin\alpha \cdot \csc\alpha = 1$$
$$\cos\alpha \cdot \sec\alpha = 1$$
$$\tan\alpha \cdot \cot\alpha = 1$$

**商数关系**：
$$\tan\alpha = \frac{\sin\alpha}{\cos\alpha}$$
$$\cot\alpha = \frac{\cos\alpha}{\sin\alpha}$$

## 3. 和差公式

$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$$

$$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$$

$$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$$

$$\cot(\alpha \pm \beta) = \frac{\cot\alpha\cot\beta \mp 1}{\cot\beta \pm \cot\alpha}$$

## 4. 倍角公式

$$\sin 2\alpha = 2\sin\alpha\cos\alpha$$

$$\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha$$

$$\tan 2\alpha = \frac{2\tan\alpha}{1 - \tan^2\alpha}$$

$$\cot 2\alpha = \frac{\cot^2\alpha - 1}{2\cot\alpha}$$

### 4.1 三倍角公式

$$\sin 3\alpha = 3\sin\alpha - 4\sin^3\alpha$$

$$\cos 3\alpha = 4\cos^3\alpha - 3\cos\alpha$$

$$\tan 3\alpha = \frac{3\tan\alpha - \tan^3\alpha}{1 - 3\tan^2\alpha}$$

## 5. 半角公式

$$\sin\frac{\alpha}{2} = \pm\sqrt{\frac{1 - \cos\alpha}{2}}$$

$$\cos\frac{\alpha}{2} = \pm\sqrt{\frac{1 + \cos\alpha}{2}}$$

$$\tan\frac{\alpha}{2} = \pm\sqrt{\frac{1 - \cos\alpha}{1 + \cos\alpha}} = \frac{1 - \cos\alpha}{\sin\alpha} = \frac{\sin\alpha}{1 + \cos\alpha}$$

$$\cot\frac{\alpha}{2} = \pm\sqrt{\frac{1 + \cos\alpha}{1 - \cos\alpha}} = \frac{1 + \cos\alpha}{\sin\alpha} = \frac{\sin\alpha}{1 - \cos\alpha}$$

## 6. 积化和差公式

$$\sin\alpha\cos\beta = \frac{1}{2}[\sin(\alpha + \beta) + \sin(\alpha - \beta)]$$

$$\cos\alpha\sin\beta = \frac{1}{2}[\sin(\alpha + \beta) - \sin(\alpha - \beta)]$$

$$\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha + \beta) + \cos(\alpha - \beta)]$$

$$\sin\alpha\sin\beta = -\frac{1}{2}[\cos(\alpha + \beta) - \cos(\alpha - \beta)]$$

## 7. 和差化积公式

$$\sin\alpha + \sin\beta = 2\sin\frac{\alpha + \beta}{2}\cos\frac{\alpha - \beta}{2}$$

$$\sin\alpha - \sin\beta = 2\cos\frac{\alpha + \beta}{2}\sin\frac{\alpha - \beta}{2}$$

$$\cos\alpha + \cos\beta = 2\cos\frac{\alpha + \beta}{2}\cos\frac{\alpha - \beta}{2}$$

$$\cos\alpha - \cos\beta = -2\sin\frac{\alpha + \beta}{2}\sin\frac{\alpha - \beta}{2}$$

## 8. 万能公式

令 $t = \tan\frac{\alpha}{2}$，则：

$$\sin\alpha = \frac{2t}{1 + t^2}$$

$$\cos\alpha = \frac{1 - t^2}{1 + t^2}$$

$$\tan\alpha = \frac{2t}{1 - t^2}$$

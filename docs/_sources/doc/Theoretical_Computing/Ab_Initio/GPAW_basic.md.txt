# GPAW 基组

* 在时间传播的LCAO-TDDFT计算中, 与基态LCAO计算相比, 更加重要的是考虑基组集合. 基组集合需要能够充分地表示占据态(空穴)和相关的非占态(电子). 为了时间传播, 应根据自己的需求生成定制的基组集合, 并进行基准测试.

* 无论您选择哪种基组集合, 都应始终通过对最大系统上的有限差分时间传播代码进行基准测试来评估LCAO计算结果. 例如, 可以创建一个原型系统, 该系统由与父系统中相同原子种类和相同作用角色的原子组成, 但足够小以在格点传播模式下进行计算.

* 在这些说明之后, 我们描述了两套基组集合的工具, 可以作为选择适合您需求的合适基组集合的起点. 具体来说, 是p价电子基组集合和完备性优化基组集合.

## Atomic PAW Setups

* Setups是对PAW方法而言的,  赝势是对赝势方法而言的. 所有可用的Setups都包含在tar文件中. 有LDA、PBE、revPBE、RPBE 和 GLLBSC 泛函的Setups. 这些Setups被存储为压缩的XML规范, 用于原子PAW数据集文件. 有关详细信息, 请参阅PAW数据集的基组安装.

### p-valence 基组

* 所谓的p价电子基组是通过将默认基组的p型极化函数替换为一个束缚的未占据p型轨道及其分裂价电子互补来构建的过渡金属基组.  这些基组显著改善了未占据态的态密度.

* 可以使用gpaw install-data工具以以下选项轻松获取适当元素的p价电子基组：

    ```bash
    gpaw install-data {<directory>} --basis --version=pvalence-0. 9. 20000
    # 示例
    gpaw install-data . / --basis --version=pvalence-0. 9. 20000
    ```

### 完备性优化基组

* 通过所谓的完备性优化方法可以获得改进基组的系统方法. 使用该方法生成了用于铜、银和金团簇的TDDFT计算的基组系列.

* 为方便起见, 可以轻松获取这些基组：

    ```bash
    gpaw install-data {<directory>} --basis --version=coopt
    # 示例
    gpaw install-data . / --basis --version=coopt
    ```

* 请参阅PAW数据集的基组安装. 最后, 再次强调, 在使用基组时, 对于您的应用程序来说, 评估其适用性是至关重要的.

## 安装PAW数据集

* PAW数据集可以自动或手动安装.

* 要自动安装它们, 请运行 `gpaw install-data {<dir>}`. 这将下载并解压最新的软件包到`<dir>/gpaw-setups-<version>`. 在提示时, 回答是(y), 以在GPAW配置文件中注册该路径.

    ```bash
    gpaw install-data {<dir>}
    # 示例
    gpaw install-data . /
    ```

* 注意：
    dzp和pvalence. dz两个基组的考虑的外层价电子相同, 例如Au元素均为11. 但是pvalence. dz基组的内层价电子比dzp基组多一个, 例如Au元素为10. 因此, pvalence. dz基组的计算量比dzp基组大.

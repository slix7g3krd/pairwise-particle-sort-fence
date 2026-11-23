# pairwise-particle-sort-fence

## 领域

游戏、图形与多媒体

## 主题

粒子排序与异步栅栏

## 说明

视深排序键、命令缓冲生命周期与跨队列同步。

初始状态下 `graphics/particle_sort_fence.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。

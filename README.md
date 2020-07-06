# SORTING-ALGORITHM
排序算法（java、python）

- 冒泡排序，O(n^2)， O(1)， 稳定, 即总是把最大的数往后面放
- 选择排序，O(n^2)，O(1)，不稳定（比如2 2 1），即总是把最小的数放前面放
- 快速排序，O(nlogn), O(nlogn)（主要是递归过程的空间），不稳定
  右侧开始遇到一个小的丢左边，左侧开始遇到一个大的丢右边，中间就是元素的合适位置
  然后继续递归左右两侧，直到剩下一个元素为止
- 插入排序，O(n^2)，O(1)，稳定，即把当前的数一直往前放到合适的位置
  适合于本来就已经相对有序的序列，能够降低遍历次数和交换次数
- 希尔排序，O(n^2)（平均是n^1.3）, O(1), 不稳定
  本质就是分组的插入排序，直接写一个插入排序然后1改为gap分组即可
- 归并排序，O(nlogn), O(1)，稳定
  细分到每个都是排好序的数组，然后逐个数组按照大小顺序合并得到一个排好序的大数组
- 堆排序，O(nlogn), O(1), 不稳定
  先把数组调整为最大堆，然后堆头放尾巴一直再重新调整堆，此时堆尾是好的不用再调整
  最大堆调整算法就是，调整当前节点为最大值，循环往下调整堆

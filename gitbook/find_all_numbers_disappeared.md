# Find All Numbers Disappeared in an Array \(Arrays | Cyclic sort\)

{% embed url="https://www.youtube.com/watch?v=nTt3929ik8U" %}

{% embed url="https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/" %}

{% tabs %}
{% tab title="Решение ➡️" %}
```
Сначала попробуйте решить сами
```
{% endtab %}

{% tab title="Python" %}
```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
          pos = nums[i] - 1 # correct position
          if nums[i] != nums[pos]:
            nums[i], nums[pos] = nums[pos], nums[i]
          else:
            i += 1

        miss = []
        for i in range(len(nums)):
          if nums[i] != i + 1:
            miss.append(i + 1)

        return miss
```
{% endtab %}
{% endtabs %}


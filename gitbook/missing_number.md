# Missing Number \(Arrays\)

{% embed url="https://www.youtube.com/watch?v=nTt3929ik8U" %}

{% embed url="https://leetcode.com/problems/missing-number/" caption="Missing Number" %}

{% tabs %}
{% tab title="Решение ➡️" %}
```
Сначала попробуйте решить сами
```
{% endtab %}

{% tab title="Python" %}
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n+1) //2 - sum(nums)
```
{% endtab %}
{% endtabs %}


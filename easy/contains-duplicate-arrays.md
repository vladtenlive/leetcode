# Contains Duplicate \(Arrays\)

{% embed url="https://www.youtube.com/watch?v=a14p8DYFdCA" %}

{% embed url="https://leetcode.com/problems/contains-duplicate/" caption="Contains Duplicate" %}

{% tabs %}
{% tab title="Решение ➡️" %}
```
Сначала попробуйте решить сами
```
{% endtab %}

{% tab title="Python" %}
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set([])

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```
{% endtab %}
{% endtabs %}





# CollatorRewards

---------
## Events

---------
### CollatorRewarded
Collator was rewarded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| currency | `T::CurrencyId` | ```u32```

---------
## Storage functions

---------
### Collators
 Stores the collators per session (index).

#### Python
```python
result = substrate.query(
    'CollatorRewards', 'Collators', ['u32']
)
```

#### Return value
```python
['AccountId']
```
---------
## Constants

---------
### RewardCurrencyId
 Reward Asset Id
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('CollatorRewards', 'RewardCurrencyId')
```
---------
### RewardPerCollator
 Reward amount per one collator.
#### Value
```python
15216000000000000
```
#### Python
```python
constant = substrate.get_constant('CollatorRewards', 'RewardPerCollator')
```
---------
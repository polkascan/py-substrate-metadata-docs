
# Vesting

---------
## Events

---------
### VestFailed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AccountOf<T>` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}```

---------
### Vested
A vest occured.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `AccountOf<T>` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### TotalUnvestedAllocation

#### Python
```python
result = substrate.query(
    'Vesting', 'TotalUnvestedAllocation', []
)
```

#### Return value
```python
'u128'
```
---------
### VestingSchedule
 The closed pallet map. Each pallet in here will not receive transcations.

#### Python
```python
result = substrate.query(
    'Vesting', 'VestingSchedule', ['u64']
)
```

#### Return value
```python
[('AccountId', 'u128')]
```
---------
## Errors

---------
### BlockTimeNotSet
Block time not set.

---------
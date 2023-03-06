
# Base

---------
## Events

---------
### UnexpectedError
An unexpected error happened that should be investigated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<DispatchError>` | ```(None, {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')})```

---------
## Constants

---------
### MaxLen
#### Value
```python
2048
```
#### Python
```python
constant = substrate.get_constant('Base', 'MaxLen')
```
---------
## Errors

---------
### CounterOverflow
The sequence counter for something overflowed.

When this happens depends on e.g., the capacity of the identifier type.
For example, we might have `pub struct PipId(u32);`, with `u32::MAX` capacity.
In practice, these errors will never happen but no code path should result in a panic,
so these corner cases need to be covered with an error variant.

---------
### TooLong
Exceeded a generic length limit.
The limit could be for any sort of lists of things, including a string.

---------
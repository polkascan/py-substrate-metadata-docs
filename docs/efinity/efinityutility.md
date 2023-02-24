
# EfinityUtility

---------
## Calls

---------
### batch
Dispatch a batch of calls.

May be called from any origin except `None`.

- `calls`: The calls to be dispatched from the same origin. The number of call must not
  exceed the constant: `batched_calls_limit` (available in constant metadata).

If origin is root then the calls are dispatched without checking origin filter. (This
includes bypassing `frame_system::Config::BaseCallFilter`).
#### Attributes
| Name | Type |
| -------- | -------- | 
| calls | `Vec<<T as Config>::RuntimeCall>` | 
| continue_on_failure | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'EfinityUtility', 'batch', {
    'calls': ['Call'],
    'continue_on_failure': 'bool',
}
)
```

---------
## Events

---------
### BatchDispatched
Batch of calls dispatched without errors.
#### Attributes
No attributes

---------
### BatchFailed
Batch of calls did not disptach completely.
Index and error of the failing dispatch call is provided.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `u32` | ```u32```
| error | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}```

---------
### BatchPartiallyDispatched
Batch of calls dispatched, but some calls resulted in error.
Indexes and errors of failing dispatch calls are provided.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BatchErrors` | ```[('u32', {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None})]```

---------
## Constants

---------
### batched_calls_limit
 The limit on the number of batched calls.
#### Value
```python
10922
```
#### Python
```python
constant = substrate.get_constant('EfinityUtility', 'batched_calls_limit')
```
---------
## Errors

---------
### TooManyCalls
Too many calls batched.

---------

# Structure

---------
## Events

---------
### Executed
Executed call on behalf of the token.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
## Errors

---------
### BreadthLimit
While nesting, reached the breadth limit of nesting, exceeding the provided budget.

---------
### DepthLimit
While nesting, reached the depth limit of nesting, exceeding the provided budget.

---------
### OuroborosDetected
While nesting, encountered an already checked account, detecting a loop.

---------
### TokenNotFound
Couldn&\#x27;t find the token owner that is itself a token.

---------
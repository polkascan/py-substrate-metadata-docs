
# Structure

---------
## Events

---------
### Executed
Executed call on behalf of the token.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
## Errors

---------
### BreadthLimit
While nesting, reached the breadth limit of nesting, exceeding the provided budget.

---------
### CantNestTokenUnderCollection
Tried to nest token under collection contract address, instead of token address

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
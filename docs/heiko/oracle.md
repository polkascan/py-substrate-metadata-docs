
# Oracle

---------
## Calls

---------
### feed_values
Feed the external value.

Require authorized operator.
#### Attributes
| Name | Type |
| -------- | -------- | 
| values | `Vec<(T::OracleKey, T::OracleValue)>` | 

#### Python
```python
call = substrate.compose_call(
    'Oracle', 'feed_values', {'values': [('u32', 'u128')]}
)
```

---------
## Events

---------
### NewFeedData
New feed data is submitted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `T::AccountId` | ```AccountId```
| values | `Vec<(T::OracleKey, T::OracleValue)>` | ```[('u32', 'u128')]```

---------
## Storage functions

---------
### HasDispatched
 If an oracle operator has fed a value in this block

#### Python
```python
result = substrate.query(
    'Oracle', 'HasDispatched', []
)
```

#### Return value
```python
['AccountId']
```
---------
### RawValues
 Raw values for each oracle operators

#### Python
```python
result = substrate.query(
    'Oracle', 'RawValues', ['AccountId', 'u32']
)
```

#### Return value
```python
{'timestamp': 'u64', 'value': 'u128'}
```
---------
### Values
 Up to date combined value from Raw Values

#### Python
```python
result = substrate.query(
    'Oracle', 'Values', ['u32']
)
```

#### Return value
```python
{'timestamp': 'u64', 'value': 'u128'}
```
---------
## Constants

---------
### MaxHasDispatchedSize
 Maximum size of HasDispatched
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'MaxHasDispatchedSize')
```
---------
### RootOperatorAccountId
 The root operator account id, record all sudo feeds on this account.
#### Value
```python
'hJFDU5ssbB3JU6PyvaS4DrdVosVZd4zqJcqSd4rJt1W2ekYfn'
```
#### Python
```python
constant = substrate.get_constant('Oracle', 'RootOperatorAccountId')
```
---------
## Errors

---------
### AlreadyFeeded
Feeder has already feeded at this block

---------
### NoPermission
Sender does not have permission

---------
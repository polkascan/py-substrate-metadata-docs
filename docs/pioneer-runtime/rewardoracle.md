
# RewardOracle

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
    'RewardOracle', 'feed_values', {'values': [('u32', 'Bytes')]}
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
| values | `Vec<(T::OracleKey, T::OracleValue)>` | ```[('u32', 'Bytes')]```

---------
## Storage functions

---------
### HasDispatched
 If an oracle operator has fed a value in this block

#### Python
```python
result = substrate.query(
    'RewardOracle', 'HasDispatched', []
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
    'RewardOracle', 'RawValues', ['AccountId', 'u32']
)
```

#### Return value
```python
{'timestamp': 'u64', 'value': 'Bytes'}
```
---------
### Values
 Up to date combined value from Raw Values

#### Python
```python
result = substrate.query(
    'RewardOracle', 'Values', ['u32']
)
```

#### Return value
```python
{'timestamp': 'u64', 'value': 'Bytes'}
```
---------
## Constants

---------
### MaxHasDispatchedSize
 Maximum size of HasDispatched
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('RewardOracle', 'MaxHasDispatchedSize')
```
---------
### RootOperatorAccountId
 The root operator account id, record all sudo feeds on this account.
#### Value
```python
'WWdEH3Nm7jou4BvebuwiST74MaY38UpFYmp7Gho7qd31UhPzB'
```
#### Python
```python
constant = substrate.get_constant('RewardOracle', 'RootOperatorAccountId')
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
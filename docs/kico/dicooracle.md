
# DicoOracle

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
    'DicoOracle', 'feed_values', {'values': [('u32', 'u128')]}
)
```

---------
## Events

---------
### NewFeedData
New feed data is submitted. [sender, values,Time]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<(T::OracleKey, T::OracleValue)>` | ```[('u32', 'u128')]```
| None | `MomentOf<T, I>` | ```u64```

---------
### NewLockedPrice
New price is locked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::OracleKey` | ```u32```
| None | `T::OracleValue` | ```u128```

---------
### UnLockedPrice
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::OracleKey` | ```u32```

---------
## Storage functions

---------
### HasDispatched
 If an oracle operator has feed a value in this block

#### Python
```python
result = substrate.query(
    'DicoOracle', 'HasDispatched', []
)
```

#### Return value
```python
['AccountId']
```
---------
### IsUpdated
 True if Self::values(key) is up to date, otherwise the value is stale

#### Python
```python
result = substrate.query(
    'DicoOracle', 'IsUpdated', ['u32']
)
```

#### Return value
```python
'bool'
```
---------
### LockedPrice
 Mapping from currency id to it&#x27;s locked price

#### Python
```python
result = substrate.query(
    'DicoOracle', 'LockedPrice', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### Members
 The current members of the collective. This is stored sorted (just by
 value).

#### Python
```python
result = substrate.query(
    'DicoOracle', 'Members', []
)
```

#### Return value
```python
['AccountId']
```
---------
### Nonces

#### Python
```python
result = substrate.query(
    'DicoOracle', 'Nonces', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### OrcleKeys

#### Python
```python
result = substrate.query(
    'DicoOracle', 'OrcleKeys', ['u32']
)
```

#### Return value
```python
'bool'
```
---------
### RawValues
 Raw values for each oracle operators

#### Python
```python
result = substrate.query(
    'DicoOracle', 'RawValues', ['AccountId', 'u32']
)
```

#### Return value
```python
{'timestamp': 'u64', 'value': 'u128'}
```
---------
### Values
 Combined value, may not be up to date

#### Python
```python
result = substrate.query(
    'DicoOracle', 'Values', ['u32']
)
```

#### Return value
```python
{'timestamp': 'u64', 'value': 'u128'}
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
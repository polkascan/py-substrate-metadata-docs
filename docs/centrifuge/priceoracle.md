
# PriceOracle

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
    'PriceOracle', 'feed_values', {
    'values': [
        ({'Isin': '[u8; 12]'}, 'u128'),
    ],
}
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
| values | `Vec<(T::OracleKey, T::OracleValue)>` | ```[({'Isin': '[u8; 12]'}, 'u128')]```

---------
## Storage functions

---------
### HasDispatched
 If an oracle operator has fed a value in this block

#### Python
```python
result = substrate.query(
    'PriceOracle', 'HasDispatched', []
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
    'PriceOracle', 'RawValues', ['AccountId', {'Isin': '[u8; 12]'}]
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
    'PriceOracle', 'Values', [{'Isin': '[u8; 12]'}]
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
5
```
#### Python
```python
constant = substrate.get_constant('PriceOracle', 'MaxHasDispatchedSize')
```
---------
### RootOperatorAccountId
 The root operator account id, record all sudo feeds on this account.
#### Value
```python
'4dpEcgqJE2p7TzicFimuWRzCn3HLsgHwybW89vWwhp9pUi8F'
```
#### Python
```python
constant = substrate.get_constant('PriceOracle', 'RootOperatorAccountId')
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
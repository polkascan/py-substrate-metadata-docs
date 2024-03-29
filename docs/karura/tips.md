
# Tips

---------
## Calls

---------
### close_tip
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'close_tip', {'hash': 'scale_info::12'}
)
```

---------
### report_awesome
#### Attributes
| Name | Type |
| -------- | -------- | 
| reason | `Vec<u8>` | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'report_awesome', {
    'reason': 'Bytes',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### retract_tip
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'retract_tip', {'hash': 'scale_info::12'}
)
```

---------
### slash_tip
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'slash_tip', {'hash': 'scale_info::12'}
)
```

---------
### tip
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 
| tip_value | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'tip', {
    'hash': 'scale_info::12',
    'tip_value': 'u128',
}
)
```

---------
### tip_new
#### Attributes
| Name | Type |
| -------- | -------- | 
| reason | `Vec<u8>` | 
| who | `AccountIdLookupOf<T>` | 
| tip_value | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'Tips', 'tip_new', {
    'reason': 'Bytes',
    'tip_value': 'u128',
    'who': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
## Events

---------
### NewTip
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```scale_info::12```

---------
### TipClosed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```scale_info::12```
| who | `T::AccountId` | ```AccountId```
| payout | `BalanceOf<T, I>` | ```u128```

---------
### TipClosing
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```scale_info::12```

---------
### TipRetracted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```scale_info::12```

---------
### TipSlashed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```scale_info::12```
| finder | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Reasons

#### Python
```python
result = substrate.query(
    'Tips', 'Reasons', ['scale_info::12']
)
```

#### Return value
```python
'Bytes'
```
---------
### Tips

#### Python
```python
result = substrate.query(
    'Tips', 'Tips', ['scale_info::12']
)
```

#### Return value
```python
{
    'closes': (None, 'u32'),
    'deposit': 'u128',
    'finder': 'AccountId',
    'finders_fee': 'bool',
    'reason': 'scale_info::12',
    'tips': [('AccountId', 'u128')],
    'who': 'AccountId',
}
```
---------
## Constants

---------
### DataDepositPerByte
#### Value
```python
300000000
```
#### Python
```python
constant = substrate.get_constant('Tips', 'DataDepositPerByte')
```
---------
### MaxTipAmount
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Tips', 'MaxTipAmount')
```
---------
### MaximumReasonLength
#### Value
```python
8192
```
#### Python
```python
constant = substrate.get_constant('Tips', 'MaximumReasonLength')
```
---------
### TipCountdown
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('Tips', 'TipCountdown')
```
---------
### TipFindersFee
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Tips', 'TipFindersFee')
```
---------
### TipReportDepositBase
#### Value
```python
2000000000000
```
#### Python
```python
constant = substrate.get_constant('Tips', 'TipReportDepositBase')
```
---------
## Errors

---------
### AlreadyKnown

---------
### MaxTipAmountExceeded

---------
### NotFinder

---------
### Premature

---------
### ReasonTooBig

---------
### StillOpen

---------
### UnknownTip

---------

# Tips

---------
## Calls

---------
### close_tip
See [`Pallet::close_tip`].
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
See [`Pallet::report_awesome`].
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
    'who': 'AccountId',
}
)
```

---------
### retract_tip
See [`Pallet::retract_tip`].
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
See [`Pallet::slash_tip`].
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
See [`Pallet::tip`].
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
See [`Pallet::tip_new`].
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
    'who': 'AccountId',
}
)
```

---------
## Events

---------
### NewTip
A new tip suggestion has been opened.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```scale_info::12```

---------
### TipClosed
A tip suggestion has been closed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```scale_info::12```
| who | `T::AccountId` | ```AccountId```
| payout | `BalanceOf<T, I>` | ```u128```

---------
### TipClosing
A tip suggestion has reached threshold and is closing.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```scale_info::12```

---------
### TipRetracted
A tip suggestion has been retracted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| tip_hash | `T::Hash` | ```scale_info::12```

---------
### TipSlashed
A tip suggestion has been slashed.
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
 Simple preimage lookup from the reason&#x27;s hash to the original data. Again, has an
 insecure enumerable hash since the key is guaranteed to be the result of a secure hash.

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
 TipsMap that are not yet completed. Keyed by the hash of `(reason, who)` from the value.
 This has the insecure enumerable hash function since the key itself is already
 guaranteed to be a secure hash.

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
 The amount held on deposit per byte within the tip report reason or bounty description.
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Tips', 'DataDepositPerByte')
```
---------
### MaximumReasonLength
 Maximum acceptable reason length.

 Benchmarks depend on this value, be sure to update weights file when changing this value
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('Tips', 'MaximumReasonLength')
```
---------
### TipCountdown
 The period for which a tip remains open after is has achieved threshold tippers.
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
 The percent of the final tip which goes to the original reporter of the tip.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Tips', 'TipFindersFee')
```
---------
### TipReportDepositBase
 The amount held on deposit for placing a tip report.
#### Value
```python
1000000000000000
```
#### Python
```python
constant = substrate.get_constant('Tips', 'TipReportDepositBase')
```
---------
## Errors

---------
### AlreadyKnown
The tip was already found/started.

---------
### NotFinder
The account attempting to retract the tip is not the finder of the tip.

---------
### Premature
The tip cannot be claimed/closed because it&\#x27;s still in the countdown period.

---------
### ReasonTooBig
The reason given is just too big.

---------
### StillOpen
The tip cannot be claimed/closed because there are not enough tippers yet.

---------
### UnknownTip
The tip hash is unknown.

---------
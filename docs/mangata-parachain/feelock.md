
# FeeLock

---------
## Calls

---------
### unlock_fee
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'FeeLock', 'unlock_fee', {}
)
```

---------
### update_fee_lock_metadata
#### Attributes
| Name | Type |
| -------- | -------- | 
| period_length | `Option<T::BlockNumber>` | 
| fee_lock_amount | `Option<Balance>` | 
| swap_value_threshold | `Option<Balance>` | 
| should_be_whitelisted | `Option<Vec<(TokenId, bool)>>` | 

#### Python
```python
call = substrate.compose_call(
    'FeeLock', 'update_fee_lock_metadata', {
    'fee_lock_amount': (None, 'u128'),
    'period_length': (None, 'u32'),
    'should_be_whitelisted': (
        None,
        [('u32', 'bool')],
    ),
    'swap_value_threshold': (
        None,
        'u128',
    ),
}
)
```

---------
## Events

---------
### FeeLockMetadataUpdated
#### Attributes
No attributes

---------
### FeeLockUnlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### AccountFeeLockData

#### Python
```python
result = substrate.query(
    'FeeLock', 'AccountFeeLockData', ['AccountId']
)
```

#### Return value
```python
{'last_fee_lock_block': 'u32', 'total_fee_lock_amount': 'u128'}
```
---------
### FeeLockMetadata

#### Python
```python
result = substrate.query(
    'FeeLock', 'FeeLockMetadata', []
)
```

#### Return value
```python
{
    'fee_lock_amount': 'u128',
    'period_length': 'u32',
    'swap_value_threshold': 'u128',
    'whitelisted_tokens': 'scale_info::203',
}
```
---------
## Constants

---------
### MaxCuratedTokens
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('FeeLock', 'MaxCuratedTokens')
```
---------
### NativeTokenId
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('FeeLock', 'NativeTokenId')
```
---------
## Errors

---------
### CantUnlockFeeYet
The lock cannot be unlocked yet

---------
### FeeLocksIncorrectlyInitialzed
Locks were incorrectly initialized

---------
### FeeLocksNotInitialized
Locks have not been initialzed

---------
### InvalidFeeLockMetadata
Lock metadata is invalid

---------
### MaxCuratedTokensLimitExceeded
The limit on the maximum curated tokens for which there is a swap threshold is exceeded

---------
### NotFeeLocked
No tokens of the user are fee-locked

---------
### UnexpectedFailure
An unexpected failure has occured

---------
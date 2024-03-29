
# BridgeTransfer

---------
## Calls

---------
### sudo_change_fee
See [`Pallet::sudo_change_fee`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_fee | `BalanceOf<T>` | 
| fee_scale | `u32` | 
| dest_id | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeTransfer', 'sudo_change_fee', {
    'dest_id': 'u8',
    'fee_scale': 'u32',
    'min_fee': 'u128',
}
)
```

---------
### transfer
See [`Pallet::transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| amount | `BalanceOf<T>` | 
| rid | `[u8; 32]` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeTransfer', 'transfer', {
    'amount': 'u128',
    'rid': '[u8; 32]',
    'to': 'AccountId',
}
)
```

---------
### transfer_native
See [`Pallet::transfer_native`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| recipient | `Vec<u8>` | 
| dest_id | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeTransfer', 'transfer_native', {
    'amount': 'u128',
    'dest_id': 'u8',
    'recipient': 'Bytes',
}
)
```

---------
## Events

---------
### FeeUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u8` | ```u8```
| None | `BalanceOf<T>` | ```u128```
| None | `u32` | ```u32```

---------
## Storage functions

---------
### BridgeFee
 Tracks current relayer set

#### Python
```python
result = substrate.query(
    'BridgeTransfer', 'BridgeFee', ['u8']
)
```

#### Return value
```python
('u128', 'u32')
```
---------
## Errors

---------
### FeeOptionsMissiing

---------
### InvalidCommand

---------
### InvalidFeeOption

---------
### InvalidPayload

---------
### InvalidTransfer

---------
### LessThanFee

---------
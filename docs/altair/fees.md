
# Fees

---------
## Calls

---------
### set_fee
Set the given fee for the key
#### Attributes
| Name | Type |
| -------- | -------- | 
| key | `T::FeeKey` | 
| fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Fees', 'set_fee', {
    'fee': 'u128',
    'key': (
        'AnchorsCommit',
        'AnchorsPreCommit',
        'BridgeNativeTransfer',
        'NftProofValidation',
        'AllowanceCreation',
    ),
}
)
```

---------
## Events

---------
### FeeChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| key | `T::FeeKey` | ```('AnchorsCommit', 'AnchorsPreCommit', 'BridgeNativeTransfer', 'NftProofValidation', 'AllowanceCreation')```
| fee | `BalanceOf<T>` | ```u128```

---------
### FeeToAuthor
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| balance | `BalanceOf<T>` | ```u128```

---------
### FeeToBurn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| balance | `BalanceOf<T>` | ```u128```

---------
### FeeToTreasury
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| balance | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### FeeBalances
 Stores the fee balances associated with a Hash identifier

#### Python
```python
result = substrate.query(
    'Fees', 'FeeBalances', [
    (
        'AnchorsCommit',
        'AnchorsPreCommit',
        'BridgeNativeTransfer',
        'NftProofValidation',
        'AllowanceCreation',
    ),
]
)
```

#### Return value
```python
'u128'
```
---------
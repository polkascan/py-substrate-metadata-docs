
# OracleFinance

---------
## Calls

---------
### take_all_purchase_reward
Validators get rewards, it will help validators get all available rewards

_Note_: An ear cannot be the current unfinished era, and rewards are not permanently stored.
If the reward exceeds the depth defined by T::HistoryDepth, you will not be able to claim it.

The dispatch origin for this call must be _Signed_

Earliest reward Era = Current-Era - T::HistoryDepth
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'OracleFinance', 'take_all_purchase_reward', {}
)
```

---------
### take_purchase_reward
Validators get rewards corresponding to eras.

_Note_: An ear cannot be the current unfinished era, and rewards are not permanently stored.
If the reward exceeds the depth defined by T::HistoryDepth, you will not be able to claim it.

The dispatch origin for this call must be _Signed_

Earliest reward Era = Current-Era - T::HistoryDepth

- ask_era: Era number is a u32
#### Attributes
| Name | Type |
| -------- | -------- | 
| ask_era | `EraIndex` | 

#### Python
```python
call = substrate.compose_call(
    'OracleFinance', 'take_purchase_reward', {'ask_era': 'u32'}
)
```

---------
## Events

---------
### EndOfAskEra
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| era | `EraIndex` | ```u32```
| era_income | `BalanceOf<T>` | ```u128```
| era_points | `AskPointNum` | ```u32```
| session_index | `SessionIndex` | ```u32```

---------
### PayForPurchase
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| agg_count | `u32` | ```u32```
| dest | `T::AccountId` | ```AccountId```
| fee | `BalanceOf<T>` | ```u128```
| purchase_id | `PurchaseId` | ```Bytes```
| unreserve_balance | `BalanceOf<T>` | ```u128```
| who | `T::AccountId` | ```AccountId```

---------
### PurchaseRewardSlashedAfterExpiration
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| created_at | `T::BlockNumber` | ```u32```
| era | `EraIndex` | ```u32```
| slash | `BalanceOf<T>` | ```u128```

---------
### PurchaseRewardToken
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| created_at | `T::BlockNumber` | ```u32```
| era | `EraIndex` | ```u32```
| who | `T::AccountId` | ```AccountId```
| reward | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AskEraPayment

#### Python
```python
result = substrate.query(
    'OracleFinance', 'AskEraPayment', ['u32', ('AccountId', 'Bytes')]
)
```

#### Return value
```python
'u128'
```
---------
### AskEraPoint

#### Python
```python
result = substrate.query(
    'OracleFinance', 'AskEraPoint', ['u32', ('AccountId', 'Bytes')]
)
```

#### Return value
```python
'u32'
```
---------
### CurrentEra

#### Python
```python
result = substrate.query(
    'OracleFinance', 'CurrentEra', []
)
```

#### Return value
```python
'u32'
```
---------
### ErasStartSessionIndex

#### Python
```python
result = substrate.query(
    'OracleFinance', 'ErasStartSessionIndex', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### PaymentTrace

#### Python
```python
result = substrate.query(
    'OracleFinance', 'PaymentTrace', ['Bytes', 'AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'create_bn': 'u32', 'is_income': 'bool', 'paid_era': 'u32'}
```
---------
### RewardEra

#### Python
```python
result = substrate.query(
    'OracleFinance', 'RewardEra', ['AccountId']
)
```

#### Return value
```python
[('u32', 'u32', 'Bytes')]
```
---------
### RewardTrace

#### Python
```python
result = substrate.query(
    'OracleFinance', 'RewardTrace', ['u32', 'AccountId']
)
```

#### Return value
```python
('u32', 'u128')
```
---------
## Constants

---------
### AskPerEra
#### Value
```python
6
```
#### Python
```python
constant = substrate.get_constant('OracleFinance', 'AskPerEra')
```
---------
### BasicDollars
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('OracleFinance', 'BasicDollars')
```
---------
### HistoryDepth
#### Value
```python
84
```
#### Python
```python
constant = substrate.get_constant('OracleFinance', 'HistoryDepth')
```
---------
### PalletId
#### Value
```python
'0x616f652f66756e64'
```
#### Python
```python
constant = substrate.get_constant('OracleFinance', 'PalletId')
```
---------
## Errors

---------
### CalculateFeeError

---------
### NoPotAccount

---------
### NoRewardPoints

---------
### NoStashAccount

---------
### NoneValue
Error names should be descriptive.

---------
### NotFoundPaymentRecord

---------
### PointRecordIsAlreadyExists

---------
### RefundFailed

---------
### RewardEraHasExpired

---------
### RewardHasBeenClaimed

---------
### RewardSlotNotExpired

---------
### StorageOverflow
Errors should have helpful documentation associated with them.

---------
### TransferBalanceError

---------
### UnReserveBalanceError

---------
### VectorIsFull

---------
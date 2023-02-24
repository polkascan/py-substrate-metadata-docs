
# FarmExtend

---------
## Calls

---------
### create_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| start_block | `T::BlockNumber` | 
| end_block | `T::BlockNumber` | 
| reward_per_block | `Balance` | 
| stake_currency_id | `AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'FarmExtend', 'create_pool', {
    'currency_id': 'u32',
    'end_block': 'u32',
    'reward_per_block': 'u128',
    'stake_currency_id': 'u32',
    'start_block': 'u32',
}
)
```

---------
### deposit_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_extend_id | `T::PoolExtendId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'FarmExtend', 'deposit_asset', {
    'amount': 'u128',
    'pool_extend_id': 'u32',
}
)
```

---------
### withdraw_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_extend_id | `T::PoolExtendId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'FarmExtend', 'withdraw_asset', {
    'amount': 'u128',
    'pool_extend_id': 'u32',
}
)
```

---------
## Events

---------
### AssetDeposited
Liquidity was deposited. [who, pool id, liquidity amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::PoolExtendId` | ```u32```
| None | `Balance` | ```u128```

---------
### AssetWithdrawn
Liquidity was Withdrawn. [who, pool id, liquidity amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::PoolExtendId` | ```u32```
| None | `Balance` | ```u128```

---------
### PoolExtendCreated
The mining pool was created. [pool id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::PoolExtendId` | ```u32```
| None | `AssetId` | ```u32```
| None | `Balance` | ```u128```
| None | `AssetId` | ```u32```

---------
## Storage functions

---------
### NextPoolExtendId

#### Python
```python
result = substrate.query(
    'FarmExtend', 'NextPoolExtendId', []
)
```

#### Return value
```python
'u32'
```
---------
### ParticipantExtends

#### Python
```python
result = substrate.query(
    'FarmExtend', 'ParticipantExtends', ['u32', 'AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'reward_debt': 'u128'}
```
---------
### PoolExtends

#### Python
```python
result = substrate.query(
    'FarmExtend', 'PoolExtends', ['u32']
)
```

#### Return value
```python
{
    'acc_reward_per_share': 'u128',
    'currency_amount': 'u128',
    'currency_id': 'u32',
    'end_block': 'u32',
    'last_reward_block': 'u32',
    'owner': 'AccountId',
    'reward_per_block': 'u128',
    'stake_currency_id': 'u32',
    'start_block': 'u32',
    'total_stake_amount': 'u128',
}
```
---------
## Constants

---------
### PalletId
 The mining pool&#x27;s module id, keep all assets in pool.
#### Value
```python
'0x6469636f2f666d65'
```
#### Python
```python
constant = substrate.get_constant('FarmExtend', 'PalletId')
```
---------
## Errors

---------
### InsufficientWithdrawAmount
Invalid withdrawal amount.

---------
### InvalidBlockConfigure

---------
### InvalidRewardPerBlock

---------
### MustBeDifferentAsset

---------
### NoPoolExtendIdAvailable
No pool id available.

---------
### PoolExtendExisted
Pool already exists.

---------
### PoolExtendNotFind
The mining pool does not exist.

---------
### StartBlockOutDate

---------
### UserNotFindInPoolExtend
The user does not exist in the mining pool.

---------
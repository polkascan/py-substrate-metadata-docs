
# Farm

---------
## Calls

---------
### create_pool
Create a new mining pool.

The liquidity id can be the lp id or the asset id of a single currency.

Emits `PoolCreated` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `AssetId` | 
| alloc_point | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Farm', 'create_pool', {
    'alloc_point': 'u128',
    'currency_id': 'u32',
}
)
```

---------
### deposit_lp
Deposit liquid assets to designated mining pools to participate in mining.

Emits `LpDeposited` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Farm', 'deposit_lp', {'amount': 'u128', 'pool_id': 'u32'}
)
```

---------
### set_dico_per_block
Set the reward for each block when starting mining.

The actual mining reward for each block depends on this parameter and the halving cycle.

This method needs to be called before the mining pool is created.
Once mining starts, do not call this method again, otherwise it may
 cause an error in the reward calculation.

Emits `DicoPerBlockIsSet` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_per_block | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Farm', 'set_dico_per_block', {'new_per_block': 'u128'}
)
```

---------
### set_halving_period
Set the mining reward halving cycle,the unit is the number of blocks.

This method needs to be called before the mining pool is created.
Once mining starts, do not call this method again, otherwise it may
 cause an error in the reward calculation.
Emits `HalvingPeriodIsSet` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_number | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Farm', 'set_halving_period', {'block_number': 'u32'}
)
```

---------
### set_start_block
Set the block number of the mining pool to start mining.

This method needs to be called before the mining pool is created.
Once mining starts, do not call this method again, otherwise it may
cause an error in the reward calculation.

Emits `StartBlockIsSet` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| block_number | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Farm', 'set_start_block', {'block_number': 'u32'}
)
```

---------
### update_pool_alloc_point
Update the allocated points of each designated mining pool.

This method can be called multiple times without causing a reward calculation error.

Emits `PoolAllocPointUpdated` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| alloc_point | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'Farm', 'update_pool_alloc_point', {
    'alloc_point': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### withdraw_lp
Withdraw liquidity.

if amount = 0, then only withdraw mining harvest,and liquidity assets remain unchanged.
if amount &gt; 0, in addition to the withdrawal of mining rewards, the amount of assets
will also be withdrawn.

Emits `LpWithdrawn` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Farm', 'withdraw_lp', {'amount': 'u128', 'pool_id': 'u32'}
)
```

---------
## Events

---------
### DicoPerBlockIsSet
The reward for each block was set. [dico amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### HalvingPeriodIsSet
The mining reward halving cycle was set. [block number]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
### LpDeposited
Liquidity was deposited. [who, pool id, liquidity amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::PoolId` | ```u32```
| None | `Balance` | ```u128```

---------
### LpWithdrawn
Liquidity was Withdrawn. [who, pool id, liquidity amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::PoolId` | ```u32```
| None | `Balance` | ```u128```

---------
### PoolAllocPointUpdated
The allocated points of each designated mining pool was updated. [pool id, alloc point]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::PoolId` | ```u32```
| None | `u128` | ```u128```

---------
### PoolCreated
The mining pool was created. [pool id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::PoolId` | ```u32```

---------
### StartBlockIsSet
The block number of the mining pool to start mining was set. [block number]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### DicoPerBlock

#### Python
```python
result = substrate.query(
    'Farm', 'DicoPerBlock', []
)
```

#### Return value
```python
'u128'
```
---------
### HalvingPeriod

#### Python
```python
result = substrate.query(
    'Farm', 'HalvingPeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### NextPoolId

#### Python
```python
result = substrate.query(
    'Farm', 'NextPoolId', []
)
```

#### Return value
```python
'u32'
```
---------
### Participants

#### Python
```python
result = substrate.query(
    'Farm', 'Participants', ['u32', 'AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'reward_debt': 'u128'}
```
---------
### Pools

#### Python
```python
result = substrate.query(
    'Farm', 'Pools', ['u32']
)
```

#### Return value
```python
{
    'acc_dico_per_share': 'u128',
    'alloc_point': 'u128',
    'currency_id': 'u32',
    'last_reward_block': 'u32',
    'total_amount': 'u128',
}
```
---------
### StartBlock

#### Python
```python
result = substrate.query(
    'Farm', 'StartBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### TotalAllocPoint

#### Python
```python
result = substrate.query(
    'Farm', 'TotalAllocPoint', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### NativeAssetId
 Native Asset Id
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Farm', 'NativeAssetId')
```
---------
### PalletId
 The mining pool&#x27;s module id, keep all assets in pool.
#### Value
```python
'0x6469636f2f66616d'
```
#### Python
```python
constant = substrate.get_constant('Farm', 'PalletId')
```
---------
## Errors

---------
### InsufficientWithdrawAmount
Invalid withdrawal amount.

---------
### LiquidityIdCreated
Liquidity already exists.

---------
### LiquidityIdZeroIssuance
The total issuance of liquid assets is zero.

---------
### NoPoolIdAvailable
No pool id available.

---------
### PoolExisted
Pool already exists.

---------
### PoolNotFind
The mining pool does not exist.

---------
### UserNotFindInPool
The user does not exist in the mining pool.

---------
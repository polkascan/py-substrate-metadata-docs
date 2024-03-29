
# Farming

---------
## Calls

---------
### charge
After create farming pool, need to deposit reward token into the pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'charge', {
    'pool_id': 'u128',
    'rewards': [('u128', 'u128')],
}
)
```

---------
### claim
`claim` operation can claim rewards and also un-stake if user share info has `withdraw_list`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'claim', {'pool_id': 'u128'}
)
```

---------
### close_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'close_pool', {'pool_id': 'u128'}
)
```

---------
### create_farming_pool
`ControlOrigin` create the farming pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| tokens_proportion | `Vec<(CurrencyIdOf<T>, Perbill)>` | 
| basic_rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | 
| gauge_init | `Option<GaugeInitType<T>>` | 
| min_deposit_to_start | `BalanceOf<T>` | 
| after_block_to_start | `BlockNumberFor<T>` | 
| withdraw_limit_time | `BlockNumberFor<T>` | 
| claim_limit_time | `BlockNumberFor<T>` | 
| withdraw_limit_count | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'create_farming_pool', {
    'after_block_to_start': 'u32',
    'basic_rewards': [('u128', 'u128')],
    'claim_limit_time': 'u32',
    'gauge_init': (
        None,
        (
            'u128',
            'u32',
            [('u128', 'u128')],
        ),
    ),
    'min_deposit_to_start': 'u128',
    'tokens_proportion': [
        ('u128', 'u32'),
    ],
    'withdraw_limit_count': 'u8',
    'withdraw_limit_time': 'u32',
}
)
```

---------
### deposit
User can deposit token to farming pool, and get share of pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| add_value | `BalanceOf<T>` | 
| gauge_info | `Option<(BalanceOf<T>, BlockNumberFor<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'deposit', {
    'add_value': 'u128',
    'gauge_info': (
        None,
        ('u128', 'u32'),
    ),
    'pool_id': 'u128',
}
)
```

---------
### edit_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| basic_rewards | `Option<Vec<(CurrencyIdOf<T>, BalanceOf<T>)>>` | 
| withdraw_limit_time | `Option<BlockNumberFor<T>>` | 
| claim_limit_time | `Option<BlockNumberFor<T>>` | 
| gauge_basic_rewards | `Option<Vec<(CurrencyIdOf<T>, BalanceOf<T>)>>` | 
| withdraw_limit_count | `Option<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'edit_pool', {
    'basic_rewards': (
        None,
        [('u128', 'u128')],
    ),
    'claim_limit_time': (None, 'u32'),
    'gauge_basic_rewards': (
        None,
        [('u128', 'u128')],
    ),
    'pool_id': 'u128',
    'withdraw_limit_count': (
        None,
        'u8',
    ),
    'withdraw_limit_time': (
        None,
        'u32',
    ),
}
)
```

---------
### force_gauge_claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| gid | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'force_gauge_claim', {'gid': 'u128'}
)
```

---------
### gauge_withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| gid | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'gauge_withdraw', {'gid': 'u128'}
)
```

---------
### kill_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'kill_pool', {'pool_id': 'u128'}
)
```

---------
### reset_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| basic_rewards | `Option<Vec<(CurrencyIdOf<T>, BalanceOf<T>)>>` | 
| min_deposit_to_start | `Option<BalanceOf<T>>` | 
| after_block_to_start | `Option<BlockNumberFor<T>>` | 
| withdraw_limit_time | `Option<BlockNumberFor<T>>` | 
| claim_limit_time | `Option<BlockNumberFor<T>>` | 
| withdraw_limit_count | `Option<u8>` | 
| gauge_init | `Option<GaugeInitType<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'reset_pool', {
    'after_block_to_start': (
        None,
        'u32',
    ),
    'basic_rewards': (
        None,
        [('u128', 'u128')],
    ),
    'claim_limit_time': (None, 'u32'),
    'gauge_init': (
        None,
        (
            'u128',
            'u32',
            [('u128', 'u128')],
        ),
    ),
    'min_deposit_to_start': (
        None,
        'u128',
    ),
    'pool_id': 'u128',
    'withdraw_limit_count': (
        None,
        'u8',
    ),
    'withdraw_limit_time': (
        None,
        'u32',
    ),
}
)
```

---------
### retire_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'retire_pool', {'pool_id': 'u128'}
)
```

---------
### set_retire_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'set_retire_limit', {'limit': 'u32'}
)
```

---------
### withdraw
`Withdraw` operation only remove share and get claim rewards, then update `withdraw_list` of user share info.
This operation don&\#x27;t withdrawn staked token.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| remove_value | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'withdraw', {
    'pool_id': 'u128',
    'remove_value': (None, 'u128'),
}
)
```

---------
### withdraw_claim
`withdraw_claim` operation will un-stake user staked token on farming pool from keeper account to user account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Farming', 'withdraw_claim', {'pool_id': 'u128'}
)
```

---------
## Events

---------
### AllForceGaugeClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| gid | `PoolId` | ```u128```

---------
### AllRetired
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u128```

---------
### Charged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u128```
| rewards | `Vec<(CurrencyIdOf<T>, BalanceOf<T>)>` | ```[('u128', 'u128')]```

---------
### Claimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u128```

---------
### Deposited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u128```
| add_value | `BalanceOf<T>` | ```u128```
| gauge_info | `Option<(BalanceOf<T>, BlockNumberFor<T>)>` | ```(None, ('u128', 'u32'))```

---------
### FarmingPoolClosed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u128```

---------
### FarmingPoolCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u128```

---------
### FarmingPoolEdited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u128```

---------
### FarmingPoolKilled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u128```

---------
### FarmingPoolReset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u128```

---------
### GaugeWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| gid | `PoolId` | ```u128```

---------
### PartiallyForceGaugeClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| gid | `PoolId` | ```u128```

---------
### PartiallyRetired
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `PoolId` | ```u128```

---------
### RetireLimitSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| limit | `u32` | ```u32```

---------
### WithdrawClaimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u128```

---------
### Withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| pid | `PoolId` | ```u128```
| remove_value | `Option<BalanceOf<T>>` | ```(None, 'u128')```

---------
## Storage functions

---------
### GaugeInfos
 Record gauge info for specific `AccountId` under `PoolId`.

 double_map (PoolId, AccountId) =&gt; GaugeInfo

#### Python
```python
result = substrate.query(
    'Farming', 'GaugeInfos', ['u128', 'AccountId']
)
```

#### Return value
```python
{
    'claimed_time_factor': 'u128',
    'gauge_amount': 'u128',
    'gauge_last_block': 'u32',
    'gauge_start_block': 'u32',
    'gauge_stop_block': 'u32',
    'last_claim_block': 'u32',
    'latest_time_factor': 'u128',
    'total_time_factor': 'u128',
    'who': 'AccountId',
}
```
---------
### GaugePoolInfos
 Record gauge farming pool info.

 map PoolId =&gt; GaugePoolInfo

#### Python
```python
result = substrate.query(
    'Farming', 'GaugePoolInfos', ['u128']
)
```

#### Return value
```python
{
    'gauge_amount': 'u128',
    'gauge_basic_rewards': 'scale_info::505',
    'gauge_last_block': 'u32',
    'gauge_state': ('Unbond', 'Bonded'),
    'keeper': 'AccountId',
    'max_block': 'u32',
    'pool_id': 'u128',
    'reward_issuer': 'AccountId',
    'rewards': 'scale_info::511',
    'token': 'u128',
    'total_time_factor': 'u128',
}
```
---------
### GaugePoolNextId
 The next gauge farming pool id.

#### Python
```python
result = substrate.query(
    'Farming', 'GaugePoolNextId', []
)
```

#### Return value
```python
'u128'
```
---------
### PoolInfos
 Record reward pool info.

 map PoolId =&gt; PoolInfo

#### Python
```python
result = substrate.query(
    'Farming', 'PoolInfos', ['u128']
)
```

#### Return value
```python
{
    'after_block_to_start': 'u32',
    'basic_rewards': 'scale_info::505',
    'basic_token': ('u128', 'u32'),
    'block_startup': (None, 'u32'),
    'claim_limit_time': 'u32',
    'gauge': (None, 'u128'),
    'keeper': 'AccountId',
    'min_deposit_to_start': 'u128',
    'reward_issuer': 'AccountId',
    'rewards': 'scale_info::506',
    'state': ('UnCharged', 'Charged', 'Ongoing', 'Dead', 'Retired'),
    'tokens_proportion': 'scale_info::504',
    'total_shares': 'u128',
    'withdraw_limit_count': 'u8',
    'withdraw_limit_time': 'u32',
}
```
---------
### PoolNextId
 The next farming pool id.

#### Python
```python
result = substrate.query(
    'Farming', 'PoolNextId', []
)
```

#### Return value
```python
'u128'
```
---------
### RetireLimit
 The retire limit of one operation when retire farming pool.

#### Python
```python
result = substrate.query(
    'Farming', 'RetireLimit', []
)
```

#### Return value
```python
'u32'
```
---------
### SharesAndWithdrawnRewards
 Record share amount, reward currency and withdrawn reward amount for
 specific `AccountId` under `PoolId`.

 double_map (PoolId, AccountId) =&gt; ShareInfo

#### Python
```python
result = substrate.query(
    'Farming', 'SharesAndWithdrawnRewards', ['u128', 'AccountId']
)
```

#### Return value
```python
{
    'claim_last_block': 'u32',
    'share': 'u128',
    'who': 'AccountId',
    'withdraw_list': [('u32', 'u128')],
    'withdrawn_rewards': 'scale_info::505',
}
```
---------
## Constants

---------
### Keeper
 ModuleID for creating sub account
#### Value
```python
'0x6d742f666d6b7072'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'Keeper')
```
---------
### RewardIssuer
#### Value
```python
'0x6d742f666d726972'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'RewardIssuer')
```
---------
### TreasuryAccount
#### Value
```python
'dmwQify37xfGt1wDhAi8zfvovsAkdK3aD4iqW8dn8nfrsAYsX'
```
#### Python
```python
constant = substrate.get_constant('Farming', 'TreasuryAccount')
```
---------
## Errors

---------
### CanNotClaim
claim_limit_time exceeded

---------
### CanNotDeposit
Can not deposit to pool yet

---------
### GaugeInfoNotExist
Gauge info not exist

---------
### GaugeMaxBlockOverflow
gauge pool max_block exceeded

---------
### GaugePoolNotExist
Gauge pool not exist

---------
### InvalidPoolParameter
Pool parameter is invalid

---------
### InvalidPoolState
Pool state is invalid

---------
### LastGaugeNotClaim
Can not claim gauge

---------
### PoolDoesNotExist
Pool not exist

---------
### RetireLimitNotSet
The retire limit number is not set

---------
### ShareInfoNotExists
Share info is not exist

---------
### WithdrawLimitCountExceeded
withdraw_limit_time exceeded

---------
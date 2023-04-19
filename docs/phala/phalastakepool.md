
# PhalaStakePool

---------
## Storage functions

---------
### PoolContributionWhitelists
 Mapping for pools that specify certain stakers to contribute stakes

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'PoolContributionWhitelists', ['u64']
)
```

#### Return value
```python
['AccountId']
```
---------
### PoolCount
 The number of total pools

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'PoolCount', []
)
```

#### Return value
```python
'u64'
```
---------
### PoolDescriptions
 Mapping for pools that store their descriptions set by owner

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'PoolDescriptions', ['u64']
)
```

#### Return value
```python
'Bytes'
```
---------
### PoolStakers
 Mapping from (pid, staker) to UserStakeInfo

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'PoolStakers', [('u64', 'AccountId')]
)
```

#### Return value
```python
{
    'available_rewards': 'u128',
    'locked': 'u128',
    'reward_debt': 'u128',
    'shares': 'u128',
    'user': 'AccountId',
}
```
---------
### StakeLedger
 Mapping staker to it&#x27;s the balance locked in all pools

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'StakeLedger', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### StakePools
 Mapping from pool id to PoolInfo

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'StakePools', ['u64']
)
```

#### Return value
```python
{
    'cap': (None, 'u128'),
    'free_stake': 'u128',
    'owner': 'AccountId',
    'owner_reward': 'u128',
    'payout_commission': (None, 'u32'),
    'pid': 'u64',
    'releasing_stake': 'u128',
    'reward_acc': 'u128',
    'total_shares': 'u128',
    'total_stake': 'u128',
    'withdraw_queue': [
        {'shares': 'u128', 'start_time': 'u64', 'user': 'AccountId'},
    ],
    'workers': ['[u8; 32]'],
}
```
---------
### SubAccountAssignments
 (Deprecated)

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'SubAccountAssignments', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### SubAccountPreimages
 Helper storage to track the preimage of the mining sub-accounts. Not used in consensus.

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'SubAccountPreimages', ['AccountId']
)
```

#### Return value
```python
('u64', '[u8; 32]')
```
---------
### WithdrawalQueuedPools
 Mapping from the block timestamp to pools that has withdrawal requests queued in that block

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'WithdrawalQueuedPools', ['u64']
)
```

#### Return value
```python
['u64']
```
---------
### WithdrawalTimestamps
 Queue that contains all block&#x27;s timestamp, in that block contains the waiting withdraw reqeust.
 This queue has a max size of (T::GracePeriod * 8) bytes

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'WithdrawalTimestamps', []
)
```

#### Return value
```python
['u64']
```
---------
### WorkerAssignments
 Mapping from workers to the pool they belong to

 The map entry lasts from `add_worker()` to `remove_worker()` or force unbinding.

#### Python
```python
result = substrate.query(
    'PhalaStakePool', 'WorkerAssignments', ['[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
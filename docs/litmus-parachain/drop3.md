
# Drop3

---------
## Calls

---------
### approve_reward_pool
Approve a RewardPool proposal, must be called from admin
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Drop3', 'approve_reward_pool', {'id': 'u64'}
)
```

---------
### close_reward_pool
Close a reward pool, can be called by admin or reward pool owner

Note here `approved` state is not required, which gives the owner a
chance to close it before the admin evaluates the proposal
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Drop3', 'close_reward_pool', {'id': 'u64'}
)
```

---------
### propose_reward_pool
Create a RewardPool proposal, can be called by any signed account
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `Vec<u8>` | 
| total | `BalanceOf<T>` | 
| start_at | `T::BlockNumber` | 
| end_at | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Drop3', 'propose_reward_pool', {
    'end_at': 'u32',
    'name': 'Bytes',
    'start_at': 'u32',
    'total': 'u128',
}
)
```

---------
### reject_reward_pool
Reject a RewardPool proposal, must be called from admin
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Drop3', 'reject_reward_pool', {'id': 'u64'}
)
```

---------
### send_reward
transfer an amount of reserved balance to some other user
must be called by reward pool owner
TODO:
`repatriate_reserved()` requires that the destination account is active
otherwise `DeadAccount` error is returned. Is it OK in our case?
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::PoolId` | 
| to | `T::AccountId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Drop3', 'send_reward', {
    'amount': 'u128',
    'id': 'u64',
    'to': 'AccountId',
}
)
```

---------
### set_admin
Change the admin account
similar to sudo.set_key, the old account will be supplied in event
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Drop3', 'set_admin', {'new': 'AccountId'}
)
```

---------
### start_reward_pool
Start a reward pool, can be called by admin or reward pool owner
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Drop3', 'start_reward_pool', {'id': 'u64'}
)
```

---------
### stop_reward_pool
Stop a reward pool, can be called by admin or reward pool owner
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Drop3', 'stop_reward_pool', {'id': 'u64'}
)
```

---------
## Events

---------
### AdminChanged
Admin acccount was changed, the \[ old admin \] is provided
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_admin | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### BalanceSlashed
An \[ amount \] balance of \[ who \] was slashed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardPoolApproved
A reward pool with \[ id \] was approved by admin
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `T::PoolId` | ```u64```

---------
### RewardPoolProposed
A reward pool with \[ id, name, owner \] was proposed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `T::PoolId` | ```u64```
| name | `Vec<u8>` | ```Bytes```
| owner | `T::AccountId` | ```AccountId```

---------
### RewardPoolRejected
A reward pool with \[ id \] was rejected by admin
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `T::PoolId` | ```u64```

---------
### RewardPoolRemoved
A reward pool with \[ id, name, owner \] was removed, either by admin or owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `T::PoolId` | ```u64```
| name | `Vec<u8>` | ```Bytes```
| owner | `T::AccountId` | ```AccountId```

---------
### RewardPoolStarted
A reward pool with \[ id \] was started, either by admin or owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `T::PoolId` | ```u64```

---------
### RewardPoolStopped
A reward pool with \[ id \] was stopped, either by admin or owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `T::PoolId` | ```u64```

---------
### RewardSent
An \[ amount \] of reward was sent to \[ to \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| to | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Admin
 The reward pool admin account
 The reason why such an account is needed (other than just using ROOT) is for
 fast processing of reward proposals, imagine later when sudo is removed

#### Python
```python
result = substrate.query(
    'Drop3', 'Admin', []
)
```

#### Return value
```python
'AccountId'
```
---------
### CurrentMaxPoolId

#### Python
```python
result = substrate.query(
    'Drop3', 'CurrentMaxPoolId', []
)
```

#### Return value
```python
'u64'
```
---------
### RewardPoolOwners
 Map for PoolId &lt;&gt; RewardPoolOwner

#### Python
```python
result = substrate.query(
    'Drop3', 'RewardPoolOwners', ['u64']
)
```

#### Return value
```python
'AccountId'
```
---------
### RewardPools
 Map for PoolId &lt;&gt; RewardPool

#### Python
```python
result = substrate.query(
    'Drop3', 'RewardPools', ['u64']
)
```

#### Return value
```python
{
    'approved': 'bool',
    'create_at': 'u32',
    'end_at': 'u32',
    'id': 'u64',
    'name': 'Bytes',
    'owner': 'AccountId',
    'remain': 'u128',
    'start_at': 'u32',
    'started': 'bool',
    'total': 'u128',
}
```
---------
## Constants

---------
### MaximumNameLength
 The maximum length a on-chain string can be
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('Drop3', 'MaximumNameLength')
```
---------
### SlashPercent
 percent of the total amount slashed when proposal gets rejected
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Drop3', 'SlashPercent')
```
---------
## Errors

---------
### InsufficientRemain
Error when the remaning of a reward pool is not enough

---------
### InsufficientReservedBalance
Error when the sender doesn&\#x27;t have enough reserved balance

---------
### InvalidProposedBlock
Error when start_at &lt; end_at when proposing reward pool

---------
### InvalidTotalBalance
Error when `total` amount is 0 when proposing reward pool

---------
### NoSuchRewardPool
Error when a reward pool can&\#x27;t be found

---------
### NoVacantPoolId
Error when no vacant PoolId can be acquired

---------
### RequireAdmin
Error when the caller account is not the admin

---------
### RequireAdminOrRewardPoolOwner
Error when the caller account is not the reward pool owner or admin

---------
### RequireRewardPoolOwner
Error when the caller account is not the reward pool owner

---------
### RewardPoolAlreadyApproved
Error when the reward pool is first approved then rejected

---------
### RewardPoolRanTooEarly
Error when the reward pool is runing before `start_at`

---------
### RewardPoolRanTooLate
Error when the reward pool is runing after `end_at`

---------
### RewardPoolStopped
Error when the reward pool is stopped

---------
### RewardPoolUnapproved
Error when the reward pool is unapproved

---------
### UnexpectedUnMovedAmount
Error of unexpected unmoved amount when calling repatriate_reserved

---------
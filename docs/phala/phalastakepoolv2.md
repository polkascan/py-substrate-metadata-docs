
# PhalaStakePoolv2

---------
## Calls

---------
### add_worker
Adds a worker to a pool

This will bind a worker to the corresponding pool sub-account. The binding will not be
released until the worker is removed gracefully by `remove_worker()`, or a force unbind
by the worker operator via `Computation::unbind()`.

Requires:
1. The worker is registered and benchmarked
2. The worker is not bound a pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| pubkey | `WorkerPublicKey` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'add_worker', {'pid': 'u64', 'pubkey': '[u8; 32]'}
)
```

---------
### backfill_add_missing_reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| input | `Vec<(T::AccountId, u64, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'backfill_add_missing_reward', {
    'input': [
        ('AccountId', 'u64', 'u128'),
    ],
}
)
```

---------
### check_and_maybe_force_withdraw
Let any user to launch a stakepool withdraw. Then check if the pool need to be forced shutdown.

If the shutdown condition is met, all workers in the pool will be forced shutdown.
Note: This function doesn&\#x27;t guarantee no-op when there&\#x27;s error.
TODO(mingxuan): add more detail comment later.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'check_and_maybe_force_withdraw', {'pid': 'u64'}
)
```

---------
### claim_legacy_rewards
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| target | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'claim_legacy_rewards', {'pid': 'u64', 'target': 'AccountId'}
)
```

---------
### claim_owner_rewards
Claims pool-owner&\#x27;s pending rewards of the sender and send to the `target`

The rewards associate to sender&\#x27;s &quot;staker role&quot; will not be claimed

Requires:
1. The sender is a pool owner
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| target | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'claim_owner_rewards', {'pid': 'u64', 'target': 'AccountId'}
)
```

---------
### contribute
Contributes some stake to a stakepool

Requires:
1. The pool exists
2. After the deposit, the pool doesn&\#x27;t reach the cap
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| amount | `BalanceOf<T>` | 
| as_vault | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'contribute', {
    'amount': 'u128',
    'as_vault': (None, 'u64'),
    'pid': 'u64',
}
)
```

---------
### create
Creates a new stake pool
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'create', {}
)
```

---------
### fix_missing_worker_lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_iterations | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'fix_missing_worker_lock', {'max_iterations': 'u32'}
)
```

---------
### reclaim_pool_worker
Reclaims the releasing stake of a worker in a pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| worker | `WorkerPublicKey` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'reclaim_pool_worker', {'pid': 'u64', 'worker': '[u8; 32]'}
)
```

---------
### remove_worker
Removes a worker from a pool

Requires:
1. The worker is registered
2. The worker is associated with a pool
3. The worker is removable (not in computing)
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| worker | `WorkerPublicKey` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'remove_worker', {'pid': 'u64', 'worker': '[u8; 32]'}
)
```

---------
### reset_iter_pos
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'reset_iter_pos', {}
)
```

---------
### restart_computing
Restarts the worker with a higher stake
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| worker | `WorkerPublicKey` | 
| stake | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'restart_computing', {
    'pid': 'u64',
    'stake': 'u128',
    'worker': '[u8; 32]',
}
)
```

---------
### set_cap
Sets the hard cap of the pool

Note: a smaller cap than current total_value if not allowed.
Requires:
1. The sender is the owner
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| cap | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'set_cap', {'cap': 'u128', 'pid': 'u64'}
)
```

---------
### set_payout_pref
Changes the pool commission rate

Requires:
1. The sender is the owner
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| payout_commission | `Option<Permill>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'set_payout_pref', {
    'payout_commission': (None, 'u32'),
    'pid': 'u64',
}
)
```

---------
### start_computing
Starts a worker on behalf of the stake pool

Requires:
1. The worker is bound to the pool and is in Ready state
2. The remaining stake in the pool can cover the minimal stake required
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| worker | `WorkerPublicKey` | 
| stake | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'start_computing', {
    'pid': 'u64',
    'stake': 'u128',
    'worker': '[u8; 32]',
}
)
```

---------
### stop_computing
Stops a worker on behalf of the stake pool
Note: this would let worker enter CoolingDown if everything is good

Requires:
1. There worker is bound to the pool and is in a stoppable state
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| worker | `WorkerPublicKey` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'stop_computing', {'pid': 'u64', 'worker': '[u8; 32]'}
)
```

---------
### withdraw
Demands the return of some stake from a pool.

Note: there are two scenarios people may meet

Once a withdraw request is proceeded successfully, The withdrawal would be queued and waiting to be dealed.
Afer the withdrawal is queued, The withdraw queue will be automaticly consumed util there are not enough free stakes to fullfill withdrawals.
Everytime the free stakes in the pools increases (except for rewards distributing), the withdraw queue will be consumed as it describes above.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| shares | `BalanceOf<T>` | 
| as_vault | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaStakePoolv2', 'withdraw', {
    'as_vault': (None, 'u64'),
    'pid': 'u64',
    'shares': 'u128',
}
)
```

---------
## Events

---------
### Contribution
Someone contributed to a pool

Affected states:
- the stake related fields in [`Pools`]
- the user W-PHA balance reduced
- the user recive ad share NFT once contribution succeeded
- when there was any request in the withdraw queue, the action may trigger withdrawals
  ([`Withdrawal`](\#variant.Withdrawal) event)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| user | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| shares | `BalanceOf<T>` | ```u128```
| as_vault | `Option<u64>` | ```(None, 'u64')```

---------
### OwnerRewardsWithdrawn
Owner rewards were withdrawn by pool owner

Affected states:
- the stake related fields in [`Pools`]
- the owner asset account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| user | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### PoolCapacitySet
The stake capacity of the pool is updated

Affected states:
- the `cap` field in [`Pools`] is updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| cap | `BalanceOf<T>` | ```u128```

---------
### PoolCommissionSet
The commission of a pool is updated

The commission ratio is represented by an integer. The real value is
`commission / 1_000_000u32`.

Affected states:
- the `payout_commission` field in [`Pools`] is updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| commission | `u32` | ```u32```

---------
### PoolCreated
A stake pool is created by `owner`

Affected states:
- a new entry in [`Pools`] with the pid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| pid | `u64` | ```u64```
| cid | `CollectionId` | ```u32```
| pool_account_id | `T::AccountId` | ```AccountId```

---------
### PoolSlashed
The pool received a slash event from one of its workers (currently disabled)

The slash is accured to the pending slash accumulator.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| amount | `BalanceOf<T>` | ```u128```

---------
### PoolWorkerAdded
A worker is added to the pool

Affected states:
- the `worker` is added to the vector `workers` in [`Pools`]
- the worker in the [`WorkerAssignments`] is pointed to `pid`
- the worker-session binding is updated in `computation` pallet ([`WorkerBindings`](computation::pallet::WorkerBindings),
  [`SessionBindings`](computation::pallet::SessionBindings))
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| worker | `WorkerPublicKey` | ```[u8; 32]```
| session | `T::AccountId` | ```AccountId```

---------
### PoolWorkerRemoved
A worker is removed from a pool.

Affected states:
- the worker item in [`WorkerAssignments`] is removed
- the worker is removed from the [`Pools`] item
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| worker | `WorkerPublicKey` | ```[u8; 32]```

---------
### RewardDismissedDust
Some reward is dismissed because the amount is too tiny (dust)

There&\#x27;s no affected state.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardDismissedNoShare
Some reward is dismissed because the pool doesn&\#x27;t have any share

There&\#x27;s no affected state.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardDismissedNotInPool
Some reward is dismissed because the worker is no longer bound to a pool

There&\#x27;s no affected state.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| worker | `WorkerPublicKey` | ```[u8; 32]```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardReceived
The amount of reward that distributed to owner and stakers
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| to_owner | `BalanceOf<T>` | ```u128```
| to_stakers | `BalanceOf<T>` | ```u128```

---------
### SlashSettled
Some slash is actually settled to a contributor (currently disabled)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| user | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### WorkerReclaimed
A worker is reclaimed from the pool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| worker | `WorkerPublicKey` | ```[u8; 32]```

---------
### WorkingStarted
The amount of stakes for a worker to start computing
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| worker | `WorkerPublicKey` | ```[u8; 32]```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### LegacyRewards

#### Python
```python
result = substrate.query(
    'PhalaStakePoolv2', 'LegacyRewards', [('AccountId', 'u64')]
)
```

#### Return value
```python
'u128'
```
---------
### StakepoolIterateStartPos

#### Python
```python
result = substrate.query(
    'PhalaStakePoolv2', 'StakepoolIterateStartPos', []
)
```

#### Return value
```python
(None, 'u64')
```
---------
### SubAccountAssignments
 (Deprecated)

#### Python
```python
result = substrate.query(
    'PhalaStakePoolv2', 'SubAccountAssignments', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### SubAccountPreimages
 Helper storage to track the preimage of the computing sub-accounts. Not used in consensus.

#### Python
```python
result = substrate.query(
    'PhalaStakePoolv2', 'SubAccountPreimages', ['AccountId']
)
```

#### Return value
```python
('u64', '[u8; 32]')
```
---------
### WorkerAssignments
 Mapping from workers to the pool they belong to

 The map entry lasts from `add_worker()` to `remove_worker()` or force unbinding.

#### Python
```python
result = substrate.query(
    'PhalaStakePoolv2', 'WorkerAssignments', ['[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### GracePeriod
 The grace period for force withdraw request, in seconds.
#### Value
```python
604800
```
#### Python
```python
constant = substrate.get_constant('PhalaStakePoolv2', 'GracePeriod')
```
---------
### MaxPoolWorkers
 The max allowed workers in a pool
#### Value
```python
200
```
#### Python
```python
constant = substrate.get_constant('PhalaStakePoolv2', 'MaxPoolWorkers')
```
---------
### MinContribution
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('PhalaStakePoolv2', 'MinContribution')
```
---------
## Errors

---------
### BenchmarkMissing
The worker doesn&\#x27;t have a valid benchmark when adding to the pool

---------
### CannotRestartWithLessStake
Restarted with a less stake is not allowed in the tokenomic.

---------
### FailedToBindSessionAndWorker
Couldn&\#x27;t bind worker and the pool computing subaccount

---------
### FeatureNotEnabled
The StakePool is not enabled yet.

---------
### InadequateCapacity
The stake capacity is set too low to cover the existing stake

---------
### InsufficientBalance
Trying to contribute more than the available balance

---------
### InsufficientContribution
The contributed stake is smaller than the minimum threshold

---------
### InsufficientFreeStake
Cannot start computing because there&\#x27;s no enough free stake

---------
### InternalSubsidyPoolCannotWithdraw
Internal error: Cannot withdraw from the subsidy pool. This should never happen.

---------
### InvalidForceRewardAmount
Invalid amount of balance input when force reward.

---------
### InvalidWithdrawalAmount
The withdrawal amount is too small (considered as dust)

---------
### LockAccountStakeError

---------
### MissingCollectionId
Stakepool&\#x27;s collection_id isn&\#x27;t founded

---------
### NoLegacyRewardToClaim

---------
### NoNftToWithdraw
The caller has no nft to withdraw

---------
### NoRewardToClaim
There&\#x27;s no pending reward to claim

---------
### PoolBankrupt
The pool has already got all the stake completely slashed.

In this case, no more funds can be contributed to the pool until all the pending slash
has been resolved.

---------
### PoolDoesNotExist
The specified pool doesn&\#x27;t exist

---------
### PoolStakeNotFound
The user doesn&\#x27;t have stake in a pool

---------
### SessionDoesNotExist
The target miner is not in the 	`miner` storage

---------
### StakeExceedsCapacity
The stake added to a pool exceeds its capacity

---------
### UnauthorizedOperator
The owner of the pool doesn&\#x27;t have the access to the worker

The access to a worker is granted by it&\#x27;s `operator` parameter set by `register_worker`

---------
### UnauthorizedPoolOwner
The caller is not the owner of the pool

---------
### VaultIsLocked
Vault is forced locked for it has some expired withdrawal

---------
### WithdrawQueueNotEmpty
Withdraw queue is not empty so that we can&\#x27;t restart computing

---------
### WorkerAlreadyStopped
The worker is already in cd_workers

---------
### WorkerDoesNotExist
The target worker is not in the pool

---------
### WorkerExists
The worker is already added to the pool

---------
### WorkerInAnotherPool
The worker is already added to another pool

---------
### WorkerIsNotReady
The target worker is not reclaimed and can not be removed from a pool.

---------
### WorkerNotRegistered
The worker is not registered in the registry when adding to the pool

---------
### WorkersExceedLimit
Failed to add a worker because the number of the workers exceeds the upper limit.

---------
### _PoolIsBusy

---------
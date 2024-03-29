
# NominationPools

---------
## Calls

---------
### adjust_pool_deposit
See [`Pallet::adjust_pool_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'adjust_pool_deposit', {'pool_id': 'u32'}
)
```

---------
### bond_extra
See [`Pallet::bond_extra`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| extra | `BondExtra<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'bond_extra', {
    'extra': {
        'FreeBalance': 'u128',
        'Rewards': None,
    },
}
)
```

---------
### bond_extra_other
See [`Pallet::bond_extra_other`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| member | `AccountIdLookupOf<T>` | 
| extra | `BondExtra<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'bond_extra_other', {
    'extra': {
        'FreeBalance': 'u128',
        'Rewards': None,
    },
    'member': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### chill
See [`Pallet::chill`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'chill', {'pool_id': 'u32'}
)
```

---------
### claim_commission
See [`Pallet::claim_commission`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'claim_commission', {'pool_id': 'u32'}
)
```

---------
### claim_payout
See [`Pallet::claim_payout`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'claim_payout', {}
)
```

---------
### claim_payout_other
See [`Pallet::claim_payout_other`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| other | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'claim_payout_other', {'other': 'AccountId'}
)
```

---------
### create
See [`Pallet::create`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| root | `AccountIdLookupOf<T>` | 
| nominator | `AccountIdLookupOf<T>` | 
| bouncer | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'create', {
    'amount': 'u128',
    'bouncer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'nominator': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'root': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### create_with_pool_id
See [`Pallet::create_with_pool_id`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| root | `AccountIdLookupOf<T>` | 
| nominator | `AccountIdLookupOf<T>` | 
| bouncer | `AccountIdLookupOf<T>` | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'create_with_pool_id', {
    'amount': 'u128',
    'bouncer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'nominator': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'pool_id': 'u32',
    'root': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### join
See [`Pallet::join`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'join', {'amount': 'u128', 'pool_id': 'u32'}
)
```

---------
### nominate
See [`Pallet::nominate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| validators | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'nominate', {
    'pool_id': 'u32',
    'validators': ['AccountId'],
}
)
```

---------
### pool_withdraw_unbonded
See [`Pallet::pool_withdraw_unbonded`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| num_slashing_spans | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'pool_withdraw_unbonded', {
    'num_slashing_spans': 'u32',
    'pool_id': 'u32',
}
)
```

---------
### set_claim_permission
See [`Pallet::set_claim_permission`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| permission | `ClaimPermission` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'set_claim_permission', {
    'permission': (
        'Permissioned',
        'PermissionlessCompound',
        'PermissionlessWithdraw',
        'PermissionlessAll',
    ),
}
)
```

---------
### set_commission
See [`Pallet::set_commission`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| new_commission | `Option<(Perbill, T::AccountId)>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'set_commission', {
    'new_commission': (
        None,
        ('u32', 'AccountId'),
    ),
    'pool_id': 'u32',
}
)
```

---------
### set_commission_change_rate
See [`Pallet::set_commission_change_rate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| change_rate | `CommissionChangeRate<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'set_commission_change_rate', {
    'change_rate': {
        'max_increase': 'u32',
        'min_delay': 'u32',
    },
    'pool_id': 'u32',
}
)
```

---------
### set_commission_max
See [`Pallet::set_commission_max`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| max_commission | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'set_commission_max', {
    'max_commission': 'u32',
    'pool_id': 'u32',
}
)
```

---------
### set_configs
See [`Pallet::set_configs`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_join_bond | `ConfigOp<BalanceOf<T>>` | 
| min_create_bond | `ConfigOp<BalanceOf<T>>` | 
| max_pools | `ConfigOp<u32>` | 
| max_members | `ConfigOp<u32>` | 
| max_members_per_pool | `ConfigOp<u32>` | 
| global_max_commission | `ConfigOp<Perbill>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'set_configs', {
    'global_max_commission': {
        'Noop': None,
        'Remove': None,
        'Set': 'u32',
    },
    'max_members': {
        'Noop': None,
        'Remove': None,
        'Set': 'u32',
    },
    'max_members_per_pool': {
        'Noop': None,
        'Remove': None,
        'Set': 'u32',
    },
    'max_pools': {
        'Noop': None,
        'Remove': None,
        'Set': 'u32',
    },
    'min_create_bond': {
        'Noop': None,
        'Remove': None,
        'Set': 'u128',
    },
    'min_join_bond': {
        'Noop': None,
        'Remove': None,
        'Set': 'u128',
    },
}
)
```

---------
### set_metadata
See [`Pallet::set_metadata`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| metadata | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'set_metadata', {
    'metadata': 'Bytes',
    'pool_id': 'u32',
}
)
```

---------
### set_state
See [`Pallet::set_state`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| state | `PoolState` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'set_state', {
    'pool_id': 'u32',
    'state': (
        'Open',
        'Blocked',
        'Destroying',
    ),
}
)
```

---------
### unbond
See [`Pallet::unbond`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_account | `AccountIdLookupOf<T>` | 
| unbonding_points | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'unbond', {
    'member_account': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'unbonding_points': 'u128',
}
)
```

---------
### update_roles
See [`Pallet::update_roles`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| new_root | `ConfigOp<T::AccountId>` | 
| new_nominator | `ConfigOp<T::AccountId>` | 
| new_bouncer | `ConfigOp<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'update_roles', {
    'new_bouncer': {
        'Noop': None,
        'Remove': None,
        'Set': 'AccountId',
    },
    'new_nominator': {
        'Noop': None,
        'Remove': None,
        'Set': 'AccountId',
    },
    'new_root': {
        'Noop': None,
        'Remove': None,
        'Set': 'AccountId',
    },
    'pool_id': 'u32',
}
)
```

---------
### withdraw_unbonded
See [`Pallet::withdraw_unbonded`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| member_account | `AccountIdLookupOf<T>` | 
| num_slashing_spans | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'NominationPools', 'withdraw_unbonded', {
    'member_account': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'num_slashing_spans': 'u32',
}
)
```

---------
## Events

---------
### Bonded
A member has became bonded in a pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```
| pool_id | `PoolId` | ```u32```
| bonded | `BalanceOf<T>` | ```u128```
| joined | `bool` | ```bool```

---------
### Created
A pool has been created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| depositor | `T::AccountId` | ```AccountId```
| pool_id | `PoolId` | ```u32```

---------
### Destroyed
A pool has been destroyed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```

---------
### MemberRemoved
A member has been removed from a pool.

The removal can be voluntary (withdrawn all unbonded funds) or involuntary (kicked).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| member | `T::AccountId` | ```AccountId```

---------
### MinBalanceDeficitAdjusted
Topped up deficit in frozen ED of the reward pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| amount | `BalanceOf<T>` | ```u128```

---------
### MinBalanceExcessAdjusted
Claimed excess frozen ED of af the reward pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| amount | `BalanceOf<T>` | ```u128```

---------
### PaidOut
A payout has been made to a member.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```
| pool_id | `PoolId` | ```u32```
| payout | `BalanceOf<T>` | ```u128```

---------
### PoolCommissionChangeRateUpdated
A pool&\#x27;s commission `change_rate` has been changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| change_rate | `CommissionChangeRate<BlockNumberFor<T>>` | ```{'max_increase': 'u32', 'min_delay': 'u32'}```

---------
### PoolCommissionClaimed
Pool commission has been claimed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| commission | `BalanceOf<T>` | ```u128```

---------
### PoolCommissionUpdated
A pool&\#x27;s commission setting has been changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| current | `Option<(Perbill, T::AccountId)>` | ```(None, ('u32', 'AccountId'))```

---------
### PoolMaxCommissionUpdated
A pool&\#x27;s maximum commission setting has been changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| max_commission | `Perbill` | ```u32```

---------
### PoolSlashed
The active balance of pool `pool_id` has been slashed to `balance`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| balance | `BalanceOf<T>` | ```u128```

---------
### RolesUpdated
The roles of a pool have been updated to the given new roles. Note that the depositor
can never change.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| root | `Option<T::AccountId>` | ```(None, 'AccountId')```
| bouncer | `Option<T::AccountId>` | ```(None, 'AccountId')```
| nominator | `Option<T::AccountId>` | ```(None, 'AccountId')```

---------
### StateChanged
The state of a pool has changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| new_state | `PoolState` | ```('Open', 'Blocked', 'Destroying')```

---------
### Unbonded
A member has unbonded from their pool.

- `balance` is the corresponding balance of the number of points that has been
  requested to be unbonded (the argument of the `unbond` transaction) from the bonded
  pool.
- `points` is the number of points that are issued as a result of `balance` being
dissolved into the corresponding unbonding pool.
- `era` is the era in which the balance will be unbonded.
In the absence of slashing, these values will match. In the presence of slashing, the
number of points that are issued in the unbonding pool will be less than the amount
requested to be unbonded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```
| pool_id | `PoolId` | ```u32```
| balance | `BalanceOf<T>` | ```u128```
| points | `BalanceOf<T>` | ```u128```
| era | `EraIndex` | ```u32```

---------
### UnbondingPoolSlashed
The unbond pool at `era` of pool `pool_id` has been slashed to `balance`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolId` | ```u32```
| era | `EraIndex` | ```u32```
| balance | `BalanceOf<T>` | ```u128```

---------
### Withdrawn
A member has withdrawn from their pool.

The given number of `points` have been dissolved in return of `balance`.

Similar to `Unbonded` event, in the absence of slashing, the ratio of point to balance
will be 1.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| member | `T::AccountId` | ```AccountId```
| pool_id | `PoolId` | ```u32```
| balance | `BalanceOf<T>` | ```u128```
| points | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### BondedPools
 Storage for bonded pools.

#### Python
```python
result = substrate.query(
    'NominationPools', 'BondedPools', ['u32']
)
```

#### Return value
```python
{
    'commission': {
        'change_rate': (None, {'max_increase': 'u32', 'min_delay': 'u32'}),
        'current': (None, ('u32', 'AccountId')),
        'max': (None, 'u32'),
        'throttle_from': (None, 'u32'),
    },
    'member_counter': 'u32',
    'points': 'u128',
    'roles': {
        'bouncer': (None, 'AccountId'),
        'depositor': 'AccountId',
        'nominator': (None, 'AccountId'),
        'root': (None, 'AccountId'),
    },
    'state': ('Open', 'Blocked', 'Destroying'),
}
```
---------
### ClaimPermissions
 Map from a pool member account to their opted claim permission.

#### Python
```python
result = substrate.query(
    'NominationPools', 'ClaimPermissions', ['AccountId']
)
```

#### Return value
```python
(
    'Permissioned',
    'PermissionlessCompound',
    'PermissionlessWithdraw',
    'PermissionlessAll',
)
```
---------
### CounterForBondedPools
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'NominationPools', 'CounterForBondedPools', []
)
```

#### Return value
```python
'u32'
```
---------
### CounterForMetadata
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'NominationPools', 'CounterForMetadata', []
)
```

#### Return value
```python
'u32'
```
---------
### CounterForPoolMembers
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'NominationPools', 'CounterForPoolMembers', []
)
```

#### Return value
```python
'u32'
```
---------
### CounterForReversePoolIdLookup
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'NominationPools', 'CounterForReversePoolIdLookup', []
)
```

#### Return value
```python
'u32'
```
---------
### CounterForRewardPools
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'NominationPools', 'CounterForRewardPools', []
)
```

#### Return value
```python
'u32'
```
---------
### CounterForSubPoolsStorage
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'NominationPools', 'CounterForSubPoolsStorage', []
)
```

#### Return value
```python
'u32'
```
---------
### GlobalMaxCommission
 The maximum commission that can be charged by a pool. Used on commission payouts to bound
 pool commissions that are &gt; `GlobalMaxCommission`, necessary if a future
 `GlobalMaxCommission` is lower than some current pool commissions.

#### Python
```python
result = substrate.query(
    'NominationPools', 'GlobalMaxCommission', []
)
```

#### Return value
```python
'u32'
```
---------
### LastPoolId
 Ever increasing number of all pools created so far.

#### Python
```python
result = substrate.query(
    'NominationPools', 'LastPoolId', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxPoolMembers
 Maximum number of members that can exist in the system. If `None`, then the count
 members are not bound on a system wide basis.

#### Python
```python
result = substrate.query(
    'NominationPools', 'MaxPoolMembers', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxPoolMembersPerPool
 Maximum number of members that may belong to pool. If `None`, then the count of
 members is not bound on a per pool basis.

#### Python
```python
result = substrate.query(
    'NominationPools', 'MaxPoolMembersPerPool', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxPools
 Maximum number of nomination pools that can exist. If `None`, then an unbounded number of
 pools can exist.

#### Python
```python
result = substrate.query(
    'NominationPools', 'MaxPools', []
)
```

#### Return value
```python
'u32'
```
---------
### Metadata
 Metadata for the pool.

#### Python
```python
result = substrate.query(
    'NominationPools', 'Metadata', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### MinCreateBond
 Minimum bond required to create a pool.

 This is the amount that the depositor must put as their initial stake in the pool, as an
 indication of &quot;skin in the game&quot;.

 This is the value that will always exist in the staking ledger of the pool bonded account
 while all other accounts leave.

#### Python
```python
result = substrate.query(
    'NominationPools', 'MinCreateBond', []
)
```

#### Return value
```python
'u128'
```
---------
### MinJoinBond
 Minimum amount to bond to join a pool.

#### Python
```python
result = substrate.query(
    'NominationPools', 'MinJoinBond', []
)
```

#### Return value
```python
'u128'
```
---------
### PoolMembers
 Active members.

 TWOX-NOTE: SAFE since `AccountId` is a secure hash.

#### Python
```python
result = substrate.query(
    'NominationPools', 'PoolMembers', ['AccountId']
)
```

#### Return value
```python
{
    'last_recorded_reward_counter': 'u128',
    'points': 'u128',
    'pool_id': 'u32',
    'unbonding_eras': 'scale_info::665',
}
```
---------
### ReversePoolIdLookup
 A reverse lookup from the pool&#x27;s account id to its id.

 This is only used for slashing. In all other instances, the pool id is used, and the
 accounts are deterministically derived from it.

#### Python
```python
result = substrate.query(
    'NominationPools', 'ReversePoolIdLookup', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### RewardPools
 Reward pools. This is where there rewards for each pool accumulate. When a members payout is
 claimed, the balance comes out fo the reward pool. Keyed by the bonded pools account.

#### Python
```python
result = substrate.query(
    'NominationPools', 'RewardPools', ['u32']
)
```

#### Return value
```python
{
    'last_recorded_reward_counter': 'u128',
    'last_recorded_total_payouts': 'u128',
    'total_commission_claimed': 'u128',
    'total_commission_pending': 'u128',
    'total_rewards_claimed': 'u128',
}
```
---------
### SubPoolsStorage
 Groups of unbonding pools. Each group of unbonding pools belongs to a
 bonded pool, hence the name sub-pools. Keyed by the bonded pools account.

#### Python
```python
result = substrate.query(
    'NominationPools', 'SubPoolsStorage', ['u32']
)
```

#### Return value
```python
{'no_era': {'balance': 'u128', 'points': 'u128'}, 'with_era': 'scale_info::675'}
```
---------
### TotalValueLocked
 The sum of funds across all pools.

 This might be lower but never higher than the sum of `total_balance` of all [`PoolMembers`]
 because calling `pool_withdraw_unbonded` might decrease the total stake of the pool&#x27;s
 `bonded_account` without adjusting the pallet-internal `UnbondingPool`&#x27;s.

#### Python
```python
result = substrate.query(
    'NominationPools', 'TotalValueLocked', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### MaxPointsToBalance
 The maximum pool points-to-balance ratio that an `open` pool can have.

 This is important in the event slashing takes place and the pool&#x27;s points-to-balance
 ratio becomes disproportional.

 Moreover, this relates to the `RewardCounter` type as well, as the arithmetic operations
 are a function of number of points, and by setting this value to e.g. 10, you ensure
 that the total number of points in the system are at most 10 times the total_issuance of
 the chain, in the absolute worse case.

 For a value of 10, the threshold would be a pool points-to-balance ratio of 10:1.
 Such a scenario would also be the equivalent of the pool being 90% slashed.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('NominationPools', 'MaxPointsToBalance')
```
---------
### PalletId
 The nomination pool&#x27;s pallet id.
#### Value
```python
'0x70792f6e6f706c73'
```
#### Python
```python
constant = substrate.get_constant('NominationPools', 'PalletId')
```
---------
## Errors

---------
### AccountBelongsToOtherPool
An account is already delegating in another pool. An account may only belong to one
pool at a time.

---------
### BondExtraRestricted
Bonding extra is restricted to the exact pending reward amount.

---------
### CanNotChangeState
The pools state cannot be changed.

---------
### CannotWithdrawAny
None of the funds can be withdrawn yet because the bonding duration has not passed.

---------
### CommissionChangeRateNotAllowed
The submitted changes to commission change rate are not allowed.

---------
### CommissionChangeThrottled
Not enough blocks have surpassed since the last commission update.

---------
### CommissionExceedsGlobalMaximum
The supplied commission exceeds global maximum commission.

---------
### CommissionExceedsMaximum
The supplied commission exceeds the max allowed commission.

---------
### Defensive
Some error occurred that should never happen. This should be reported to the
maintainers.

---------
### DoesNotHavePermission
The caller does not have adequate permissions.

---------
### FullyUnbonding
The member is fully unbonded (and thus cannot access the bonded and reward pool
anymore to, for example, collect rewards).

---------
### InvalidPoolId
Pool id provided is not correct/usable.

---------
### MaxCommissionRestricted
The pool&\#x27;s max commission cannot be set higher than the existing value.

---------
### MaxPoolMembers
Too many members in the pool or system.

---------
### MaxPools
The system is maxed out on pools.

---------
### MaxUnbondingLimit
The member cannot unbond further chunks due to reaching the limit.

---------
### MetadataExceedsMaxLen
Metadata exceeds [`Config::MaxMetadataLen`]

---------
### MinimumBondNotMet
The amount does not meet the minimum bond to either join or create a pool.

The depositor can never unbond to a value less than `Pallet::depositor_min_bond`. The
caller does not have nominating permissions for the pool. Members can never unbond to a
value below `MinJoinBond`.

---------
### NoCommissionCurrentSet
No commission current has been set.

---------
### NoPendingCommission
There is no pending commission to claim.

---------
### NotDestroying
A pool must be in [`PoolState::Destroying`] in order for the depositor to unbond or for
other members to be permissionlessly unbonded.

---------
### NotKickerOrDestroying
Either a) the caller cannot make a valid kick or b) the pool is not destroying.

---------
### NotNominator
The caller does not have nominating permissions for the pool.

---------
### NotOpen
The pool is not open to join

---------
### NothingToAdjust
No imbalance in the ED deposit for the pool.

---------
### OverflowRisk
The transaction could not be executed due to overflow risk for the pool.

---------
### PartialUnbondNotAllowedPermissionlessly
Partial unbonding now allowed permissionlessly.

---------
### PoolIdInUse
Pool id currently in use.

---------
### PoolMemberNotFound
An account is not a member.

---------
### PoolNotFound
A (bonded) pool id does not exist.

---------
### RewardPoolNotFound
A reward pool does not exist. In all cases this is a system logic error.

---------
### SubPoolsNotFound
A sub pool does not exist.

---------
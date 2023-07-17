
# NominationPools

---------
## Calls

---------
### bond_extra
Bond `extra` more funds from `origin` into the pool to which they already belong.

Additional funds can come from either the free balance of the account, of from the
accumulated rewards, see [`BondExtra`].

Bonding extra funds implies an automatic payout of all pending rewards as well.
See `bond_extra_other` to bond pending rewards of `other` members.
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
`origin` bonds funds from `extra` for some pool member `member` into their respective
pools.

`origin` can bond extra funds from free balance or pending rewards when `origin ==
other`.

In the case of `origin != other`, `origin` can only bond extra pending rewards of
`other` members assuming set_claim_permission for the given member is
`PermissionlessAll` or `PermissionlessCompound`.
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
Chill on behalf of the pool.

The dispatch origin of this call must be signed by the pool nominator or the pool
root role, same as [`Pallet::nominate`].

This directly forward the call to the staking pallet, on behalf of the pool bonded
account.
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
Claim pending commission.

The dispatch origin of this call must be signed by the `root` role of the pool. Pending
commission is paid out and added to total claimed commission`. Total pending commission
is reset to zero. the current.
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
A bonded member can use this to claim their payout based on the rewards that the pool
has accumulated since their last claimed payout (OR since joining if this is their first
time claiming rewards). The payout will be transferred to the member&\#x27;s account.

The member will earn rewards pro rata based on the members stake vs the sum of the
members in the pools stake. Rewards do not &quot;expire&quot;.

See `claim_payout_other` to caim rewards on bahalf of some `other` pool member.
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
`origin` can claim payouts on some pool member `other`&\#x27;s behalf.

Pool member `other` must have a `PermissionlessAll` or `PermissionlessWithdraw` in order
for this call to be successful.
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
Create a new delegation pool.

\# Arguments

* `amount` - The amount of funds to delegate to the pool. This also acts of a sort of
  deposit since the pools creator cannot fully unbond funds until the pool is being
  destroyed.
* `index` - A disambiguation index for creating the account. Likely only useful when
  creating multiple pools in the same extrinsic.
* `root` - The account to set as [`PoolRoles::root`].
* `nominator` - The account to set as the [`PoolRoles::nominator`].
* `bouncer` - The account to set as the [`PoolRoles::bouncer`].

\# Note

In addition to `amount`, the caller will transfer the existential deposit; so the caller
needs at have at least `amount + existential_deposit` transferrable.
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
Create a new delegation pool with a previously used pool id

\# Arguments

same as `create` with the inclusion of
* `pool_id` - `A valid PoolId.
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
Stake funds with a pool. The amount to bond is transferred from the member to the
pools account and immediately increases the pools bond.

\# Note

* An account can only be a member of a single pool.
* An account cannot join the same pool multiple times.
* This call will *not* dust the member account, so the member must have at least
  `existential deposit + amount` in their account.
* Only a pool with [`PoolState::Open`] can be joined
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
Nominate on behalf of the pool.

The dispatch origin of this call must be signed by the pool nominator or the pool
root role.

This directly forward the call to the staking pallet, on behalf of the pool bonded
account.
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
Call `withdraw_unbonded` for the pools account. This call can be made by any account.

This is useful if their are too many unlocking chunks to call `unbond`, and some
can be cleared by withdrawing. In the case there are too many unlocking chunks, the user
would probably see an error like `NoMoreChunks` emitted from the staking system when
they attempt to unbond.
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
Allows a pool member to set a claim permission to allow or disallow permissionless
bonding and withdrawing.

By default, this is `Permissioned`, which implies only the pool member themselves can
claim their pending rewards. If a pool member wishes so, they can set this to
`PermissionlessAll` to allow any account to claim their rewards and bond extra to the
pool.

\# Arguments

* `origin` - Member of a pool.
* `actor` - Account to claim reward. // improve this
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
Set the commission of a pool.
Both a commission percentage and a commission payee must be provided in the `current`
tuple. Where a `current` of `None` is provided, any current commission will be removed.

- If a `None` is supplied to `new_commission`, existing commission will be removed.
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
Set the commission change rate for a pool.

Initial change rate is not bounded, whereas subsequent updates can only be more
restrictive than the current.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| change_rate | `CommissionChangeRate<T::BlockNumber>` | 

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
Set the maximum commission of a pool.

- Initial max can be set to any `Perbill`, and only smaller values thereafter.
- Current commission will be lowered in the event it is higher than a new max
  commission.
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
Update configurations for the nomination pools. The origin for this call must be
Root.

\# Arguments

* `min_join_bond` - Set [`MinJoinBond`].
* `min_create_bond` - Set [`MinCreateBond`].
* `max_pools` - Set [`MaxPools`].
* `max_members` - Set [`MaxPoolMembers`].
* `max_members_per_pool` - Set [`MaxPoolMembersPerPool`].
* `global_max_commission` - Set [`GlobalMaxCommission`].
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
Set a new metadata for the pool.

The dispatch origin of this call must be signed by the bouncer, or the root role of the
pool.
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
Set a new state for the pool.

If a pool is already in the `Destroying` state, then under no condition can its state
change again.

The dispatch origin of this call must be either:

1. signed by the bouncer, or the root role of the pool,
2. if the pool conditions to be open are NOT met (as described by `ok_to_be_open`), and
   then the state of the pool can be permissionlessly changed to `Destroying`.
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
Unbond up to `unbonding_points` of the `member_account`&\#x27;s funds from the pool. It
implicitly collects the rewards one last time, since not doing so would mean some
rewards would be forfeited.

Under certain conditions, this call can be dispatched permissionlessly (i.e. by any
account).

\# Conditions for a permissionless dispatch.

* The pool is blocked and the caller is either the root or bouncer. This is refereed to
  as a kick.
* The pool is destroying and the member is not the depositor.
* The pool is destroying, the member is the depositor and no other members are in the
  pool.

\#\# Conditions for permissioned dispatch (i.e. the caller is also the
`member_account`):

* The caller is not the depositor.
* The caller is the depositor, the pool is destroying and no other members are in the
  pool.

\# Note

If there are too many unlocking chunks to unbond with the pool account,
[`Call::pool_withdraw_unbonded`] can be called to try and minimize unlocking chunks.
The [`StakingInterface::unbond`] will implicitly call [`Call::pool_withdraw_unbonded`]
to try to free chunks if necessary (ie. if unbound was called and no unlocking chunks
are available). However, it may not be possible to release the current unlocking chunks,
in which case, the result of this call will likely be the `NoMoreChunks` error from the
staking system.
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
Update the roles of the pool.

The root is the only entity that can change any of the roles, including itself,
excluding the depositor, who can never change.

It emits an event, notifying UIs of the role change. This event is quite relevant to
most pool members and they should be informed of changes to pool roles.
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
Withdraw unbonded funds from `member_account`. If no bonded funds can be unbonded, an
error is returned.

Under certain conditions, this call can be dispatched permissionlessly (i.e. by any
account).

\# Conditions for a permissionless dispatch

* The pool is in destroy mode and the target is not the depositor.
* The target is the depositor and they are the only member in the sub pools.
* The pool is blocked and the caller is either the root or bouncer.

\# Conditions for permissioned dispatch

* The caller is the target and they are not the depositor.

\# Note

If the target is the depositor, the pool will be destroyed.
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
| change_rate | `CommissionChangeRate<T::BlockNumber>` | ```{'max_increase': 'u32', 'min_delay': 'u32'}```

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
    'unbonding_eras': 'scale_info::692',
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
{'no_era': {'balance': 'u128', 'points': 'u128'}, 'with_era': 'scale_info::702'}
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

The depositor can never unbond to a value less than
`Pallet::depositor_min_bond`. The caller does not have nominating
permissions for the pool. Members can never unbond to a value below `MinJoinBond`.

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

# PhalaVault

---------
## Calls

---------
### check_and_maybe_force_withdraw
Let any user to launch a vault withdraw. Then check if the vault need to be forced withdraw all its contributions.

If the shutdown condition is met, all shares owned by the vault will be forced withdraw.
Note: This function doesn&\#x27;t guarantee no-op when there&\#x27;s error.
#### Attributes
| Name | Type |
| -------- | -------- | 
| vault_pid | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaVault', 'check_and_maybe_force_withdraw', {'vault_pid': 'u64'}
)
```

---------
### claim_owner_shares
Transfers some owner shares wrapped in a nft to the assigned account

Requires:
1. The sender is the owner
#### Attributes
| Name | Type |
| -------- | -------- | 
| vault_pid | `u64` | 
| target | `T::AccountId` | 
| shares | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaVault', 'claim_owner_shares', {
    'shares': 'u128',
    'target': 'AccountId',
    'vault_pid': 'u64',
}
)
```

---------
### contribute
Contributes some stake to a vault

Requires:
1. The pool exists
2. After the deposit, the pool doesn&\#x27;t reach the cap
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaVault', 'contribute', {'amount': 'u128', 'pid': 'u64'}
)
```

---------
### create
Creates a new vault
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PhalaVault', 'create', {}
)
```

---------
### maybe_gain_owner_shares
Tries to settle owner shares if the vault profits

The mechanism of issuing shares to distribute owner reward is metioned in comments of struct `Vault` in poolproxy.rs

Requires:
1. The sender is the owner
#### Attributes
| Name | Type |
| -------- | -------- | 
| vault_pid | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaVault', 'maybe_gain_owner_shares', {'vault_pid': 'u64'}
)
```

---------
### refresh_vault_lock_and_check
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaVault', 'refresh_vault_lock_and_check', {'pid': 'u64'}
)
```

---------
### set_payout_pref
Changes the vault commission rate

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
    'PhalaVault', 'set_payout_pref', {
    'payout_commission': (None, 'u32'),
    'pid': 'u64',
}
)
```

---------
### withdraw
Demands the return of some stake from a pool.

Once a withdraw request is proceeded successfully, The withdrawal would be queued and waiting to be dealed.
Afer the withdrawal is queued, The withdraw queue will be automaticly consumed util there are not enough free stakes to fullfill withdrawals.
Everytime the free stakes in the pools increases, the withdraw queue will be consumed as it describes above.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| shares | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaVault', 'withdraw', {'pid': 'u64', 'shares': 'u128'}
)
```

---------
## Events

---------
### Contribution
Someone contributed to a vault

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

---------
### ForceShutdown
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| reason | `ForceShutdownReason` | ```('NoEnoughReleasingStake', 'Waiting3xGracePeriod')```

---------
### OwnerSharesClaimed
Owner shares is claimed by pool owner
Affected states:
- the shares related fields in [`Pools`]
- the nft related storages in rmrk and pallet unique
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| user | `T::AccountId` | ```AccountId```
| shares | `BalanceOf<T>` | ```u128```

---------
### OwnerSharesGained
Additional owner shares are mint into the pool

Affected states:
- the shares related fields in [`Pools`]
- last_share_price_checkpoint in [`Pools`]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| shares | `BalanceOf<T>` | ```u128```
| checkout_price | `BalanceOf<T>` | ```u128```

---------
### PoolCreated
A vault is created by `owner`

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
### VaultCommissionSet
The commission of a vault is updated

The commission ratio is represented by an integer. The real value is
`commission / 1_000_000u32`.

Affected states:
- the `commission` field in [`Pools`] is updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| commission | `u32` | ```u32```

---------
## Storage functions

---------
### VaultLocks
 Mapping from the vault pid to its owner authority locking status

 Using to forbid vault&#x27;s owner to trigger an withdraw for the vault and override the withdraw request issued by `force shutdown`.

#### Python
```python
result = substrate.query(
    'PhalaVault', 'VaultLocks', ['u64']
)
```

#### Return value
```python
()
```
---------
## Constants

---------
### InitialPriceCheckPoint
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('PhalaVault', 'InitialPriceCheckPoint')
```
---------
### VaultQueuePeriod
#### Value
```python
1814400
```
#### Python
```python
constant = substrate.get_constant('PhalaVault', 'VaultQueuePeriod')
```
---------
## Errors

---------
### AssetAccountNotExist
The asset account hasn&\#x27;t been created. It indicates an internal error.

---------
### CommissionNotChanged
The commission is not changed

---------
### InsufficientBalance
Trying to contribute more than the available balance

---------
### InsufficientContribution
The contributed stake is smaller than the minimum threshold

---------
### NoEnoughShareToClaim
The withdrawal amount is too small or too large

---------
### NoNftToWithdraw
The caller has no nft to withdraw

---------
### NoRewardToClaim
The vault have no owner shares to claim

---------
### UnauthorizedPoolOwner
The caller is not the owner of the pool

---------
### VaultBankrupt
The Vault was bankrupt; cannot interact with it unless all the shares are withdrawn.

---------
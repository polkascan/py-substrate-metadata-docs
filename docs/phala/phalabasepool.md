
# PhalaBasePool

---------
## Calls

---------
### add_staker_to_whitelist
Adds a staker accountid to contribution whitelist.

Calling this method will forbide stakers contribute who isn&\#x27;t in the whitelist.
The caller must be the owner of the pool.
If a pool hasn&\#x27;t registed in the wihtelist map, any staker could contribute as what they use to do.
The whitelist has a lmit len of 100 stakers.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| staker | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaBasePool', 'add_staker_to_whitelist', {'pid': 'u64', 'staker': 'AccountId'}
)
```

---------
### remove_staker_from_whitelist
Removes a staker accountid to contribution whitelist.

The caller must be the owner of the pool.
If the last staker in the whitelist is removed, the pool will return back to a normal pool that allow anyone to contribute.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| staker | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaBasePool', 'remove_staker_from_whitelist', {'pid': 'u64', 'staker': 'AccountId'}
)
```

---------
### remove_unused_lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_iterations | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaBasePool', 'remove_unused_lock', {'max_iterations': 'u32'}
)
```

---------
### reset_lock_iter_pos
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PhalaBasePool', 'reset_lock_iter_pos', {}
)
```

---------
### set_pool_description
Adds a description to the pool

The caller must be the owner of the pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `u64` | 
| description | `DescStr` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaBasePool', 'set_pool_description', {'description': 'Bytes', 'pid': 'u64'}
)
```

---------
## Events

---------
### NftCreated
A Nft is created to contain pool shares
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| cid | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| shares | `BalanceOf<T>` | ```u128```

---------
### PoolWhitelistCreated
A pool contribution whitelist is added

- lazy operated when the first staker is added to the whitelist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```

---------
### PoolWhitelistDeleted
The pool contribution whitelist is deleted

- lazy operated when the last staker is removed from the whitelist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```

---------
### PoolWhitelistStakerAdded
A staker is added to the pool contribution whitelist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| staker | `T::AccountId` | ```AccountId```

---------
### PoolWhitelistStakerRemoved
A staker is removed from the pool contribution whitelist
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| staker | `T::AccountId` | ```AccountId```

---------
### Withdrawal
Some stake was withdrawn from a pool

The lock in [`Balances`](pallet_balances::pallet::Pallet) is updated to release the
locked stake.

Affected states:
- the stake related fields in [`Pools`]
- the user staking asset account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| user | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| shares | `BalanceOf<T>` | ```u128```

---------
### WithdrawalQueued
A withdrawal request is inserted to a queue

Affected states:
- a new item is inserted to or an old item is being replaced by the new item in the
  withdraw queue in [`Pools`]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pid | `u64` | ```u64```
| user | `T::AccountId` | ```AccountId```
| shares | `BalanceOf<T>` | ```u128```
| nft_id | `NftId` | ```u32```
| as_vault | `Option<u64>` | ```(None, 'u64')```

---------
## Storage functions

---------
### CollectionIndex
 The Next available collectionid to be created

#### Python
```python
result = substrate.query(
    'PhalaBasePool', 'CollectionIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### LockIterateStartPos

#### Python
```python
result = substrate.query(
    'PhalaBasePool', 'LockIterateStartPos', []
)
```

#### Return value
```python
(None, ('u32', 'u32'))
```
---------
### NextNftId
 Mapping from the next self-increased nft ids to collections

#### Python
```python
result = substrate.query(
    'PhalaBasePool', 'NextNftId', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### NftLocks
 Mapping from the NftId to its internal locking status

 Used to ensure nft attributes can&#x27;t be read and override when it has already be accessed and haven&#x27;t updated yet.

#### Python
```python
result = substrate.query(
    'PhalaBasePool', 'NftLocks', [('u32', 'u32')]
)
```

#### Return value
```python
()
```
---------
### PoolCollections
 Mapping from collectionids to pids

#### Python
```python
result = substrate.query(
    'PhalaBasePool', 'PoolCollections', ['u32']
)
```

#### Return value
```python
'u64'
```
---------
### PoolContributionWhitelists
 Mapping for pools that specify certain stakers to contribute stakes

#### Python
```python
result = substrate.query(
    'PhalaBasePool', 'PoolContributionWhitelists', ['u64']
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
    'PhalaBasePool', 'PoolCount', []
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
    'PhalaBasePool', 'PoolDescriptions', ['u64']
)
```

#### Return value
```python
'Bytes'
```
---------
### Pools
 Mapping from pids to pools (including stake pools and vaults)

#### Python
```python
result = substrate.query(
    'PhalaBasePool', 'Pools', ['u64']
)
```

#### Return value
```python
{
    'StakePool': {
        'basepool': {
            'cid': 'u32',
            'owner': 'AccountId',
            'pid': 'u64',
            'pool_account_id': 'AccountId',
            'total_shares': 'u128',
            'total_value': 'u128',
            'value_subscribers': ['u64'],
            'withdraw_queue': [
                {'nft_id': 'u32', 'start_time': 'u64', 'user': 'AccountId'},
            ],
        },
        'cap': (None, 'u128'),
        'cd_workers': ['[u8; 32]'],
        'lock_account': 'AccountId',
        'owner_reward_account': 'AccountId',
        'payout_commission': (None, 'u32'),
        'workers': ['[u8; 32]'],
    },
    'Vault': {
        'basepool': {
            'cid': 'u32',
            'owner': 'AccountId',
            'pid': 'u64',
            'pool_account_id': 'AccountId',
            'total_shares': 'u128',
            'total_value': 'u128',
            'value_subscribers': ['u64'],
            'withdraw_queue': [
                {'nft_id': 'u32', 'start_time': 'u64', 'user': 'AccountId'},
            ],
        },
        'commission': (None, 'u32'),
        'invest_pools': ['u64'],
        'last_share_price_checkpoint': 'u128',
        'owner_shares': 'u128',
    },
}
```
---------
## Errors

---------
### AlreadyInContributeWhitelist
Can not add the staker to whitelist because the staker is already in whitelist.

---------
### AttrLocked
Tried to get a `NftGuard` when the nft is locked. It indicates an internal error occured.

---------
### BurnNftFailed
Burn nft failed

---------
### ExceedMaxDescriptionLen
Too long for pool description length

---------
### ExceedWhitelistMaxLen
Too many stakers in contribution whitelist that exceed the limit

---------
### InvalidSharePrice
Occurs when pool&\#x27;s shares is zero

---------
### InvalidShareToWithdraw
CheckSub less than zero, indicate share amount is invalid

---------
### InvalidWithdrawalAmount
The withdrawal amount is too small (considered as dust)

---------
### MissCollectionId
basepool&\#x27;s collection_id isn&\#x27;t founded

---------
### NftIdNotFound
NftId does not match any nft

---------
### NoWhitelistCreated
The pool hasn&\#x27;t have a whitelist created

---------
### NotInContributeWhitelist
Invalid staker to contribute because origin isn&\#x27;t in Pool&\#x27;s contribution whitelist.

---------
### NotMigrationRoot
Migration root not authorized

---------
### PoolBankrupt
The pool has already got all the stake completely slashed.

In this case, no more funds can be contributed to the pool until all the pending slash
has been resolved.

---------
### PoolDoesNotExist
The Specified pid does not match to any pool

---------
### PoolTypeNotMatch
Tried to access a pool type that doesn&\#x27;t match the actual pool type in the storage.

E.g. Try to access a vault but it&\#x27;s actually a  stake pool.

---------
### RmrkError
RMRK errors

---------
### TransferSharesAmountInvalid

---------
### UnauthorizedPoolOwner
The caller is not the owner of the pool

---------
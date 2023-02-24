
# Metaverse

---------
## Calls

---------
### create_metaverse
Create a metaverse.

The dispatch origin for this call must be _Signed_.
- `metadata&\#x27;: the metadata of the new metaverse

Emits `NewMetaverseCreated` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| metadata | `MetaverseMetadata` | 

#### Python
```python
call = substrate.compose_call(
    'Metaverse', 'create_metaverse', {'metadata': 'Bytes'}
)
```

---------
### destroy_metaverse
Destroy a frozen meataverse.

The dispatch origin for this call must be _Signed_.
Only metaverse owner can perform this call
- `metaverse_id`: the metaverse ID which will be destroyed

Emits `MetaverseDestroyed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| metaverse_id | `MetaverseId` | 

#### Python
```python
call = substrate.compose_call(
    'Metaverse', 'destroy_metaverse', {'metaverse_id': 'u64'}
)
```

---------
### freeze_metaverse
Freeze an existing meataverse.

The dispatch origin for this call must be _Signed_.
Only metaverse council can perform this call.
- `metaverse_id`: the metaverse ID which will be freezed

Emits `MetaverseFreezed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| metaverse_id | `MetaverseId` | 

#### Python
```python
call = substrate.compose_call(
    'Metaverse', 'freeze_metaverse', {'metaverse_id': 'u64'}
)
```

---------
### transfer_metaverse
Transfer a metaverse.

The dispatch origin for this call must be _Signed_.
Only metaverse owner can perform this call.
- &\#x27;to&\#x27;: the account which will receive the transferred metaverse
- `metaverse_id&\#x27;: the metaverse ID which will be transferred

Emits `TransferredMetaverse` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| metaverse_id | `MetaverseId` | 

#### Python
```python
call = substrate.compose_call(
    'Metaverse', 'transfer_metaverse', {
    'metaverse_id': 'u64',
    'to': 'AccountId',
}
)
```

---------
### unfreeze_metaverse
Unfreeze existing frozen meataverse.

The dispatch origin for this call must be _Signed_.
Only metaverse council can perform this call.
- `metaverse_id`: the metaverse ID which will be unfreezed

Emits `MetaverseUnfreezed` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| metaverse_id | `MetaverseId` | 

#### Python
```python
call = substrate.compose_call(
    'Metaverse', 'unfreeze_metaverse', {'metaverse_id': 'u64'}
)
```

---------
### update_metaverse_listing_fee
Updates the meatverse&\#x27;s local marketplace listing fee

The dispatch origin for this call must be _Signed_.
Only metaverse owner can withdraw funds.
- `metaverse_id`: the meatverse ID which fees will be updated
- &\#x27;new_listng_fee&\#x27;: the updated metaverse&\#x27;s local marketplace listing fee

Emits `MetaverseListingFeeUpdated` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| metaverse_id | `MetaverseId` | 
| new_listing_fee | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'Metaverse', 'update_metaverse_listing_fee', {
    'metaverse_id': 'u64',
    'new_listing_fee': 'u32',
}
)
```

---------
### withdraw_from_metaverse_fund
Withdraws funds from metaverse treasury fund

The dispatch origin for this call must be _Signed_.
Only metaverse owner can withdraw funds.
- `metaverse_id`: the meatverse ID of the local treasury which funds will be withdrawn

Emits `MetaverseTreasuryFundsWithdrawn` if successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| metaverse_id | `MetaverseId` | 

#### Python
```python
call = substrate.compose_call(
    'Metaverse', 'withdraw_from_metaverse_fund', {'metaverse_id': 'u64'}
)
```

---------
## Events

---------
### MetaverseDestroyed
Successfully destroyed a metaverse
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```

---------
### MetaverseFreezed
Successfully frozen a metaverse
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```

---------
### MetaverseListingFeeUpdated
Successfully updated the local marketplace listing fee for a metaverse
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```
| None | `Perbill` | ```u32```

---------
### MetaverseMintedNewCurrency
Successfully minted new metaverse currency
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```
| None | `FungibleTokenId` | ```{'NativeToken': 'u64', 'FungibleToken': 'u64', 'DEXShare': ('u64', 'u64'), 'MiningResource': 'u64', 'Stable': 'u64'}```

---------
### MetaverseStaked
Successfully staked funds to a metaverse
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `MetaverseId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### MetaverseStakingRewarded
Successfully payed rewards for a metaverse staking round
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `MetaverseId` | ```u64```
| None | `RoundIndex` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### MetaverseTreasuryFundsWithdrawn
Successfully withdrawn funds from a metaverse treasury fund
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```

---------
### MetaverseUnfreezed
Successfully unfreezed a metaverse
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```

---------
### MetaverseUnstaked
Successfully unstaked funds from a metaverse
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `MetaverseId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### NewMetaverseCreated
Successfully created a metaverse
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
### NewMetaverseRegisteredForStaking
Successfully registerred a metaverse for staking
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```
| None | `T::AccountId` | ```AccountId```

---------
### TransferredMetaverse
Successfully transferred a metaverse
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `MetaverseId` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### AllMetaversesCount
 Track the total amount of metaverses.

#### Python
```python
result = substrate.query(
    'Metaverse', 'AllMetaversesCount', []
)
```

#### Return value
```python
'u64'
```
---------
### FreezedMetaverses
 Stores frozen metaverses.

#### Python
```python
result = substrate.query(
    'Metaverse', 'FreezedMetaverses', ['u64']
)
```

#### Return value
```python
()
```
---------
### MetaverseOwner
 Stores metaverses owned by each account.

#### Python
```python
result = substrate.query(
    'Metaverse', 'MetaverseOwner', ['AccountId', 'u64']
)
```

#### Return value
```python
()
```
---------
### MetaverseRoundStake
 Stores amount staked and stakers for individual metaverse per staking round.

#### Python
```python
result = substrate.query(
    'Metaverse', 'MetaverseRoundStake', ['u64', 'u32']
)
```

#### Return value
```python
{'claimed_rewards': 'u128', 'stakers': 'scale_info::409', 'total': 'u128'}
```
---------
### MetaverseStakingSnapshots
 Stores metaverse staking snapshot for a staking round.

#### Python
```python
result = substrate.query(
    'Metaverse', 'MetaverseStakingSnapshots', ['u32']
)
```

#### Return value
```python
{'rewards': 'u128', 'staked': 'u128'}
```
---------
### Metaverses
 Stores metaverses&#x27; informaion.

#### Python
```python
result = substrate.query(
    'Metaverse', 'Metaverses', ['u64']
)
```

#### Return value
```python
{
    'currency_id': {
        'DEXShare': ('u64', 'u64'),
        'FungibleToken': 'u64',
        'MiningResource': 'u64',
        'NativeToken': 'u64',
        'Stable': 'u64',
    },
    'estate_class_id': 'u32',
    'is_frozen': 'bool',
    'land_class_id': 'u32',
    'listing_fee': 'u32',
    'metadata': 'Bytes',
    'owner': 'AccountId',
}
```
---------
### NextMetaverseId
 Track the next metaverse ID.

#### Python
```python
result = substrate.query(
    'Metaverse', 'NextMetaverseId', []
)
```

#### Return value
```python
'u64'
```
---------
### RegisteredMetaverse
 Stores metaverses registered for staking.

#### Python
```python
result = substrate.query(
    'Metaverse', 'RegisteredMetaverse', ['u64']
)
```

#### Return value
```python
'AccountId'
```
---------
### Round
 Metaverse staking related storage
 Tracks current staking round index and next round scheduled transition.

#### Python
```python
result = substrate.query(
    'Metaverse', 'Round', []
)
```

#### Return value
```python
{'current': 'u32', 'first': 'u32', 'length': 'u32'}
```
---------
### StakingInfo
 Stores staking info of individual stakers.

#### Python
```python
result = substrate.query(
    'Metaverse', 'StakingInfo', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### MaxMetaverseMetadata
 The  maximum metaverse metadata size
#### Value
```python
1024
```
#### Python
```python
constant = substrate.get_constant('Metaverse', 'MaxMetaverseMetadata')
```
---------
### MetaverseTreasury
 The metaverse treasury pallet
#### Value
```python
'0x6269742f6d657461'
```
#### Python
```python
constant = substrate.get_constant('Metaverse', 'MetaverseTreasury')
```
---------
### MinContribution
 Minimum contribution
#### Value
```python
50000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Metaverse', 'MinContribution')
```
---------
## Errors

---------
### AlreadyRegisteredForStaking
Already registered for staking

---------
### FungibleTokenAlreadyIssued
Fungible token already issued

---------
### InsufficientBalanceToUnstake
Exceed staked amount

---------
### InsufficientContribution
Contribution is insufficient

---------
### MaxMetadataExceeded
Max metadata exceed

---------
### MaximumAmountOfStakersPerMetaverse
Maximum amount of allowed stakers per metaverse

---------
### MetaverseHasNoStake
Metaverse has no stake

---------
### MetaverseIdNotFound
Metaverse Id not found

---------
### MetaverseInfoNotFound
Metaverse info not found

---------
### MetaverseListingFeeExceedThreshold
Listing fee exceed threshold

---------
### MetaverseStakingAlreadyPaid
Reward has been paid

---------
### MetaverseStakingInfoNotFound
Metaverse Staking Info not found

---------
### MinimumStakingAmountRequired
Minimum staking balance is not met

---------
### NoAvailableMetaverseId
No available Metaverse id

---------
### NoPermission
No permission

---------
### NotEnoughBalanceToStake
Not enough balance to stake

---------
### NotRegisteredForStaking
Metaverse is not registered for staking

---------
### OnlyFrozenMetaverseCanBeDestroyed
Only frozen metaverse can be destroy

---------
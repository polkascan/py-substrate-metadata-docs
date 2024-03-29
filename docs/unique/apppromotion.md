
# AppPromotion

---------
## Calls

---------
### force_unstake
See [`Pallet::force_unstake`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pending_blocks | `Vec<BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'force_unstake', {'pending_blocks': ['u32']}
)
```

---------
### payout_stakers
See [`Pallet::payout_stakers`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| stakers_number | `Option<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'payout_stakers', {'stakers_number': (None, 'u8')}
)
```

---------
### set_admin_address
See [`Pallet::set_admin_address`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| admin | `T::CrossAccountId` | 

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'set_admin_address', {
    'admin': {
        'Ethereum': '[u8; 20]',
        'Substrate': 'AccountId',
    },
}
)
```

---------
### sponsor_collection
See [`Pallet::sponsor_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'sponsor_collection', {'collection_id': 'u32'}
)
```

---------
### sponsor_contract
See [`Pallet::sponsor_contract`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `H160` | 

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'sponsor_contract', {'contract_id': '[u8; 20]'}
)
```

---------
### stake
See [`Pallet::stake`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'stake', {'amount': 'u128'}
)
```

---------
### stop_sponsoring_collection
See [`Pallet::stop_sponsoring_collection`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'stop_sponsoring_collection', {'collection_id': 'u32'}
)
```

---------
### stop_sponsoring_contract
See [`Pallet::stop_sponsoring_contract`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| contract_id | `H160` | 

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'stop_sponsoring_contract', {'contract_id': '[u8; 20]'}
)
```

---------
### unstake_all
See [`Pallet::unstake_all`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'unstake_all', {}
)
```

---------
### unstake_partial
See [`Pallet::unstake_partial`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AppPromotion', 'unstake_partial', {'amount': 'u128'}
)
```

---------
## Events

---------
### SetAdmin
The admin was set

\# Arguments
* AccountId: account address of the admin
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### Stake
Staking was performed

\# Arguments
* AccountId: account of the staker
* Balance : staking amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### StakingRecalculation
Staking recalculation was performed

\# Arguments
* AccountId: account of the staker.
* Balance : recalculation base
* Balance : total income
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### Unstake
Unstaking was performed

\# Arguments
* AccountId: account of the staker
* Balance : unstaking amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Admin
 Stores the `admin` account. Some extrinsics can only be executed if they were signed by `admin`.

#### Python
```python
result = substrate.query(
    'AppPromotion', 'Admin', []
)
```

#### Return value
```python
'AccountId'
```
---------
### PendingUnstake
 Pending unstake records for an `Account`.

 * **Key** - Staker account.
 * **Value** - Amount of stakes.

#### Python
```python
result = substrate.query(
    'AppPromotion', 'PendingUnstake', ['u32']
)
```

#### Return value
```python
[('AccountId', 'u128')]
```
---------
### PreviousCalculatedRecord
 Stores a key for record for which the revenue recalculation was performed.
 If `None`, then recalculation has not yet been performed or calculations have been completed for all stakers.

#### Python
```python
result = substrate.query(
    'AppPromotion', 'PreviousCalculatedRecord', []
)
```

#### Return value
```python
('AccountId', 'u32')
```
---------
### Staked
 Stores the amount of tokens staked by account in the blocknumber.

 * **Key1** - Staker account.
 * **Key2** - Relay block number when the stake was made.
 * **(Balance, BlockNumber)** - Balance of the stake.
 The number of the relay block in which we must perform the interest recalculation

#### Python
```python
result = substrate.query(
    'AppPromotion', 'Staked', ['AccountId', 'u32']
)
```

#### Return value
```python
('u128', 'u32')
```
---------
### StakesPerAccount
 Stores number of stake records for an `Account`.

 * **Key** - Staker account.
 * **Value** - Amount of stakes.

#### Python
```python
result = substrate.query(
    'AppPromotion', 'StakesPerAccount', ['AccountId']
)
```

#### Return value
```python
'u8'
```
---------
### TotalStaked
 Stores the total staked amount.

#### Python
```python
result = substrate.query(
    'AppPromotion', 'TotalStaked', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### FreezeIdentifier
 Freeze identifier used by the pallet
#### Value
```python
'0x6170707374616b656170707374616b65'
```
#### Python
```python
constant = substrate.get_constant('AppPromotion', 'FreezeIdentifier')
```
---------
### IntervalIncome
 Rate of return for interval in blocks defined in `RecalculationInterval`.
#### Value
```python
453256
```
#### Python
```python
constant = substrate.get_constant('AppPromotion', 'IntervalIncome')
```
---------
### Nominal
 Decimals for the `Currency`.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('AppPromotion', 'Nominal')
```
---------
### PalletId
 The app&#x27;s pallet id, used for deriving its sovereign account address.
#### Value
```python
'0x6170707374616b65'
```
#### Python
```python
constant = substrate.get_constant('AppPromotion', 'PalletId')
```
---------
### PendingInterval
 In parachain blocks.
#### Value
```python
50400
```
#### Python
```python
constant = substrate.get_constant('AppPromotion', 'PendingInterval')
```
---------
### RecalculationInterval
 In relay blocks.
#### Value
```python
14400
```
#### Python
```python
constant = substrate.get_constant('AppPromotion', 'RecalculationInterval')
```
---------
## Errors

---------
### AdminNotSet
Error due to action requiring admin to be set.

---------
### InconsistencyState
Errors caused by incorrect state of a staker in context of the pallet.

---------
### InsufficientStakedBalance
Errors caused by insufficient staked balance.

---------
### NoPermission
No permission to perform an action.

---------
### NotSufficientFunds
Insufficient funds to perform an action.

---------
### PendingForBlockOverflow
Occurs when a pending unstake cannot be added in this block. PENDING_LIMIT_PER_BLOCK` limits exceeded.

---------
### SponsorNotSet
The error is due to the fact that the collection/contract must already be sponsored in order to perform the action.

---------
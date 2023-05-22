
# AppPromotion

---------
## Calls

---------
### payout_stakers
Recalculates interest for the specified number of stakers.
If all stakers are not recalculated, the next call of the extrinsic
will continue the recalculation, from those stakers for whom this
was not perform in last call.

\# Permissions

* Pallet admin

\# Arguments

* `stakers_number`: the number of stakers for which recalculation will be performed
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
Sets an address as the the admin.

\# Permissions

* Sudo

\# Arguments

* `admin`: account of the new admin.
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
Sets the pallet to be the sponsor for the collection.

\# Permissions

* Pallet admin

\# Arguments

* `collection_id`: ID of the collection that will be sponsored by `pallet_id`
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
Sets the pallet to be the sponsor for the contract.

\# Permissions

* Pallet admin

\# Arguments

* `contract_id`: the contract address that will be sponsored by `pallet_id`
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
Stakes the amount of native tokens.
Sets `amount` to the locked state.
The maximum number of stakes for a staker is 10.

\# Arguments

* `amount`: in native tokens.
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
Removes the pallet as the sponsor for the collection.
Returns [`NoPermission`][`Error::NoPermission`]
if the pallet wasn&\#x27;t the sponsor.

\# Permissions

* Pallet admin

\# Arguments

* `collection_id`: ID of the collection that is sponsored by `pallet_id`
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
Removes the pallet as the sponsor for the contract.
Returns [`NoPermission`][`Error::NoPermission`]
if the pallet wasn&\#x27;t the sponsor.

\# Permissions

* Pallet admin

\# Arguments

* `contract_id`: the contract address that is sponsored by `pallet_id`
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
Unstakes all stakes.
After the end of `PendingInterval` this sum becomes completely
free for further use.
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
Unstakes the amount of balance for the staker.
After the end of `PendingInterval` this sum becomes completely
free for further use.

 \# Arguments

* `staker`: staker account.
* `amount`: amount of unstaked funds.
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
### IntervalIncome
 Rate of return for interval in blocks defined in `RecalculationInterval`.
#### Value
```python
500000
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
### IncorrectLockedBalanceOperation
Errors caused by incorrect actions with a locked balance.

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
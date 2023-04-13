
# Economy

---------
## Calls

---------
### force_unreserved_staking
Force unreserved unstake native token from staking ledger. The unstaked amount able to
unreserve immediately


The dispatch origin for this call must be _Root_.

`amount`: the stake amount
`who`: the address of staker

Emit `SelfStakingRemovedFromEconomy101` event if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Economy', 'force_unreserved_staking', {'amount': 'u128', 'who': 'AccountId'}
)
```

---------
### force_unstake
Force unstake native token from staking ledger. The unstaked amount able to redeem
immediately


The dispatch origin for this call must be _Root_.

`amount`: the stake amount
`who`: the address of staker

Emit `SelfStakingRemovedFromEconomy101` event or `EstateStakingRemovedFromEconomy101`
event if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| who | `T::AccountId` | 
| estate | `Option<EstateId>` | 

#### Python
```python
call = substrate.compose_call(
    'Economy', 'force_unstake', {
    'amount': 'u128',
    'estate': (None, 'u64'),
    'who': 'AccountId',
}
)
```

---------
### set_bit_power_exchange_rate
Set bit power exchange rate

The dispatch origin for this call must be _Root_.

`rate`: exchange rate of bit to power. input is BIT price per power

Emit `BitPowerExchangeRateUpdated` event if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| rate | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Economy', 'set_bit_power_exchange_rate', {'rate': 'u128'}
)
```

---------
### set_power_balance
Set power balance for specific NFT

The dispatch origin for this call must be _Root_.

`beneficiary`: NFT account that receives power
`amount`: amount of power

Emit `SetPowerBalance` event if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiary | `(ClassId, TokenId)` | 
| amount | `PowerAmount` | 

#### Python
```python
call = substrate.compose_call(
    'Economy', 'set_power_balance', {
    'amount': 'u64',
    'beneficiary': ('u32', 'u64'),
}
)
```

---------
### stake
Stake native token to staking ledger to receive build material every round

The dispatch origin for this call must be _Signed_.

`amount`: the stake amount

Emit `SelfStakedToEconomy101` event or `EstateStakedToEconomy101` event if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| estate | `Option<EstateId>` | 

#### Python
```python
call = substrate.compose_call(
    'Economy', 'stake', {
    'amount': 'u128',
    'estate': (None, 'u64'),
}
)
```

---------
### unstake
Unstake native token from staking ledger. The unstaked amount able to redeem from the
next round

The dispatch origin for this call must be _Signed_.

`amount`: the stake amount

Emit `SelfStakingRemovedFromEconomy101` event or `EstateStakingRemovedFromEconomy101`
event if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| estate | `Option<EstateId>` | 

#### Python
```python
call = substrate.compose_call(
    'Economy', 'unstake', {
    'amount': 'u128',
    'estate': (None, 'u64'),
}
)
```

---------
### unstake_new_estate_owner
Unstake native token (staked by previous owner) from staking ledger.

The dispatch origin for this call must be _Signed_. Works if the origin is the estate
owner and the previous owner got staked funds

`estate_id`: the estate ID which funds are going to be unstaked

Emit `EstateStakingRemovedFromEconomy101` event if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| estate_id | `EstateId` | 

#### Python
```python
call = substrate.compose_call(
    'Economy', 'unstake_new_estate_owner', {'estate_id': 'u64'}
)
```

---------
### withdraw_estate_unreserved
Withdraw unstaked token from estate unstaking queue. The unstaked amount will be
unreserved and become transferrable

The dispatch origin for this call must be _Signed_.

`round_index`: the round index that user can redeem.
`estate_id`: the estate id that user can redeem.

Emit `UnstakedAmountWithdrew` event if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_index | `RoundIndex` | 
| estate_id | `EstateId` | 

#### Python
```python
call = substrate.compose_call(
    'Economy', 'withdraw_estate_unreserved', {
    'estate_id': 'u64',
    'round_index': 'u32',
}
)
```

---------
### withdraw_unreserved
Withdraw unstaked token from unstaking queue. The unstaked amount will be unreserved and
become transferrable

The dispatch origin for this call must be _Signed_.

`round_index`: the round index that user can unstake.

Emit `UnstakedAmountWithdrew` event if successful
#### Attributes
| Name | Type |
| -------- | -------- | 
| round_index | `RoundIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Economy', 'withdraw_unreserved', {'round_index': 'u32'}
)
```

---------
## Events

---------
### BitPowerExchangeRateUpdated
New BIT to Power exchange rate has updated [amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### CancelPowerConversionRequest
Power conversion request has cancelled [(class_id, token_id), account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `(ClassId, TokenId)` | ```('u32', 'u64')```
| None | `T::AccountId` | ```AccountId```

---------
### EstateStakedToEconomy101
Estate staking to economy 101 [staker, estate_id, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EstateId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### EstateStakingRemovedFromEconomy101
Estate staking remoed from economy 101 [staker, estate_id, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `EstateId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### MiningResourceBurned
Mining resource burned [amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### SelfStakedToEconomy101
Self staking to economy 101 [staker, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### SelfStakingRemovedFromEconomy101
Self staking removed from economy 101 [staker, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### SetPowerBalance
Set power balance by sudo [account, power_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PowerAmount` | ```u64```

---------
### UnstakedAmountWithdrew
Unstaked amount has been withdrew after it&\#x27;s expired [account, rate]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AcceptedDomain
 TBD Accept domain

#### Python
```python
result = substrate.query(
    'Economy', 'AcceptedDomain', ['u32']
)
```

#### Return value
```python
()
```
---------
### BitPowerExchangeRate
 BIT to power exchange rate

#### Python
```python
result = substrate.query(
    'Economy', 'BitPowerExchangeRate', []
)
```

#### Return value
```python
'u128'
```
---------
### EstateExitQueue
 Estate self-staking exit estate queue info
 This will keep track of staked estate exits queue, unstake only allows after 1 round

#### Python
```python
result = substrate.query(
    'Economy', 'EstateExitQueue', ['AccountId', 'u32', 'u64']
)
```

#### Return value
```python
'u128'
```
---------
### EstateStakingInfo
 Estate-staking info

#### Python
```python
result = substrate.query(
    'Economy', 'EstateStakingInfo', ['u64']
)
```

#### Return value
```python
{'amount': 'u128', 'staker': 'AccountId'}
```
---------
### ExitQueue
 Self-staking exit queue info
 This will keep track of stake exits queue, unstake only allows after 1 round

#### Python
```python
result = substrate.query(
    'Economy', 'ExitQueue', ['AccountId', 'u32']
)
```

#### Return value
```python
'u128'
```
---------
### PowerBalance
 Power balance of user

#### Python
```python
result = substrate.query(
    'Economy', 'PowerBalance', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### StakingInfo
 Self-staking info

#### Python
```python
result = substrate.query(
    'Economy', 'StakingInfo', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### TotalEstateStake
 Total native token locked estate staking pallet

#### Python
```python
result = substrate.query(
    'Economy', 'TotalEstateStake', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalStake
 Total native token locked in this pallet

#### Python
```python
result = substrate.query(
    'Economy', 'TotalStake', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### EconomyTreasury
 Economy treasury fund
#### Value
```python
'0x6269742f65636f6e'
```
#### Python
```python
constant = substrate.get_constant('Economy', 'EconomyTreasury')
```
---------
### MaximumEstateStake
 The maximum estate staked per land unit
#### Value
```python
1000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Economy', 'MaximumEstateStake')
```
---------
### MinimumStake
 The minimum stake required for staking
#### Value
```python
100000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Economy', 'MinimumStake')
```
---------
### MiningCurrencyId
 The currency id of BIT
#### Value
```python
{'MiningResource': 0}
```
#### Python
```python
constant = substrate.get_constant('Economy', 'MiningCurrencyId')
```
---------
### PowerAmountPerBlock
 The Power Amount per block
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Economy', 'PowerAmountPerBlock')
```
---------
## Errors

---------
### AccountHasNoPowerBalance
Insufficient power balance

---------
### EstateExitQueueAlreadyScheduled
Has scheduled exit estate staking, only stake after queue exit

---------
### EstateExitQueueDoesNotExit
Estate exit queue does not exist

---------
### ExitQueueAlreadyScheduled
Has scheduled exit staking, only stake after queue exit

---------
### ExitQueueDoesNotExit
Exit queue does not exist

---------
### InsufficientBalanceForStaking
Not enough free balance for staking

---------
### NFTAssetDoesNotExist
NFT asset does not exist

---------
### NFTClassDoesNotExist
NFT class does not exist

---------
### NFTCollectionDoesNotExist
NFT collection does not exist

---------
### NoAuthorization
No authorization

---------
### NoFundsStakedAtEstate
No funds staked at estate

---------
### NoPermission
No permission

---------
### NotReadyToExecute
Order has not reach target

---------
### PowerAmountIsZero
Power amount is zero

---------
### PreviousOwnerStillStakesAtEstate
Previous owner still stakes at estate

---------
### RequestAlreadyExist
Request already exists

---------
### StakeAmountExceedMaximumAmount
Stake amount exceed estate max amount

---------
### StakeBelowMinimum
Stake amount below minimum staking required

---------
### StakeEstateDoesNotExist
Staking estate does not exist

---------
### StakerNotEstateOwner
Staker is not estate owner

---------
### StakerNotPreviousOwner
Stake is not previous owner

---------
### UnstakeAmountExceedStakedAmount
Unstake amount greater than staked amount

---------
### UnstakeAmountIsZero
Unstaked amount is zero

---------
### WithdrawFutureRound
Withdraw future round

---------
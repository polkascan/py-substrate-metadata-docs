
# Mining

---------
## Calls

---------
### add_minting_origin
Add new Minting Origin to Mining Resource
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Mining', 'add_minting_origin', {'who': 'AccountId'}
)
```

---------
### burn
Burn mining resource on metaverse. There are, and will only ever be, `total`
such assets and they&\#x27;ll all belong to the `origin` initially. It will have an
identifier `TokenId` instance: this will be specified in the `Issued` event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Mining', 'burn', {'amount': 'u128', 'who': 'AccountId'}
)
```

---------
### deposit
Deposit Mining Resource from address to mining treasury
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Mining', 'deposit', {'amount': 'u128'}
)
```

---------
### mint
Issue mining resource on metaverse. There are, and will only ever be, `total`
such assets and they&\#x27;ll all belong to the `origin` initially. It will have an
identifier `TokenId` instance: this will be specified in the `Issued` event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Mining', 'mint', {'amount': 'u128', 'who': 'AccountId'}
)
```

---------
### pause_mining_round
Pause current mining round so new round will not roll out until unpaused
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Mining', 'pause_mining_round', {}
)
```

---------
### remove_minting_origin
Remove Minting Origin to Mining Resource
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Mining', 'remove_minting_origin', {'who': 'AccountId'}
)
```

---------
### unpause_mining_round
Unpause current mining round so new round can roll out
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Mining', 'unpause_mining_round', {}
)
```

---------
### update_mining_issuance_config
Update mining issuance configuration
#### Attributes
| Name | Type |
| -------- | -------- | 
| config | `MiningResourceRateInfo` | 

#### Python
```python
call = substrate.compose_call(
    'Mining', 'update_mining_issuance_config', {
    'config': {
        'mining_reward': 'u32',
        'rate': 'u32',
        'staking_reward': 'u32',
    },
}
)
```

---------
### update_round_length
Update round length
#### Attributes
| Name | Type |
| -------- | -------- | 
| length | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Mining', 'update_round_length', {'length': 'u32'}
)
```

---------
### withdraw
Withdraw Mining Resource from mining engine to destination wallet
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `T::AccountId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Mining', 'withdraw', {
    'amount': 'u128',
    'dest': 'AccountId',
}
)
```

---------
## Events

---------
### AddNewMiningOrigin
Add new mining origins [who]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### DepositMiningResource
Deposit mining resource [who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### MiningConfigUpdated
New mining config update
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```
| None | `MiningResourceRateInfo` | ```{'rate': 'u32', 'staking_reward': 'u32', 'mining_reward': 'u32'}```

---------
### MiningResourceBurnFrom
Burn new Mining resource of [who] [amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### MiningResourceBurned
Mining resource burned [amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### MiningResourceMinted
Mining resource minted [amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Balance` | ```u128```

---------
### MiningResourceMintedTo
Minting new Mining resource to [who] [amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### MiningRoundPaused
Temporary pause mining round rotation
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```
| None | `RoundIndex` | ```u32```

---------
### MiningRoundUnPaused
Mining round rotation is unpaused
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```
| None | `RoundIndex` | ```u32```

---------
### NewMiningRound
New round
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `RoundIndex` | ```u32```
| None | `MiningRange<Balance>` | ```{'min': 'u128', 'ideal': 'u128', 'max': 'u128', 'staking_allocation': 'u128', 'mining_allocation': 'u128'}```

---------
### RemoveMiningOrigin
Remove mining origin [who]
Add new mining origins [who]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### RoundLengthUpdated
Round length update
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::BlockNumber` | ```u32```

---------
### WithdrawMiningResource
Withdraw mining resource [who, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### CurrentMiningResourceAllocation
 Mining resource issuance ratio config

#### Python
```python
result = substrate.query(
    'Mining', 'CurrentMiningResourceAllocation', []
)
```

#### Return value
```python
{
    'ideal': 'u128',
    'max': 'u128',
    'min': 'u128',
    'mining_allocation': 'u128',
    'staking_allocation': 'u128',
}
```
---------
### MiningConfig
 Mining resource issuance ratio config

#### Python
```python
result = substrate.query(
    'Mining', 'MiningConfig', []
)
```

#### Return value
```python
{'mining_reward': 'u32', 'rate': 'u32', 'staking_reward': 'u32'}
```
---------
### MiningPaused
 Mining resource issuance ratio config

#### Python
```python
result = substrate.query(
    'Mining', 'MiningPaused', []
)
```

#### Return value
```python
'bool'
```
---------
### MintingOrigins
 Minting origins

#### Python
```python
result = substrate.query(
    'Mining', 'MintingOrigins', ['AccountId']
)
```

#### Return value
```python
()
```
---------
### Round
 Current round index and next round scheduled transition

#### Python
```python
result = substrate.query(
    'Mining', 'Round', []
)
```

#### Return value
```python
{'current': 'u32', 'first': 'u32', 'length': 'u32'}
```
---------
## Constants

---------
### BitMiningTreasury
#### Value
```python
'0x63622f6d696e6967'
```
#### Python
```python
constant = substrate.get_constant('Mining', 'BitMiningTreasury')
```
---------
## Errors

---------
### AmountZero
Transfer amount should be non-zero

---------
### BalanceLow
Account balance must be greater than or equal to the transfer amount

---------
### BalanceZero
Balance should be non-zero

---------
### InsufficientBalance
Insufficient balance

---------
### MiningRoundAlreadyPaused
Mining round already paused

---------
### MiningRoundIsNotPaused
Mining round is not paused

---------
### NoPermission
No permission to interact with mining resource

---------
### NoPermissionTokenIssuance
No permission to issue token

---------
### OriginsAlreadyExist
Origins already exist

---------
### OriginsIsNotExist
Origin is not exist

---------
### RoundUpdateIsOnProgress
Round update is on progress

---------
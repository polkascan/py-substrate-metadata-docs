
# Issuance

---------
## Calls

---------
### execute_tge
#### Attributes
| Name | Type |
| -------- | -------- | 
| tge_infos | `Vec<TgeInfo<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Issuance', 'execute_tge', {
    'tge_infos': [
        {
            'amount': 'u128',
            'who': 'AccountId',
        },
    ],
}
)
```

---------
### finalize_tge
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Issuance', 'finalize_tge', {}
)
```

---------
### init_issuance_config
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Issuance', 'init_issuance_config', {}
)
```

---------
## Events

---------
### IssuanceConfigInitialized
Issuance configuration has been finalized
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IssuanceInfo` | ```{'cap': 'u128', 'issuance_at_init': 'u128', 'linear_issuance_blocks': 'u32', 'liquidity_mining_split': 'u32', 'staking_split': 'u32', 'total_crowdloan_allocation': 'u128'}```

---------
### SessionIssuanceIssued
Issuance for upcoming session issued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### SessionIssuanceRecorded
Issuance for upcoming session calculated and recorded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### TGEFinalized
TGE has been finalized
#### Attributes
No attributes

---------
### TGEInstanceFailed
A TGE instance has failed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TgeInfo<T::AccountId>` | ```{'who': 'AccountId', 'amount': 'u128'}```

---------
### TGEInstanceSucceeded
A TGE instance has succeeded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `TgeInfo<T::AccountId>` | ```{'who': 'AccountId', 'amount': 'u128'}```

---------
## Storage functions

---------
### IsTGEFinalized

#### Python
```python
result = substrate.query(
    'Issuance', 'IsTGEFinalized', []
)
```

#### Return value
```python
'bool'
```
---------
### IssuanceConfigStore

#### Python
```python
result = substrate.query(
    'Issuance', 'IssuanceConfigStore', []
)
```

#### Return value
```python
{
    'cap': 'u128',
    'issuance_at_init': 'u128',
    'linear_issuance_blocks': 'u32',
    'liquidity_mining_split': 'u32',
    'staking_split': 'u32',
    'total_crowdloan_allocation': 'u128',
}
```
---------
### PromotedPoolsRewards

#### Python
```python
result = substrate.query(
    'Issuance', 'PromotedPoolsRewards', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### PromotedPoolsRewardsV2

#### Python
```python
result = substrate.query(
    'Issuance', 'PromotedPoolsRewardsV2', []
)
```

#### Return value
```python
'scale_info::357'
```
---------
### SessionIssuance

#### Python
```python
result = substrate.query(
    'Issuance', 'SessionIssuance', ['u32']
)
```

#### Return value
```python
(None, ('u128', 'u128'))
```
---------
### TGETotal

#### Python
```python
result = substrate.query(
    'Issuance', 'TGETotal', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### BlocksPerRound
 Number of blocks per session/round
#### Value
```python
1200
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'BlocksPerRound')
```
---------
### HistoryLimit
 Number of sessions to store issuance history for
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'HistoryLimit')
```
---------
### ImmediateTGEReleasePercent
 The maximum amount of Mangata tokens
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'ImmediateTGEReleasePercent')
```
---------
### IssuanceCap
 The maximum amount of Mangata tokens
#### Value
```python
4000000000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'IssuanceCap')
```
---------
### LinearIssuanceBlocks
 The number of blocks the issuance is linear
#### Value
```python
13140000
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'LinearIssuanceBlocks')
```
---------
### LiquidityMiningIssuanceVault
 The account id that holds the liquidity mining issuance
#### Value
```python
'5EYCAe5ijiYetuT4xrRZx2vbVopfJjhvfsZ4546K1Mmdexb1'
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'LiquidityMiningIssuanceVault')
```
---------
### LiquidityMiningSplit
 The split of issuance for liquidity mining rewards
#### Value
```python
555555556
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'LiquidityMiningSplit')
```
---------
### StakingIssuanceVault
 The account id that holds the staking issuance
#### Value
```python
'5EYCAe5ijiYfqsPVaS1Spou5yMsPSGJDSoCZr6iYazvbVgUy'
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'StakingIssuanceVault')
```
---------
### StakingSplit
 The split of issuance for staking rewards
#### Value
```python
444444444
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'StakingSplit')
```
---------
### TGEReleaseBegin
 The block at which the tge tokens begin to vest
#### Value
```python
100800
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'TGEReleaseBegin')
```
---------
### TGEReleasePeriod
 The number of blocks the tge tokens vest for
#### Value
```python
5256000
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'TGEReleasePeriod')
```
---------
### TotalCrowdloanAllocation
 The total mga allocated for crowdloans
#### Value
```python
330000000000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Issuance', 'TotalCrowdloanAllocation')
```
---------
## Errors

---------
### IssuanceConfigAlreadyInitialized
The issuance config has already been initialized

---------
### IssuanceConfigInvalid
The issuance config is invalid

---------
### IssuanceConfigNotInitialized
The issuance config has not been initialized

---------
### MathError
An underflow or an overflow has occured

---------
### TGEIsAlreadyFinalized
The TGE is already finalized

---------
### TGENotFinalized
TGE must be finalized before issuance config is inti

---------
### UnknownPool
unknown pool

---------
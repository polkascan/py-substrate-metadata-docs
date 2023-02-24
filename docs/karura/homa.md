
# Homa

---------
## Calls

---------
### claim_redemption
#### Attributes
| Name | Type |
| -------- | -------- | 
| redeemer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'claim_redemption', {'redeemer': 'AccountId'}
)
```

---------
### fast_match_redeems
#### Attributes
| Name | Type |
| -------- | -------- | 
| redeemer_list | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'fast_match_redeems', {'redeemer_list': ['AccountId']}
)
```

---------
### fast_match_redeems_completely
#### Attributes
| Name | Type |
| -------- | -------- | 
| redeemer_list | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'fast_match_redeems_completely', {'redeemer_list': ['AccountId']}
)
```

---------
### force_bump_current_era
#### Attributes
| Name | Type |
| -------- | -------- | 
| bump_amount | `EraIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'force_bump_current_era', {'bump_amount': 'u32'}
)
```

---------
### mint
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'mint', {'amount': 'u128'}
)
```

---------
### request_redeem
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 
| allow_fast_match | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'request_redeem', {
    'allow_fast_match': 'bool',
    'amount': 'u128',
}
)
```

---------
### reset_current_era
#### Attributes
| Name | Type |
| -------- | -------- | 
| era_index | `EraIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'reset_current_era', {'era_index': 'u32'}
)
```

---------
### reset_ledgers
#### Attributes
| Name | Type |
| -------- | -------- | 
| updates | `Vec<(u16, Option<Balance>, Option<Vec<UnlockChunk>>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'reset_ledgers', {
    'updates': [
        (
            'u16',
            (None, 'u128'),
            (
                None,
                [
                    {
                        'era': 'u32',
                        'value': 'u128',
                    },
                ],
            ),
        ),
    ],
}
)
```

---------
### update_bump_era_params
#### Attributes
| Name | Type |
| -------- | -------- | 
| last_era_bumped_block | `Option<T::BlockNumber>` | 
| frequency | `Option<T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'update_bump_era_params', {
    'frequency': (None, 'u32'),
    'last_era_bumped_block': (
        None,
        'u32',
    ),
}
)
```

---------
### update_homa_params
#### Attributes
| Name | Type |
| -------- | -------- | 
| soft_bonded_cap_per_sub_account | `Option<Balance>` | 
| estimated_reward_rate_per_era | `Option<Rate>` | 
| commission_rate | `Option<Rate>` | 
| fast_match_fee_rate | `Option<Rate>` | 

#### Python
```python
call = substrate.compose_call(
    'Homa', 'update_homa_params', {
    'commission_rate': (None, 'u128'),
    'estimated_reward_rate_per_era': (
        None,
        'u128',
    ),
    'fast_match_fee_rate': (
        None,
        'u128',
    ),
    'soft_bonded_cap_per_sub_account': (
        None,
        'u128',
    ),
}
)
```

---------
## Events

---------
### BumpEraFrequencyUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| frequency | `T::BlockNumber` | ```u32```

---------
### CommissionRateUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| commission_rate | `Rate` | ```u128```

---------
### CurrentEraBumped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_era_index | `EraIndex` | ```u32```

---------
### CurrentEraReset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_era_index | `EraIndex` | ```u32```

---------
### EstimatedRewardRatePerEraUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| reward_rate | `Rate` | ```u128```

---------
### FastMatchFeeRateUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| fast_match_fee_rate | `Rate` | ```u128```

---------
### LastEraBumpedBlockUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| last_era_bumped_block | `T::BlockNumber` | ```u32```

---------
### LedgerBondedReset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sub_account_index | `u16` | ```u16```
| new_bonded_amount | `Balance` | ```u128```

---------
### LedgerUnlockingReset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sub_account_index | `u16` | ```u16```
| new_unlocking | `Vec<UnlockChunk>` | ```[{'value': 'u128', 'era': 'u32'}]```

---------
### Minted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| minter | `T::AccountId` | ```AccountId```
| staking_currency_amount | `Balance` | ```u128```
| liquid_amount_received | `Balance` | ```u128```
| liquid_amount_added_to_void | `Balance` | ```u128```

---------
### RedeemRequestCancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| cancelled_liquid_amount | `Balance` | ```u128```

---------
### RedeemedByFastMatch
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| matched_liquid_amount | `Balance` | ```u128```
| fee_in_liquid | `Balance` | ```u128```
| redeemed_staking_amount | `Balance` | ```u128```

---------
### RedeemedByUnbond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| era_index_when_unbond | `EraIndex` | ```u32```
| liquid_amount | `Balance` | ```u128```
| unbonding_staking_amount | `Balance` | ```u128```

---------
### RequestedRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| liquid_amount | `Balance` | ```u128```
| allow_fast_match | `bool` | ```bool```

---------
### SoftBondedCapPerSubAccountUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cap_amount | `Balance` | ```u128```

---------
### WithdrawRedemption
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| redemption_amount | `Balance` | ```u128```

---------
## Storage functions

---------
### BumpEraFrequency

#### Python
```python
result = substrate.query(
    'Homa', 'BumpEraFrequency', []
)
```

#### Return value
```python
'u32'
```
---------
### CommissionRate

#### Python
```python
result = substrate.query(
    'Homa', 'CommissionRate', []
)
```

#### Return value
```python
'u128'
```
---------
### EstimatedRewardRatePerEra

#### Python
```python
result = substrate.query(
    'Homa', 'EstimatedRewardRatePerEra', []
)
```

#### Return value
```python
'u128'
```
---------
### FastMatchFeeRate

#### Python
```python
result = substrate.query(
    'Homa', 'FastMatchFeeRate', []
)
```

#### Return value
```python
'u128'
```
---------
### LastEraBumpedBlock

#### Python
```python
result = substrate.query(
    'Homa', 'LastEraBumpedBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### RedeemRequests

#### Python
```python
result = substrate.query(
    'Homa', 'RedeemRequests', ['AccountId']
)
```

#### Return value
```python
('u128', 'bool')
```
---------
### RelayChainCurrentEra

#### Python
```python
result = substrate.query(
    'Homa', 'RelayChainCurrentEra', []
)
```

#### Return value
```python
'u32'
```
---------
### SoftBondedCapPerSubAccount

#### Python
```python
result = substrate.query(
    'Homa', 'SoftBondedCapPerSubAccount', []
)
```

#### Return value
```python
'u128'
```
---------
### StakingLedgers

#### Python
```python
result = substrate.query(
    'Homa', 'StakingLedgers', ['u16']
)
```

#### Return value
```python
{'bonded': 'u128', 'unlocking': [{'era': 'u32', 'value': 'u128'}]}
```
---------
### ToBondPool

#### Python
```python
result = substrate.query(
    'Homa', 'ToBondPool', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalStakingBonded

#### Python
```python
result = substrate.query(
    'Homa', 'TotalStakingBonded', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalVoidLiquid

#### Python
```python
result = substrate.query(
    'Homa', 'TotalVoidLiquid', []
)
```

#### Return value
```python
'u128'
```
---------
### Unbondings

#### Python
```python
result = substrate.query(
    'Homa', 'Unbondings', ['AccountId', 'u32']
)
```

#### Return value
```python
'u128'
```
---------
### UnclaimedRedemption

#### Python
```python
result = substrate.query(
    'Homa', 'UnclaimedRedemption', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### ActiveSubAccountsIndexList
#### Value
```python
[0, 1, 2]
```
#### Python
```python
constant = substrate.get_constant('Homa', 'ActiveSubAccountsIndexList')
```
---------
### BondingDuration
#### Value
```python
28
```
#### Python
```python
constant = substrate.get_constant('Homa', 'BondingDuration')
```
---------
### DefaultExchangeRate
#### Value
```python
100000000000000000
```
#### Python
```python
constant = substrate.get_constant('Homa', 'DefaultExchangeRate')
```
---------
### LiquidCurrencyId
#### Value
```python
{'Token': 'LKSM'}
```
#### Python
```python
constant = substrate.get_constant('Homa', 'LiquidCurrencyId')
```
---------
### MintThreshold
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Homa', 'MintThreshold')
```
---------
### PalletId
#### Value
```python
'0x6163612f686f6d61'
```
#### Python
```python
constant = substrate.get_constant('Homa', 'PalletId')
```
---------
### RedeemThreshold
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Homa', 'RedeemThreshold')
```
---------
### StakingCurrencyId
#### Value
```python
{'Token': 'KSM'}
```
#### Python
```python
constant = substrate.get_constant('Homa', 'StakingCurrencyId')
```
---------
### TreasuryAccount
#### Value
```python
'qmmNufxeWaAUy17XBWGc1q4n2dkdxNS2dPkhtzCZRoExdAs'
```
#### Python
```python
constant = substrate.get_constant('Homa', 'TreasuryAccount')
```
---------
## Errors

---------
### BelowMintThreshold

---------
### BelowRedeemThreshold

---------
### CannotCompletelyFastMatch

---------
### ExceededStakingCurrencySoftCap

---------
### FastMatchIsNotAllowed

---------
### InsufficientUnclaimedRedemption

---------
### InvalidLastEraBumpedBlock

---------
### InvalidRate

---------
### OutdatedEraIndex

---------

# XMiningAsset

---------
## Calls

---------
### claim
Claims the staking reward given the `target` validator.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'XMiningAsset', 'claim', {'target': 'u32'}
)
```

---------
### set_asset_power
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| new | `FixedAssetPower` | 

#### Python
```python
call = substrate.compose_call(
    'XMiningAsset', 'set_asset_power', {'asset_id': 'u32', 'new': 'u32'}
)
```

---------
### set_claim_frequency_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'XMiningAsset', 'set_claim_frequency_limit', {'asset_id': 'u32', 'new': 'u32'}
)
```

---------
### set_claim_staking_requirement
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetId` | 
| new | `StakingRequirement` | 

#### Python
```python
call = substrate.compose_call(
    'XMiningAsset', 'set_claim_staking_requirement', {'asset_id': 'u32', 'new': 'u32'}
)
```

---------
## Events

---------
### Claimed
An asset miner claimed the mining reward. [claimer, asset_id, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### Minted
Issue new balance to the reward pot. [reward_pot_account, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AssetLedgers
 Mining weight information of the mining assets.

#### Python
```python
result = substrate.query(
    'XMiningAsset', 'AssetLedgers', ['u32']
)
```

#### Return value
```python
{'last_total_mining_weight': 'u128', 'last_total_mining_weight_update': 'u32'}
```
---------
### ClaimRestrictionOf
 Can not claim if the claimer violates the restriction.

#### Python
```python
result = substrate.query(
    'XMiningAsset', 'ClaimRestrictionOf', ['u32']
)
```

#### Return value
```python
{'frequency_limit': 'u32', 'staking_requirement': 'u32'}
```
---------
### DepositReward
 Possible reward for the new asset owners that does not have native coins yet.

#### Python
```python
result = substrate.query(
    'XMiningAsset', 'DepositReward', []
)
```

#### Return value
```python
'u128'
```
---------
### FixedAssetPowerOf
 Mining power map of X-type assets.

#### Python
```python
result = substrate.query(
    'XMiningAsset', 'FixedAssetPowerOf', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### MinerLedgers
 The map from nominator to the vote weight ledger of all mining assets.

#### Python
```python
result = substrate.query(
    'XMiningAsset', 'MinerLedgers', ['AccountId', 'u32']
)
```

#### Return value
```python
{
    'last_claim': (None, 'u32'),
    'last_mining_weight': 'u128',
    'last_mining_weight_update': 'u32',
}
```
---------
### MiningPrevilegedAssets
 External Assets that have the mining rights.

#### Python
```python
result = substrate.query(
    'XMiningAsset', 'MiningPrevilegedAssets', []
)
```

#### Return value
```python
['u32']
```
---------
## Errors

---------
### DispatchError
Balances error.

---------
### InsufficientStaking
Claimer does not have enough Staking locked balance.

---------
### NotPrevilegedAsset
The asset does not have the mining rights.

---------
### UnexpiredFrequencyLimit
Claimer just did a claim recently, the next frequency limit is not expired.

---------
### ZeroMiningWeight
Zero mining weight.

---------

# LBP

---------
## Calls

---------
### add_fundraising_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| fundraising | `AssetId` | 
| min_fundraising_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'add_fundraising_asset', {
    'fundraising': 'u32',
    'min_fundraising_amount': 'u128',
}
)
```

---------
### create_lbp
#### Attributes
| Name | Type |
| -------- | -------- | 
| afs_asset | `AssetId` | 
| fundraising_asset | `AssetId` | 
| afs_balance | `Balance` | 
| fundraising_balance | `Balance` | 
| afs_start_weight | `u128` | 
| afs_end_weight | `u128` | 
| fundraising_start_weight | `u128` | 
| fundraising_end_weight | `u128` | 
| start_block | `T::BlockNumber` | 
| end_block | `T::BlockNumber` | 
| steps | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'create_lbp', {
    'afs_asset': 'u32',
    'afs_balance': 'u128',
    'afs_end_weight': 'u128',
    'afs_start_weight': 'u128',
    'end_block': 'u32',
    'fundraising_asset': 'u32',
    'fundraising_balance': 'u128',
    'fundraising_end_weight': 'u128',
    'fundraising_start_weight': 'u128',
    'start_block': 'u32',
    'steps': 'u32',
}
)
```

---------
### exit_lbp
#### Attributes
| Name | Type |
| -------- | -------- | 
| lbp_id | `T::LbpId` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'exit_lbp', {'lbp_id': 'u32'}
)
```

---------
### remove_fundraising_asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| fundraising | `AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'remove_fundraising_asset', {'fundraising': 'u32'}
)
```

---------
### swap_exact_amount_supply
#### Attributes
| Name | Type |
| -------- | -------- | 
| supply_asset | `AssetId` | 
| supply_amount | `Balance` | 
| target_asset | `AssetId` | 
| min_target_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'swap_exact_amount_supply', {
    'min_target_amount': 'u128',
    'supply_amount': 'u128',
    'supply_asset': 'u32',
    'target_asset': 'u32',
}
)
```

---------
### swap_exact_amount_target
#### Attributes
| Name | Type |
| -------- | -------- | 
| supply_asset | `AssetId` | 
| max_supply_amount | `Balance` | 
| target_asset | `AssetId` | 
| target_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LBP', 'swap_exact_amount_target', {
    'max_supply_amount': 'u128',
    'supply_asset': 'u32',
    'target_amount': 'u128',
    'target_asset': 'u32',
}
)
```

---------
## Events

---------
### FundraisingAssetAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```
| None | `Balance` | ```u128```

---------
### FundraisingAssetRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetId` | ```u32```

---------
### LbpCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::LbpId` | ```u32```
| None | `AssetId` | ```u32```
| None | `AssetId` | ```u32```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### LbpExited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::LbpId` | ```u32```

---------
### Swapped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::LbpId` | ```u32```
| None | `AssetId` | ```u32```
| None | `AssetId` | ```u32```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### Lbps

#### Python
```python
result = substrate.query(
    'LBP', 'Lbps', ['u32']
)
```

#### Return value
```python
{
    'afs_asset': 'u32',
    'afs_balance': 'u128',
    'afs_weight': 'u128',
    'end_block': 'u32',
    'fundraising_asset': 'u32',
    'fundraising_balance': 'u128',
    'fundraising_weight': 'u128',
    'initial_afs_balance': 'u128',
    'initial_afs_end_weight': 'u128',
    'initial_afs_start_weight': 'u128',
    'initial_fundraising_balance': 'u128',
    'initial_fundraising_end_weight': 'u128',
    'initial_fundraising_start_weight': 'u128',
    'next_block': 'u32',
    'owner': 'AccountId',
    'start_block': 'u32',
    'status': ('Pending', 'Cancelled', 'InProgress', 'Finished'),
    'step': 'u32',
    'steps': 'u32',
}
```
---------
### NextLbpId

#### Python
```python
result = substrate.query(
    'LBP', 'NextLbpId', []
)
```

#### Return value
```python
'u32'
```
---------
### OngoingLbps

#### Python
```python
result = substrate.query(
    'LBP', 'OngoingLbps', [('u32', 'u32')]
)
```

#### Return value
```python
('AccountId', 'u32')
```
---------
### PriceHistory

#### Python
```python
result = substrate.query(
    'LBP', 'PriceHistory', ['u32']
)
```

#### Return value
```python
[('u32', 'u128', 'u128', 'u128', 'u128')]
```
---------
### SupportFundraisingAssets

#### Python
```python
result = substrate.query(
    'LBP', 'SupportFundraisingAssets', []
)
```

#### Return value
```python
[('u32', 'u128')]
```
---------
## Constants

---------
### PalletId
 The LBP&#x27;s module id, keep all assets in LBP.
#### Value
```python
'0x6469636f2f6c6270'
```
#### Python
```python
constant = substrate.get_constant('LBP', 'PalletId')
```
---------
## Errors

---------
### ErrMathApprox

---------
### ErrMaxDurationBlock

---------
### ErrMaxSteps

---------
### ErrMaxWeight

---------
### ErrMinDurationBlock

---------
### ErrMinSteps

---------
### ErrMinWeight

---------
### ErrStartEndBlock

---------
### InvalidFundraisingAmount

---------
### InvalidFundraisingAsset

---------
### InvalidTargetAmount

---------
### LbpNotFind

---------
### LbpPairOngoing

---------
### MustBeDifferentAsset

---------
### MustBeInProgressStatus

---------
### MustBeNonTradingStatus

---------
### MustBeNotEndStatus

---------
### MustBeOwner

---------
### NoLbpIdAvailable

---------
### OngoingLbpNotFind

---------
### StartBlockOutDate

---------
### UnacceptableSupplyAmount

---------
### UnacceptableTargetAmount

---------
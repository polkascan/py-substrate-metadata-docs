
# AMM

---------
## Calls

---------
### add_liquidity
Add liquidity to previously created asset pair pool.

Emits `LiquidityAdded` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_a | `AssetId` | 
| asset_b | `AssetId` | 
| amount_a_desired | `Balance` | 
| amount_b_desired | `Balance` | 
| amount_a_min | `Balance` | 
| amount_b_min | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'AMM', 'add_liquidity', {
    'amount_a_desired': 'u128',
    'amount_a_min': 'u128',
    'amount_b_desired': 'u128',
    'amount_b_min': 'u128',
    'asset_a': 'u32',
    'asset_b': 'u32',
}
)
```

---------
### remove_liquidity
Remove liquidity from specific liquidity pool in the form of burning shares.

Emits &\#x27;LiquidityRemoved&\#x27; when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_a | `AssetId` | 
| asset_b | `AssetId` | 
| remove_liquidity | `Balance` | 
| amount_a_min | `Balance` | 
| amount_b_min | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'AMM', 'remove_liquidity', {
    'amount_a_min': 'u128',
    'amount_b_min': 'u128',
    'asset_a': 'u32',
    'asset_b': 'u32',
    'remove_liquidity': 'u128',
}
)
```

---------
### swap_assets_for_exact_assets
Use no more than `amount_in_max` supply assets to exchange for a fixed amount of target
assets.

Emits &\#x27;Swapped&\#x27; when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_out | `Balance` | 
| amount_in_max | `Balance` | 
| path | `Vec<AssetId>` | 

#### Python
```python
call = substrate.compose_call(
    'AMM', 'swap_assets_for_exact_assets', {
    'amount_in_max': 'u128',
    'amount_out': 'u128',
    'path': ['u32'],
}
)
```

---------
### swap_exact_assets_for_assets
Use a fixed amount of supply assets to exchange for target assets not less than
`amount_out_min`.

Emits &\#x27;Swapped&\#x27; when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_in | `Balance` | 
| amount_out_min | `Balance` | 
| path | `Vec<AssetId>` | 

#### Python
```python
call = substrate.compose_call(
    'AMM', 'swap_exact_assets_for_assets', {
    'amount_in': 'u128',
    'amount_out_min': 'u128',
    'path': ['u32'],
}
)
```

---------
## Events

---------
### LiquidityAdded
New liquidity was provided to the pool. [who, liquidity_id, asset a, asset b, amount a,
amount b]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```
| None | `AssetId` | ```u32```
| None | `AssetId` | ```u32```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### LiquidityRemoved
Liquidity was removed from the pool. [who, liquidity_id, asset a, asset b, liquidity]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetId` | ```u32```
| None | `AssetId` | ```u32```
| None | `AssetId` | ```u32```
| None | `Balance` | ```u128```

---------
### Swapped
Swap asset cross path. [who, path, amount in, amount out]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<AssetId>` | ```['u32']```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### Liquidity

#### Python
```python
result = substrate.query(
    'AMM', 'Liquidity', [('u32', 'u32')]
)
```

#### Return value
```python
('u128', 'u128', 'u32')
```
---------
### NextLiquidityId

#### Python
```python
result = substrate.query(
    'AMM', 'NextLiquidityId', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### LiquidityAssetIdBase
#### Value
```python
4000000000
```
#### Python
```python
constant = substrate.get_constant('AMM', 'LiquidityAssetIdBase')
```
---------
### PalletId
 The AMM&#x27;s module id, keep all assets in AMM.
#### Value
```python
'0x6469636f2f616d6d'
```
#### Python
```python
constant = substrate.get_constant('AMM', 'PalletId')
```
---------
## Errors

---------
### AssetMetadataInvalid
The asset metadata is invalid.

---------
### InsufficientAmount
add insufficient assets amount.

---------
### InsufficientLiquidity
Liquidity is not enough.

---------
### InsufficientMintLiquidity
Add too little liquidity.

---------
### InvalidSwapPath
The asset exchange path does not exist.

---------
### InvariantCheckFailed
The swap doesn&\#x27;t meet the invariant check.

---------
### LiquidityNotFind
The liquidity pool does not exist.

---------
### MustAddNonZeroAmount
The number of added liquid assets must be greater than 0.

---------
### MustBeDifferentAsset
Must use different assets to add liquidity.

---------
### MustBeNonLiquidAsset
Liquid asset can not add liquidity pool.

---------
### NoLiquidityIdAvailable
The liquidity number has been exhausted.

---------
### RemoveZeroLiquidity
The amount of liquidity removed is 0.

---------
### UnacceptableInputAmount
Too many input assets are required for the exchange, and the user cannot accept it.

---------
### UnacceptableLiquidityWithdrawn
The assets obtained by removing the liquidity are too few for users to accept.

---------
### UnacceptableOutputAmount
The number of exchanged output assets is too small for users to accept.

---------
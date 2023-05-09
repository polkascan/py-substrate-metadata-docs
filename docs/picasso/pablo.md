
# Pablo

---------
## Calls

---------
### add_liquidity
Add liquidity to the given pool.

Emits `LiquidityAdded` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| assets | `BTreeMap<T::AssetId, T::Balance>` | 
| min_mint_amount | `T::Balance` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Pablo', 'add_liquidity', {
    'assets': 'scale_info::179',
    'keep_alive': 'bool',
    'min_mint_amount': 'u128',
    'pool_id': 'u128',
}
)
```

---------
### buy
Execute a buy order on pool.

Emits `Swapped` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| in_asset_id | `T::AssetId` | 
| out_asset | `AssetAmount<T::AssetId, T::Balance>` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Pablo', 'buy', {
    'in_asset_id': 'u128',
    'keep_alive': 'bool',
    'out_asset': {
        'amount': 'u128',
        'asset_id': 'u128',
    },
    'pool_id': 'u128',
}
)
```

---------
### create
Create a new pool. Note that this extrinsic does NOT validate if a pool with the same
assets already exists in the runtime.

Emits `PoolCreated` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool | `PoolInitConfigurationOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Pablo', 'create', {
    'pool': {
        'DualAssetConstantProduct': {
            'assets_weights': [
                ('u128', 'u32'),
            ],
            'fee': 'u32',
            'owner': 'AccountId',
        },
    },
}
)
```

---------
### enable_twap
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Pablo', 'enable_twap', {'pool_id': 'u128'}
)
```

---------
### remove_liquidity
Remove liquidity from the given pool.

Emits `LiquidityRemoved` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| lp_amount | `T::Balance` | 
| min_receive | `BTreeMap<T::AssetId, T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'Pablo', 'remove_liquidity', {
    'lp_amount': 'u128',
    'min_receive': 'scale_info::179',
    'pool_id': 'u128',
}
)
```

---------
### swap
Execute a specific swap operation.

The `quote_amount` is always the quote asset amount (A/B =&gt; B), (B/A =&gt; A).

Emits `Swapped` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| in_asset | `AssetAmount<T::AssetId, T::Balance>` | 
| min_receive | `AssetAmount<T::AssetId, T::Balance>` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Pablo', 'swap', {
    'in_asset': {
        'amount': 'u128',
        'asset_id': 'u128',
    },
    'keep_alive': 'bool',
    'min_receive': {
        'amount': 'u128',
        'asset_id': 'u128',
    },
    'pool_id': 'u128',
}
)
```

---------
## Events

---------
### LiquidityAdded
Liquidity added into the pool `T::PoolId`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| pool_id | `T::PoolId` | ```u128```
| asset_amounts | `BTreeMap<T::AssetId, T::Balance>` | ```scale_info::179```
| minted_lp | `T::Balance` | ```u128```

---------
### LiquidityRemoved
Liquidity removed from pool `T::PoolId` by `T::AccountId` in balanced way.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| pool_id | `T::PoolId` | ```u128```
| asset_amounts | `BTreeMap<T::AssetId, T::Balance>` | ```scale_info::179```

---------
### PoolCreated
Pool with specified id `T::PoolId` was created successfully by `T::AccountId`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u128```
| owner | `T::AccountId` | ```AccountId```
| asset_weights | `BTreeMap<T::AssetId, Permill>` | ```scale_info::175```
| lp_token_id | `T::AssetId` | ```u128```

---------
### Swapped
Token exchange happened.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u128```
| who | `T::AccountId` | ```AccountId```
| base_asset | `T::AssetId` | ```u128```
| quote_asset | `T::AssetId` | ```u128```
| base_amount | `T::Balance` | ```u128```
| quote_amount | `T::Balance` | ```u128```
| fee | `Fee<T::AssetId, T::Balance>` | ```{'fee': 'u128', 'lp_fee': 'u128', 'owner_fee': 'u128', 'protocol_fee': 'u128', 'asset_id': 'u128'}```

---------
### TwapUpdated
TWAP updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u128```
| timestamp | `MomentOf<T>` | ```u64```
| twaps | `BTreeMap<T::AssetId, Rate>` | ```scale_info::183```

---------
## Storage functions

---------
### LPTNonce

#### Python
```python
result = substrate.query(
    'Pablo', 'LPTNonce', []
)
```

#### Return value
```python
'u64'
```
---------
### PoolCount

#### Python
```python
result = substrate.query(
    'Pablo', 'PoolCount', []
)
```

#### Return value
```python
'u128'
```
---------
### Pools

#### Python
```python
result = substrate.query(
    'Pablo', 'Pools', ['u128']
)
```

#### Return value
```python
{
    'DualAssetConstantProduct': {
        'assets_weights': 'scale_info::175',
        'fee_config': {
            'fee_rate': 'u32',
            'owner_fee_rate': 'u32',
            'protocol_fee_rate': 'u32',
        },
        'lp_token': 'u128',
        'owner': 'AccountId',
    },
}
```
---------
### PriceCumulativeState

#### Python
```python
result = substrate.query(
    'Pablo', 'PriceCumulativeState', ['u128']
)
```

#### Return value
```python
{
    'base_price_cumulative': 'u128',
    'quote_price_cumulative': 'u128',
    'timestamp': 'u64',
}
```
---------
### TWAPState

#### Python
```python
result = substrate.query(
    'Pablo', 'TWAPState', ['u128']
)
```

#### Return value
```python
{
    'base_price_cumulative': 'u128',
    'base_twap': 'u128',
    'quote_price_cumulative': 'u128',
    'quote_twap': 'u128',
    'timestamp': 'u64',
}
```
---------
## Constants

---------
### PalletId
#### Value
```python
'0x70616c5f70626c6f'
```
#### Python
```python
constant = substrate.get_constant('Pablo', 'PalletId')
```
---------
### TWAPInterval
 The interval between TWAP computations.
#### Value
```python
120000
```
#### Python
```python
constant = substrate.get_constant('Pablo', 'TWAPInterval')
```
---------
## Errors

---------
### AmpFactorMustBeGreaterThanZero

---------
### AssetAmountMustBePositiveNumber

---------
### AssetNotFound

---------
### CannotBuyAssetWithItself
Cannot buy an asset with itself.

---------
### CannotRespectMinimumRequested

---------
### CannotSwapSameAsset
Cannot swap an asset with itself.

---------
### IncorrectAssetAmounts

---------
### IncorrectPoolConfig

---------
### InitialDepositCannotBeZero

---------
### InitialDepositMustContainAllAssets

---------
### InvalidAmount

---------
### InvalidAsset

---------
### InvalidFees

---------
### InvalidPair

---------
### InvalidSaleState

---------
### MinAmountsMustContainAtLeastOneAsset
The `min_amounts` map passed to `remove_liquidity` must contain at least one asset.

---------
### MissingAmount

---------
### MissingMinExpectedAmount

---------
### MoreThanTwoAssetsNotYetSupported

---------
### MustBeOwner

---------
### MustDepositMinimumOneAsset
The `assets` map passed to `add_liquidity` must contain at least one asset.

---------
### NoLpTokenForLbp

---------
### NoXTokenForLbp

---------
### NotEnoughLiquidity

---------
### NotEnoughLpToken

---------
### PairMismatch

---------
### PoolNotFound

---------
### StakingPoolConfigError

---------
### UnsupportedOperation

---------
### WeightsMustBeNonZero

---------
### WeightsMustSumToOne

---------
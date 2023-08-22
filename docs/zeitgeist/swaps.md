
# Swaps

---------
## Calls

---------
### admin_clean_up_pool
Clean up the pool of a resolved market.

\# Arguments

- `origin`: The root origin.
- `market_id`: The id of the market that the pool belongs to.
- `outcome_report`: The report that resolved the market.

\# Weight

Complexity: `O(1)` if the market is scalar, `O(n)` where `n` is the number of
assets in the pool if the market is categorical.
#### Attributes
| Name | Type |
| -------- | -------- | 
| market_id | `MarketIdOf<T>` | 
| outcome_report | `OutcomeReport` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'admin_clean_up_pool', {
    'market_id': 'u128',
    'outcome_report': {
        'Categorical': 'u16',
        'Scalar': 'u128',
    },
}
)
```

---------
### pool_exit
Pool - Exit

Retrieves a given set of assets from `pool_id` to `origin`.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be received.
* `pool_id`: Unique pool identifier.
* `pool_amount`: The amount of LP shares of this pool being burned based on the
retrieved assets.
* `min_assets_out`: List of asset lower bounds. No asset should be lower than the
provided values.

\# Weight

Complexity: `O(n)` where `n` is the number of assets in the specified pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| pool_amount | `BalanceOf<T>` | 
| min_assets_out | `Vec<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'pool_exit', {
    'min_assets_out': ['u128'],
    'pool_amount': 'u128',
    'pool_id': 'u128',
}
)
```

---------
### pool_exit_subsidy
Pool - Remove subsidty from a pool that uses the Rikiddo scoring rule.

Unreserves `pool_amount` of the base currency from being used as subsidy.
If `amount` is greater than the amount reserved for subsidy by `origin`,
then the whole amount reserved for subsidy will be unreserved.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be unreserved.
* `pool_id`: Unique pool identifier.
* `amount`: The amount of base currency that should be removed from subsidy.

\# Weight

Complexity: O(1)
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'pool_exit_subsidy', {'amount': 'u128', 'pool_id': 'u128'}
)
```

---------
### pool_exit_with_exact_asset_amount
Pool - Exit with exact pool amount

Takes an asset from `pool_id` and transfers to `origin`. Differently from `pool_exit`,
this method injects the exactly amount of `asset_amount` to `origin`.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be received.
* `pool_id`: Unique pool identifier.
* `asset`: Asset leaving the pool.
* `asset_amount`: Asset amount that is leaving the pool.
* `max_pool_amount`: The calculated amount of assets for the pool must be equal or
greater than the given value.

\# Weight

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| asset | `Asset<MarketIdOf<T>>` | 
| asset_amount | `BalanceOf<T>` | 
| max_pool_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'pool_exit_with_exact_asset_amount', {
    'asset': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
    'asset_amount': 'u128',
    'max_pool_amount': 'u128',
    'pool_id': 'u128',
}
)
```

---------
### pool_exit_with_exact_pool_amount
Pool - Exit with exact pool amount

Takes an asset from `pool_id` and transfers to `origin`. Differently from `pool_exit`,
this method injects the exactly amount of `pool_amount` to `pool_id`.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be received.
* `pool_id`: Unique pool identifier.
* `asset`: Asset leaving the pool.
* `pool_amount`: Pool amount that is entering the pool.
* `min_asset_amount`: The calculated amount for the asset must the equal or less
than the given value.

\# Weight

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| asset | `Asset<MarketIdOf<T>>` | 
| pool_amount | `BalanceOf<T>` | 
| min_asset_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'pool_exit_with_exact_pool_amount', {
    'asset': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
    'min_asset_amount': 'u128',
    'pool_amount': 'u128',
    'pool_id': 'u128',
}
)
```

---------
### pool_join
Pool - Join

Joins a given set of assets provided from `origin` to `pool_id`.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be transferred.
* `pool_id`: Unique pool identifier.
* `pool_amount`: The amount of LP shares for this pool that should be minted to the provider.
* `max_assets_in`: List of asset upper bounds. No asset should be greater than the
provided values.

\# Weight

Complexity: `O(n)` where `n` is the number of assets in the specified pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| pool_amount | `BalanceOf<T>` | 
| max_assets_in | `Vec<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'pool_join', {
    'max_assets_in': ['u128'],
    'pool_amount': 'u128',
    'pool_id': 'u128',
}
)
```

---------
### pool_join_subsidy
Pool - Add subsidy to a pool that uses the Rikiddo scoring rule.

Reserves `pool_amount` of the base currency to be added as subsidy on pool activation.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be reserved.
* `pool_id`: Unique pool identifier.
* `amount`: The amount of base currency that should be added to subsidy.

\# Weight

Complexity: O(1)
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'pool_join_subsidy', {'amount': 'u128', 'pool_id': 'u128'}
)
```

---------
### pool_join_with_exact_asset_amount
Pool - Join with exact asset amount

Joins an asset provided from `origin` to `pool_id`. Differently from `pool_join`,
this method transfers the exactly amount of `asset_amount` to `pool_id`.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be received.
* `pool_id`: Unique pool identifier.
* `asset_in`: Asset entering the pool.
* `asset_amount`: Asset amount that is entering the pool.
* `min_pool_amount`: The calculated amount for the pool must be equal or greater
than the given value.

\# Weight

Complexity: O(1)
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| asset_in | `Asset<MarketIdOf<T>>` | 
| asset_amount | `BalanceOf<T>` | 
| min_pool_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'pool_join_with_exact_asset_amount', {
    'asset_amount': 'u128',
    'asset_in': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
    'min_pool_amount': 'u128',
    'pool_id': 'u128',
}
)
```

---------
### pool_join_with_exact_pool_amount
Pool - Join with exact pool amount

Joins an asset provided from `origin` to `pool_id`. Differently from `pool_join`,
this method injects the exactly amount of `pool_amount` to `origin`.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be received.
* `pool_id`: Unique pool identifier.
* `asset`: Asset entering the pool.
* `pool_amount`: Asset amount that is entering the pool.
* `max_asset_amount`: The calculated amount of assets for the pool must be equal or
less than the given value.

\# Weight

Complexity: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| asset | `Asset<MarketIdOf<T>>` | 
| pool_amount | `BalanceOf<T>` | 
| max_asset_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'pool_join_with_exact_pool_amount', {
    'asset': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
    'max_asset_amount': 'u128',
    'pool_amount': 'u128',
    'pool_id': 'u128',
}
)
```

---------
### swap_exact_amount_in
Swap - Exact amount in

Swaps a given `asset_amount_in` of the `asset_in/asset_out` pair to `pool_id`.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be transferred.
* `pool_id`: Unique pool identifier.
* `asset_in`: Asset entering the pool.
* `asset_amount_in`: Amount that will be transferred from the provider to the pool.
* `asset_out`: Asset leaving the pool.
* `min_asset_amount_out`: Minimum asset amount that can leave the pool.
* `max_price`: Market price must be equal or less than the provided value.

\# Weight

Complexity: `O(1)` if the scoring rule is CPMM, `O(n)` where `n` is the amount of
assets if the scoring rule is Rikiddo.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| asset_in | `Asset<MarketIdOf<T>>` | 
| asset_amount_in | `BalanceOf<T>` | 
| asset_out | `Asset<MarketIdOf<T>>` | 
| min_asset_amount_out | `Option<BalanceOf<T>>` | 
| max_price | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'swap_exact_amount_in', {
    'asset_amount_in': 'u128',
    'asset_in': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
    'asset_out': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
    'max_price': (None, 'u128'),
    'min_asset_amount_out': (
        None,
        'u128',
    ),
    'pool_id': 'u128',
}
)
```

---------
### swap_exact_amount_out
Swap - Exact amount out

Swaps a given `asset_amount_out` of the `asset_in/asset_out` pair to `origin`.

\# Arguments

* `origin`: Liquidity Provider (LP). The account whose assets should be received.
* `pool_id`: Unique pool identifier.
* `asset_in`: Asset entering the pool.
* `max_asset_amount_in`: Maximum asset amount that can enter the pool.
* `asset_out`: Asset leaving the pool.
* `asset_amount_out`: Amount that will be transferred from the pool to the provider.
* `max_price`: Market price must be equal or less than the provided value.

\# Weight

Complexity: `O(1)` if the scoring rule is CPMM, `O(n)` where `n` is the amount of
assets if the scoring rule is Rikiddo.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| asset_in | `Asset<MarketIdOf<T>>` | 
| max_asset_amount_in | `Option<BalanceOf<T>>` | 
| asset_out | `Asset<MarketIdOf<T>>` | 
| asset_amount_out | `BalanceOf<T>` | 
| max_price | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Swaps', 'swap_exact_amount_out', {
    'asset_amount_out': 'u128',
    'asset_in': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
    'asset_out': {
        'CategoricalOutcome': (
            'u128',
            'u16',
        ),
        'CombinatorialOutcome': None,
        'ForeignAsset': 'u32',
        'PoolShare': 'u128',
        'ScalarOutcome': (
            'u128',
            ('Long', 'Short'),
        ),
        'Ztg': None,
    },
    'max_asset_amount_in': (
        None,
        'u128',
    ),
    'max_price': (None, 'u128'),
    'pool_id': 'u128',
}
)
```

---------
## Events

---------
### ArbitrageBuyBurn
Buy-burn arbitrage was executed on a CPMM pool. \[pool_id, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### ArbitrageMintSell
Mint-sell arbitrage was executed on a CPMM pool. \[pool_id, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### ArbitrageSkipped
Arbitrage was skipped on a CPMM pool. \[pool_id\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```

---------
### DistributeShareHolderRewards
Share holder rewards were distributed. \[pool_id, num_accounts_rewarded, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```
| None | `u64` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### PoolActive
A pool was opened. \[pool_id\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```

---------
### PoolCleanedUp
A pool was cleaned up. \[pool_id\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```

---------
### PoolClosed
A pool was closed. \[pool_id\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```

---------
### PoolCreate
A new pool has been created. \[CommonPoolEventParams, pool, pool_amount, pool_account\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CommonPoolEventParams<<T as frame_system::Config>::AccountId>` | ```{'pool_id': 'u128', 'who': 'AccountId'}```
| None | `Pool<BalanceOf<T>, MarketIdOf<T>>` | ```{'assets': [{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}], 'base_asset': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'market_id': 'u128', 'pool_status': ('Active', 'CollectingSubsidy', 'Closed', 'Clean', 'Initialized'), 'scoring_rule': ('CPMM', 'RikiddoSigmoidFeeMarketEma'), 'swap_fee': (None, 'u128'), 'total_subsidy': (None, 'u128'), 'total_weight': (None, 'u128'), 'weights': (None, 'scale_info::82')}```
| None | `BalanceOf<T>` | ```u128```
| None | `T::AccountId` | ```AccountId```

---------
### PoolDestroyed
Pool was manually destroyed. \[pool_id\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```

---------
### PoolDestroyedInSubsidyPhase
Pool destroyed due to insufficient subsidy. \[pool_id, \[(provider, subsidy), ...\]\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```
| None | `Vec<(<T as frame_system::Config>::AccountId, BalanceOf<T>)>` | ```[('AccountId', 'u128')]```

---------
### PoolExit
Someone has exited a pool. \[PoolAssetsEvent\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolAssetsEvent<<T as frame_system::Config>::AccountId, Asset<
MarketIdOf<T>>, BalanceOf<T>,>` | ```{'assets': [{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}], 'bounds': ['u128'], 'cpep': {'pool_id': 'u128', 'who': 'AccountId'}, 'transferred': ['u128'], 'pool_amount': 'u128'}```

---------
### PoolExitSubsidy
Someone has (partially) exited a pool by removing subsidy. \[asset, bound, pool_id, who, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Asset<MarketIdOf<T>>` | ```{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}```
| None | `BalanceOf<T>` | ```u128```
| None | `CommonPoolEventParams<<T as frame_system::Config>::AccountId>` | ```{'pool_id': 'u128', 'who': 'AccountId'}```
| None | `BalanceOf<T>` | ```u128```

---------
### PoolExitWithExactAssetAmount
Exits a pool given an exact amount of an asset. \[PoolAssetEvent\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolAssetEvent<<T as frame_system::Config>::AccountId, Asset<
MarketIdOf<T>>, BalanceOf<T>,>` | ```{'asset': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'bound': 'u128', 'cpep': {'pool_id': 'u128', 'who': 'AccountId'}, 'transferred': 'u128', 'pool_amount': 'u128'}```

---------
### PoolExitWithExactPoolAmount
Exits a pool given an exact pool&\#x27;s amount. \[PoolAssetEvent\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolAssetEvent<<T as frame_system::Config>::AccountId, Asset<
MarketIdOf<T>>, BalanceOf<T>,>` | ```{'asset': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'bound': 'u128', 'cpep': {'pool_id': 'u128', 'who': 'AccountId'}, 'transferred': 'u128', 'pool_amount': 'u128'}```

---------
### PoolJoin
Someone has joined a pool. \[PoolAssetsEvent\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolAssetsEvent<<T as frame_system::Config>::AccountId, Asset<
MarketIdOf<T>>, BalanceOf<T>,>` | ```{'assets': [{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}], 'bounds': ['u128'], 'cpep': {'pool_id': 'u128', 'who': 'AccountId'}, 'transferred': ['u128'], 'pool_amount': 'u128'}```

---------
### PoolJoinSubsidy
Someone has joined a pool by providing subsidy. \[asset, amount, pool_id, who\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Asset<MarketIdOf<T>>` | ```{'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}```
| None | `BalanceOf<T>` | ```u128```
| None | `CommonPoolEventParams<<T as frame_system::Config>::AccountId>` | ```{'pool_id': 'u128', 'who': 'AccountId'}```

---------
### PoolJoinWithExactAssetAmount
Joins a pool given an exact amount of an asset. \[PoolAssetEvent\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolAssetEvent<<T as frame_system::Config>::AccountId, Asset<
MarketIdOf<T>>, BalanceOf<T>,>` | ```{'asset': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'bound': 'u128', 'cpep': {'pool_id': 'u128', 'who': 'AccountId'}, 'transferred': 'u128', 'pool_amount': 'u128'}```

---------
### PoolJoinWithExactPoolAmount
Joins a pool given an exact pool&\#x27;s amount. \[PoolAssetEvent\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolAssetEvent<<T as frame_system::Config>::AccountId, Asset<
MarketIdOf<T>>, BalanceOf<T>,>` | ```{'asset': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'bound': 'u128', 'cpep': {'pool_id': 'u128', 'who': 'AccountId'}, 'transferred': 'u128', 'pool_amount': 'u128'}```

---------
### SubsidyCollected
Total subsidy collected for a pool. \[pool_id, \[(provider, subsidy), ...\], total_subsidy\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u128```
| None | `Vec<(<T as frame_system::Config>::AccountId, BalanceOf<T>)>` | ```[('AccountId', 'u128')]```
| None | `BalanceOf<T>` | ```u128```

---------
### SwapExactAmountIn
An exact amount of an asset is entering the pool. \[SwapEvent\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SwapEvent<<T as frame_system::Config>::AccountId, Asset<MarketIdOf<
T>>, BalanceOf<T>>` | ```{'asset_amount_in': 'u128', 'asset_amount_out': 'u128', 'asset_bound': (None, 'u128'), 'asset_in': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'asset_out': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'cpep': {'pool_id': 'u128', 'who': 'AccountId'}, 'max_price': (None, 'u128')}```

---------
### SwapExactAmountOut
An exact amount of an asset is leaving the pool. \[SwapEvent\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SwapEvent<<T as frame_system::Config>::AccountId, Asset<MarketIdOf<
T>>, BalanceOf<T>>` | ```{'asset_amount_in': 'u128', 'asset_amount_out': 'u128', 'asset_bound': (None, 'u128'), 'asset_in': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'asset_out': {'CategoricalOutcome': ('u128', 'u16'), 'ScalarOutcome': ('u128', ('Long', 'Short')), 'CombinatorialOutcome': None, 'PoolShare': 'u128', 'Ztg': None, 'ForeignAsset': 'u32'}, 'cpep': {'pool_id': 'u128', 'who': 'AccountId'}, 'max_price': (None, 'u128')}```

---------
## Storage functions

---------
### NextPoolId

#### Python
```python
result = substrate.query(
    'Swaps', 'NextPoolId', []
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
    'Swaps', 'Pools', ['u128']
)
```

#### Return value
```python
(
    None,
    {
        'assets': [
            {
                'CategoricalOutcome': ('u128', 'u16'),
                'CombinatorialOutcome': None,
                'ForeignAsset': 'u32',
                'PoolShare': 'u128',
                'ScalarOutcome': ('u128', 'scale_info::64'),
                'Ztg': None,
            },
        ],
        'base_asset': {
            'CategoricalOutcome': ('u128', 'u16'),
            'CombinatorialOutcome': None,
            'ForeignAsset': 'u32',
            'PoolShare': 'u128',
            'ScalarOutcome': ('u128', ('Long', 'Short')),
            'Ztg': None,
        },
        'market_id': 'u128',
        'pool_status': (
            'Active',
            'CollectingSubsidy',
            'Closed',
            'Clean',
            'Initialized',
        ),
        'scoring_rule': ('CPMM', 'RikiddoSigmoidFeeMarketEma'),
        'swap_fee': (None, 'u128'),
        'total_subsidy': (None, 'u128'),
        'total_weight': (None, 'u128'),
        'weights': (None, 'scale_info::82'),
    },
)
```
---------
### PoolsCachedForArbitrage

#### Python
```python
result = substrate.query(
    'Swaps', 'PoolsCachedForArbitrage', ['u128']
)
```

#### Return value
```python
()
```
---------
### SubsidyProviders

#### Python
```python
result = substrate.query(
    'Swaps', 'SubsidyProviders', ['u128', 'AccountId']
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### ExitFee
 The fee for exiting a pool.
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'ExitFee')
```
---------
### MaxAssets
#### Value
```python
65
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MaxAssets')
```
---------
### MaxInRatio
#### Value
```python
3333333334
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MaxInRatio')
```
---------
### MaxOutRatio
#### Value
```python
3333333334
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MaxOutRatio')
```
---------
### MaxSwapFee
#### Value
```python
1000000000
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MaxSwapFee')
```
---------
### MaxTotalWeight
#### Value
```python
1280000000000
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MaxTotalWeight')
```
---------
### MaxWeight
#### Value
```python
640000000000
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MaxWeight')
```
---------
### MinAssets
 The minimum amount of assets in a pool.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MinAssets')
```
---------
### MinSubsidy
 The minimum amount of subsidy required to state transit a market into active state.
 Must be greater than 0, but can be arbitrarily close to 0.
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MinSubsidy')
```
---------
### MinSubsidyPerAccount
 The minimum amount of subsidy that each subsidy provider must contribute.
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MinSubsidyPerAccount')
```
---------
### MinWeight
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'MinWeight')
```
---------
### PalletId
 The module identifier.
#### Value
```python
'0x7a67652f73776170'
```
#### Python
```python
constant = substrate.get_constant('Swaps', 'PalletId')
```
---------
## Errors

---------
### AboveMaximumWeight
The weight of an asset in a CPMM swap pool is greather than the upper weight cap.

---------
### AssetNotBound
The weight of an asset in a CPMM swap pool could not be found.

---------
### AssetNotInPool
The asset in question could not be found within the pool.

---------
### BadLimitPrice
The spot price of an asset pair was greater than the specified limit.

---------
### BaseAssetNotFound
The base asset of the swaps pool was None although a value was expected.

---------
### BelowMinimumWeight
The weight of an asset in a CPMM swap pool is lower than the upper weight cap.

---------
### InsufficientBalance
Some funds could not be transferred due to a too low balance.

---------
### InsufficientLiquidity
Liquidity provided to new CPMM pool is less than the minimum allowed balance.

---------
### InsufficientSubsidy
The market was not started since the subsidy goal was not reached.

---------
### InvalidAmountArgument
Could not create CPMM pool since no amount was specified.

---------
### InvalidFeeArgument
Could not create CPMM pool since no fee was supplied.

---------
### InvalidPoolStatus
Dispatch called on pool with invalid status.

---------
### InvalidScoringRule
A function that is only valid for pools with specific scoring rules was called for a
pool with another scoring rule.

---------
### InvalidStateTransition
A function was called for a swaps pool that does not fulfill the state requirement.

---------
### InvalidSubsidyAmount
Subsidy amount is too small.

---------
### InvalidWeightArgument
Could not create CPMM pool since no weights were supplied.

---------
### LimitIn
A transferal of funds into a swaps pool was above a threshhold specified by the sender.

---------
### LimitMissing
No limit was specified for a swap.

---------
### LimitOut
A transferal of funds out of a swaps pool was below a threshhold specified by the
receiver.

---------
### MathApproximation
The custom math library yielded an invalid result (most times unexpected zero value).

---------
### MaxInRatio
The proportion of an asset added into a pool in comparison to the amount
of that asset in the pool is above the threshhold specified by a constant.

---------
### MaxOutRatio
The proportion of an asset taken from a pool in comparison to the amount
of that asset in the pool is above the threshhold specified by a constant.

---------
### MaxTotalWeight
The total weight of all assets within a CPMM pool is above a treshhold specified
by a constant.

---------
### NoSubsidyProvided
It was tried to remove subsidy from a pool which does not have subsidy provided by
the address that tried to remove the subsidy.

---------
### PoolDoesNotExist
The pool in question does not exist.

---------
### PoolDrain
A pool balance dropped below the allowed minimum.

---------
### PoolIsNotActive
The pool in question is inactive.

---------
### PoolMissingFee
The CPMM pool in question does not have a fee, although it should.

---------
### PoolMissingSubsidy
The Rikiddo pool in question does not have subsidy, although it should.

---------
### PoolMissingWeight
The CPPM pool in question does not have weights, although it should.

---------
### ProvidedValuesLenMustEqualAssetsLen
Two vectors do not have the same length (usually CPMM pool assets and weights).

---------
### SomeIdenticalAssets
Tried to create a pool with at least two identical assets.

---------
### SwapFeeMissing
No swap fee information found for CPMM pool

---------
### SwapFeeTooHigh
The swap fee is higher than the allowed maximum.

---------
### TooFewAssets
Tried to create a pool that has less assets than the lower threshhold specified by
a constant.

---------
### TooManyAssets
Tried to create a pool that has more assets than the upper threshhold specified by
a constant.

---------
### UnsupportedTrade
The pool does not support swapping the assets in question.

---------
### WinningAssetNotFound
The outcome asset specified as the winning asset was not found in the pool.

---------
### ZeroAmount
Some amount in a transaction equals zero.

---------
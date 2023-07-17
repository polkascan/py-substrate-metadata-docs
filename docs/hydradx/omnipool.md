
# Omnipool

---------
## Calls

---------
### add_liquidity
Add liquidity of asset `asset` in quantity `amount` to Omnipool

`add_liquidity` adds specified asset amount to pool and in exchange gives the origin
corresponding shares amount in form of NFT at current price.

Asset&\#x27;s tradable state must contain ADD_LIQUIDITY flag, otherwise `NotAllowed` error is returned.

NFT is minted using NTFHandler which implements non-fungibles traits from frame_support.

Asset weight cap must be respected, otherwise `AssetWeightExceeded` error is returned.
Asset weight is ratio between new HubAsset reserve and total reserve of Hub asset in Omnipool.

Parameters:
- `asset`: The identifier of the new asset added to the pool. Must be already in the pool
- `amount`: Amount of asset added to omnipool

Emits `LiquidityAdded` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `T::AssetId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'add_liquidity', {'amount': 'u128', 'asset': 'u32'}
)
```

---------
### add_token
Add new token to omnipool in quantity `amount` at price `initial_price`

Can be called only after pool is initialized, otherwise it returns `NoStableAssetInPool`

Initial liquidity must be transferred to pool&\#x27;s account for this new token manually prior to calling `add_token`.

Initial liquidity is pool&\#x27;s account balance of the token.

Position NFT token is minted for `position_owner`.

Parameters:
- `asset`: The identifier of the new asset added to the pool. Must be registered in Asset registry
- `initial_price`: Initial price
- `position_owner`: account id for which share are distributed in form on NFT

Emits `TokenAdded` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `T::AssetId` | 
| initial_price | `Price` | 
| weight_cap | `Permill` | 
| position_owner | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'add_token', {
    'asset': 'u32',
    'initial_price': 'u128',
    'position_owner': 'AccountId',
    'weight_cap': 'u32',
}
)
```

---------
### buy
Execute a swap of `asset_out` for `asset_in`.

Price is determined by the Omnipool.

Hub asset is traded separately.

Asset&\#x27;s tradable states must contain SELL flag for asset_in and BUY flag for asset_out, otherwise `NotAllowed` error is returned.

Parameters:
- `asset_in`: ID of asset sold to the pool
- `asset_out`: ID of asset bought from the pool
- `amount`: Amount of asset sold
- `max_sell_amount`: Maximum amount to be sold.

Emits `BuyExecuted` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_out | `T::AssetId` | 
| asset_in | `T::AssetId` | 
| amount | `Balance` | 
| max_sell_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'buy', {
    'amount': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'max_sell_amount': 'u128',
}
)
```

---------
### initialize_pool
Initialize Omnipool with stable asset and native asset.

First added assets must be:
- preferred stable coin asset set as `StableCoinAssetId` pallet parameter
- native asset

Omnipool account must already have correct balances of stable and native asset.

Parameters:
- `stable_asset_price`: Initial price of stable asset
- `native_asset_price`: Initial price of stable asset

Emits two `TokenAdded` events when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| stable_asset_price | `Price` | 
| native_asset_price | `Price` | 
| stable_weight_cap | `Permill` | 
| native_weight_cap | `Permill` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'initialize_pool', {
    'native_asset_price': 'u128',
    'native_weight_cap': 'u32',
    'stable_asset_price': 'u128',
    'stable_weight_cap': 'u32',
}
)
```

---------
### refund_refused_asset
Refund given amount of asset to a recipient.

A refund is needed when a token is refused to be added to Omnipool, and initial liquidity of the asset has been already transferred to pool&\#x27;s account.

Transfer is performed only when asset is not in Omnipool and pool&\#x27;s balance has sufficient amount.

Only `AuthorityOrigin` can perform this operition -same as `add_token`o

Emits `AssetRefunded`
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| amount | `Balance` | 
| recipient | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'refund_refused_asset', {
    'amount': 'u128',
    'asset_id': 'u32',
    'recipient': 'AccountId',
}
)
```

---------
### remove_liquidity
Remove liquidity of asset `asset` in quantity `amount` from Omnipool

`remove_liquidity` removes specified shares amount from given PositionId (NFT instance).

Asset&\#x27;s tradable state must contain REMOVE_LIQUIDITY flag, otherwise `NotAllowed` error is returned.

if all shares from given position are removed, NFT is burned.

Parameters:
- `position_id`: The identifier of position which liquidity is removed from.
- `amount`: Amount of shares removed from omnipool

Emits `LiquidityRemoved` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| position_id | `T::PositionItemId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'remove_liquidity', {
    'amount': 'u128',
    'position_id': 'u128',
}
)
```

---------
### sacrifice_position
Sacrifice LP position in favor of pool.

A position is destroyed and liquidity owned by LP becomes pool owned liquidity.

Only owner of position can perform this action.

Emits `PositionDestroyed`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| position_id | `T::PositionItemId` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'sacrifice_position', {'position_id': 'u128'}
)
```

---------
### sell
Execute a swap of `asset_in` for `asset_out`.

Price is determined by the Omnipool.

Hub asset is traded separately.

Asset&\#x27;s tradable states must contain SELL flag for asset_in and BUY flag for asset_out, otherwise `NotAllowed` error is returned.

Parameters:
- `asset_in`: ID of asset sold to the pool
- `asset_out`: ID of asset bought from the pool
- `amount`: Amount of asset sold
- `min_buy_amount`: Minimum amount required to receive

Emits `SellExecuted` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_in | `T::AssetId` | 
| asset_out | `T::AssetId` | 
| amount | `Balance` | 
| min_buy_amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'sell', {
    'amount': 'u128',
    'asset_in': 'u32',
    'asset_out': 'u32',
    'min_buy_amount': 'u128',
}
)
```

---------
### set_asset_tradable_state
Update asset&\#x27;s tradable state.

Parameters:
- `asset_id`: asset id
- `state`: new state

Emits `TradableStateUpdated` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| state | `Tradability` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'set_asset_tradable_state', {
    'asset_id': 'u32',
    'state': {'bits': 'u8'},
}
)
```

---------
### set_asset_weight_cap
Update asset&\#x27;s weight cap

Parameters:
- `asset_id`: asset id
- `cap`: new weight cap

Emits `AssetWeightCapUpdated` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| cap | `Permill` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'set_asset_weight_cap', {'asset_id': 'u32', 'cap': 'u32'}
)
```

---------
### set_tvl_cap
Update TVL cap

Parameters:
- `cap`: new tvl cap

Emits `TVLCapUpdated` event when successful.

#### Attributes
| Name | Type |
| -------- | -------- | 
| cap | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'set_tvl_cap', {'cap': 'u128'}
)
```

---------
## Events

---------
### AssetRefunded
Amount has been refunded for asset which has not been accepted to add to omnipool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| amount | `Balance` | ```u128```
| recipient | `T::AccountId` | ```AccountId```

---------
### AssetWeightCapUpdated
Asset&\#x27;s weight cap has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| cap | `Permill` | ```u32```

---------
### BuyExecuted
Buy trade executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_in | `T::AssetId` | ```u32```
| asset_out | `T::AssetId` | ```u32```
| amount_in | `Balance` | ```u128```
| amount_out | `Balance` | ```u128```

---------
### LiquidityAdded
Liquidity of an asset was added to Omnipool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_id | `T::AssetId` | ```u32```
| amount | `Balance` | ```u128```
| position_id | `T::PositionItemId` | ```u128```

---------
### LiquidityRemoved
Liquidity of an asset was removed to Omnipool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| position_id | `T::PositionItemId` | ```u128```
| asset_id | `T::AssetId` | ```u32```
| shares_removed | `Balance` | ```u128```
| fee | `FixedU128` | ```u128```

---------
### PositionCreated
LP Position was created and NFT instance minted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| position_id | `T::PositionItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```
| asset | `T::AssetId` | ```u32```
| amount | `Balance` | ```u128```
| shares | `Balance` | ```u128```
| price | `Price` | ```u128```

---------
### PositionDestroyed
LP Position was destroyed and NFT instance burned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| position_id | `T::PositionItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```

---------
### PositionUpdated
LP Position was created and NFT instance minted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| position_id | `T::PositionItemId` | ```u128```
| owner | `T::AccountId` | ```AccountId```
| asset | `T::AssetId` | ```u32```
| amount | `Balance` | ```u128```
| shares | `Balance` | ```u128```
| price | `Price` | ```u128```

---------
### SellExecuted
Sell trade executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_in | `T::AssetId` | ```u32```
| asset_out | `T::AssetId` | ```u32```
| amount_in | `Balance` | ```u128```
| amount_out | `Balance` | ```u128```

---------
### TVLCapUpdated
TVL cap has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| cap | `Balance` | ```u128```

---------
### TokenAdded
An asset was added to Omnipool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| initial_amount | `Balance` | ```u128```
| initial_price | `Price` | ```u128```

---------
### TradableStateUpdated
Aseet&\#x27;s tradable state has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| state | `Tradability` | ```{'bits': 'u8'}```

---------
## Storage functions

---------
### Assets
 State of an asset in the omnipool

#### Python
```python
result = substrate.query(
    'Omnipool', 'Assets', ['u32']
)
```

#### Return value
```python
{
    'cap': 'u128',
    'hub_reserve': 'u128',
    'protocol_shares': 'u128',
    'shares': 'u128',
    'tradable': {'bits': 'u8'},
}
```
---------
### HubAssetImbalance
 Imbalance of hub asset

#### Python
```python
result = substrate.query(
    'Omnipool', 'HubAssetImbalance', []
)
```

#### Return value
```python
{'negative': 'bool', 'value': 'u128'}
```
---------
### HubAssetTradability
 Tradable state of hub asset.

#### Python
```python
result = substrate.query(
    'Omnipool', 'HubAssetTradability', []
)
```

#### Return value
```python
{'bits': 'u8'}
```
---------
### NextPositionId
 Position ids sequencer

#### Python
```python
result = substrate.query(
    'Omnipool', 'NextPositionId', []
)
```

#### Return value
```python
'u128'
```
---------
### Positions
 LP positions. Maps NFT instance id to corresponding position

#### Python
```python
result = substrate.query(
    'Omnipool', 'Positions', ['u128']
)
```

#### Return value
```python
{'amount': 'u128', 'asset_id': 'u32', 'price': ('u128', 'u128'), 'shares': 'u128'}
```
---------
### TvlCap
 TVL cap

#### Python
```python
result = substrate.query(
    'Omnipool', 'TvlCap', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### AssetFee
 Asset fee
#### Value
```python
2500
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'AssetFee')
```
---------
### HdxAssetId
 Native Asset ID
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'HdxAssetId')
```
---------
### HubAssetId
 Hub Asset ID
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'HubAssetId')
```
---------
### MaxInRatio
 Max fraction of asset reserve to sell in single transaction
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'MaxInRatio')
```
---------
### MaxOutRatio
 Max fraction of asset reserve to buy in single transaction
#### Value
```python
3
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'MaxOutRatio')
```
---------
### MinWithdrawalFee
 Minimum withdrawal fee
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'MinWithdrawalFee')
```
---------
### MinimumPoolLiquidity
 Minimum pool liquidity which can be added
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'MinimumPoolLiquidity')
```
---------
### MinimumTradingLimit
 Minimum trading limit
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'MinimumTradingLimit')
```
---------
### NFTCollectionId
 Non fungible class id
#### Value
```python
1337
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'NFTCollectionId')
```
---------
### ProtocolFee
 Protocol fee
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'ProtocolFee')
```
---------
### StableCoinAssetId
 Preferred stable Asset ID
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('Omnipool', 'StableCoinAssetId')
```
---------
## Errors

---------
### AssetAlreadyAdded
Asset is already in omnipool

---------
### AssetNotFound
Asset is not in omnipool

---------
### AssetNotRegistered
Asset is not registered in asset registry

---------
### AssetRefundNotAllowed
Asset is not allowed to be refunded.

---------
### AssetWeightCapExceeded
Asset weight cap has been exceeded.

---------
### BuyLimitNotReached
Minimum limit has not been reached during trade.

---------
### Forbidden
Signed account is not owner of position instance.

---------
### HubAssetUpdateError
LRNA update after trade results in positive value.

---------
### InsufficientBalance
Balance too low

---------
### InsufficientLiquidity
Provided liquidity is below minimum allowed limit

---------
### InsufficientShares
Insufficient shares in position

---------
### InsufficientTradingAmount
Traded amount is below minimum allowed limit

---------
### InvalidHubAssetTradableState
HJb Asset&\#x27;s trabable is only allowed to be SELL or BUY.

---------
### InvalidInitialAssetPrice
Invalid initial asset price. Price must be non-zero.

---------
### InvalidOraclePrice
Invalid oracle price - division by zero.

---------
### InvalidSharesAmount
Amount of shares provided cannot be 0.

---------
### InvalidWithdrawalFee
Failed to calculate withdrawal fee.

---------
### MaxInRatioExceeded
Max fraction of asset reserve to sell has been exceeded.

---------
### MaxOutRatioExceeded
Max fraction of asset reserve to buy has been exceeded.

---------
### MissingBalance
Adding token as protocol ( root ), token balance has not been updated prior to add token.

---------
### NoNativeAssetInPool
No native asset in the pool yet.

---------
### NoStableAssetInPool
No stable asset in the pool

---------
### NotAllowed
Asset is not allowed to be bought or sold

---------
### PositionNotFound
Position has not been found.

---------
### PositiveImbalance
Imbalance results in positive value.

---------
### PriceDifferenceTooHigh
Max allowed price difference has been exceeded.

---------
### SameAssetTradeNotAllowed
Sell or buy with same asset ids is not allowed.

---------
### SellLimitExceeded
Maximum limit has been exceeded during trade.

---------
### TVLCapExceeded
TVL cap has been exceeded

---------
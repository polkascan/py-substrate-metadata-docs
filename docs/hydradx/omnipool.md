
# Omnipool

---------
## Calls

---------
### add_liquidity
See [`Pallet::add_liquidity`].
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
See [`Pallet::add_token`].
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
See [`Pallet::buy`].
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
### refund_refused_asset
See [`Pallet::refund_refused_asset`].
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
See [`Pallet::remove_liquidity`].
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
### remove_token
See [`Pallet::remove_token`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| beneficiary | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'remove_token', {
    'asset_id': 'u32',
    'beneficiary': 'AccountId',
}
)
```

---------
### sacrifice_position
See [`Pallet::sacrifice_position`].
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
See [`Pallet::sell`].
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
See [`Pallet::set_asset_tradable_state`].
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
See [`Pallet::set_asset_weight_cap`].
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
### withdraw_protocol_liquidity
See [`Pallet::withdraw_protocol_liquidity`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| amount | `Balance` | 
| price | `(Balance, Balance)` | 
| dest | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Omnipool', 'withdraw_protocol_liquidity', {
    'amount': 'u128',
    'asset_id': 'u32',
    'dest': 'AccountId',
    'price': ('u128', 'u128'),
}
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
| hub_amount_in | `Balance` | ```u128```
| hub_amount_out | `Balance` | ```u128```
| asset_fee_amount | `Balance` | ```u128```
| protocol_fee_amount | `Balance` | ```u128```

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
Liquidity of an asset was removed from Omnipool.
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
LP Position was updated.
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
### ProtocolLiquidityRemoved
PRotocol Liquidity was removed from Omnipool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| asset_id | `T::AssetId` | ```u32```
| amount | `Balance` | ```u128```
| hub_amount | `Balance` | ```u128```
| shares_removed | `Balance` | ```u128```

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
| hub_amount_in | `Balance` | ```u128```
| hub_amount_out | `Balance` | ```u128```
| asset_fee_amount | `Balance` | ```u128```
| protocol_fee_amount | `Balance` | ```u128```

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
### TokenRemoved
An asset was removed from Omnipool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| asset_id | `T::AssetId` | ```u32```
| amount | `Balance` | ```u128```
| hub_withdrawn | `Balance` | ```u128```

---------
### TradableStateUpdated
Asset&\#x27;s tradable state has been updated.
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
## Constants

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
## Errors

---------
### AssetAlreadyAdded
Asset is already in omnipool

---------
### AssetNotFound
Asset is not in omnipool

---------
### AssetNotFrozen
Token cannot be removed from Omnipool because asset is not frozen.

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
Slippage protection - minimum limit has not been reached.

---------
### FeeOverdraft
More than allowed amount of fee has been transferred.

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
Hub asset is only allowed to be sold.

---------
### InvalidInitialAssetPrice
Invalid initial asset price.

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
Max fraction of asset to sell has been exceeded.

---------
### MaxOutRatioExceeded
Max fraction of asset to buy has been exceeded.

---------
### MissingBalance
Failed to add token to Omnipool due to insufficient initial liquidity.

---------
### NotAllowed
Asset is not allowed to be traded.

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
Slippage protection - maximum limit has been exceeded.

---------
### SharesRemaining
Token cannot be removed from Omnipool due to shares still owned by other users.

---------
### ZeroAmountOut
Calculated amount out from sell trade is zero.

---------
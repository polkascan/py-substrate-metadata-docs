
# AMM

---------
## Calls

---------
### add_liquidity
Allow users to add liquidity to a given pool

- `pool`: Currency pool, in which liquidity will be added
- `liquidity_amounts`: Liquidity amounts to be added in pool
- `minimum_amounts`: specifying its &quot;worst case&quot; ratio when pool already exists
#### Attributes
| Name | Type |
| -------- | -------- | 
| pair | `(AssetIdOf<T, I>, AssetIdOf<T, I>)` | 
| desired_amounts | `(BalanceOf<T, I>, BalanceOf<T, I>)` | 
| minimum_amounts | `(BalanceOf<T, I>, BalanceOf<T, I>)` | 

#### Python
```python
call = substrate.compose_call(
    'AMM', 'add_liquidity', {
    'desired_amounts': (
        'u128',
        'u128',
    ),
    'minimum_amounts': (
        'u128',
        'u128',
    ),
    'pair': ('u32', 'u32'),
}
)
```

---------
### create_pool
Create of a new pool, governance only

- `pool`: Currency pool, in which liquidity will be added
- `liquidity_amounts`: Liquidity amounts to be added in pool
- `lptoken_receiver`: Allocate any liquidity tokens to lptoken_receiver
- `lp_token_id`: Liquidity pool share representative token
#### Attributes
| Name | Type |
| -------- | -------- | 
| pair | `(AssetIdOf<T, I>, AssetIdOf<T, I>)` | 
| liquidity_amounts | `(BalanceOf<T, I>, BalanceOf<T, I>)` | 
| lptoken_receiver | `T::AccountId` | 
| lp_token_id | `AssetIdOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'AMM', 'create_pool', {
    'liquidity_amounts': (
        'u128',
        'u128',
    ),
    'lp_token_id': 'u32',
    'lptoken_receiver': 'AccountId',
    'pair': ('u32', 'u32'),
}
)
```

---------
### remove_liquidity
Allow users to remove liquidity from a given pool

- `pair`: Currency pool, in which liquidity will be removed
- `liquidity`: liquidity to be removed from user&\#x27;s liquidity
#### Attributes
| Name | Type |
| -------- | -------- | 
| pair | `(AssetIdOf<T, I>, AssetIdOf<T, I>)` | 
| liquidity | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'AMM', 'remove_liquidity', {
    'liquidity': 'u128',
    'pair': ('u32', 'u32'),
}
)
```

---------
### update_protocol_fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| protocol_fee | `Ratio` | 

#### Python
```python
call = substrate.compose_call(
    'AMM', 'update_protocol_fee', {'protocol_fee': 'u32'}
)
```

---------
### update_protocol_fee_receiver
#### Attributes
| Name | Type |
| -------- | -------- | 
| protocol_fee_receiver | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'AMM', 'update_protocol_fee_receiver', {'protocol_fee_receiver': 'AccountId'}
)
```

---------
## Events

---------
### LiquidityAdded
Add liquidity into pool
[sender, base_currency_id, quote_currency_id, base_amount_added, quote_amount_added, lp_token_id, new_base_amount, new_quote_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```

---------
### LiquidityRemoved
Remove liquidity from pool
[sender, base_currency_id, quote_currency_id, liquidity, base_amount_removed, quote_amount_removed, lp_token_id, new_base_amount, new_quote_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```

---------
### PoolCreated
A Pool has been created
[trader, currency_id_in, currency_id_out, lp_token_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `AssetIdOf<T, I>` | ```u32```

---------
### ProtocolFeeReceiverUpdated
Protocol fee receiver updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### ProtocolFeeUpdated
Protocol fee proportion of LP fee updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Ratio` | ```u32```

---------
### Traded
Trade using liquidity
[trader, currency_id_in, currency_id_out, amount_in, amount_out, lp_token_id, new_quote_amount, new_base_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```
| None | `AssetIdOf<T, I>` | ```u32```
| None | `BalanceOf<T, I>` | ```u128```
| None | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Pools
 A bag of liquidity composed by two different assets

#### Python
```python
result = substrate.query(
    'AMM', 'Pools', ['u32', 'u32']
)
```

#### Return value
```python
{
    'base_amount': 'u128',
    'base_amount_last': 'u128',
    'block_timestamp_last': 'u32',
    'lp_token_id': 'u32',
    'price_0_cumulative_last': 'u128',
    'price_1_cumulative_last': 'u128',
    'quote_amount': 'u128',
    'quote_amount_last': 'u128',
}
```
---------
### ProtocolFee
 How much the protocol is taking out of each trade.

#### Python
```python
result = substrate.query(
    'AMM', 'ProtocolFee', []
)
```

#### Return value
```python
'u32'
```
---------
### ProtocolFeeReceiver
 Who/where to send the protocol fees

#### Python
```python
result = substrate.query(
    'AMM', 'ProtocolFeeReceiver', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### GetNativeCurrencyId
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('AMM', 'GetNativeCurrencyId')
```
---------
### LockAccountId
#### Value
```python
'p8AxskWHQBViXqKEeX2nUCLmxNrzQrDLd75fcJzDbGTTVUbBz'
```
#### Python
```python
constant = substrate.get_constant('AMM', 'LockAccountId')
```
---------
### LpFee
 Defines the fees taken out of each trade and sent back to the AMM pool,
 typically 0.3%.
#### Value
```python
3000
```
#### Python
```python
constant = substrate.get_constant('AMM', 'LpFee')
```
---------
### MaxLengthRoute
 How many routes we support at most
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('AMM', 'MaxLengthRoute')
```
---------
### MinimumLiquidity
 Minimum amount of liquidty needed to init a new pool
 this amount is burned when the pool is created.

 It&#x27;s important that we include this value in order to
 prevent attacks where a bad actor will create and
 remove pools with malious intentions. By requiring
 a `MinimumLiquidity`, a pool cannot be removed since
 a small amount of tokens are locked forever when liquidity
 is first added.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('AMM', 'MinimumLiquidity')
```
---------
### PalletId
#### Value
```python
'0x7061722f616d6d70'
```
#### Python
```python
constant = substrate.get_constant('AMM', 'PalletId')
```
---------
## Errors

---------
### ConversionToU128Failed
Conversion failure to u128

---------
### IdenticalAssets
Identical assets

---------
### InsufficientAmountIn
Insufficient amount in

---------
### InsufficientAmountOut
Insufficient amount out

---------
### InsufficientLiquidity
Insufficient liquidity

---------
### InsufficientSupplyOut
Insufficient supply out.

---------
### LpTokenAlreadyExists
LP token has already been minted

---------
### NotAnIdealPrice
Not an ideal price ratio

---------
### PoolAlreadyExists
Pool does not exist

---------
### PoolDoesNotExist
Pool does not exist

---------
### ProtocolFeeReceiverNotSet
Protocol fee receiver not set

---------
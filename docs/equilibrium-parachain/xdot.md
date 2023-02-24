
# Xdot

---------
## Calls

---------
### burn
Burn liquidity tokens in exchange for base and fyToken or base only with `trade_to_base=true`
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| min_ratio | `(u32, u32)` | 
| max_ratio | `(u32, u32)` | 
| tokens_burned | `T::Balance` | 
| trade_to_base | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'burn', {
    'max_ratio': ('u32', 'u32'),
    'min_ratio': ('u32', 'u32'),
    'pool_id': 'u32',
    'tokens_burned': 'u128',
    'trade_to_base': 'bool',
}
)
```

---------
### buy_base
Buy base for xbase token
buy_base_amount - amount of base being bought that will be deposited to caller
max - maximum amount of xbase token that will be paid for the trade
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| base_to_buy | `T::Balance` | 
| xbase_to_sell | `T::Balance` | 
| max | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'buy_base', {
    'base_to_buy': 'u128',
    'max': 'u128',
    'pool_id': 'u32',
    'xbase_to_sell': 'u128',
}
)
```

---------
### buy_xbase
Buy xbase for base
xbase_to_buy - amount of xbase being bought that will be transfered to caller
max - maximum amount of base token that will be paid for the trade
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| base_to_sell | `T::Balance` | 
| xbase_to_buy | `T::Balance` | 
| max | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'buy_xbase', {
    'base_to_sell': 'u128',
    'max': 'u128',
    'pool_id': 'u32',
    'xbase_to_buy': 'u128',
}
)
```

---------
### change_initializer
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| account | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'change_initializer', {'account': (None, 'AccountId'), 'pool_id': 'u32'}
)
```

---------
### create_pool
Creates pool
- maturity: unix timestamp when maturity is coming
- ts_period: period in secs for ts coeff
#### Attributes
| Name | Type |
| -------- | -------- | 
| initializer | `T::AccountId` | 
| base_asset | `T::AssetId` | 
| xbase_asset | `T::AssetId` | 
| sell_base_fee_coeff | `T::XdotNumber` | 
| sell_xbase_fee_coeff | `T::XdotNumber` | 
| maturity | `u64` | 
| ts_period | `T::XdotNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'create_pool', {
    'base_asset': 'u64',
    'initializer': 'AccountId',
    'maturity': 'u64',
    'sell_base_fee_coeff': {
        'bits': 'i128',
    },
    'sell_xbase_fee_coeff': {
        'bits': 'i128',
    },
    'ts_period': {'bits': 'i128'},
    'xbase_asset': 'u64',
}
)
```

---------
### initialize
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| base_amount | `T::Balance` | 
| xbase_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'initialize', {
    'base_amount': 'u128',
    'pool_id': 'u32',
    'xbase_amount': 'u128',
}
)
```

---------
### mint
Mint liquidity tokens, with an optional internal trade to buy xbase tokens beforehand.
The amount of liquidity tokens is calculated from the amount of xbase tokens to buy from the pool,
plus the `xbase_in`. A proportional amount of base tokens need to be sent.
It fails if amount of base tokens for trade less than `base_in`
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| min_ratio | `(u32, u32)` | 
| max_ratio | `(u32, u32)` | 
| base_in | `T::Balance` | 
| xbase_in | `T::Balance` | 
| xbase_to_buy | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'mint', {
    'base_in': 'u128',
    'max_ratio': ('u32', 'u32'),
    'min_ratio': ('u32', 'u32'),
    'pool_id': 'u32',
    'xbase_in': 'u128',
    'xbase_to_buy': 'u128',
}
)
```

---------
### optimal_mint
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| base_in | `T::Balance` | 
| xbase_in | `T::Balance` | 
| lp_to_mint | `T::Balance` | 
| base_in_ratio_corridor | `Option<(u64, u64)>` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'optimal_mint', {
    'base_in': 'u128',
    'base_in_ratio_corridor': (
        None,
        ('u64', 'u64'),
    ),
    'lp_to_mint': 'u128',
    'pool_id': 'u32',
    'xbase_in': 'u128',
}
)
```

---------
### remove_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'remove_pool', {'pool_id': 'u32'}
)
```

---------
### sell_base
Sell base for xbase token.
min -  minimm accepted amount of xbase token
Returns amount of xbase token that will be transfered on caller account
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| base_to_sell | `T::Balance` | 
| min | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'sell_base', {
    'base_to_sell': 'u128',
    'min': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### sell_xbase
Sell xbase token for base
xbase_to_sell - amount of xbase token to sell for base
min - minimum accepted amount of base
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| xbase_to_sell | `T::Balance` | 
| min | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Xdot', 'sell_xbase', {
    'min': 'u128',
    'pool_id': 'u32',
    'xbase_to_sell': 'u128',
}
)
```

---------
## Events

---------
### Burned
LP tokens was burned, base and xbase was transfered from pool

Included values are:
- account identifier `T::AccountId`
- pool indentifier `PoolId`
- base asset amount `T::Balance`
- xbase asset amount `T::Balance`
- lp tokens amount `T::Balance`

\[who, pool_id, base_out, xbase_out, tokens_burned\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### BuyBase
Base was bought from pool in exchange for xbase

Included values are:
- account identifier `T::AccountId`
- pool indentifier `PoolId`
- base asset amount `T::Balance`
- xbase asset amount `T::Balance`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### BuyXBase
Xbase was bought from pool in exchange for base

Included values are:
- account identifier `T::AccountId`
- pool indentifier `PoolId`
- base asset amount `T::Balance`
- xbase asset amount `T::Balance`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### Minted
LP tokens was minted, base and xbase was transfered into pool

Included values are:
- account identifier `T::AccountId`
- pool indentifier `PoolId`
- base asset amount `T::Balance`
- xbase asset amount `T::Balance`
- lp tokens amount `T::Balance`

\[who, pool_id, base_in, xbase_in, tokens_minted\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### PoolCreated
Pool with specified id `PoolId` was created successfully.

Included values are:
- pool identifier `PoolId`
- LP asset
- Base asset
- XBase asset
- g1 coeff
- g2 coeff
- ts coeff
\[pool_id, base_asset, xbase_asset, g1, g2, ts\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u32```
| None | `T::AssetId` | ```u64```
| None | `T::AssetId` | ```u64```
| None | `T::AssetId` | ```u64```
| None | `T::XdotNumber` | ```{'bits': 'i128'}```
| None | `T::XdotNumber` | ```{'bits': 'i128'}```
| None | `T::XdotNumber` | ```{'bits': 'i128'}```

---------
### SaleBase
Base was sold into pool in exchange for xbase.

Included values are:
- account identifier `T::AccountId`
- pool indentifier `PoolId`
- base asset amount `T::Balance`
- xbase asset amount `T::Balance`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### SellXBase
Xbase was sold into pool in exchange for base

Included values are:
- account identifier `T::AccountId`
- pool indentifier `PoolId`
- base asset amount `T::Balance`
- xbase asset amount `T::Balance`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
## Storage functions

---------
### Initializer

#### Python
```python
result = substrate.query(
    'Xdot', 'Initializer', ['u32']
)
```

#### Return value
```python
'AccountId'
```
---------
### PoolCount
 Current number of pools (also ID for the next created pool)

#### Python
```python
result = substrate.query(
    'Xdot', 'PoolCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Pools

#### Python
```python
result = substrate.query(
    'Xdot', 'Pools', ['u32']
)
```

#### Return value
```python
{
    'account': 'AccountId',
    'base_asset': 'u64',
    'g1': {'bits': 'i128'},
    'g2': {'bits': 'i128'},
    'lp_total_supply': 'u128',
    'maturity': 'u64',
    'pool_asset': 'u64',
    'ts': {'bits': 'i128'},
    'xbase_asset': 'u64',
}
```
---------
## Errors

---------
### BalanceConvertOverflow

---------
### BuyBaseTooMuchForMax

---------
### BuyXbaseTooMuchForMax

---------
### CalcRatioMathError

---------
### CalcVirtualXbaseOverflow

---------
### ExternalAssetCheckFailed

---------
### ExternalError

---------
### InconsistentStorage

---------
### LPAssetNotCreated

---------
### MathError

---------
### MaturityInThePast

---------
### MaturityTooFarFromNow

---------
### MethodNotAllowed

---------
### NeedToInitialize

---------
### NoNeedToInitialize

---------
### NotAuthorized

---------
### PoolCountOverflow

---------
### PoolNotFound

---------
### SellBaseTooLowForMin

---------
### SellXBaseTooLowForMin

---------
### TooLowBaseIn

---------
### TooLowXbaseIn

---------
### TooMuchBaseIn

---------
### TooMuchXbaseOut

---------
### TsPeriodTooLarge

---------
### WrongMaxRatio

---------
### WrongMinRatio

---------
### XbaseBalanceTooLow

---------
### YieldMathBaseInForFyOut

---------
### YieldMathBaseOutForFyIn

---------
### YieldMathFyInForBaseOut

---------
### YieldMathFyOutForBaseIn

---------
### YieldMathInvariant

---------
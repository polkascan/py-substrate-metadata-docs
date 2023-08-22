
# CurveAmm

---------
## Calls

---------
### add_liquidity
Deposit coins into the pool
`amounts` - list of amounts of coins to deposit,
`min_mint_amount` - minimum amount of LP tokens to mint from the deposit.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| amounts | `Vec<T::Balance>` | 
| min_mint_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CurveAmm', 'add_liquidity', {
    'amounts': ['u128'],
    'min_mint_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### create_pool
Creates a pool, taking a creation fee from the caller
#### Attributes
| Name | Type |
| -------- | -------- | 
| assets | `Vec<T::AssetId>` | 
| amplification | `T::Number` | 
| fee | `Permill` | 
| admin_fee | `Permill` | 

#### Python
```python
call = substrate.compose_call(
    'CurveAmm', 'create_pool', {
    'admin_fee': 'u32',
    'amplification': 'u128',
    'assets': ['u64'],
    'fee': 'u32',
}
)
```

---------
### exchange
Perform an exchange between two coins.
`i` - index value of the coin to send,
`j` - index value of the coin to receive,
`dx` - amount of `i` being exchanged,
`min_dy` - minimum amount of `j` to receive.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| i | `PoolTokenIndex` | 
| j | `PoolTokenIndex` | 
| dx | `T::Balance` | 
| min_dy | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CurveAmm', 'exchange', {
    'dx': 'u128',
    'i': 'u32',
    'j': 'u32',
    'min_dy': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### remove_liquidity
Withdraw coins from the pool.
Withdrawal amount are based on current deposit ratios.
`amount` - quantity of LP tokens to burn in the withdrawal,
`min_amounts` - minimum amounts of underlying coins to receive.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| amount | `T::Balance` | 
| min_amounts | `Vec<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'CurveAmm', 'remove_liquidity', {
    'amount': 'u128',
    'min_amounts': ['u128'],
    'pool_id': 'u32',
}
)
```

---------
### remove_liquidity_imbalance
Withdraw coins from the pool in an imbalanced amount.
`amounts` - list of amounts of underlying coins to withdraw,
`max_burn_amount` - maximum amount of LP token to burn in the withdrawal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| amounts | `Vec<T::Balance>` | 
| max_burn_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CurveAmm', 'remove_liquidity_imbalance', {
    'amounts': ['u128'],
    'max_burn_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### remove_liquidity_one_coin
Withdraw a single coin from the pool.
`token_amount` - amount of LP tokens to burn in the withdrawal,
`i` - index value of the coin to withdraw,
`min_amount` - minimum amount of coin to receive.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| token_amount | `T::Balance` | 
| i | `PoolTokenIndex` | 
| min_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CurveAmm', 'remove_liquidity_one_coin', {
    'i': 'u32',
    'min_amount': 'u128',
    'pool_id': 'u32',
    'token_amount': 'u128',
}
)
```

---------
### set_enable_state
Set enable pool state.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 
| is_enabled | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'CurveAmm', 'set_enable_state', {
    'is_enabled': 'bool',
    'pool_id': 'u32',
}
)
```

---------
### withdraw_admin_fees
Withdraw admin fee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'CurveAmm', 'withdraw_admin_fees', {'pool_id': 'u32'}
)
```

---------
## Events

---------
### AddLiquidity
Liquidity added into the pool `PoolId` by `T::AccountId`.

Included values are:
- account identifier `T::AccountId`
- pool identifier `PoolId`
- added token amounts `Vec&lt;T::Balance&gt;`
- charged fees `Vec&lt;T::Balance&gt;`
- actual invariant `T::Balance`
- actual token supply `T::Balance`
- minted amount `T::Balance`

\[who, pool_id, token_amounts, fees, invariant, token_supply, mint_amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `Vec<T::Balance>` | ```['u128']```
| None | `Vec<T::Balance>` | ```['u128']```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### CreatePool
Pool with specified id `PoolId` was created successfully by `T::AccountId`.

Included values are:
- account identifier `T::AccountId`
- pool identifier `PoolId`

\[who, pool_id\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```

---------
### PoolEnableStateChanged
Pool with specified id `PoolId` changed enable state `bool`.

Included values are:
- pool identifier `PoolId`
- pool is enabled `bool`

\[pool_id, is_enabled\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PoolId` | ```u32```
| None | `bool` | ```bool```

---------
### RemoveLiquidity
Liquidity removed from pool `PoolId` by `T::AccountId` in balanced way.

Included values are:
- account identifier `T::AccountId`
- pool identifier `PoolId`
- removed token amounts `Vec&lt;T::Balance&gt;`
- charged fees `Vec&lt;T::Balance&gt;`
- actual token supply `T::Balance`
- quantity of LP tokens to burn in the withdrawal `T::Balance`

\[who, pool_id, token_amounts, fees, token_supply, burn_amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `Vec<T::Balance>` | ```['u128']```
| None | `Vec<T::Balance>` | ```['u128']```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### RemoveLiquidityImbalance
Liquidity removed from pool `PoolId` by `T::AccountId` in imbalanced way.

Included values are:
- account identifier `T::AccountId`
- pool identifier `PoolId`
- removed token amounts `Vec&lt;T::Balance&gt;`
- charged fees `Vec&lt;T::Balance&gt;`
- actual invariant `T::Balance`
- actual token supply `T::Balance`
- removed LP token amount `T::Balance`

\[who, pool_id, token_amounts, fees, invariant, token_supply, burn_amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `Vec<T::Balance>` | ```['u128']```
| None | `Vec<T::Balance>` | ```['u128']```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### RemoveLiquidityOne
Liquidity removed from pool `PoolId` only for one token.

Included values are:
- account identifier `T::AccountId`
- pool identifier `PoolId`
- removed token amount `T::Balance`
- received token index `PoolTokenIndex`
- received token amount `T::Balance`
- actual token supply `T::Balance`
- charged fee `T::Balance`

\[who, pool_id, burn_amount, received_token, received_amount, token_supply, fee\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `T::Balance` | ```u128```
| None | `PoolTokenIndex` | ```u32```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### TokenExchange
Token exchange happened.

Included values are:
- account identifier `T::AccountId`
- pool identifier `PoolId`
- index of sent token `PoolTokenIndex`
- amount of sent token `T::Balance`
- index of received token `PoolTokenIndex`
- amount of received token `T::Balance`
- charged fee `T::Balance`

\[who, pool_id, sent_token_index, sent_amount, received_token_index, received_amount, fee\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `PoolTokenIndex` | ```u32```
| None | `T::Balance` | ```u128```
| None | `PoolTokenIndex` | ```u32```
| None | `T::Balance` | ```u128```
| None | `T::Balance` | ```u128```

---------
### WithdrawAdminFees
Withdraw admin fees `Vec&lt;T::Balance&gt;` from pool `PoolId` by user `T::AccountId`

Included values are:
- account identifier `T::AccountId`
- pool identifier `PoolId`
- withdrew admin fees `Vec&lt;T::Balance&gt;`

[who, pool_id, admin_fees]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `PoolId` | ```u32```
| None | `Vec<T::Balance>` | ```['u128']```

---------
## Storage functions

---------
### PoolCount
 Current number of pools (also ID for the next created pool)

#### Python
```python
result = substrate.query(
    'CurveAmm', 'PoolCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Pools
 Existing pools

#### Python
```python
result = substrate.query(
    'CurveAmm', 'Pools', ['u32']
)
```

#### Return value
```python
{
    'admin_fee': 'u32',
    'amplification': 'u128',
    'assets': ['u64'],
    'balances': ['u128'],
    'fee': 'u32',
    'is_enabled': 'bool',
    'owner': 'AccountId',
    'pool_asset': 'u64',
    'total_balances': ['u128'],
}
```
---------
## Constants

---------
### CreationFee
 Anti ddos fee for pool creation
#### Value
```python
100000000000000
```
#### Python
```python
constant = substrate.get_constant('CurveAmm', 'CreationFee')
```
---------
### PalletId
 Module account
#### Value
```python
'0x65712f637276616d'
```
#### Python
```python
constant = substrate.get_constant('CurveAmm', 'PalletId')
```
---------
## Errors

---------
### AssetNotCreated
Could not create new asset

---------
### Disabled
User can call only removeLiquidity method for pool

---------
### DuplicateAssets
Some provided assets are not unique

---------
### ExternalAssetCheckFailed
The `AssetChecker` can use this error in case it can&\#x27;t provide better error

---------
### InconsistentStorage
Values in the storage are inconsistent

---------
### IndexOutOfRange
Specified index is out of range

---------
### InsufficientFunds
Source does not have required amount of coins to complete operation

---------
### Math
Error occurred while performing math calculations

---------
### NotEnoughAssets
Not enough assets provided

---------
### PoolNotFound
Pool with specified id is not found

---------
### RequiredAmountNotReached
Required amount of some token did not reached during adding or removing liquidity

---------
### WrongAssetAmount
Specified asset amount is wrong

---------
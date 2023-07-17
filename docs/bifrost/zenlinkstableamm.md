
# ZenlinkStableAMM

---------
## Calls

---------
### add_liquidity
Supply amounts of currencies to the pool.

\# Argument

- `pool_id`: The id of pool.
- `amounts`: Supply amounts of currencies.
- `min_mint_amount`: The min amount of lp currency get.
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| amounts | `Vec<Balance>` | 
| min_mint_amount | `Balance` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'add_liquidity', {
    'amounts': ['u128'],
    'deadline': 'u32',
    'min_mint_amount': 'u128',
    'pool_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### add_pool_and_base_pool_liquidity
Supply amounts of currencies to the pool which contains the lp currency of the base
pool.

\# Argument

- `pool_id`: The id of pool.
- `base_pool_id`: The id of base pool.
- `meta_amounts`: Supply amounts of currencies to pool. The last element must be zero.
- `base_amounts`: Supply amounts of currencies to base pool.
- `min_to_mint`: The min amount of pool lp currency get.
- `deadline`: Height of the cutoff block of this transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| base_pool_id | `T::PoolId` | 
| meta_amounts | `Vec<Balance>` | 
| base_amounts | `Vec<Balance>` | 
| min_to_mint | `Balance` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'add_pool_and_base_pool_liquidity', {
    'base_amounts': ['u128'],
    'base_pool_id': 'u32',
    'deadline': 'u32',
    'meta_amounts': ['u128'],
    'min_to_mint': 'u128',
    'pool_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### create_base_pool
Create a stable amm pool.

Only admin can create pool.

\# Argument

- `currency_ids`: The currencies will be join the created pool.
- `currency_decimals`: The currencies corresponding decimals.
- `lp_currency_id`: The specify lp currency id of the created pool.
- `a`: The initial A of created pool.
- `fee`: The swap fee of created pool.
- `admin_fee`: The admin fee of created pool.
- `admin_fee_receiver`: The admin fee receiver of created pool.
- `lp_currency_symbol`: The symbol of created pool lp currency.
- `lp_currency_decimal`: The decimal of created pool lp currency.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_ids | `Vec<T::CurrencyId>` | 
| currency_decimals | `Vec<u32>` | 
| a | `Number` | 
| fee | `Number` | 
| admin_fee | `Number` | 
| admin_fee_receiver | `T::AccountId` | 
| lp_currency_symbol | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'create_base_pool', {
    'a': 'u128',
    'admin_fee': 'u128',
    'admin_fee_receiver': 'AccountId',
    'currency_decimals': ['u32'],
    'currency_ids': [
        {
            'ForeignAsset': 'u32',
            'LPToken': (
                (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'u8',
                (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'u8',
            ),
            'Native': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'Stable': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'StableLpToken': 'u32',
            'Token': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'Token2': 'u8',
            'VSBond': (
                (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'u32',
                'u32',
                'u32',
            ),
            'VSBond2': (
                'u8',
                'u32',
                'u32',
                'u32',
            ),
            'VSToken': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'VSToken2': 'u8',
            'VToken': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'VToken2': 'u8',
        },
    ],
    'fee': 'u128',
    'lp_currency_symbol': 'Bytes',
}
)
```

---------
### create_meta_pool
Create a stable amm meta pool.

Only admin can create pool.

\# Argument

- `currency_ids`: The currencies will be join the created pool.
- `currency_decimals`: The currencies corresponding decimals.
- `lp_currency_id`: The specify lp currency id of the created pool.
- `a`: The initial A of created pool.
- `fee`: The swap fee of created pool.
- `admin_fee`: The admin fee of created pool.
- `admin_fee_receiver`: The admin fee receiver of created pool.
- `lp_currency_symbol`: The symbol of created pool lp currency.
- `lp_currency_decimal`: The decimal of created pool lp currency.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_ids | `Vec<T::CurrencyId>` | 
| currency_decimals | `Vec<u32>` | 
| a | `Number` | 
| fee | `Number` | 
| admin_fee | `Number` | 
| admin_fee_receiver | `T::AccountId` | 
| lp_currency_symbol | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'create_meta_pool', {
    'a': 'u128',
    'admin_fee': 'u128',
    'admin_fee_receiver': 'AccountId',
    'currency_decimals': ['u32'],
    'currency_ids': [
        {
            'ForeignAsset': 'u32',
            'LPToken': (
                (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'u8',
                (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'u8',
            ),
            'Native': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'Stable': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'StableLpToken': 'u32',
            'Token': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'Token2': 'u8',
            'VSBond': (
                (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'u32',
                'u32',
                'u32',
            ),
            'VSBond2': (
                'u8',
                'u32',
                'u32',
                'u32',
            ),
            'VSToken': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'VSToken2': 'u8',
            'VToken': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'VToken2': 'u8',
        },
    ],
    'fee': 'u128',
    'lp_currency_symbol': 'Bytes',
}
)
```

---------
### ramp_a
Start ramping up or down A parameter towards given future_a and future_a_time

Only called by admin.
Checks if the change is too rapid, and commits the new A value only when it falls under
the limit range.

\# Argument

- `pool_id`: The id of pool.
- `future_a`: The new A to ramp towards.
- `future_a_time`: Timestamp when the new A should be reached
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| future_a | `Number` | 
| future_a_time | `Number` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'ramp_a', {
    'future_a': 'u128',
    'future_a_time': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### remove_liquidity
Remove liquidity from a pool.

\# Argument

- `pool_id`: The id of pool.
- `lp_amount`: The amounts of lp currency.
- `min_amounts`: The min amounts of pool&\#x27;s currencies to get.
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| poo_id | `T::PoolId` | 
| lp_amount | `Balance` | 
| min_amounts | `Vec<Balance>` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'remove_liquidity', {
    'deadline': 'u32',
    'lp_amount': 'u128',
    'min_amounts': ['u128'],
    'poo_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### remove_liquidity_imbalance
Remove liquidity from a pool to the specify amounts of currencies.

\# Argument

- `pool_id`: The id of pool.
- `amounts`: The specify amounts of receive currencies.
- `max_burn_amount`: The max amount of burned lp currency.
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| amounts | `Vec<Balance>` | 
| max_burn_amount | `Balance` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'remove_liquidity_imbalance', {
    'amounts': ['u128'],
    'deadline': 'u32',
    'max_burn_amount': 'u128',
    'pool_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### remove_liquidity_one_currency
Remove liquidity from a pool to get one currency.

\# Argument

- `pool_id`: The id of pool.
- `lp_amount`: The amounts of lp currency.
- `index`: The index of receive currency.
- `min_amount`: The min amounts of received currency;
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| poo_id | `T::PoolId` | 
| lp_amount | `Balance` | 
| index | `u32` | 
| min_amount | `Balance` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'remove_liquidity_one_currency', {
    'deadline': 'u32',
    'index': 'u32',
    'lp_amount': 'u128',
    'min_amount': 'u128',
    'poo_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### remove_pool_and_base_pool_liquidity
Remove liquidity from a pool which contains the lp currency of the base pool.

\# Argument

- `pool_id`: The id of pool.
- `base_pool_id`: The id of base pool.
- `amount`: The amounts of lp currency to burn.
- `min_amounts_meta`: The min amounts of pool&\#x27;s currencies to get.
- `min_amounts_base`: The min amounts of basic pool&\#x27;s currencies to get.
- `deadline`: Height of the cutoff block of this transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| base_pool_id | `T::PoolId` | 
| amount | `Balance` | 
| min_amounts_meta | `Vec<Balance>` | 
| min_amounts_base | `Vec<Balance>` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'remove_pool_and_base_pool_liquidity', {
    'amount': 'u128',
    'base_pool_id': 'u32',
    'deadline': 'u32',
    'min_amounts_base': ['u128'],
    'min_amounts_meta': ['u128'],
    'pool_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### remove_pool_and_base_pool_liquidity_one_currency
Remove liquidity from a pool which contains the lp currency of the base pool
to get one currency.

\# Argument

- `pool_id`: The id of pool.
- `base_pool_id`: The id of base pool.
- `amount`: The amounts of lp currency to burn.
- `i`: The index of target currency in basic pool.
- `min_amount`: The min amounts of received currency.
- `deadline`: Height of the cutoff block of this transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| base_pool_id | `T::PoolId` | 
| amount | `Balance` | 
| i | `u32` | 
| min_amount | `Balance` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'remove_pool_and_base_pool_liquidity_one_currency', {
    'amount': 'u128',
    'base_pool_id': 'u32',
    'deadline': 'u32',
    'i': 'u32',
    'min_amount': 'u128',
    'pool_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### set_admin_fee
Update admin fee of the pool.

Only called by admin.

\# Argument

- `pool_id`: The id of pool.
- `new_admin_fee`: The new admin fee of this pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| new_admin_fee | `Number` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'set_admin_fee', {
    'new_admin_fee': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### set_swap_fee
Update fee of the pool.

Only called by admin.

\# Argument

- `pool_id`: The id of pool.
- `new_swap_fee`: The new swap fee of this pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| new_swap_fee | `Number` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'set_swap_fee', {
    'new_swap_fee': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### stop_ramp_a
Stop ramping A parameter.

Only called by admin.

\# Argument

- `pool_id`: The id of pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'stop_ramp_a', {'pool_id': 'u32'}
)
```

---------
### swap
Swap a amounts of currencies to get other.

\# Argument

- `pool_id`: The id of pool.
- `from_index`: The index of swap currency id.
- `to_index`: The index of receive currency id.
- `in_amount`: The amounts of currencies swap.
- `min_mint_amount`: The min amount of receive currency.
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| poo_id | `T::PoolId` | 
| from_index | `u32` | 
| to_index | `u32` | 
| in_amount | `Balance` | 
| min_out_amount | `Balance` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'swap', {
    'deadline': 'u32',
    'from_index': 'u32',
    'in_amount': 'u128',
    'min_out_amount': 'u128',
    'poo_id': 'u32',
    'to': 'AccountId',
    'to_index': 'u32',
}
)
```

---------
### swap_meta_pool_underlying
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| in_index | `u32` | 
| out_index | `u32` | 
| dx | `Balance` | 
| min_dy | `Balance` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'swap_meta_pool_underlying', {
    'deadline': 'u32',
    'dx': 'u128',
    'in_index': 'u32',
    'min_dy': 'u128',
    'out_index': 'u32',
    'pool_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### swap_pool_from_base
Swap the currency from basic pool to get amounts of other currency in pool.
to get one currency.

\# Argument

- `pool_id`: The id of pool.
- `base_pool_id`: The id of base pool.
- `in_index`: The index of swap currency in basic pool.
- `out_index`: The index of target currency in pool.
- `dx`: The amounts of swap currency.
- `min_dy`: The min amounts of target currency.
- `deadline`: Height of the cutoff block of this transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| base_pool_id | `T::PoolId` | 
| in_index | `u32` | 
| out_index | `u32` | 
| dx | `Balance` | 
| min_dy | `Balance` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'swap_pool_from_base', {
    'base_pool_id': 'u32',
    'deadline': 'u32',
    'dx': 'u128',
    'in_index': 'u32',
    'min_dy': 'u128',
    'out_index': 'u32',
    'pool_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### swap_pool_to_base
Swap the currency from pool to get amounts of other currency in basic pool.
to get one currency.

\# Argument

- `pool_id`: The id of pool.
- `base_pool_id`: The id of base pool.
- `in_index`: The index of swap currency in basic pool.
- `out_index`: The index of target currency in pool.
- `dx`: The amounts of swap currency.
- `min_dy`: The min amounts of target currency.
- `deadline`: Height of the cutoff block of this transaction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| base_pool_id | `T::PoolId` | 
| in_index | `u32` | 
| out_index | `u32` | 
| dx | `Balance` | 
| min_dy | `Balance` | 
| to | `T::AccountId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'swap_pool_to_base', {
    'base_pool_id': 'u32',
    'deadline': 'u32',
    'dx': 'u128',
    'in_index': 'u32',
    'min_dy': 'u128',
    'out_index': 'u32',
    'pool_id': 'u32',
    'to': 'AccountId',
}
)
```

---------
### update_fee_receiver
Update admin fee receiver of the pool.

Only called by admin.

\# Argument

- `pool_id`: The id of pool.
- `fee_receiver`: The new admin fee receiver of this pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| fee_receiver | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'update_fee_receiver', {
    'fee_receiver': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'pool_id': 'u32',
}
)
```

---------
### withdraw_admin_fee
Withdraw the admin fee from pool to admin fee receiver.

Can called by anyone.

\# Argument

- `pool_id`: The id of pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'ZenlinkStableAMM', 'withdraw_admin_fee', {'pool_id': 'u32'}
)
```

---------
## Events

---------
### AddLiquidity
Supply some liquidity to a pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| supply_amounts | `Vec<Balance>` | ```['u128']```
| fees | `Vec<Balance>` | ```['u128']```
| new_d | `Balance` | ```u128```
| mint_amount | `Balance` | ```u128```

---------
### CollectProtocolFee
A pool&\#x27;s admin fee was collected.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| currency_id | `T::CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| fee_amount | `Balance` | ```u128```

---------
### CreatePool
A pool was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| currency_ids | `Vec<T::CurrencyId>` | ```[{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}]```
| lp_currency_id | `T::CurrencyId` | ```{'Native': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Token': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'Stable': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSToken': ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'VSBond': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u32', 'u32', 'u32'), 'LPToken': (('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8', ('ASG', 'BNC', 'KUSD', 'DOT', 'KSM', 'ETH', 'KAR', 'ZLK', 'PHA', 'RMRK', 'MOVR'), 'u8'), 'ForeignAsset': 'u32', 'Token2': 'u8', 'VToken2': 'u8', 'VSToken2': 'u8', 'VSBond2': ('u8', 'u32', 'u32', 'u32'), 'StableLpToken': 'u32'}```
| a | `Number` | ```u128```
| account | `T::AccountId` | ```AccountId```
| admin_fee_receiver | `T::AccountId` | ```AccountId```

---------
### CurrencyExchange
Swap a amounts of currency to get other.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| in_index | `u32` | ```u32```
| in_amount | `Balance` | ```u128```
| out_index | `u32` | ```u32```
| out_amount | `Balance` | ```u128```

---------
### CurrencyExchangeUnderlying
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| account | `T::AccountId` | ```AccountId```
| in_amount | `Balance` | ```u128```
| out_amount | `Balance` | ```u128```
| currency_index_from | `u32` | ```u32```
| currency_index_to | `u32` | ```u32```
| to | `T::AccountId` | ```AccountId```

---------
### NewAdminFee
A pool&\#x27;s admin fee parameters was updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| new_admin_fee | `Number` | ```u128```

---------
### NewSwapFee
A pool&\#x27;s swap fee parameters was updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| new_swap_fee | `Number` | ```u128```

---------
### RampA
A pool&\#x27;s &\#x27;A&\#x27; was ramped.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| initial_a_precise | `Number` | ```u128```
| future_a_precise | `Number` | ```u128```
| now | `Number` | ```u128```
| future_a_time | `Number` | ```u128```

---------
### RemoveLiquidity
Remove some liquidity from a pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amounts | `Vec<Balance>` | ```['u128']```
| fees | `Vec<Balance>` | ```['u128']```
| new_total_supply | `Balance` | ```u128```

---------
### RemoveLiquidityImbalance
Remove liquidity from a pool with specify the amounts of currencies to be obtained.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| amounts | `Vec<Balance>` | ```['u128']```
| fees | `Vec<Balance>` | ```['u128']```
| new_d | `Balance` | ```u128```
| new_total_supply | `Balance` | ```u128```

---------
### RemoveLiquidityOneCurrency
Remove some liquidity from a pool to get only one currency.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| who | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| out_index | `u32` | ```u32```
| burn_amount | `Balance` | ```u128```
| out_amount | `Balance` | ```u128```

---------
### StopRampA
A pool&\#x27;s ramping A was stopped.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| current_a | `Number` | ```u128```
| now | `Number` | ```u128```

---------
### UpdateAdminFeeReceiver
A pool&\#x27;s admin_fee_receiver was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u32```
| admin_fee_receiver | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### LpCurrencies
 The pool id corresponding to lp currency

#### Python
```python
result = substrate.query(
    'ZenlinkStableAMM', 'LpCurrencies', [
    {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
]
)
```

#### Return value
```python
'u32'
```
---------
### NextPoolId
 The id of next pool

#### Python
```python
result = substrate.query(
    'ZenlinkStableAMM', 'NextPoolId', []
)
```

#### Return value
```python
'u32'
```
---------
### Pools
 Info of a pool.

#### Python
```python
result = substrate.query(
    'ZenlinkStableAMM', 'Pools', ['u32']
)
```

#### Return value
```python
{
    'Base': {
        'account': 'AccountId',
        'admin_fee': 'u128',
        'admin_fee_receiver': 'AccountId',
        'balances': ['u128'],
        'currency_ids': [
            {
                'ForeignAsset': 'u32',
                'LPToken': ('scale_info::253', 'u8', 'scale_info::253', 'u8'),
                'Native': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'Stable': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'Token2': 'u8',
                'VSBond': ('scale_info::253', 'u32', 'u32', 'u32'),
                'VSBond2': ('u8', 'u32', 'u32', 'u32'),
                'VSToken': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'VSToken2': 'u8',
                'VToken': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'VToken2': 'u8',
            },
        ],
        'fee': 'u128',
        'future_a': 'u128',
        'future_a_time': 'u128',
        'initial_a': 'u128',
        'initial_a_time': 'u128',
        'lp_currency_decimal': 'u8',
        'lp_currency_id': {
            'ForeignAsset': 'u32',
            'LPToken': (
                (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'u8',
                (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'u8',
            ),
            'Native': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'Stable': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'StableLpToken': 'u32',
            'Token': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'Token2': 'u8',
            'VSBond': (
                (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'u32',
                'u32',
                'u32',
            ),
            'VSBond2': ('u8', 'u32', 'u32', 'u32'),
            'VSToken': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'VSToken2': 'u8',
            'VToken': (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'VToken2': 'u8',
        },
        'lp_currency_symbol': 'Bytes',
        'token_multipliers': ['u128'],
    },
    'Meta': {
        'base_cache_last_updated': 'u64',
        'base_currencies': [
            {
                'ForeignAsset': 'u32',
                'LPToken': ('scale_info::253', 'u8', 'scale_info::253', 'u8'),
                'Native': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'Stable': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'Token2': 'u8',
                'VSBond': ('scale_info::253', 'u32', 'u32', 'u32'),
                'VSBond2': ('u8', 'u32', 'u32', 'u32'),
                'VSToken': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'VSToken2': 'u8',
                'VToken': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'VToken2': 'u8',
            },
        ],
        'base_pool_id': 'u32',
        'base_virtual_price': 'u128',
        'info': {
            'account': 'AccountId',
            'admin_fee': 'u128',
            'admin_fee_receiver': 'AccountId',
            'balances': ['u128'],
            'currency_ids': [
                {
                    'ForeignAsset': 'u32',
                    'LPToken': (
                        'scale_info::253',
                        'u8',
                        'scale_info::253',
                        'u8',
                    ),
                    'Native': 'scale_info::253',
                    'Stable': 'scale_info::253',
                    'StableLpToken': 'u32',
                    'Token': 'scale_info::253',
                    'Token2': 'u8',
                    'VSBond': ('scale_info::253', 'u32', 'u32', 'u32'),
                    'VSBond2': ('u8', 'u32', 'u32', 'u32'),
                    'VSToken': 'scale_info::253',
                    'VSToken2': 'u8',
                    'VToken': 'scale_info::253',
                    'VToken2': 'u8',
                },
            ],
            'fee': 'u128',
            'future_a': 'u128',
            'future_a_time': 'u128',
            'initial_a': 'u128',
            'initial_a_time': 'u128',
            'lp_currency_decimal': 'u8',
            'lp_currency_id': {
                'ForeignAsset': 'u32',
                'LPToken': ('scale_info::253', 'u8', 'scale_info::253', 'u8'),
                'Native': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'Stable': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'Token2': 'u8',
                'VSBond': ('scale_info::253', 'u32', 'u32', 'u32'),
                'VSBond2': ('u8', 'u32', 'u32', 'u32'),
                'VSToken': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'VSToken2': 'u8',
                'VToken': (
                    'ASG',
                    'BNC',
                    'KUSD',
                    'DOT',
                    'KSM',
                    'ETH',
                    'KAR',
                    'ZLK',
                    'PHA',
                    'RMRK',
                    'MOVR',
                ),
                'VToken2': 'u8',
            },
            'lp_currency_symbol': 'Bytes',
            'token_multipliers': ['u128'],
        },
    },
}
```
---------
## Constants

---------
### PalletId
 This pallet ID.
#### Value
```python
'0x62662f7374616d6d'
```
#### Python
```python
constant = substrate.get_constant('ZenlinkStableAMM', 'PalletId')
```
---------
### PoolCurrencySymbolLimit
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('ZenlinkStableAMM', 'PoolCurrencySymbolLimit')
```
---------
## Errors

---------
### AlreadyStoppedRampA
The ramping A of this pool is already stopped.

---------
### AmountSlippage
Slippage is too large.

---------
### Arithmetic
The error generate by some arithmetic function.

---------
### BadPoolCurrencySymbol
The symbol of created pool maybe exceed length limit.

---------
### CheckDFailed
The new d below then older.

---------
### CurrencyIndexOutRange
The index of currency id bigger the length of pool&\#x27;s currencies;

---------
### Deadline
The call already expired.

---------
### ExceedMaxA
The A parameter exceed MAX_A when create pool.

---------
### ExceedMaxAChange
Forbid change A of a pool bigger than MAX_A.

---------
### ExceedMaxAdminFee
The admin fee parameter exceeds MAX_ADMIN_FEE when create pool.

---------
### ExceedMaxFee
The fee parameter exceeds MAX_SWAP_FEE when create pool.

---------
### ExceedThreshold
The setting value exceed threshold.

---------
### InsufficientLpReserve
The pool does not have enough lp currency.

---------
### InsufficientReserve
The pool does not have enough currencies.

---------
### InsufficientSupply
The caller does not have enough currencies.

---------
### InvalidBasePool
The base pool mismatch this pool.

---------
### InvalidBasePoolLpCurrency
The base pool lp currency is invalid when create meta pool.

---------
### InvalidCurrencyDecimal
The decimal of currency is invalid when create pool.

---------
### InvalidLpCurrency
The currency id can&\#x27;t become the lp currency id of stable amm pool.

---------
### InvalidPoolId
The pool id is invalid.

---------
### InvalidPooledCurrency
The currency id can&\#x27;t join stable amm pool.

---------
### InvalidTransaction
The transaction change nothing.

---------
### LpCurrencyAlreadyUsed
The lp currency id is already used when create pool.

---------
### MinRampTime
The value of feature_a_time is too small.

---------
### MismatchParameter
The parameters of a call are contradictory.

---------
### RampADelay
The A of this pool is already ramped in current period.

---------
### RequireAllCurrencies
Require all currencies of this pool when first supply.

---------
### SwapSameCurrency
Forbid swap same currency.

---------
### TokenIndexOutOfRange
The token index out of range.

---------
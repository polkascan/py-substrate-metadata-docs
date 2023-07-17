
# StableAsset

---------
## Calls

---------
### create_pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_asset | `T::AssetId` | 
| assets | `Vec<T::AssetId>` | 
| precisions | `Vec<T::AtLeast64BitUnsigned>` | 
| mint_fee | `T::AtLeast64BitUnsigned` | 
| swap_fee | `T::AtLeast64BitUnsigned` | 
| redeem_fee | `T::AtLeast64BitUnsigned` | 
| initial_a | `T::AtLeast64BitUnsigned` | 
| fee_recipient | `T::AccountId` | 
| yield_recipient | `T::AccountId` | 
| precision | `T::AtLeast64BitUnsigned` | 

#### Python
```python
call = substrate.compose_call(
    'StableAsset', 'create_pool', {
    'assets': [
        {
            'DexShare': (
                {
                    'Erc20': '[u8; 20]',
                    'ForeignAsset': 'u16',
                    'LiquidCrowdloan': 'u32',
                    'StableAssetPoolToken': 'u32',
                    'Token': (
                        'ACA',
                        'AUSD',
                        'DOT',
                        'LDOT',
                        'TAP',
                        'KAR',
                        'KUSD',
                        'KSM',
                        'LKSM',
                        'TAI',
                        'BNC',
                        'VSKSM',
                        'PHA',
                        'KINT',
                        'KBTC',
                    ),
                },
                {
                    'Erc20': '[u8; 20]',
                    'ForeignAsset': 'u16',
                    'LiquidCrowdloan': 'u32',
                    'StableAssetPoolToken': 'u32',
                    'Token': (
                        'ACA',
                        'AUSD',
                        'DOT',
                        'LDOT',
                        'TAP',
                        'KAR',
                        'KUSD',
                        'KSM',
                        'LKSM',
                        'TAI',
                        'BNC',
                        'VSKSM',
                        'PHA',
                        'KINT',
                        'KBTC',
                    ),
                },
            ),
            'Erc20': '[u8; 20]',
            'ForeignAsset': 'u16',
            'LiquidCrowdloan': 'u32',
            'StableAssetPoolToken': 'u32',
            'Token': (
                'ACA',
                'AUSD',
                'DOT',
                'LDOT',
                'TAP',
                'KAR',
                'KUSD',
                'KSM',
                'LKSM',
                'TAI',
                'BNC',
                'VSKSM',
                'PHA',
                'KINT',
                'KBTC',
            ),
        },
    ],
    'fee_recipient': 'AccountId',
    'initial_a': 'u128',
    'mint_fee': 'u128',
    'pool_asset': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'precision': 'u128',
    'precisions': ['u128'],
    'redeem_fee': 'u128',
    'swap_fee': 'u128',
    'yield_recipient': 'AccountId',
}
)
```

---------
### mint
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| amounts | `Vec<T::Balance>` | 
| min_mint_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'StableAsset', 'mint', {
    'amounts': ['u128'],
    'min_mint_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### modify_a
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| a | `T::AtLeast64BitUnsigned` | 
| future_a_block | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'StableAsset', 'modify_a', {
    'a': 'u128',
    'future_a_block': 'u32',
    'pool_id': 'u32',
}
)
```

---------
### modify_fees
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| mint_fee | `Option<T::AtLeast64BitUnsigned>` | 
| swap_fee | `Option<T::AtLeast64BitUnsigned>` | 
| redeem_fee | `Option<T::AtLeast64BitUnsigned>` | 

#### Python
```python
call = substrate.compose_call(
    'StableAsset', 'modify_fees', {
    'mint_fee': (None, 'u128'),
    'pool_id': 'u32',
    'redeem_fee': (None, 'u128'),
    'swap_fee': (None, 'u128'),
}
)
```

---------
### modify_recipients
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| fee_recipient | `Option<T::AccountId>` | 
| yield_recipient | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'StableAsset', 'modify_recipients', {
    'fee_recipient': (
        None,
        'AccountId',
    ),
    'pool_id': 'u32',
    'yield_recipient': (
        None,
        'AccountId',
    ),
}
)
```

---------
### redeem_multi
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| amounts | `Vec<T::Balance>` | 
| max_redeem_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'StableAsset', 'redeem_multi', {
    'amounts': ['u128'],
    'max_redeem_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### redeem_proportion
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| amount | `T::Balance` | 
| min_redeem_amounts | `Vec<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'StableAsset', 'redeem_proportion', {
    'amount': 'u128',
    'min_redeem_amounts': ['u128'],
    'pool_id': 'u32',
}
)
```

---------
### redeem_single
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| amount | `T::Balance` | 
| i | `PoolTokenIndex` | 
| min_redeem_amount | `T::Balance` | 
| asset_length | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'StableAsset', 'redeem_single', {
    'amount': 'u128',
    'asset_length': 'u32',
    'i': 'u32',
    'min_redeem_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### swap
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| i | `PoolTokenIndex` | 
| j | `PoolTokenIndex` | 
| dx | `T::Balance` | 
| min_dy | `T::Balance` | 
| asset_length | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'StableAsset', 'swap', {
    'asset_length': 'u32',
    'dx': 'u128',
    'i': 'u32',
    'j': 'u32',
    'min_dy': 'u128',
    'pool_id': 'u32',
}
)
```

---------
## Events

---------
### AModified
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `StableAssetPoolId` | ```u32```
| value | `T::AtLeast64BitUnsigned` | ```u128```
| time | `T::BlockNumber` | ```u32```

---------
### BalanceUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `StableAssetPoolId` | ```u32```
| old_balances | `Vec<T::Balance>` | ```['u128']```
| new_balances | `Vec<T::Balance>` | ```['u128']```

---------
### CreatePool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `StableAssetPoolId` | ```u32```
| a | `T::AtLeast64BitUnsigned` | ```u128```
| swap_id | `T::AccountId` | ```AccountId```
| pallet_id | `T::AccountId` | ```AccountId```

---------
### FeeCollected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `StableAssetPoolId` | ```u32```
| a | `T::AtLeast64BitUnsigned` | ```u128```
| old_balances | `Vec<T::Balance>` | ```['u128']```
| new_balances | `Vec<T::Balance>` | ```['u128']```
| old_total_supply | `T::Balance` | ```u128```
| new_total_supply | `T::Balance` | ```u128```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### FeeModified
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `StableAssetPoolId` | ```u32```
| mint_fee | `T::AtLeast64BitUnsigned` | ```u128```
| swap_fee | `T::AtLeast64BitUnsigned` | ```u128```
| redeem_fee | `T::AtLeast64BitUnsigned` | ```u128```

---------
### Minted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| minter | `T::AccountId` | ```AccountId```
| pool_id | `StableAssetPoolId` | ```u32```
| a | `T::AtLeast64BitUnsigned` | ```u128```
| input_amounts | `Vec<T::Balance>` | ```['u128']```
| min_output_amount | `T::Balance` | ```u128```
| balances | `Vec<T::Balance>` | ```['u128']```
| total_supply | `T::Balance` | ```u128```
| fee_amount | `T::Balance` | ```u128```
| output_amount | `T::Balance` | ```u128```

---------
### RecipientModified
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `StableAssetPoolId` | ```u32```
| fee_recipient | `T::AccountId` | ```AccountId```
| yield_recipient | `T::AccountId` | ```AccountId```

---------
### RedeemedMulti
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| pool_id | `StableAssetPoolId` | ```u32```
| a | `T::AtLeast64BitUnsigned` | ```u128```
| output_amounts | `Vec<T::Balance>` | ```['u128']```
| max_input_amount | `T::Balance` | ```u128```
| balances | `Vec<T::Balance>` | ```['u128']```
| total_supply | `T::Balance` | ```u128```
| fee_amount | `T::Balance` | ```u128```
| input_amount | `T::Balance` | ```u128```

---------
### RedeemedProportion
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| pool_id | `StableAssetPoolId` | ```u32```
| a | `T::AtLeast64BitUnsigned` | ```u128```
| input_amount | `T::Balance` | ```u128```
| min_output_amounts | `Vec<T::Balance>` | ```['u128']```
| balances | `Vec<T::Balance>` | ```['u128']```
| total_supply | `T::Balance` | ```u128```
| fee_amount | `T::Balance` | ```u128```
| output_amounts | `Vec<T::Balance>` | ```['u128']```

---------
### RedeemedSingle
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| pool_id | `StableAssetPoolId` | ```u32```
| a | `T::AtLeast64BitUnsigned` | ```u128```
| input_amount | `T::Balance` | ```u128```
| output_asset | `T::AssetId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```
| min_output_amount | `T::Balance` | ```u128```
| balances | `Vec<T::Balance>` | ```['u128']```
| total_supply | `T::Balance` | ```u128```
| fee_amount | `T::Balance` | ```u128```
| output_amount | `T::Balance` | ```u128```

---------
### TokenSwapped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| swapper | `T::AccountId` | ```AccountId```
| pool_id | `StableAssetPoolId` | ```u32```
| a | `T::AtLeast64BitUnsigned` | ```u128```
| input_asset | `T::AssetId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```
| output_asset | `T::AssetId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```
| input_amount | `T::Balance` | ```u128```
| min_output_amount | `T::Balance` | ```u128```
| balances | `Vec<T::Balance>` | ```['u128']```
| total_supply | `T::Balance` | ```u128```
| output_amount | `T::Balance` | ```u128```

---------
### YieldCollected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `StableAssetPoolId` | ```u32```
| a | `T::AtLeast64BitUnsigned` | ```u128```
| old_total_supply | `T::Balance` | ```u128```
| new_total_supply | `T::Balance` | ```u128```
| who | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### PoolCount

#### Python
```python
result = substrate.query(
    'StableAsset', 'PoolCount', []
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
    'StableAsset', 'Pools', ['u32']
)
```

#### Return value
```python
{
    'a': 'u128',
    'a_block': 'u32',
    'account_id': 'AccountId',
    'assets': [
        {
            'DexShare': (
                {
                    'Erc20': '[u8; 20]',
                    'ForeignAsset': 'u16',
                    'LiquidCrowdloan': 'u32',
                    'StableAssetPoolToken': 'u32',
                    'Token': 'scale_info::52',
                },
                {
                    'Erc20': '[u8; 20]',
                    'ForeignAsset': 'u16',
                    'LiquidCrowdloan': 'u32',
                    'StableAssetPoolToken': 'u32',
                    'Token': 'scale_info::52',
                },
            ),
            'Erc20': '[u8; 20]',
            'ForeignAsset': 'u16',
            'LiquidCrowdloan': 'u32',
            'StableAssetPoolToken': 'u32',
            'Token': (
                'ACA',
                'AUSD',
                'DOT',
                'LDOT',
                'TAP',
                'KAR',
                'KUSD',
                'KSM',
                'LKSM',
                'TAI',
                'BNC',
                'VSKSM',
                'PHA',
                'KINT',
                'KBTC',
            ),
        },
    ],
    'balances': ['u128'],
    'fee_recipient': 'AccountId',
    'future_a': 'u128',
    'future_a_block': 'u32',
    'mint_fee': 'u128',
    'pool_asset': {
        'DexShare': (
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
            {
                'Erc20': '[u8; 20]',
                'ForeignAsset': 'u16',
                'LiquidCrowdloan': 'u32',
                'StableAssetPoolToken': 'u32',
                'Token': (
                    'ACA',
                    'AUSD',
                    'DOT',
                    'LDOT',
                    'TAP',
                    'KAR',
                    'KUSD',
                    'KSM',
                    'LKSM',
                    'TAI',
                    'BNC',
                    'VSKSM',
                    'PHA',
                    'KINT',
                    'KBTC',
                ),
            },
        ),
        'Erc20': '[u8; 20]',
        'ForeignAsset': 'u16',
        'LiquidCrowdloan': 'u32',
        'StableAssetPoolToken': 'u32',
        'Token': (
            'ACA',
            'AUSD',
            'DOT',
            'LDOT',
            'TAP',
            'KAR',
            'KUSD',
            'KSM',
            'LKSM',
            'TAI',
            'BNC',
            'VSKSM',
            'PHA',
            'KINT',
            'KBTC',
        ),
    },
    'precision': 'u128',
    'precisions': ['u128'],
    'redeem_fee': 'u128',
    'swap_fee': 'u128',
    'total_supply': 'u128',
    'yield_recipient': 'AccountId',
}
```
---------
## Constants

---------
### APrecision
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('StableAsset', 'APrecision')
```
---------
### FeePrecision
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('StableAsset', 'FeePrecision')
```
---------
### PalletId
#### Value
```python
'0x6e7574732f737461'
```
#### Python
```python
constant = substrate.get_constant('StableAsset', 'PalletId')
```
---------
### PoolAssetLimit
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('StableAsset', 'PoolAssetLimit')
```
---------
### SwapExactOverAmount
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('StableAsset', 'SwapExactOverAmount')
```
---------
## Errors

---------
### ArgumentsError

---------
### ArgumentsMismatch

---------
### InconsistentStorage

---------
### InvalidPoolAsset

---------
### InvalidPoolValue

---------
### Math

---------
### MintUnderMin

---------
### PoolNotFound

---------
### RedeemOverMax

---------
### RedeemUnderMin

---------
### SwapUnderMin

---------
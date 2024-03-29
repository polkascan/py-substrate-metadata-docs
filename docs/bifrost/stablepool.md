
# StablePool

---------
## Calls

---------
### add_liquidity
See [`Pallet::add_liquidity`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| amounts | `Vec<T::Balance>` | 
| min_mint_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'add_liquidity', {
    'amounts': ['u128'],
    'min_mint_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### config_vtoken_auto_refresh
See [`Pallet::config_vtoken_auto_refresh`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| vtoken | `AssetIdOf<T>` | 
| hardcap | `Permill` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'config_vtoken_auto_refresh', {
    'hardcap': 'u32',
    'vtoken': {
        'BLP': 'u32',
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
        'Lend': 'u8',
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
}
)
```

---------
### create_pool
See [`Pallet::create_pool`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| assets | `Vec<AssetIdOf<T>>` | 
| precisions | `Vec<AtLeast64BitUnsignedOf<T>>` | 
| mint_fee | `AtLeast64BitUnsignedOf<T>` | 
| swap_fee | `AtLeast64BitUnsignedOf<T>` | 
| redeem_fee | `AtLeast64BitUnsignedOf<T>` | 
| initial_a | `AtLeast64BitUnsignedOf<T>` | 
| fee_recipient | `AccountIdOf<T>` | 
| yield_recipient | `AccountIdOf<T>` | 
| precision | `AtLeast64BitUnsignedOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'create_pool', {
    'assets': [
        {
            'BLP': 'u32',
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
            'Lend': 'u8',
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
    'fee_recipient': 'AccountId',
    'initial_a': 'u128',
    'mint_fee': 'u128',
    'precision': 'u128',
    'precisions': ['u128'],
    'redeem_fee': 'u128',
    'swap_fee': 'u128',
    'yield_recipient': 'AccountId',
}
)
```

---------
### edit_token_rate
See [`Pallet::edit_token_rate`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| token_rate_info | `Vec<
(AssetIdOf<T>,
(AtLeast64BitUnsignedOf<T>, AtLeast64BitUnsignedOf<T>),)>` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'edit_token_rate', {
    'pool_id': 'u32',
    'token_rate_info': [
        (
            {
                'BLP': 'u32',
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
                'Lend': 'u8',
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
            ('u128', 'u128'),
        ),
    ],
}
)
```

---------
### modify_a
See [`Pallet::modify_a`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| a | `T::AtLeast64BitUnsigned` | 
| future_a_block | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'modify_a', {
    'a': 'u128',
    'future_a_block': 'u32',
    'pool_id': 'u32',
}
)
```

---------
### modify_fees
See [`Pallet::modify_fees`].
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
    'StablePool', 'modify_fees', {
    'mint_fee': (None, 'u128'),
    'pool_id': 'u32',
    'redeem_fee': (None, 'u128'),
    'swap_fee': (None, 'u128'),
}
)
```

---------
### modify_recipients
See [`Pallet::modify_recipients`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| fee_recipient | `Option<T::AccountId>` | 
| yield_recipient | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'modify_recipients', {
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
See [`Pallet::redeem_multi`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| amounts | `Vec<T::Balance>` | 
| max_redeem_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'redeem_multi', {
    'amounts': ['u128'],
    'max_redeem_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### redeem_proportion
See [`Pallet::redeem_proportion`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| amount | `T::Balance` | 
| min_redeem_amounts | `Vec<T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'redeem_proportion', {
    'amount': 'u128',
    'min_redeem_amounts': ['u128'],
    'pool_id': 'u32',
}
)
```

---------
### redeem_single
See [`Pallet::redeem_single`].
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
    'StablePool', 'redeem_single', {
    'amount': 'u128',
    'asset_length': 'u32',
    'i': 'u32',
    'min_redeem_amount': 'u128',
    'pool_id': 'u32',
}
)
```

---------
### remove_vtoken_auto_refresh
See [`Pallet::remove_vtoken_auto_refresh`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| vtoken | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'remove_vtoken_auto_refresh', {
    'vtoken': {
        'BLP': 'u32',
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
        'Lend': 'u8',
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
}
)
```

---------
### swap
See [`Pallet::swap`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `StableAssetPoolId` | 
| i | `PoolTokenIndex` | 
| j | `PoolTokenIndex` | 
| dx | `T::Balance` | 
| min_dy | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'StablePool', 'swap', {
    'dx': 'u128',
    'i': 'u32',
    'j': 'u32',
    'min_dy': 'u128',
    'pool_id': 'u32',
}
)
```

---------
## Errors

---------
### CantMint

---------
### MintUnderMin

---------
### RedeemOverMax

---------
### SwapUnderMin

---------
### TokenRateNotSet

---------
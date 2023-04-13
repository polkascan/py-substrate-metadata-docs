
# DexGeneral

---------
## Calls

---------
### add_liquidity
Provide liquidity to a pair.

The order of assets does not effect the result.

\# Arguments

- `asset_0`: Asset which make up pair
- `asset_1`: Asset which make up pair
- `amount_0_desired`: Maximum amount of asset_0 added to the pair
- `amount_1_desired`: Maximum amount of asset_1 added to the pair
- `amount_0_min`: Minimum amount of asset_0 added to the pair
- `amount_1_min`: Minimum amount of asset_1 added to the pair
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| amount_0_desired | `AssetBalance` | 
| amount_1_desired | `AssetBalance` | 
| amount_0_min | `AssetBalance` | 
| amount_1_min | `AssetBalance` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'add_liquidity', {
    'amount_0_desired': 'u128',
    'amount_0_min': 'u128',
    'amount_1_desired': 'u128',
    'amount_1_min': 'u128',
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'deadline': 'u32',
}
)
```

---------
### bootstrap_charge_reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| charge_rewards | `Vec<(T::AssetId, AssetBalance)>` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'bootstrap_charge_reward', {
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'charge_rewards': [
        (
            {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': (
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            'u128',
        ),
    ],
}
)
```

---------
### bootstrap_claim
Claim lp asset from a bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'bootstrap_claim', {
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'deadline': 'u32',
    'recipient': 'AccountId',
}
)
```

---------
### bootstrap_contribute
Contribute some asset to a bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
- `amount_0_contribute`: The amount of asset_0 contribute to this bootstrap pair
- `amount_1_contribute`: The amount of asset_1 contribute to this bootstrap pair
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| amount_0_contribute | `AssetBalance` | 
| amount_1_contribute | `AssetBalance` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'bootstrap_contribute', {
    'amount_0_contribute': 'u128',
    'amount_1_contribute': 'u128',
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'deadline': 'u32',
}
)
```

---------
### bootstrap_create
Create bootstrap pair

The order of asset don&\#x27;t affect result.

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
- `target_supply_0`: Target amount of asset_0 total contribute
- `target_supply_0`: Target amount of asset_1 total contribute
- `capacity_supply_0`: The max amount of asset_0 total contribute
- `capacity_supply_1`: The max amount of asset_1 total contribute
- `end`: The earliest ending block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| target_supply_0 | `AssetBalance` | 
| target_supply_1 | `AssetBalance` | 
| capacity_supply_0 | `AssetBalance` | 
| capacity_supply_1 | `AssetBalance` | 
| end | `T::BlockNumber` | 
| rewards | `Vec<T::AssetId>` | 
| limits | `Vec<(T::AssetId, AssetBalance)>` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'bootstrap_create', {
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'capacity_supply_0': 'u128',
    'capacity_supply_1': 'u128',
    'end': 'u32',
    'limits': [
        (
            {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': (
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            'u128',
        ),
    ],
    'rewards': [
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ],
    'target_supply_0': 'u128',
    'target_supply_1': 'u128',
}
)
```

---------
### bootstrap_end
End a bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'bootstrap_end', {
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
}
)
```

---------
### bootstrap_refund
Contributor refund from disable bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'bootstrap_refund', {
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
}
)
```

---------
### bootstrap_update
update a bootstrap pair

\# Arguments

- `asset_0`: Asset which make up bootstrap pair
- `asset_1`: Asset which make up bootstrap pair
- `min_contribution_0`: The new min amount of asset_0 contribute
- `min_contribution_0`: The new min amount of asset_1 contribute
- `target_supply_0`: The new target amount of asset_0 total contribute
- `target_supply_0`: The new target amount of asset_1 total contribute
- `capacity_supply_0`: The new max amount of asset_0 total contribute
- `capacity_supply_1`: The new max amount of asset_1 total contribute
- `end`: The earliest ending block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| target_supply_0 | `AssetBalance` | 
| target_supply_1 | `AssetBalance` | 
| capacity_supply_0 | `AssetBalance` | 
| capacity_supply_1 | `AssetBalance` | 
| end | `T::BlockNumber` | 
| rewards | `Vec<T::AssetId>` | 
| limits | `Vec<(T::AssetId, AssetBalance)>` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'bootstrap_update', {
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'capacity_supply_0': 'u128',
    'capacity_supply_1': 'u128',
    'end': 'u32',
    'limits': [
        (
            {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': (
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            'u128',
        ),
    ],
    'rewards': [
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ],
    'target_supply_0': 'u128',
    'target_supply_1': 'u128',
}
)
```

---------
### bootstrap_withdraw_reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'bootstrap_withdraw_reward', {
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'recipient': 'AccountId',
}
)
```

---------
### create_pair
Create pair by two assets.

The order of assets does not effect the result.

\# Arguments

- `asset_0`: Asset which make up Pair
- `asset_1`: Asset which make up Pair
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| fee_rate | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'create_pair', {
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'fee_rate': 'u128',
}
)
```

---------
### remove_liquidity
Extract liquidity.

The order of assets does not effect the result.

\# Arguments

- `asset_0`: Asset which make up pair
- `asset_1`: Asset which make up pair
- `amount_asset_0_min`: Minimum amount of asset_0 to exact
- `amount_asset_1_min`: Minimum amount of asset_1 to exact
- `recipient`: Account that accepts withdrawal of assets
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| liquidity | `AssetBalance` | 
| amount_0_min | `AssetBalance` | 
| amount_1_min | `AssetBalance` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'remove_liquidity', {
    'amount_0_min': 'u128',
    'amount_1_min': 'u128',
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'deadline': 'u32',
    'liquidity': 'u128',
    'recipient': 'AccountId',
}
)
```

---------
### set_exchange_fee
Set the exchange fee rate.

\# Arguments

- `asset_0`: Asset which makes up the pair
- `asset_1`: Asset which makes up the pair
- `fee_rate`:
Value denoting the trading fee taken from the amount paid in,
multiplied by the fee adjustment to simplify calculations.
e.g. 0.3% / 100 = 0.003
     0.003 * 10000 = 30
See section 3.2.1 of the Uniswap v2 whitepaper
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_0 | `T::AssetId` | 
| asset_1 | `T::AssetId` | 
| fee_rate | `u128` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'set_exchange_fee', {
    'asset_0': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'asset_1': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'StableLpToken': 'u32',
        'Token': (
            'DOT',
            'IBTC',
            'INTR',
            'KSM',
            'KBTC',
            'KINT',
        ),
    },
    'fee_rate': 'u128',
}
)
```

---------
### set_fee_point
Set the protocol fee point.

\# Arguments

- `fee_point`:
An integer y which satisfies the equation `1/x-1=y`
where x is the percentage of the exchange fee
e.g. 1/(1/6)-1=5, 1/(1/2)-1=1
See section 2.4 of the Uniswap v2 whitepaper
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee_point | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'set_fee_point', {'fee_point': 'u8'}
)
```

---------
### set_fee_receiver
Set the new receiver of the protocol fee.

\# Arguments

- `send_to`:
(1) Some(receiver): it turn on the protocol fee and the new receiver account.
(2) None: it turn off the protocol fee.
#### Attributes
| Name | Type |
| -------- | -------- | 
| send_to | `Option<<T::Lookup as StaticLookup>::Source>` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'set_fee_receiver', {'send_to': (None, 'AccountId')}
)
```

---------
### swap_assets_for_exact_assets
Buy amount of asset by path.

\# Arguments

- `amount_out`: Amount of the asset will be bought
- `amount_in_max`: Maximum amount of sold asset
- `path`: path can convert to pairs.
- `recipient`: Account that receive the target asset
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_out | `AssetBalance` | 
| amount_in_max | `AssetBalance` | 
| path | `Vec<T::AssetId>` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'swap_assets_for_exact_assets', {
    'amount_in_max': 'u128',
    'amount_out': 'u128',
    'deadline': 'u32',
    'path': [
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ],
    'recipient': 'AccountId',
}
)
```

---------
### swap_exact_assets_for_assets
Sell amount of asset by path.

\# Arguments

- `amount_in`: Amount of the asset will be sold
- `amount_out_min`: Minimum amount of target asset
- `path`: path can convert to pairs.
- `recipient`: Account that receive the target asset
- `deadline`: Height of the cutoff block of this transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_in | `AssetBalance` | 
| amount_out_min | `AssetBalance` | 
| path | `Vec<T::AssetId>` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| deadline | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DexGeneral', 'swap_exact_assets_for_assets', {
    'amount_in': 'u128',
    'amount_out_min': 'u128',
    'deadline': 'u32',
    'path': [
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ],
    'recipient': 'AccountId',
}
)
```

---------
## Events

---------
### AssetSwap
Transact in trading \[owner, recipient, swap_path, balances\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `Vec<T::AssetId>` | ```[{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}]```
| None | `Vec<AssetBalance>` | ```['u128']```

---------
### BootstrapClaim
Claim a bootstrap pair. \[bootstrap_pair_account, claimer, receiver, asset_0, asset_1,
asset_0_refund, asset_1_refund, lp_amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### BootstrapContribute
Contribute to bootstrap pair. \[who, asset_0, asset_0_contribute, asset_1_contribute\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `AssetBalance` | ```u128```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `AssetBalance` | ```u128```

---------
### BootstrapCreated
Create a bootstrap pair. \[bootstrap_pair_account, asset_0, asset_1,
total_supply_0,total_supply_1, capacity_supply_0,capacity_supply_1, end\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `T::BlockNumber` | ```u32```

---------
### BootstrapEnd
A bootstrap pair end. \[asset_0, asset_1, asset_0_amount, asset_1_amount,
total_lp_supply]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### BootstrapRefund
Refund from disable bootstrap pair. \[bootstrap_pair_account, caller, asset_0, asset_1,
asset_0_refund, asset_1_refund\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### BootstrapUpdate
Update a bootstrap pair. \[caller, asset_0, asset_1,
total_supply_0,total_supply_1, capacity_supply_0,capacity_supply_1\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `T::BlockNumber` | ```u32```

---------
### ChargeReward
Charge reward into a bootstrap.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AccountId` | ```AccountId```
| None | `Vec<(T::AssetId, AssetBalance)>` | ```[({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'u128')]```

---------
### DistributeReward
Bootstrap distribute some rewards to contributors.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AccountId` | ```AccountId```
| None | `Vec<(T::AssetId, AssetBalance)>` | ```[({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'u128')]```

---------
### LiquidityAdded
Add liquidity. \[owner, asset_0, asset_1, add_balance_0, add_balance_1,
mint_balance_lp\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### LiquidityRemoved
Remove liquidity. \[owner, recipient, asset_0, asset_1, rm_balance_0, rm_balance_1,
burn_balance_lp\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```
| None | `AssetBalance` | ```u128```

---------
### PairCreated
Swap
Create a trading pair. \[asset_0, asset_1\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```

---------
### WithdrawReward
Withdraw all reward from a bootstrap.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AssetId` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### BootstrapEndStatus
 End status of bootstrap

 BootstrapEndStatus: map bootstrap pair =&gt; pairStatus

#### Python
```python
result = substrate.query(
    'DexGeneral', 'BootstrapEndStatus', [
    (
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ),
]
)
```

#### Return value
```python
{
    'Bootstrap': {
        'accumulated_supply': ('u128', 'u128'),
        'capacity_supply': ('u128', 'u128'),
        'end_block_number': 'u32',
        'pair_account': 'AccountId',
        'target_supply': ('u128', 'u128'),
    },
    'Disable': None,
    'Trading': {
        'fee_rate': 'u128',
        'pair_account': 'AccountId',
        'total_supply': 'u128',
    },
}
```
---------
### BootstrapLimits

#### Python
```python
result = substrate.query(
    'DexGeneral', 'BootstrapLimits', [
    (
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ),
]
)
```

#### Return value
```python
'scale_info::563'
```
---------
### BootstrapPersonalSupply

#### Python
```python
result = substrate.query(
    'DexGeneral', 'BootstrapPersonalSupply', [
    (
        (
            {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': (
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': (
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        ),
        'AccountId',
    ),
]
)
```

#### Return value
```python
('u128', 'u128')
```
---------
### BootstrapRewards

#### Python
```python
result = substrate.query(
    'DexGeneral', 'BootstrapRewards', [
    (
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ),
]
)
```

#### Return value
```python
'scale_info::563'
```
---------
### FeeMeta

#### Python
```python
result = substrate.query(
    'DexGeneral', 'FeeMeta', []
)
```

#### Return value
```python
((None, 'AccountId'), 'u8')
```
---------
### KLast
 Refer: https://github.com/Uniswap/uniswap-v2-core/blob/master/contracts/UniswapV2Pair.sol\#L88
 Last unliquidated protocol fee;

#### Python
```python
result = substrate.query(
    'DexGeneral', 'KLast', [
    (
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ),
]
)
```

#### Return value
```python
'[u64; 4]'
```
---------
### LiquidityPairs

#### Python
```python
result = substrate.query(
    'DexGeneral', 'LiquidityPairs', [
    (
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ),
]
)
```

#### Return value
```python
(
    None,
    {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
        ),
        'StableLpToken': 'u32',
        'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
    },
)
```
---------
### PairStatuses
 (T::AssetId, T::AssetId) -&gt; PairStatus

#### Python
```python
result = substrate.query(
    'DexGeneral', 'PairStatuses', [
    (
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    ),
]
)
```

#### Return value
```python
{
    'Bootstrap': {
        'accumulated_supply': ('u128', 'u128'),
        'capacity_supply': ('u128', 'u128'),
        'end_block_number': 'u32',
        'pair_account': 'AccountId',
        'target_supply': ('u128', 'u128'),
    },
    'Disable': None,
    'Trading': {
        'fee_rate': 'u128',
        'pair_account': 'AccountId',
        'total_supply': 'u128',
    },
}
```
---------
## Constants

---------
### PalletId
 This pallet id.
#### Value
```python
'0x6465782f67656e72'
```
#### Python
```python
constant = substrate.get_constant('DexGeneral', 'PalletId')
```
---------
## Errors

---------
### AccountIdBadLocation
Location given was invalid or unsupported.

---------
### AssetNotExists
Asset does not exist.

---------
### ChargeRewardParamsError
Charge bootstrap extrinsic args has error,

---------
### Deadline
Transaction block number is larger than the end block number.

---------
### DeniedCreatePair
Trading pair can&\#x27;t be created.

---------
### DeniedTransferToSelf
Transfer to self by XCM message.

---------
### DenyRefund
Bootstrap deny refund

---------
### DisableBootstrap
Bootstrap is disable

---------
### ExcessiveSoldAmount
Sold amount is more than exception.

---------
### ExecutionFailed
XCM execution failed.

---------
### ExistRewardsInBootstrap
Exist some reward in bootstrap,

---------
### IncorrectAssetAmountRange
Incorrect amount range.

---------
### InsufficientAssetBalance
Account balance must be greater than or equal to the transfer amount.

---------
### InsufficientLiquidity
Liquidity is not enough.

---------
### InsufficientPairReserve
Trading pair does have enough.

---------
### InsufficientTargetAmount
Get target amount is less than exception.

---------
### InvalidContributionAmount
Amount of contribution is invalid.

---------
### InvalidFeeRate
Invalid fee_rate

---------
### InvalidPath
Can&\#x27;t find pair though trading path.

---------
### InvariantCheckFailed
Can&\#x27;t pass the K value check

---------
### NativeBalanceTooLow
Account native currency balance must be greater than ExistentialDeposit.

---------
### NoRewardTokens
Reward of bootstrap is not set.

---------
### NotInBootstrap
Pair is not in bootstrap

---------
### NotQualifiedAccount
Not eligible to contribute

---------
### Overflow
Overflow.

---------
### PairAlreadyExists
Trading pair already exists.

---------
### PairCreateForbidden
Created pair can&\#x27;t create now

---------
### PairNotExists
Trading pair does not exist.

---------
### RequireProtocolAdmin
Require the admin who can reset the admin and receiver of the protocol fee.

---------
### RequireProtocolAdminCandidate
Require the admin candidate who can become new admin after confirm.

---------
### TargetChainNotRegistered
Not in registered parachains.

---------
### UnqualifiedBootstrap
Amount of contribution is invalid.

---------
### UnsupportedAssetType
Unsupported AssetId.

---------
### ZeroContribute
Zero contribute in bootstrap

---------
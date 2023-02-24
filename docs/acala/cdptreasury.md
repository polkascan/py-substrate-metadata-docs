
# CdpTreasury

---------
## Calls

---------
### auction_collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| amount | `Balance` | 
| target | `Balance` | 
| splited | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'CdpTreasury', 'auction_collateral', {
    'amount': 'u128',
    'currency_id': {
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
                    'RENBTC',
                    'CASH',
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
                    'RENBTC',
                    'CASH',
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
            'RENBTC',
            'CASH',
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
    'splited': 'bool',
    'target': 'u128',
}
)
```

---------
### exchange_collateral_to_stable
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| swap_limit | `SwapLimit<Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'CdpTreasury', 'exchange_collateral_to_stable', {
    'currency_id': {
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
                    'RENBTC',
                    'CASH',
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
                    'RENBTC',
                    'CASH',
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
            'RENBTC',
            'CASH',
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
    'swap_limit': {
        'ExactSupply': (
            'u128',
            'u128',
        ),
        'ExactTarget': (
            'u128',
            'u128',
        ),
    },
}
)
```

---------
### extract_surplus_to_treasury
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CdpTreasury', 'extract_surplus_to_treasury', {'amount': 'u128'}
)
```

---------
### set_debit_offset_buffer
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CdpTreasury', 'set_debit_offset_buffer', {'amount': 'u128'}
)
```

---------
### set_expected_collateral_auction_size
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId` | 
| size | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CdpTreasury', 'set_expected_collateral_auction_size', {
    'currency_id': {
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
                    'RENBTC',
                    'CASH',
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
                    'RENBTC',
                    'CASH',
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
            'RENBTC',
            'CASH',
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
    'size': 'u128',
}
)
```

---------
## Events

---------
### DebitOffsetBufferUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `Balance` | ```u128```

---------
### ExpectedCollateralAuctionSizeUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collateral_type | `CurrencyId` | ```{'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'RENBTC', 'CASH', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'DexShare': ({'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'RENBTC', 'CASH', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}, {'Token': ('ACA', 'AUSD', 'DOT', 'LDOT', 'TAP', 'RENBTC', 'CASH', 'KAR', 'KUSD', 'KSM', 'LKSM', 'TAI', 'BNC', 'VSKSM', 'PHA', 'KINT', 'KBTC'), 'Erc20': '[u8; 20]', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16', 'StableAssetPoolToken': 'u32'}), 'Erc20': '[u8; 20]', 'StableAssetPoolToken': 'u32', 'LiquidCrowdloan': 'u32', 'ForeignAsset': 'u16'}```
| new_size | `Balance` | ```u128```

---------
## Storage functions

---------
### DebitOffsetBuffer

#### Python
```python
result = substrate.query(
    'CdpTreasury', 'DebitOffsetBuffer', []
)
```

#### Return value
```python
'u128'
```
---------
### DebitPool

#### Python
```python
result = substrate.query(
    'CdpTreasury', 'DebitPool', []
)
```

#### Return value
```python
'u128'
```
---------
### ExpectedCollateralAuctionSize

#### Python
```python
result = substrate.query(
    'CdpTreasury', 'ExpectedCollateralAuctionSize', [
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
                    'RENBTC',
                    'CASH',
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
                    'RENBTC',
                    'CASH',
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
            'RENBTC',
            'CASH',
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
]
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### GetStableCurrencyId
#### Value
```python
{'Token': 'AUSD'}
```
#### Python
```python
constant = substrate.get_constant('CdpTreasury', 'GetStableCurrencyId')
```
---------
### MaxAuctionsCount
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('CdpTreasury', 'MaxAuctionsCount')
```
---------
### PalletId
#### Value
```python
'0x6163612f63647074'
```
#### Python
```python
constant = substrate.get_constant('CdpTreasury', 'PalletId')
```
---------
### TreasuryAccount
#### Value
```python
'23M5ttkmR6Kco5uGj64jEZbG6PYyZSwvjeoeUVTMqQEG71yu'
```
#### Python
```python
constant = substrate.get_constant('CdpTreasury', 'TreasuryAccount')
```
---------
## Errors

---------
### CannotSwap

---------
### CollateralNotEnough

---------
### DebitPoolNotEnough

---------
### NotDexShare

---------
### SurplusPoolNotEnough

---------
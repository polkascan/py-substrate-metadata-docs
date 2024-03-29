
# TreasuryBuyoutExtension

---------
## Calls

---------
### buyout
Allows caller to buyout a given amount of native token.
When denoting the `amount` as `Buyout` the caller will receive this exact amount of the native token in exchange for a corresponding amount of an allowed asset.
When denoting the `amount` as `Exchange`, the caller will spend this exact amount of an allowed asset in exchange for a corresponding amount of the native token.

Parameters

- `origin`: Caller&\#x27;s origin.
- `asset`: Exchange asset used for buyout of basic asset.
- `amount`: Amount of basic asset to buyout or amount of asset to exchange.

Emits `Buyout` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `CurrencyIdOf<T>` | 
| amount | `Amount<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryBuyoutExtension', 'buyout', {
    'amount': {
        'Buyout': 'u128',
        'Exchange': 'u128',
    },
    'asset': {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
}
)
```

---------
### update_allowed_assets
Allows root to update the allowed currencies for buyout.
`AllowedCurrencies` storage will be reset and updated with provided `assets`.

Parameters

- `origin`: Origin must be root.
- `assets`: List of assets to be inserted into `AllowedCurrencies` storage.

Emits `AllowedAssetsForBuyoutUpdated` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| assets | `Vec<CurrencyIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryBuyoutExtension', 'update_allowed_assets', {
    'assets': [
        {
            'Native': None,
            'Stellar': {
                'AlphaNum12': {
                    'code': '[u8; 12]',
                    'issuer': '[u8; 32]',
                },
                'AlphaNum4': {
                    'code': '[u8; 4]',
                    'issuer': '[u8; 32]',
                },
                'StellarNative': None,
            },
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    ],
}
)
```

---------
### update_buyout_limit
Allows root to update the buyout limit.

Parameters

- `origin`: Origin must be root.
- `limit`: New buyout limit. If None, then buyouts are not limited.

Emits `BuyoutLimitUpdated` event when successful.
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'TreasuryBuyoutExtension', 'update_buyout_limit', {'limit': (None, 'u128')}
)
```

---------
## Events

---------
### AllowedAssetsForBuyoutUpdated
Updated allowed assets for buyout event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| allowed_assets | `Vec<CurrencyIdOf<T>>` | ```[{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}]```

---------
### Buyout
Buyout event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `AccountIdOf<T>` | ```AccountId```
| buyout_amount | `BalanceOf<T>` | ```u128```
| asset | `CurrencyIdOf<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}```
| exchange_amount | `BalanceOf<T>` | ```u128```

---------
### BuyoutLimitUpdated
Buyout limit updated event
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| limit | `Option<BalanceOf<T>>` | ```(None, 'u128')```

---------
## Storage functions

---------
### AllowedCurrencies
 Stores allowed currencies for buyout

#### Python
```python
result = substrate.query(
    'TreasuryBuyoutExtension', 'AllowedCurrencies', [
    {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'Token': 'u64',
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
]
)
```

#### Return value
```python
()
```
---------
### BuyoutLimit
 Stores buyout limit amount user could buy for a period of `BuyoutPeriod` blocks.
 Each user can buyout up to this amount in a period. After each period passes, buyout limit is reset
 When `None` - buyouts are not limited

#### Python
```python
result = substrate.query(
    'TreasuryBuyoutExtension', 'BuyoutLimit', []
)
```

#### Return value
```python
'u128'
```
---------
### Buyouts
 Stores amount of buyouts (amount, block number of last buyout)

#### Python
```python
result = substrate.query(
    'TreasuryBuyoutExtension', 'Buyouts', ['AccountId']
)
```

#### Return value
```python
('u128', 'u32')
```
---------
## Constants

---------
### BuyoutPeriod
 Buyout period in blocks in which a caller can buyout up to the amount limit stored in `BuyoutLimit`
 When attempting to buyout after this period, the buyout limit is reset for the caller
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('TreasuryBuyoutExtension', 'BuyoutPeriod')
```
---------
### MaxAllowedBuyoutCurrencies
 Maximum number of allowed currencies for buyout
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('TreasuryBuyoutExtension', 'MaxAllowedBuyoutCurrencies')
```
---------
### MinAmountToBuyout
 Min amount of native token to buyout
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('TreasuryBuyoutExtension', 'MinAmountToBuyout')
```
---------
### SellFee
 Fee from the native asset buyouts
#### Value
```python
50000
```
#### Python
```python
constant = substrate.get_constant('TreasuryBuyoutExtension', 'SellFee')
```
---------
### TreasuryAccount
 Used for getting the treasury account
#### Value
```python
'6jM63XCmW5faKXcytHPdVb5iTg7nEumoeNNNz44GhEHVJVJf'
```
#### Python
```python
constant = substrate.get_constant('TreasuryBuyoutExtension', 'TreasuryAccount')
```
---------
## Errors

---------
### BuyoutLimitExceeded
Buyout limit exceeded for the current period

---------
### BuyoutWithTreasuryAccount
Attempt to use treasury account for buyout

---------
### ExceedsNumberOfAllowedCurrencies
Exceeds number of allowed currencies for buyout

---------
### ExchangeFailure
Exchange failed

---------
### InsufficientAccountBalance
The account balance is too low for an operation

---------
### InsufficientTreasuryBalance
The treasury balance is too low for an operation

---------
### LessThanMinBuyoutAmount
Less than minimum amoount allowed for buyout

---------
### NativeTokenNotAllowed
Attempt to add native token to allowed assets

---------
### NoPrice
One of transacted currencies is missing price information

---------
### StorageClearingFailure
Storage clearing of `AllowedCurrencies` failed

---------
### WrongAssetToBuyout
Attempt to exchange native token to native token

---------

# ForeignInvestments

---------
## Events

---------
### ForeignInvestmentCleared
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investor | `T::AccountId` | ```AccountId```
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```

---------
### ForeignInvestmentUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investor | `T::AccountId` | ```AccountId```
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| state | `InvestState<Of<T>>` | ```{'NoState': None, 'InvestmentOngoing': {'invest_amount': 'u128'}, 'ActiveSwapIntoPoolCurrency': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}}, 'ActiveSwapIntoForeignCurrency': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}}, 'ActiveSwapIntoPoolCurrencyAndInvestmentOngoing': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}, 'invest_amount': 'u128'}, 'ActiveSwapIntoForeignCurrencyAndInvestmentOngoing': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}, 'invest_amount': 'u128'}, 'ActiveSwapIntoPoolCurrencyAndSwapIntoForeignDone': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}, 'done_amount': 'u128'}, 'ActiveSwapIntoForeignCurrencyAndSwapIntoForeignDone': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}, 'done_amount': 'u128'}, 'ActiveSwapIntoPoolCurrencyAndSwapIntoForeignDoneAndInvestmentOngoing': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}, 'done_amount': 'u128', 'invest_amount': 'u128'}, 'ActiveSwapIntoForeignCurrencyAndSwapIntoForeignDoneAndInvestmentOngoing': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}, 'done_amount': 'u128', 'invest_amount': 'u128'}, 'SwapIntoForeignDone': {'done_swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}}, 'SwapIntoForeignDoneAndInvestmentOngoing': {'done_swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}, 'invest_amount': 'u128'}}```

---------
### ForeignRedemptionCleared
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investor | `T::AccountId` | ```AccountId```
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```

---------
### ForeignRedemptionUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| investor | `T::AccountId` | ```AccountId```
| investment_id | `T::InvestmentId` | ```{'pool_id': 'u64', 'tranche_id': '[u8; 16]'}```
| state | `RedeemState<T::Balance, T::CurrencyId>` | ```{'NoState': None, 'Redeeming': {'redeem_amount': 'u128'}, 'ActiveSwapIntoForeignCurrency': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}}, 'ActiveSwapIntoForeignCurrencyAndSwapIntoForeignDone': {'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}, 'done_amount': 'u128'}, 'SwapIntoForeignDone': {'done_swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}}, 'RedeemingAndActiveSwapIntoForeignCurrency': {'redeem_amount': 'u128', 'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}}, 'RedeemingAndSwapIntoForeignDone': {'redeem_amount': 'u128', 'done_swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}}, 'RedeemingAndActiveSwapIntoForeignCurrencyAndSwapIntoForeignDone': {'redeem_amount': 'u128', 'swap': {'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}, 'amount': 'u128'}, 'done_amount': 'u128'}}```

---------
## Storage functions

---------
### CollectedInvestment
 Maps an investor and their `InvestmentId` to the collected investment
 amount, i.e., the payment amount of pool currency burned for the
 conversion into collected amount of tranche tokens based on the
 fulfillment price(s).

 NOTE: The lifetime of this storage starts with receiving a notification
 of an executed investment via the `CollectedInvestmentHook`. It ends
 with transferring the collected tranche tokens by executing
 `notify_executed_collect_invest` which is part of
 `collect_foreign_investment`.

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'CollectedInvestment', [
    'AccountId',
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{'amount_collected': 'u128', 'amount_payment': 'u128'}
```
---------
### CollectedRedemption
 Maps an investor and their `InvestmentId` to the collected redemption
 amount, i.e., the payment amount of tranche tokens burned for the
 conversion into collected pool currency based on the
 fulfillment price(s).

 NOTE: The lifetime of this storage starts with receiving a notification
 of an executed redemption collection into pool currency via the
 `CollectedRedemptionHook`. It ends with having swapped the entire amount
 to foreign currency which is assumed to be asynchronous.

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'CollectedRedemption', [
    'AccountId',
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{'amount_collected': 'u128', 'amount_payment': 'u128'}
```
---------
### ForeignInvestmentInfo
 Maps a token swap order id to the corresponding `ForeignInvestmentInfo`
 to implicitly enable mapping to `InvestmentState` and `RedemptionState`.

 NOTE: The storage is immediately killed when the swap order is
 completely fulfilled even if the corresponding investment and/or
 redemption might not be fully processed.

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'ForeignInvestmentInfo', ['u64']
)
```

#### Return value
```python
{
    'id': {'pool_id': 'u64', 'tranche_id': '[u8; 16]'},
    'last_swap_reason': (
        None,
        ('Investment', 'Redemption', 'InvestmentAndRedemption'),
    ),
    'owner': 'AccountId',
}
```
---------
### InvestmentPaymentCurrency
 Maps an investor and their investment id to the foreign payment currency
 provided on the initial investment increment.

 The lifetime is synchronized with the one of
 `InvestmentState`.

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'InvestmentPaymentCurrency', [
    'AccountId',
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{
    'Native': None,
    'Tranche': ('u64', '[u8; 16]'),
    None: None,
    'AUSD': None,
    'ForeignAsset': 'u32',
    'Staking': ('BlockRewards', ),
}
```
---------
### InvestmentState
 Maps an investor and their `InvestmentId` to the corresponding
 `InvestState`.

 NOTE: The lifetime of this storage starts with initializing a currency
 swap into the required pool currency and ends upon fully processing the
 investment after the potential swap. In case a swap is not required, the
 investment starts with `InvestState::InvestmentOngoing`.

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'InvestmentState', [
    'AccountId',
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{
    'ActiveSwapIntoForeignCurrency': {
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'ActiveSwapIntoForeignCurrencyAndInvestmentOngoing': {
        'invest_amount': 'u128',
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'ActiveSwapIntoForeignCurrencyAndSwapIntoForeignDone': {
        'done_amount': 'u128',
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'ActiveSwapIntoForeignCurrencyAndSwapIntoForeignDoneAndInvestmentOngoing': {
        'done_amount': 'u128',
        'invest_amount': 'u128',
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'ActiveSwapIntoPoolCurrency': {
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'ActiveSwapIntoPoolCurrencyAndInvestmentOngoing': {
        'invest_amount': 'u128',
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'ActiveSwapIntoPoolCurrencyAndSwapIntoForeignDone': {
        'done_amount': 'u128',
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'ActiveSwapIntoPoolCurrencyAndSwapIntoForeignDoneAndInvestmentOngoing': {
        'done_amount': 'u128',
        'invest_amount': 'u128',
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'InvestmentOngoing': {'invest_amount': 'u128'},
    'NoState': None,
    'SwapIntoForeignDone': {
        'done_swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'SwapIntoForeignDoneAndInvestmentOngoing': {
        'done_swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
        'invest_amount': 'u128',
    },
}
```
---------
### RedemptionPayoutCurrency
 Maps an investor and their investment id to the foreign payout currency
 requested on the initial redemption increment.

 The lifetime is synchronized with the one of
 `RedemptionState`.

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'RedemptionPayoutCurrency', [
    'AccountId',
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{
    'AUSD': None,
    'ForeignAsset': 'u32',
    'Native': None,
    'Tranche': ('u64', '[u8; 16]'),
    None: None,
    'Staking': ('BlockRewards', ),
}
```
---------
### RedemptionState
 Maps an investor and their `InvestmentId` to the corresponding
 `RedeemState`.

 NOTE: The lifetime of this storage starts with increasing a redemption
 which requires owning at least the amount of tranche tokens by which the
 redemption shall be increased by. It ends with transferring back
 the swapped return currency to the corresponding source domain from
 which the investment originated. The lifecycle must go through the
 following stages:
 	1. Increase redemption --&gt; Initialize storage
 	2. Fully process pending redemption
 	3. Collect redemption
 	4. Trigger swap from pool to return currency
 	5. Completely fulfill swap order
 	6. Transfer back to source domain --&gt; Kill storage entry

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'RedemptionState', [
    'AccountId',
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
{
    'ActiveSwapIntoForeignCurrency': {
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'ActiveSwapIntoForeignCurrencyAndSwapIntoForeignDone': {
        'done_amount': 'u128',
        'swap': {
            'amount': 'u128',
            'currency_in': {
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Native': None,
                'Staking': ('BlockRewards', ),
                'Tranche': ('u64', '[u8; 16]'),
            },
            'currency_out': {
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Native': None,
                'Staking': ('BlockRewards', ),
                'Tranche': ('u64', '[u8; 16]'),
            },
        },
    },
    'NoState': None,
    'Redeeming': {'redeem_amount': 'u128'},
    'RedeemingAndActiveSwapIntoForeignCurrency': {
        'redeem_amount': 'u128',
        'swap': {
            'amount': 'u128',
            'currency_in': {
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Native': None,
                'Staking': ('BlockRewards', ),
                'Tranche': ('u64', '[u8; 16]'),
            },
            'currency_out': {
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Native': None,
                'Staking': ('BlockRewards', ),
                'Tranche': ('u64', '[u8; 16]'),
            },
        },
    },
    'RedeemingAndActiveSwapIntoForeignCurrencyAndSwapIntoForeignDone': {
        'done_amount': 'u128',
        'redeem_amount': 'u128',
        'swap': {
            'amount': 'u128',
            'currency_in': {
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'Staking': ('BlockRewards', ),
            },
        },
    },
    'RedeemingAndSwapIntoForeignDone': {
        'done_swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
        'redeem_amount': 'u128',
    },
    'SwapIntoForeignDone': {
        'done_swap': {
            'amount': 'u128',
            'currency_in': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
            'currency_out': {
                'Native': None,
                'Tranche': ('u64', '[u8; 16]'),
                None: None,
                'AUSD': None,
                'ForeignAsset': 'u32',
                'Staking': ('BlockRewards', ),
            },
        },
    },
}
```
---------
### TokenSwapOrderIds
 Maps an investor and their `InvestmentId` to the corresponding
 `TokenSwapOrderId`.

 NOTE: The storage is immediately killed when the swap order is
 completely fulfilled even if the investment might not be fully
 processed.

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'TokenSwapOrderIds', [
    'AccountId',
    {
        'pool_id': 'u64',
        'tranche_id': '[u8; 16]',
    },
]
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### DefaultTokenSellRatio
 The default sell rate for token swaps which will be applied to all
 swaps created/updated through Foreign Investments.

 Example: Say this rate is set to 3/2, then the incoming currency
 should never cost more than 1.5 of the outgoing currency.

 NOTE: Can be removed once we implement a
 more sophisticated swap price discovery. For now, this should be set
 to one.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('ForeignInvestments', 'DefaultTokenSellRatio')
```
---------
## Errors

---------
### FulfilledTokenSwapAmountOverflow
The fulfilled token swap amount exceeds the sum of active swap
amounts of the corresponding `InvestmentState` and
`RedemptionState`.

---------
### InvestError
Failed to transition the `InvestState`.

---------
### InvestmentInfoNotFound
Failed to retrieve the `TokenSwapReason` from the given
`TokenSwapOrderId`.

---------
### InvestmentPaymentCurrencyNotFound
Failed to retrieve the foreign payment currency for a collected
investment.

NOTE: This error can only occur, if a user tries to collect before
having increased their investment as this would store the payment
currency.

---------
### PoolNotFound
Failed to retrieve the pool for the given pool id.

---------
### RedeemError
Failed to transition the `RedeemState.`

---------
### RedemptionPayoutCurrencyNotFound
Failed to retrieve the foreign payout currency for a collected
redemption.

NOTE: This error can only occur, if a user tries to collect before
having increased their redemption as this would store the payout
currency.

---------
### TokenSwapReasonNotFound
Failed to retrieve the `TokenSwapReason` from the given
`TokenSwapOrderId`.

---------
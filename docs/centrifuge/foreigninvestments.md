
# ForeignInvestments

---------
## Events

---------
### SwapCancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| swap_id | `SwapId<T>` | ```({'pool_id': 'u64', 'tranche_id': '[u8; 16]'}, ('Investment', 'Redemption'))```
| remaining | `SwapOf<T>` | ```{'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}, 'amount_out': 'u128'}```
| cancelled_in | `T::SwapBalance` | ```u128```
| opposite_in | `T::SwapBalance` | ```u128```

---------
### SwapCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| swap_id | `SwapId<T>` | ```({'pool_id': 'u64', 'tranche_id': '[u8; 16]'}, ('Investment', 'Redemption'))```
| swap | `SwapOf<T>` | ```{'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}, 'amount_out': 'u128'}```

---------
### SwapFullfilled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| swap_id | `SwapId<T>` | ```({'pool_id': 'u64', 'tranche_id': '[u8; 16]'}, ('Investment', 'Redemption'))```
| remaining | `SwapOf<T>` | ```{'currency_in': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}, 'currency_out': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}, 'amount_out': 'u128'}```
| swapped_in | `T::SwapBalance` | ```u128```
| swapped_out | `T::SwapBalance` | ```u128```

---------
## Storage functions

---------
### ForeignInvestmentInfo
 Contains the information about the foreign investment process

 NOTE: The storage is killed once the investment is fully collected, or
 decreased.

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'ForeignInvestmentInfo', [
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
    'correlation': {'foreign_amount': 'u128', 'pool_amount': 'u128'},
    'decrease_swapped_foreign_amount': 'u128',
    'foreign_currency': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Native': None,
        None: None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
}
```
---------
### ForeignRedemptionInfo
 Contains the information about the foreign redemption process

 NOTE: The storage is killed once the redemption is fully collected and
 fully swapped or decreased

#### Python
```python
result = substrate.query(
    'ForeignInvestments', 'ForeignRedemptionInfo', [
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
    'collected': {'amount_collected': 'u128', 'amount_payment': 'u128'},
    'foreign_currency': {
        'Native': None,
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Staking': ('BlockRewards', ),
    },
    'swapped_amount': 'u128',
}
```
---------
## Errors

---------
### InfoNotFound
Failed to retrieve the `ForeignInvestInfo`.

---------
### MismatchedForeignCurrency
An action for a different foreign currency is currently in process
for the same pool currency, account, and investment.
The currenct foreign actions must be finished before starting with a
different foreign currency investment / redemption.

---------
### PoolNotFound
Failed to retrieve the pool for the given pool id.

---------
### TooMuchDecrease
The decrease is greater than the current investment/redemption

---------
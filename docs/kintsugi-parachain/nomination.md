
# Nomination

---------
## Calls

---------
### deposit_collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| vault_id | `DefaultVaultId<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nomination', 'deposit_collateral', {
    'amount': 'u128',
    'vault_id': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            'wrapped': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        },
    },
}
)
```

---------
### opt_in_to_nomination
Allow nomination for this vault
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nomination', 'opt_in_to_nomination', {
    'currency_pair': {
        'collateral': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'wrapped': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    },
}
)
```

---------
### opt_out_of_nomination
Disallow nomination for this vault
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nomination', 'opt_out_of_nomination', {
    'currency_pair': {
        'collateral': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'wrapped': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    },
}
)
```

---------
### set_nomination_enabled
#### Attributes
| Name | Type |
| -------- | -------- | 
| enabled | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Nomination', 'set_nomination_enabled', {'enabled': 'bool'}
)
```

---------
### set_nomination_limit
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| limit | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Nomination', 'set_nomination_limit', {
    'currency_pair': {
        'collateral': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'wrapped': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    },
    'limit': 'u128',
}
)
```

---------
### withdraw_collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| vault_id | `DefaultVaultId<T>` | 
| amount | `BalanceOf<T>` | 
| index | `Option<T::Index>` | 

#### Python
```python
call = substrate.compose_call(
    'Nomination', 'withdraw_collateral', {
    'amount': 'u128',
    'index': (None, 'u32'),
    'vault_id': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            'wrapped': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        },
    },
}
)
```

---------
## Events

---------
### DepositCollateral
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```
| nominator_id | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### NominationOptIn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```

---------
### NominationOptOut
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```

---------
### WithdrawCollateral
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```
| nominator_id | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### NominationEnabled
 Flag indicating whether this feature is enabled

#### Python
```python
result = substrate.query(
    'Nomination', 'NominationEnabled', []
)
```

#### Return value
```python
'bool'
```
---------
### NominationLimit
 The maximum amount of collateral to be nominated for a given vault.

#### Python
```python
result = substrate.query(
    'Nomination', 'NominationLimit', [
    {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            'wrapped': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        },
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### Vaults
 Map of Vaults who have enabled nomination

#### Python
```python
result = substrate.query(
    'Nomination', 'Vaults', [
    {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            'wrapped': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        },
    },
]
)
```

#### Return value
```python
'bool'
```
---------
## Errors

---------
### CannotWithdrawCollateral
Account cannot withdraw.

---------
### CollateralizationTooLow
Vault cannot withdraw.

---------
### NominationExceedsLimit
Nomination would overburden Vault.

---------
### VaultAlreadyOptedInToNomination
Vault has already enabled nomination.

---------
### VaultNominationDisabled
Nomination is not enabled.

---------
### VaultNotFound
Vault not found.

---------
### VaultNotOptedInToNomination
Vault has not enabled nomination.

---------
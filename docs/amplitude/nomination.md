
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
                'XCM': 'u8',
            },
            'wrapped': {
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
                'XCM': 'u8',
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
            'XCM': 'u8',
        },
        'wrapped': {
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
            'XCM': 'u8',
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
            'XCM': 'u8',
        },
        'wrapped': {
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
            'XCM': 'u8',
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
                'XCM': 'u8',
            },
            'wrapped': {
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
                'XCM': 'u8',
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
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| nominator_id | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### NominationOptIn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```

---------
### NominationOptOut
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```

---------
### WithdrawCollateral
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
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
                'XCM': 'u8',
            },
            'wrapped': {
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
                'XCM': 'u8',
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
### DepositViolatesMaxNominationRatio
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
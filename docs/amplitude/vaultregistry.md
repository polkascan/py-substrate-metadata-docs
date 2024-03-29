
# VaultRegistry

---------
## Calls

---------
### accept_new_issues
Configures whether or not the vault accepts new issues.

\# Arguments

* `origin` - sender of the transaction (i.e. the vault)
* `accept_new_issues` - true indicates that the vault accepts new issues

\# Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| accept_new_issues | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'accept_new_issues', {
    'accept_new_issues': 'bool',
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
}
)
```

---------
### deposit_collateral
Deposit collateral as a security against stealing the
Stellar assets locked with the caller.

\# Arguments
* `amount` - the amount of extra collateral to lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'deposit_collateral', {
    'amount': 'u128',
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
}
)
```

---------
### recover_vault_id
Recover vault ID from a liquidated status.

\# Arguments
* `currency_pair` - the currency pair to change
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'recover_vault_id', {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
}
)
```

---------
### register_public_key
Registers a new Stellar address for the vault.

\# Arguments
* `public_key` - the Stellar public key of the vault to update
#### Attributes
| Name | Type |
| -------- | -------- | 
| public_key | `StellarPublicKeyRaw` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'register_public_key', {'public_key': '[u8; 32]'}
)
```

---------
### register_vault
Initiates the registration procedure for a new Vault.
The Vault locks up collateral, which is to be used in the issuing process.


\# Errors
* `InsufficientVaultCollateralAmount` - if the collateral is below the minimum threshold
* `VaultAlreadyRegistered` - if a vault is already registered for the origin account
* `InsufficientCollateralAvailable` - if the vault does not own enough collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| collateral | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'register_vault', {
    'collateral': 'u128',
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
}
)
```

---------
### report_undercollateralized_vault
#### Attributes
| Name | Type |
| -------- | -------- | 
| vault_id | `DefaultVaultId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'report_undercollateralized_vault', {
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
                'Token': 'u64',
                'XCM': 'u8',
                'ZenlinkLPToken': (
                    'u8',
                    'u8',
                    'u8',
                    'u8',
                ),
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
                'Token': 'u64',
                'XCM': 'u8',
                'ZenlinkLPToken': (
                    'u8',
                    'u8',
                    'u8',
                    'u8',
                ),
            },
        },
    },
}
)
```

---------
### set_custom_secure_threshold
Configures a custom, higher secure collateral threshold for the vault.

\# Arguments

* `origin` - sender of the transaction (i.e. the vault)
* `custom_threshold` - either the threshold, or None to use the systemwide default

\# Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| custom_threshold | `Option<UnsignedFixedPoint<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'set_custom_secure_threshold', {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
    'custom_threshold': (None, 'u128'),
}
)
```

---------
### set_liquidation_collateral_threshold
Changes the collateral liquidation threshold for a currency (only executable by the Root
account)

\# Arguments
* `currency_pair` - the currency pair to change
* `ceiling` - the new collateral ceiling
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| threshold | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'set_liquidation_collateral_threshold', {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
    'threshold': 'u128',
}
)
```

---------
### set_minimum_collateral
Changes the minimum amount of collateral required for registration
(only executable by the Root account)

\# Arguments
* `currency_id` - the collateral&\#x27;s currency id
* `minimum` - the new minimum collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyId<T>` | 
| minimum | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'set_minimum_collateral', {
    'currency_id': {
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
    'minimum': 'u128',
}
)
```

---------
### set_premium_redeem_threshold
Changes the collateral premium redeem threshold for a currency (only executable by the
Root account)

\# Arguments
* `currency_pair` - the currency pair to change
* `ceiling` - the new collateral ceiling
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| threshold | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'set_premium_redeem_threshold', {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
    'threshold': 'u128',
}
)
```

---------
### set_punishment_delay
#### Attributes
| Name | Type |
| -------- | -------- | 
| punishment_delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'set_punishment_delay', {'punishment_delay': 'u32'}
)
```

---------
### set_secure_collateral_threshold
Changes the secure threshold for a currency (only executable by the Root account)

\# Arguments
* `currency_pair` - the currency pair to change
* `threshold` - the new secure threshold
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| threshold | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'set_secure_collateral_threshold', {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
    'threshold': 'u128',
}
)
```

---------
### set_system_collateral_ceiling
Changes the collateral ceiling for a currency (only executable by the Root account)

\# Arguments
* `currency_pair` - the currency pair to change
* `ceiling` - the new collateral ceiling
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| ceiling | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'set_system_collateral_ceiling', {
    'ceiling': 'u128',
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
}
)
```

---------
### withdraw_collateral
Withdraws `amount` of the collateral from the amount locked by
the vault corresponding to the origin account
The collateral left after withdrawal must be more
(free or used in collateral issued tokens) than MinimumCollateralVault
and above the SecureCollateralThreshold. Collateral that is currently
being used to back issued tokens remains locked until the Vault
is used for a redeem request (full release can take multiple redeem requests).

\# Arguments
* `amount` - the amount of collateral to withdraw

\# Errors
* `VaultNotFound` - if no vault exists for the origin account
* `InsufficientCollateralAvailable` - if the vault does not own enough collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VaultRegistry', 'withdraw_collateral', {
    'amount': 'u128',
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
}
)
```

---------
## Events

---------
### BanVault
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| banned_until | `T::BlockNumber` | ```u32```

---------
### DecreaseLockedCollateral
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_pair | `DefaultVaultCurrencyPair<T>` | ```{'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}```
| delta | `BalanceOf<T>` | ```u128```
| total | `BalanceOf<T>` | ```u128```

---------
### DecreaseToBeIssuedTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| decrease | `BalanceOf<T>` | ```u128```

---------
### DecreaseToBeRedeemedTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| decrease | `BalanceOf<T>` | ```u128```

---------
### DecreaseToBeReplacedTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| decrease | `BalanceOf<T>` | ```u128```

---------
### DecreaseTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| user_id | `T::AccountId` | ```AccountId```
| decrease | `BalanceOf<T>` | ```u128```

---------
### DepositCollateral
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| new_collateral | `BalanceOf<T>` | ```u128```
| total_collateral | `BalanceOf<T>` | ```u128```
| free_collateral | `BalanceOf<T>` | ```u128```

---------
### IncreaseLockedCollateral
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| currency_pair | `DefaultVaultCurrencyPair<T>` | ```{'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}```
| delta | `BalanceOf<T>` | ```u128```
| total | `BalanceOf<T>` | ```u128```

---------
### IncreaseToBeIssuedTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| increase | `BalanceOf<T>` | ```u128```

---------
### IncreaseToBeRedeemedTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| increase | `BalanceOf<T>` | ```u128```

---------
### IncreaseToBeReplacedTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| increase | `BalanceOf<T>` | ```u128```

---------
### IssueTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| increase | `BalanceOf<T>` | ```u128```

---------
### LiquidateVault
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| issued_tokens | `BalanceOf<T>` | ```u128```
| to_be_issued_tokens | `BalanceOf<T>` | ```u128```
| to_be_redeemed_tokens | `BalanceOf<T>` | ```u128```
| to_be_replaced_tokens | `BalanceOf<T>` | ```u128```
| backing_collateral | `BalanceOf<T>` | ```u128```
| status | `VaultStatus` | ```{'Active': 'bool', 'Liquidated': None}```
| replace_collateral | `BalanceOf<T>` | ```u128```

---------
### RedeemTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| redeemed_amount | `BalanceOf<T>` | ```u128```

---------
### RedeemTokensLiquidatedVault
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| tokens | `BalanceOf<T>` | ```u128```
| collateral | `BalanceOf<T>` | ```u128```

---------
### RedeemTokensLiquidation
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer_id | `T::AccountId` | ```AccountId```
| burned_tokens | `BalanceOf<T>` | ```u128```
| transferred_collateral | `BalanceOf<T>` | ```u128```

---------
### RedeemTokensPremium
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| redeemed_amount | `BalanceOf<T>` | ```u128```
| collateral | `BalanceOf<T>` | ```u128```
| user_id | `T::AccountId` | ```AccountId```

---------
### RegisterAddress
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| address | `StellarPublicKeyRaw` | ```[u8; 32]```

---------
### RegisterVault
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| collateral | `BalanceOf<T>` | ```u128```

---------
### ReplaceTokens
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| new_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| amount | `BalanceOf<T>` | ```u128```
| additional_collateral | `BalanceOf<T>` | ```u128```

---------
### UpdatePublicKey
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| public_key | `StellarPublicKeyRaw` | ```[u8; 32]```

---------
### WithdrawCollateral
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'), 'Token': 'u64'}}}```
| withdrawn_amount | `BalanceOf<T>` | ```u128```
| total_collateral | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### LiquidationCollateralThreshold
 Determines the lower bound for the collateral rate in issued tokens. If a Vault’s
 collateral rate drops below this, automatic liquidation (forced Redeem) is triggered.

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'LiquidationCollateralThreshold', [
    {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
### LiquidationVault

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'LiquidationVault', [
    {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
        },
    },
]
)
```

#### Return value
```python
{
    'collateral': 'u128',
    'currency_pair': {
        'collateral': {
            'Native': None,
            'Stellar': {
                'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'},
                'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'},
                'StellarNative': None,
            },
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'),
        },
        'wrapped': {
            'Native': None,
            'Stellar': {
                'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'},
                'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'},
                'StellarNative': None,
            },
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'),
        },
    },
    'issued_tokens': 'u128',
    'to_be_issued_tokens': 'u128',
    'to_be_redeemed_tokens': 'u128',
}
```
---------
### MinimumCollateralVault
 The minimum collateral (e.g. DOT/KSM) a Vault needs to provide to register.

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'MinimumCollateralVault', [
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
'u128'
```
---------
### PremiumRedeemThreshold
 Determines the rate for the collateral rate of Vaults, at which users receive a premium,
 allocated from the Vault&#x27;s collateral, when performing a redeem with this Vault. This
 threshold should be greater than the LiquidationCollateralThreshold.

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'PremiumRedeemThreshold', [
    {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
### PunishmentDelay
 If a Vault fails to execute a correct redeem or replace, it is temporarily banned
 from further issue, redeem or replace requests. This value configures the duration
 of this ban (in number of blocks) .

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'PunishmentDelay', []
)
```

#### Return value
```python
'u32'
```
---------
### SecureCollateralThreshold
 Determines the over-collateralization rate for collateral locked by Vaults, necessary for
 wrapped tokens. This threshold should be greater than the LiquidationCollateralThreshold.

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'SecureCollateralThreshold', [
    {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
### SystemCollateralCeiling
 Determines the over-collateralization rate for collateral locked by Vaults, necessary for
 wrapped tokens. This threshold should be greater than the LiquidationCollateralThreshold.

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'SystemCollateralCeiling', [
    {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
### TotalUserVaultCollateral
 Total collateral used for collateral tokens issued by active vaults, excluding the
 liquidation vault

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'TotalUserVaultCollateral', [
    {
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
            'Token': 'u64',
            'XCM': 'u8',
            'ZenlinkLPToken': (
                'u8',
                'u8',
                'u8',
                'u8',
            ),
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
### VaultStellarPublicKey
 Mapping of Vaults, using the respective Vault account identifier as key.

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'VaultStellarPublicKey', ['AccountId']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### Vaults
 Mapping of Vaults, using the respective Vault account identifier as key.

#### Python
```python
result = substrate.query(
    'VaultRegistry', 'Vaults', [
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
                'Token': 'u64',
                'XCM': 'u8',
                'ZenlinkLPToken': (
                    'u8',
                    'u8',
                    'u8',
                    'u8',
                ),
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
                'Token': 'u64',
                'XCM': 'u8',
                'ZenlinkLPToken': (
                    'u8',
                    'u8',
                    'u8',
                    'u8',
                ),
            },
        },
    },
]
)
```

#### Return value
```python
{
    'active_replace_collateral': 'u128',
    'banned_until': (None, 'u32'),
    'id': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': 'InnerStruct',
                    'AlphaNum4': 'InnerStruct',
                    'StellarNative': None,
                },
                'Token': 'u64',
                'XCM': 'u8',
                'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'),
            },
            'wrapped': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': 'InnerStruct',
                    'AlphaNum4': 'InnerStruct',
                    'StellarNative': None,
                },
                'Token': 'u64',
                'XCM': 'u8',
                'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'),
            },
        },
    },
    'issued_tokens': 'u128',
    'liquidated_collateral': 'u128',
    'replace_collateral': 'u128',
    'secure_collateral_threshold': (None, 'u128'),
    'status': {'Active': 'bool', 'Liquidated': None},
    'to_be_issued_tokens': 'u128',
    'to_be_redeemed_tokens': 'u128',
    'to_be_replaced_tokens': 'u128',
}
```
---------
## Constants

---------
### GetGriefingCollateralCurrencyId
 Currency used for griefing collateral, e.g. DOT.
#### Value
```python
'Native'
```
#### Python
```python
constant = substrate.get_constant('VaultRegistry', 'GetGriefingCollateralCurrencyId')
```
---------
### PalletId
 The vault module id, used for deriving its sovereign account ID.
#### Value
```python
'0x6d6f642f76726567'
```
#### Python
```python
constant = substrate.get_constant('VaultRegistry', 'PalletId')
```
---------
## Errors

---------
### CeilingNotSet
Ceiling was not found for the given currency

---------
### CurrencyCeilingExceeded
The collateral ceiling would be exceeded for the vault&\#x27;s currency.

---------
### ExceedingVaultLimit
The amount of tokens to be issued is higher than the issuable amount by the vault

---------
### GlobalThresholdNotSet
Threshold was not found for the given currency

---------
### InsufficientCollateral
Not enough free collateral available.

---------
### InsufficientTokensCommitted
The requested amount of tokens exceeds the amount available to this vault.

---------
### InsufficientVaultCollateralAmount
The provided collateral was insufficient - it must be above ``MinimumCollateralVault``.

---------
### InvalidCurrency
Failed attempt to modify vault&\#x27;s collateral because it was in the wrong currency

---------
### InvalidPublicKey
Deposit address could not be generated with the given public key.

---------
### LiquidationCollateralThresholdNotSet
Threshold was not found for the given currency

---------
### MaxNominationRatioViolation
The Max Nomination Ratio would be exceeded.

---------
### MinimumCollateralNotSet

---------
### NoStellarPublicKey
No Stellar public key is registered for the vault.

---------
### NoTokensIssued
Collateralization is infinite if no tokens are issued

---------
### NoVaultUnderThePremiumRedeemThreshold

---------
### NoVaultWithSufficientCollateral

---------
### NoVaultWithSufficientTokens

---------
### PremiumRedeemThresholdNotSet
Threshold was not found for the given currency

---------
### PublicKeyAlreadyRegistered
A Stellar public key was already registered for this account.

---------
### SecureCollateralThresholdNotSet
Threshold was not found for the given currency

---------
### ThresholdNotAboveGlobalThreshold
Vault attempted to set secure threshold below the global secure threshold

---------
### TryIntoIntError
Unable to convert value

---------
### VaultAlreadyRegistered
Returned if a vault tries to register while already being registered

---------
### VaultBanned
Action not allowed on banned vault.

---------
### VaultLiquidated
Vault is no longer usable as it was liquidated due to undercollateralization.

---------
### VaultNotAcceptingIssueRequests
Vault is not accepting new issue requests.

---------
### VaultNotBelowLiquidationThreshold
Attempted to liquidate a vault that is not undercollateralized.

---------
### VaultNotFound
The specified vault does not exist.

---------
### VaultNotRecoverable
Vault must be liquidated.

---------
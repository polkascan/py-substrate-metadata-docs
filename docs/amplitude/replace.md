
# Replace

---------
## Calls

---------
### accept_replace
Accept request of vault replacement

\# Arguments

* `origin` - the initiator of the transaction: the new vault
* `currency_pair` - currency_pair of the new vault
* `amount` - amount of tokens to be replaced
* `collateral` - the collateral provided by the new vault to match the replace request
  (for backing the transferred tokens)
* `stellar_address` - the address that old-vault should transfer the wrapped asset to
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| old_vault | `DefaultVaultId<T>` | 
| amount | `BalanceOf<T>` | 
| collateral | `BalanceOf<T>` | 
| stellar_address | `StellarPublicKeyRaw` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'accept_replace', {
    'amount': 'u128',
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
    'old_vault': {
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
    'stellar_address': '[u8; 32]',
}
)
```

---------
### cancel_replace
Cancel vault replacement

\# Arguments

* `origin` - sender of the transaction: anyone
* `replace_id` - the ID of the replacement request
#### Attributes
| Name | Type |
| -------- | -------- | 
| replace_id | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'cancel_replace', {'replace_id': '[u8; 32]'}
)
```

---------
### execute_replace
Execute vault replacement

\# Arguments

* `origin` - sender of the transaction: the new vault
* `replace_id` - the ID of the replacement request
#### Attributes
| Name | Type |
| -------- | -------- | 
| replace_id | `H256` | 
| transaction_envelope_xdr_encoded | `Vec<u8>` | 
| externalized_envelopes_xdr_encoded | `Vec<u8>` | 
| transaction_set_xdr_encoded | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'execute_replace', {
    'externalized_envelopes_xdr_encoded': 'Bytes',
    'replace_id': '[u8; 32]',
    'transaction_envelope_xdr_encoded': 'Bytes',
    'transaction_set_xdr_encoded': 'Bytes',
}
)
```

---------
### minimum_transfer_amount_update
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_minimum_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'minimum_transfer_amount_update', {'new_minimum_amount': 'u128'}
)
```

---------
### request_replace
Request the replacement of a new vault ownership

\# Arguments

* `origin` - sender of the transaction
* `amount` - amount of issued tokens
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'request_replace', {
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
### set_replace_period
Set the default replace period for tx verification.

\# Arguments

* `origin` - the dispatch origin of this call (must be _Root_)
* `period` - default period for new requests

\# Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'set_replace_period', {'period': 'u32'}
)
```

---------
### withdraw_replace
Withdraw a request of vault replacement

\# Arguments

* `origin` - sender of the transaction: the old vault
* `amount` - amount of tokens to be withdrawn from being replaced
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'withdraw_replace', {
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
## Events

---------
### AcceptReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| replace_id | `H256` | ```[u8; 32]```
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| new_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| amount | `BalanceOf<T>` | ```u128```
| asset | `CurrencyId<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}```
| collateral | `BalanceOf<T>` | ```u128```
| stellar_address | `StellarPublicKeyRaw` | ```[u8; 32]```

---------
### CancelReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| replace_id | `H256` | ```[u8; 32]```
| new_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| griefing_collateral | `BalanceOf<T>` | ```u128```

---------
### ExecuteReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| replace_id | `H256` | ```[u8; 32]```
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| new_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```

---------
### ReplaceMinimumTransferAmountUpdate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_minimum_amount | `BalanceOf<T>` | ```u128```

---------
### ReplacePeriodChange
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| period | `T::BlockNumber` | ```u32```

---------
### RequestReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| amount | `BalanceOf<T>` | ```u128```
| asset | `CurrencyId<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}```
| griefing_collateral | `BalanceOf<T>` | ```u128```

---------
### WithdrawReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| withdrawn_tokens | `BalanceOf<T>` | ```u128```
| asset | `CurrencyId<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}```
| withdrawn_griefing_collateral | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ReplaceMinimumTransferAmount
 The minimum amount of wrapped assets that is accepted for replace requests

#### Python
```python
result = substrate.query(
    'Replace', 'ReplaceMinimumTransferAmount', []
)
```

#### Return value
```python
'u128'
```
---------
### ReplacePeriod
 The time difference in number of blocks between when a replace request is created
 and required completion time by a vault. The replace period has an upper limit
 to prevent griefing of vault collateral.

#### Python
```python
result = substrate.query(
    'Replace', 'ReplacePeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### ReplaceRequests
 Vaults create replace requests to transfer locked collateral.
 This mapping provides access from a unique hash to a `ReplaceRequest`.

#### Python
```python
result = substrate.query(
    'Replace', 'ReplaceRequests', ['[u8; 32]']
)
```

#### Return value
```python
{
    'accept_time': 'u32',
    'amount': 'u128',
    'asset': {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'},
            'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'},
            'StellarNative': None,
        },
        'XCM': 'u8',
    },
    'collateral': 'u128',
    'griefing_collateral': 'u128',
    'new_vault': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': 'InnerStruct',
                    'AlphaNum4': 'InnerStruct',
                    'StellarNative': None,
                },
                'XCM': 'u8',
            },
            'wrapped': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': 'InnerStruct',
                    'AlphaNum4': 'InnerStruct',
                    'StellarNative': None,
                },
                'XCM': 'u8',
            },
        },
    },
    'old_vault': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': 'InnerStruct',
                    'AlphaNum4': 'InnerStruct',
                    'StellarNative': None,
                },
                'XCM': 'u8',
            },
            'wrapped': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': 'InnerStruct',
                    'AlphaNum4': 'InnerStruct',
                    'StellarNative': None,
                },
                'XCM': 'u8',
            },
        },
    },
    'period': 'u32',
    'status': ('Pending', 'Completed', 'Cancelled'),
    'stellar_address': '[u8; 32]',
}
```
---------
## Errors

---------
### AmountBelowDustAmount
Replace amount is too small.

---------
### InvalidPaymentAmount
Invalid payment amount

---------
### InvalidWrappedCurrency
Vault cannot replace different currency.

---------
### NoPendingRequest
No replace request found.

---------
### ReplaceAmountZero
Replace requires non-zero increase.

---------
### ReplaceCancelled
Replace request already cancelled.

---------
### ReplaceCompleted
Replace request already completed.

---------
### ReplaceIdNotFound
Replace request not found.

---------
### ReplacePeriodNotExpired
Replace request has not expired.

---------
### ReplaceSelfNotAllowed
Cannot replace self.

---------
### UnauthorizedVault
Unexpected vault account.

---------
### VaultHasEnabledNomination
Cannot replace with nominated collateral.

---------
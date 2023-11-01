
# Identity

---------
## Calls

---------
### add_registrar
See [`Pallet::add_registrar`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'add_registrar', {
    'account': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### add_sub
See [`Pallet::add_sub`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| sub | `AccountIdLookupOf<T>` | 
| data | `Data` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'add_sub', {
    'data': {
        'BlakeTwo256': 'h256',
        'Keccak256': 'h256',
        'None': None,
        'Raw': 'Bytes',
        'Sha256': 'h256',
        'ShaThree256': 'h256',
    },
    'sub': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### cancel_request
See [`Pallet::cancel_request`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| reg_index | `RegistrarIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'cancel_request', {'reg_index': 'u32'}
)
```

---------
### clear_identity
See [`Pallet::clear_identity`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Identity', 'clear_identity', {}
)
```

---------
### force_insert_identities
See [`Pallet::force_insert_identities`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| identities | `Vec<(T::AccountId, RegistrationOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'force_insert_identities', {
    'identities': [
        (
            'AccountId',
            {
                'deposit': 'u128',
                'info': {
                    'additional': [
                        (
                            'scale_info::152',
                            'scale_info::152',
                        ),
                    ],
                    'display': {
                        'BlakeTwo256': 'h256',
                        'Keccak256': 'h256',
                        'None': None,
                        'Raw': 'Bytes',
                        'Sha256': 'h256',
                        'ShaThree256': 'h256',
                    },
                    'email': {
                        'BlakeTwo256': 'h256',
                        'Keccak256': 'h256',
                        'None': None,
                        'Raw': 'Bytes',
                        'Sha256': 'h256',
                        'ShaThree256': 'h256',
                    },
                    'image': {
                        'BlakeTwo256': 'h256',
                        'Keccak256': 'h256',
                        'None': None,
                        'Raw': 'Bytes',
                        'Sha256': 'h256',
                        'ShaThree256': 'h256',
                    },
                    'legal': {
                        'BlakeTwo256': 'h256',
                        'Keccak256': 'h256',
                        'None': None,
                        'Raw': 'Bytes',
                        'Sha256': 'h256',
                        'ShaThree256': 'h256',
                    },
                    'pgp_fingerprint': (
                        None,
                        '[u8; 20]',
                    ),
                    'riot': {
                        'BlakeTwo256': 'h256',
                        'Keccak256': 'h256',
                        'None': None,
                        'Raw': 'Bytes',
                        'Sha256': 'h256',
                        'ShaThree256': 'h256',
                    },
                    'twitter': {
                        'BlakeTwo256': 'h256',
                        'Keccak256': 'h256',
                        'None': None,
                        'Raw': 'Bytes',
                        'Sha256': 'h256',
                        'ShaThree256': 'h256',
                    },
                    'web': {
                        'BlakeTwo256': 'h256',
                        'Keccak256': 'h256',
                        'None': None,
                        'Raw': 'Bytes',
                        'Sha256': 'h256',
                        'ShaThree256': 'h256',
                    },
                },
                'judgements': [
                    (
                        'u32',
                        'scale_info::187',
                    ),
                ],
            },
        ),
    ],
}
)
```

---------
### force_remove_identities
See [`Pallet::force_remove_identities`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| identities | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'force_remove_identities', {'identities': ['AccountId']}
)
```

---------
### force_set_subs
See [`Pallet::force_set_subs`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| subs | `Vec<SubAccountsByAccountId<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'force_set_subs', {
    'subs': [
        (
            'AccountId',
            (
                'u128',
                [
                    (
                        'AccountId',
                        'scale_info::152',
                    ),
                ],
            ),
        ),
    ],
}
)
```

---------
### kill_identity
See [`Pallet::kill_identity`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'kill_identity', {
    'target': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### provide_judgement
See [`Pallet::provide_judgement`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| reg_index | `RegistrarIndex` | 
| target | `AccountIdLookupOf<T>` | 
| judgement | `Judgement<BalanceOf<T>>` | 
| identity | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'provide_judgement', {
    'identity': '[u8; 32]',
    'judgement': {
        'Erroneous': None,
        'FeePaid': 'u128',
        'KnownGood': None,
        'LowQuality': None,
        'OutOfDate': None,
        'Reasonable': None,
        'Unknown': None,
    },
    'reg_index': 'u32',
    'target': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### quit_sub
See [`Pallet::quit_sub`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Identity', 'quit_sub', {}
)
```

---------
### remove_sub
See [`Pallet::remove_sub`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| sub | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'remove_sub', {
    'sub': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### rename_sub
See [`Pallet::rename_sub`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| sub | `AccountIdLookupOf<T>` | 
| data | `Data` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'rename_sub', {
    'data': {
        'BlakeTwo256': 'h256',
        'Keccak256': 'h256',
        'None': None,
        'Raw': 'Bytes',
        'Sha256': 'h256',
        'ShaThree256': 'h256',
    },
    'sub': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### request_judgement
See [`Pallet::request_judgement`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| reg_index | `RegistrarIndex` | 
| max_fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'request_judgement', {
    'max_fee': 'u128',
    'reg_index': 'u32',
}
)
```

---------
### set_account_id
See [`Pallet::set_account_id`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `RegistrarIndex` | 
| new | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'set_account_id', {
    'index': 'u32',
    'new': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### set_fee
See [`Pallet::set_fee`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `RegistrarIndex` | 
| fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'set_fee', {'fee': 'u128', 'index': 'u32'}
)
```

---------
### set_fields
See [`Pallet::set_fields`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `RegistrarIndex` | 
| fields | `IdentityFields` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'set_fields', {'fields': 'u64', 'index': 'u32'}
)
```

---------
### set_identity
See [`Pallet::set_identity`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| info | `Box<IdentityInfo<T::MaxAdditionalFields>>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'set_identity', {
    'info': {
        'additional': [
            (
                {
                    'BlakeTwo256': 'h256',
                    'Keccak256': 'h256',
                    'None': None,
                    'Raw': 'Bytes',
                    'Sha256': 'h256',
                    'ShaThree256': 'h256',
                },
                {
                    'BlakeTwo256': 'h256',
                    'Keccak256': 'h256',
                    'None': None,
                    'Raw': 'Bytes',
                    'Sha256': 'h256',
                    'ShaThree256': 'h256',
                },
            ),
        ],
        'display': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'email': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'image': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'legal': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'pgp_fingerprint': (
            None,
            '[u8; 20]',
        ),
        'riot': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'twitter': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'web': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
    },
}
)
```

---------
### set_subs
See [`Pallet::set_subs`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| subs | `Vec<(T::AccountId, Data)>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'set_subs', {
    'subs': [
        (
            'AccountId',
            {
                'BlakeTwo256': 'h256',
                'Keccak256': 'h256',
                'None': None,
                'Raw': 'Bytes',
                'Sha256': 'h256',
                'ShaThree256': 'h256',
            },
        ),
    ],
}
)
```

---------
## Events

---------
### IdentitiesInserted
A number of identities and associated info were forcibly inserted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `u32` | ```u32```

---------
### IdentitiesRemoved
A number of identities and all associated info were forcibly removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `u32` | ```u32```

---------
### IdentityCleared
A name was cleared, and the given balance returned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### IdentityKilled
A name was removed and the given balance slashed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### IdentitySet
A name was set or reset (which will remove all judgements).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### JudgementGiven
A judgement was given by a registrar.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| target | `T::AccountId` | ```AccountId```
| registrar_index | `RegistrarIndex` | ```u32```

---------
### JudgementRequested
A judgement was asked from a registrar.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| registrar_index | `RegistrarIndex` | ```u32```

---------
### JudgementUnrequested
A judgement request was retracted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| registrar_index | `RegistrarIndex` | ```u32```

---------
### RegistrarAdded
A registrar was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| registrar_index | `RegistrarIndex` | ```u32```

---------
### SubIdentitiesInserted
A number of identities were forcibly updated with new sub-identities.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `u32` | ```u32```

---------
### SubIdentityAdded
A sub-identity was added to an identity and the deposit paid.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sub | `T::AccountId` | ```AccountId```
| main | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### SubIdentityRemoved
A sub-identity was removed from an identity and the deposit freed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sub | `T::AccountId` | ```AccountId```
| main | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### SubIdentityRevoked
A sub-identity was cleared, and the given deposit repatriated from the
main identity account to the sub-identity account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sub | `T::AccountId` | ```AccountId```
| main | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### IdentityOf
 Information that is pertinent to identify the entity behind an account.

 TWOX-NOTE: OK ― `AccountId` is a secure hash.

#### Python
```python
result = substrate.query(
    'Identity', 'IdentityOf', ['AccountId']
)
```

#### Return value
```python
{
    'deposit': 'u128',
    'info': {
        'additional': [('scale_info::152', 'scale_info::152')],
        'display': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'email': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'image': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'legal': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'pgp_fingerprint': (None, '[u8; 20]'),
        'riot': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'twitter': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
        'web': {
            'BlakeTwo256': 'h256',
            'Keccak256': 'h256',
            'None': None,
            'Raw': 'Bytes',
            'Sha256': 'h256',
            'ShaThree256': 'h256',
        },
    },
    'judgements': [
        (
            'u32',
            {
                'Erroneous': None,
                'FeePaid': 'u128',
                'KnownGood': None,
                'LowQuality': None,
                'OutOfDate': None,
                'Reasonable': None,
                'Unknown': None,
            },
        ),
    ],
}
```
---------
### Registrars
 The set of registrars. Not expected to get very big as can only be added through a
 special origin (likely a council motion).

 The index into this can be cast to `RegistrarIndex` to get a valid value.

#### Python
```python
result = substrate.query(
    'Identity', 'Registrars', []
)
```

#### Return value
```python
[(None, {'account': 'AccountId', 'fee': 'u128', 'fields': 'u64'})]
```
---------
### SubsOf
 Alternative &quot;sub&quot; identities of this account.

 The first item is the deposit, the second is a vector of the accounts.

 TWOX-NOTE: OK ― `AccountId` is a secure hash.

#### Python
```python
result = substrate.query(
    'Identity', 'SubsOf', ['AccountId']
)
```

#### Return value
```python
('u128', ['AccountId'])
```
---------
### SuperOf
 The super-identity of an alternative &quot;sub&quot; identity together with its name, within that
 context. If the account is not some other account&#x27;s sub-identity, then just `None`.

#### Python
```python
result = substrate.query(
    'Identity', 'SuperOf', ['AccountId']
)
```

#### Return value
```python
(
    'AccountId',
    {
        'BlakeTwo256': 'h256',
        'Keccak256': 'h256',
        'None': None,
        'Raw': 'Bytes',
        'Sha256': 'h256',
        'ShaThree256': 'h256',
    },
)
```
---------
## Constants

---------
### BasicDeposit
 The amount held on deposit for a registered identity
#### Value
```python
10000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Identity', 'BasicDeposit')
```
---------
### FieldDeposit
 The amount held on deposit per additional field for a registered identity.
#### Value
```python
25000000000000000
```
#### Python
```python
constant = substrate.get_constant('Identity', 'FieldDeposit')
```
---------
### MaxAdditionalFields
 Maximum number of additional fields that may be stored in an ID. Needed to bound the I/O
 required to access an identity, but can be pretty high.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Identity', 'MaxAdditionalFields')
```
---------
### MaxRegistrars
 Maxmimum number of registrars allowed in the system. Needed to bound the complexity
 of, e.g., updating judgements.
#### Value
```python
20
```
#### Python
```python
constant = substrate.get_constant('Identity', 'MaxRegistrars')
```
---------
### MaxSubAccounts
 The maximum number of sub-accounts allowed per identified account.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Identity', 'MaxSubAccounts')
```
---------
### SubAccountDeposit
 The amount held on deposit for a registered subaccount. This should account for the fact
 that one storage item&#x27;s value will increase by the size of an account ID, and there will
 be another trie item whose value is the size of an account ID plus 32 bytes.
#### Value
```python
2000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Identity', 'SubAccountDeposit')
```
---------
## Errors

---------
### AlreadyClaimed
Account ID is already named.

---------
### EmptyIndex
Empty index.

---------
### FeeChanged
Fee is changed.

---------
### InvalidIndex
The index is invalid.

---------
### InvalidJudgement
Invalid judgement.

---------
### InvalidTarget
The target is invalid.

---------
### JudgementForDifferentIdentity
The provided judgement was for a different identity.

---------
### JudgementGiven
Judgement given.

---------
### JudgementPaymentFailed
Error that occurs when there is an issue paying for judgement.

---------
### NoIdentity
No identity found.

---------
### NotFound
Account isn&\#x27;t found.

---------
### NotNamed
Account isn&\#x27;t named.

---------
### NotOwned
Sub-account isn&\#x27;t owned by sender.

---------
### NotSub
Sender is not a sub-account.

---------
### StickyJudgement
Sticky judgement.

---------
### TooManyFields
Too many additional fields.

---------
### TooManyRegistrars
Maximum amount of registrars reached. Cannot add any more.

---------
### TooManySubAccounts
Too many subs-accounts.

---------
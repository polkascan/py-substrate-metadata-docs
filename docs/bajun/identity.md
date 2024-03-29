
# Identity

---------
## Calls

---------
### accept_username
See [`Pallet::accept_username`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| username | `Username<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'accept_username', {'username': 'Bytes'}
)
```

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
### add_username_authority
See [`Pallet::add_username_authority`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| authority | `AccountIdLookupOf<T>` | 
| suffix | `Vec<u8>` | 
| allocation | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'add_username_authority', {
    'allocation': 'u32',
    'authority': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'suffix': 'Bytes',
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
    'identity': 'scale_info::12',
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
### remove_dangling_username
See [`Pallet::remove_dangling_username`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| username | `Username<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'remove_dangling_username', {'username': 'Bytes'}
)
```

---------
### remove_expired_approval
See [`Pallet::remove_expired_approval`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| username | `Username<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'remove_expired_approval', {'username': 'Bytes'}
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
### remove_username_authority
See [`Pallet::remove_username_authority`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| authority | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'remove_username_authority', {
    'authority': {
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
| fields | `<T::IdentityInformation as IdentityInformationProvider>::
FieldsIdentifier` | 

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
| info | `Box<T::IdentityInformation>` | 

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
### set_primary_username
See [`Pallet::set_primary_username`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| username | `Username<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'set_primary_username', {'username': 'Bytes'}
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
### set_username_for
See [`Pallet::set_username_for`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| username | `Vec<u8>` | 
| signature | `Option<T::OffchainSignature>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'set_username_for', {
    'signature': (
        None,
        {
            'Ecdsa': '[u8; 65]',
            'Ed25519': '[u8; 64]',
            'Sr25519': '[u8; 64]',
        },
    ),
    'username': 'Bytes',
    'who': {
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
## Events

---------
### AuthorityAdded
A username authority was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| authority | `T::AccountId` | ```AccountId```

---------
### AuthorityRemoved
A username authority was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| authority | `T::AccountId` | ```AccountId```

---------
### DanglingUsernameRemoved
A dangling username (as in, a username corresponding to an account that has removed its
identity) has been removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| username | `Username<T>` | ```Bytes```

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
### PreapprovalExpired
A queued username passed its expiration without being claimed and was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| whose | `T::AccountId` | ```AccountId```

---------
### PrimaryUsernameSet
A username was set as a primary and can be looked up from `who`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| username | `Username<T>` | ```Bytes```

---------
### RegistrarAdded
A registrar was added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| registrar_index | `RegistrarIndex` | ```u32```

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
### UsernameQueued
A username was queued, but `who` must accept it prior to `expiration`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| username | `Username<T>` | ```Bytes```
| expiration | `BlockNumberFor<T>` | ```u32```

---------
### UsernameSet
A username was set for `who`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| username | `Username<T>` | ```Bytes```

---------
## Storage functions

---------
### AccountOfUsername
 Reverse lookup from `username` to the `AccountId` that has registered it. The value should
 be a key in the `IdentityOf` map, but it may not if the user has cleared their identity.

 Multiple usernames may map to the same `AccountId`, but `IdentityOf` will only map to one
 primary username.

#### Python
```python
result = substrate.query(
    'Identity', 'AccountOfUsername', ['Bytes']
)
```

#### Return value
```python
'AccountId'
```
---------
### IdentityOf
 Information that is pertinent to identify the entity behind an account. First item is the
 registration, second is the account&#x27;s primary username.

 TWOX-NOTE: OK ― `AccountId` is a secure hash.

#### Python
```python
result = substrate.query(
    'Identity', 'IdentityOf', ['AccountId']
)
```

#### Return value
```python
(
    {
        'deposit': 'u128',
        'info': {
            'additional': [('scale_info::257', 'scale_info::257')],
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
        'judgements': [('u32', 'scale_info::290')],
    },
    (None, 'Bytes'),
)
```
---------
### PendingUsernames
 Usernames that an authority has granted, but that the account controller has not confirmed
 that they want it. Used primarily in cases where the `AccountId` cannot provide a signature
 because they are a pure proxy, multisig, etc. In order to confirm it, they should call
 [`Call::accept_username`].

 First tuple item is the account and second is the acceptance deadline.

#### Python
```python
result = substrate.query(
    'Identity', 'PendingUsernames', ['Bytes']
)
```

#### Return value
```python
('AccountId', 'u32')
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
### UsernameAuthorities
 A map of the accounts who are authorized to grant usernames.

#### Python
```python
result = substrate.query(
    'Identity', 'UsernameAuthorities', ['AccountId']
)
```

#### Return value
```python
{'allocation': 'u32', 'suffix': 'Bytes'}
```
---------
## Constants

---------
### BasicDeposit
 The amount held on deposit for a registered identity.
#### Value
```python
20258000000000
```
#### Python
```python
constant = substrate.get_constant('Identity', 'BasicDeposit')
```
---------
### ByteDeposit
 The amount held on deposit per encoded byte for a registered identity.
#### Value
```python
66000000000
```
#### Python
```python
constant = substrate.get_constant('Identity', 'ByteDeposit')
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
### MaxSuffixLength
 The maximum length of a suffix.
#### Value
```python
7
```
#### Python
```python
constant = substrate.get_constant('Identity', 'MaxSuffixLength')
```
---------
### MaxUsernameLength
 The maximum length of a username, including its suffix and any system-added delimiters.
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Identity', 'MaxUsernameLength')
```
---------
### PendingUsernameExpiration
 The number of blocks within which a username grant must be accepted.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Identity', 'PendingUsernameExpiration')
```
---------
### SubAccountDeposit
 The amount held on deposit for a registered subaccount. This should account for the fact
 that one storage item&#x27;s value will increase by the size of an account ID, and there will
 be another trie item whose value is the size of an account ID plus 32 bytes.
#### Value
```python
20053000000000
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
### InvalidSignature
The signature on a username was not valid.

---------
### InvalidSuffix
The provided suffix is too long.

---------
### InvalidTarget
The target is invalid.

---------
### InvalidUsername
The username does not meet the requirements.

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
### NoAllocation
The authority cannot allocate any more usernames.

---------
### NoIdentity
No identity found.

---------
### NoUsername
The requested username does not exist.

---------
### NotExpired
The username cannot be forcefully removed because it can still be accepted.

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
### NotUsernameAuthority
The sender does not have permission to issue a username.

---------
### RequiresSignature
Setting this username requires a signature, but none was provided.

---------
### StickyJudgement
Sticky judgement.

---------
### TooManyRegistrars
Maximum amount of registrars reached. Cannot add any more.

---------
### TooManySubAccounts
Too many subs-accounts.

---------
### UsernameTaken
The username is already taken.

---------
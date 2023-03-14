
# Identity

---------
## Calls

---------
### add_registrar
Add a registrar to the system.

The dispatch origin for this call must be `T::RegistrarOrigin`.

- `account`: the account of the registrar.

Emits `RegistrarAdded` if successful.

\# &lt;weight&gt;
- `O(R)` where `R` registrar-count (governance-bounded and code-bounded).
- One storage mutation (codec `O(R)`).
- One event.
\# &lt;/weight&gt;
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
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### add_sub
Add the given account to the sender&\#x27;s subs.

Payment: Balance reserved by a previous `set_subs` call for one sub will be repatriated
to the sender.

The dispatch origin for this call must be _Signed_ and the sender must have a registered
sub identity of `sub`.
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
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### cancel_request
Cancel a previous request.

Payment: A previously reserved deposit is returned on success.

The dispatch origin for this call must be _Signed_ and the sender must have a
registered identity.

- `reg_index`: The index of the registrar whose judgement is no longer requested.

Emits `JudgementUnrequested` if successful.

\# &lt;weight&gt;
- `O(R + X)`.
- One balance-reserve operation.
- One storage mutation `O(R + X)`.
- One event
\# &lt;/weight&gt;
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
Clear an account&\#x27;s identity info and all sub-accounts and return all deposits.

Payment: All reserved balances on the account are returned.

The dispatch origin for this call must be _Signed_ and the sender must have a registered
identity.

Emits `IdentityCleared` if successful.

\# &lt;weight&gt;
- `O(R + S + X)`
  - where `R` registrar-count (governance-bounded).
  - where `S` subs-count (hard- and deposit-bounded).
  - where `X` additional-field-count (deposit-bounded and code-bounded).
- One balance-unreserve operation.
- `2` storage reads and `S + 2` storage deletions.
- One event.
\# &lt;/weight&gt;
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
Remove an account&\#x27;s identity and sub-account information and slash the deposits.

Payment: Reserved balances from `set_subs` and `set_identity` are slashed and handled by
`Slash`. Verification request deposits are not returned; they should be cancelled
manually using `cancel_request`.

The dispatch origin for this call must match `T::ForceOrigin`.

- `target`: the account whose identity the judgement is upon. This must be an account
  with a registered identity.

Emits `IdentityKilled` if successful.

\# &lt;weight&gt;
- `O(R + S + X)`.
- One balance-reserve operation.
- `S + 2` storage mutations.
- One event.
\# &lt;/weight&gt;
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
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### provide_judgement
Provide a judgement for an account&\#x27;s identity.

The dispatch origin for this call must be _Signed_ and the sender must be the account
of the registrar whose index is `reg_index`.

- `reg_index`: the index of the registrar whose judgement is being made.
- `target`: the account whose identity the judgement is upon. This must be an account
  with a registered identity.
- `judgement`: the judgement of the registrar of index `reg_index` about `target`.
- `identity`: The hash of the [`IdentityInfo`] for that the judgement is provided.

Emits `JudgementGiven` if successful.

\# &lt;weight&gt;
- `O(R + X)`.
- One balance-transfer operation.
- Up to one account-lookup operation.
- Storage: 1 read `O(R)`, 1 mutate `O(R + X)`.
- One event.
\# &lt;/weight&gt;
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
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### quit_sub
Remove the sender as a sub-account.

Payment: Balance reserved by a previous `set_subs` call for one sub will be repatriated
to the sender (*not* the original depositor).

The dispatch origin for this call must be _Signed_ and the sender must have a registered
super-identity.

NOTE: This should not normally be used, but is provided in the case that the non-
controller of an account is maliciously registered as a sub-account.
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
Remove the given account from the sender&\#x27;s subs.

Payment: Balance reserved by a previous `set_subs` call for one sub will be repatriated
to the sender.

The dispatch origin for this call must be _Signed_ and the sender must have a registered
sub identity of `sub`.
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
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### rename_sub
Alter the associated name of the given sub-account.

The dispatch origin for this call must be _Signed_ and the sender must have a registered
sub identity of `sub`.
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
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### request_judgement
Request a judgement from a registrar.

Payment: At most `max_fee` will be reserved for payment to the registrar if judgement
given.

The dispatch origin for this call must be _Signed_ and the sender must have a
registered identity.

- `reg_index`: The index of the registrar whose judgement is requested.
- `max_fee`: The maximum fee that may be paid. This should just be auto-populated as:

```nocompile
Self::registrars().get(reg_index).unwrap().fee
```

Emits `JudgementRequested` if successful.

\# &lt;weight&gt;
- `O(R + X)`.
- One balance-reserve operation.
- Storage: 1 read `O(R)`, 1 mutate `O(X + R)`.
- One event.
\# &lt;/weight&gt;
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
Change the account associated with a registrar.

The dispatch origin for this call must be _Signed_ and the sender must be the account
of the registrar whose index is `index`.

- `index`: the index of the registrar whose fee is to be set.
- `new`: the new account ID.

\# &lt;weight&gt;
- `O(R)`.
- One storage mutation `O(R)`.
- Benchmark: 8.823 + R * 0.32 µs (min squares analysis)
\# &lt;/weight&gt;
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
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### set_fee
Set the fee required for a judgement to be requested from a registrar.

The dispatch origin for this call must be _Signed_ and the sender must be the account
of the registrar whose index is `index`.

- `index`: the index of the registrar whose fee is to be set.
- `fee`: the new fee.

\# &lt;weight&gt;
- `O(R)`.
- One storage mutation `O(R)`.
- Benchmark: 7.315 + R * 0.329 µs (min squares analysis)
\# &lt;/weight&gt;
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
Set the field information for a registrar.

The dispatch origin for this call must be _Signed_ and the sender must be the account
of the registrar whose index is `index`.

- `index`: the index of the registrar whose fee is to be set.
- `fields`: the fields that the registrar concerns themselves with.

\# &lt;weight&gt;
- `O(R)`.
- One storage mutation `O(R)`.
- Benchmark: 7.464 + R * 0.325 µs (min squares analysis)
\# &lt;/weight&gt;
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
Set an account&\#x27;s identity information and reserve the appropriate deposit.

If the account already has identity information, the deposit is taken as part payment
for the new deposit.

The dispatch origin for this call must be _Signed_.

- `info`: The identity information.

Emits `IdentitySet` if successful.

\# &lt;weight&gt;
- `O(X + X&\#x27; + R)`
  - where `X` additional-field-count (deposit-bounded and code-bounded)
  - where `R` judgements-count (registrar-count-bounded)
- One balance reserve operation.
- One storage mutation (codec-read `O(X&\#x27; + R)`, codec-write `O(X + R)`).
- One event.
\# &lt;/weight&gt;
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
Set the sub-accounts of the sender.

Payment: Any aggregate balance reserved by previous `set_subs` calls will be returned
and an amount `SubAccountDeposit` will be reserved for each item in `subs`.

The dispatch origin for this call must be _Signed_ and the sender must have a registered
identity.

- `subs`: The identity&\#x27;s (new) sub-accounts.

\# &lt;weight&gt;
- `O(P + S)`
  - where `P` old-subs-count (hard- and deposit-bounded).
  - where `S` subs-count (hard- and deposit-bounded).
- At most one balance operations.
- DB:
  - `P + S` storage mutations (codec complexity `O(1)`)
  - One storage read (codec complexity `O(P)`).
  - One storage write (codec complexity `O(S)`).
  - One storage-exists (`IdentityOf::contains_key`).
\# &lt;/weight&gt;
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
15630000000000
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
3960000000000
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
3330000000000
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
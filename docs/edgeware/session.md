
# Session

---------
## Calls

---------
### purge_keys
Removes any session key(s) of the function caller.

This doesn&\#x27;t take effect until the next session.

The dispatch origin of this function must be Signed and the account must be either be
convertible to a validator ID using the chain&\#x27;s typical addressing system (this usually
means being a controller account) or directly convertible into a validator ID (which
usually means being a stash account).

\# &lt;weight&gt;
- Complexity: `O(1)` in number of key types. Actual cost depends on the number of length
  of `T::Keys::key_ids()` which is fixed.
- DbReads: `T::ValidatorIdOf`, `NextKeys`, `origin account`
- DbWrites: `NextKeys`, `origin account`
- DbWrites per key id: `KeyOwner`
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Session', 'purge_keys', {}
)
```

---------
### set_keys
Sets the session key(s) of the function caller to `keys`.
Allows an account to set its session key prior to becoming a validator.
This doesn&\#x27;t take effect until the next session.

The dispatch origin of this function must be signed.

\# &lt;weight&gt;
- Complexity: `O(1)`. Actual cost depends on the number of length of
  `T::Keys::key_ids()` which is fixed.
- DbReads: `origin account`, `T::ValidatorIdOf`, `NextKeys`
- DbWrites: `origin account`, `NextKeys`
- DbReads per key id: `KeyOwner`
- DbWrites per key id: `KeyOwner`
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| keys | `T::Keys` | 
| proof | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Session', 'set_keys', {
    'keys': {
        'aura': '[u8; 32]',
        'authority_discovery': '[u8; 32]',
        'grandpa': '[u8; 32]',
        'im_online': '[u8; 32]',
    },
    'proof': 'Bytes',
}
)
```

---------
## Events

---------
### NewSession
New session has happened. Note that the argument is the session index, not the
block number as the type might suggest.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session_index | `SessionIndex` | ```u32```

---------
## Storage functions

---------
### CurrentIndex
 Current index of the session.

#### Python
```python
result = substrate.query(
    'Session', 'CurrentIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### DisabledValidators
 Indices of disabled validators.

 The vec is always kept sorted so that we can find whether a given validator is
 disabled using binary search. It gets cleared when `on_session_ending` returns
 a new set of identities.

#### Python
```python
result = substrate.query(
    'Session', 'DisabledValidators', []
)
```

#### Return value
```python
['u32']
```
---------
### KeyOwner
 The owner of a key. The key is the `KeyTypeId` + the encoded key.

#### Python
```python
result = substrate.query(
    'Session', 'KeyOwner', [('[u8; 4]', 'Bytes')]
)
```

#### Return value
```python
'AccountId'
```
---------
### NextKeys
 The next session keys for a validator.

#### Python
```python
result = substrate.query(
    'Session', 'NextKeys', ['AccountId']
)
```

#### Return value
```python
{
    'aura': '[u8; 32]',
    'authority_discovery': '[u8; 32]',
    'grandpa': '[u8; 32]',
    'im_online': '[u8; 32]',
}
```
---------
### QueuedChanged
 True if the underlying economic identities or weighting behind the validators
 has changed in the queued validator set.

#### Python
```python
result = substrate.query(
    'Session', 'QueuedChanged', []
)
```

#### Return value
```python
'bool'
```
---------
### QueuedKeys
 The queued keys for the next session. When the next session begins, these keys
 will be used to determine the validator&#x27;s session keys.

#### Python
```python
result = substrate.query(
    'Session', 'QueuedKeys', []
)
```

#### Return value
```python
[
    (
        'AccountId',
        {
            'aura': '[u8; 32]',
            'authority_discovery': '[u8; 32]',
            'grandpa': '[u8; 32]',
            'im_online': '[u8; 32]',
        },
    ),
]
```
---------
### Validators
 The current set of validators.

#### Python
```python
result = substrate.query(
    'Session', 'Validators', []
)
```

#### Return value
```python
['AccountId']
```
---------
## Errors

---------
### DuplicatedKey
Registered duplicate key.

---------
### InvalidProof
Invalid ownership proof.

---------
### NoAccount
Key setting account is not live, so it&\#x27;s impossible to associate keys.

---------
### NoAssociatedValidatorId
No associated validator ID for account.

---------
### NoKeys
No keys are associated with this account.

---------
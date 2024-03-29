
# DidLookup

---------
## Calls

---------
### associate_account
See [`Pallet::associate_account`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| req | `AssociateAccountRequest` | 
| expiration | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'associate_account', {
    'expiration': 'u64',
    'req': {
        'Ethereum': (
            '[u8; 20]',
            '[u8; 65]',
        ),
        'Polkadot': (
            'AccountId',
            {
                'Ecdsa': '[u8; 65]',
                'Ed25519': '[u8; 64]',
                'Sr25519': '[u8; 64]',
            },
        ),
    },
}
)
```

---------
### associate_sender
See [`Pallet::associate_sender`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'associate_sender', {}
)
```

---------
### change_deposit_owner
See [`Pallet::change_deposit_owner`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `LinkableAccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'change_deposit_owner', {
    'account': {
        'AccountId20': '[u8; 20]',
        'AccountId32': 'AccountId',
    },
}
)
```

---------
### reclaim_deposit
See [`Pallet::reclaim_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `LinkableAccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'reclaim_deposit', {
    'account': {
        'AccountId20': '[u8; 20]',
        'AccountId32': 'AccountId',
    },
}
)
```

---------
### remove_account_association
See [`Pallet::remove_account_association`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `LinkableAccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'remove_account_association', {
    'account': {
        'AccountId20': '[u8; 20]',
        'AccountId32': 'AccountId',
    },
}
)
```

---------
### remove_sender_association
See [`Pallet::remove_sender_association`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'remove_sender_association', {}
)
```

---------
### update_deposit
See [`Pallet::update_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `LinkableAccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'update_deposit', {
    'account': {
        'AccountId20': '[u8; 20]',
        'AccountId32': 'AccountId',
    },
}
)
```

---------
## Events

---------
### AssociationEstablished
A new association between a DID and an account ID was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `LinkableAccountId` | ```{'AccountId20': '[u8; 20]', 'AccountId32': 'AccountId'}```
| None | `DidIdentifierOf<T>` | ```AccountId```

---------
### AssociationRemoved
An association between a DID and an account ID was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `LinkableAccountId` | ```{'AccountId20': '[u8; 20]', 'AccountId32': 'AccountId'}```
| None | `DidIdentifierOf<T>` | ```AccountId```

---------
### MigrationCompleted
All AccountIds have been migrated to LinkableAccountId.
#### Attributes
No attributes

---------
### MigrationProgress
There was some progress in the migration process.
#### Attributes
No attributes

---------
## Storage functions

---------
### ConnectedAccounts
 Mapping from (DID + account identifier) -&gt; ().
 The empty tuple is used as a sentinel value to simply indicate the
 presence of a given tuple in the map.

#### Python
```python
result = substrate.query(
    'DidLookup', 'ConnectedAccounts', [
    'AccountId',
    {
        'AccountId20': '[u8; 20]',
        'AccountId32': 'AccountId',
    },
]
)
```

#### Return value
```python
()
```
---------
### ConnectedDids
 Mapping from account identifiers to DIDs.

#### Python
```python
result = substrate.query(
    'DidLookup', 'ConnectedDids', [
    {
        'AccountId20': '[u8; 20]',
        'AccountId32': 'AccountId',
    },
]
)
```

#### Return value
```python
{'deposit': {'amount': 'u128', 'owner': 'AccountId'}, 'did': 'AccountId'}
```
---------
## Constants

---------
### Deposit
 The amount of balance that will be taken for each DID as a deposit
 to incentivise fair use of the on chain storage. The deposit can be
 reclaimed when the DID is deleted.
#### Value
```python
60000000000000
```
#### Python
```python
constant = substrate.get_constant('DidLookup', 'Deposit')
```
---------
## Errors

---------
### InsufficientFunds
The account has insufficient funds and can&\#x27;t pay the fees or reserve
the deposit.

---------
### Migration
The ConnectedAccounts and ConnectedDids storage are out of sync.

NOTE: this will only be returned if the storage has inconsistencies.

---------
### NotAuthorized
The origin was not allowed to manage the association between the DID
and the account ID.

---------
### NotFound
The association does not exist.

---------
### OutdatedProof
The supplied proof of ownership was outdated.

---------
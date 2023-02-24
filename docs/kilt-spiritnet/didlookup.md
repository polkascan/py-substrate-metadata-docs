
# DidLookup

---------
## Calls

---------
### associate_account
Associate the given account to the DID that authorized this call.

The account has to sign the DID and a blocknumber after which the
signature expires in order to authorize the association.

The signature will be checked against the scale encoded tuple of the
method specific id of the did identifier and the block number after
which the signature should be regarded invalid.

Emits `AssociationEstablished` and, optionally, `AssociationRemoved`
if there was a previous association for the account.

\# &lt;weight&gt;
Weight: O(1)
- Reads: ConnectedDids + ConnectedAccounts + DID Origin Check
- Writes: ConnectedDids + ConnectedAccounts
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdOf<T>` | 
| expiration | `<T as frame_system::Config>::BlockNumber` | 
| proof | `SignatureOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'associate_account', {
    'account': 'AccountId',
    'expiration': 'u64',
    'proof': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
}
)
```

---------
### associate_sender
Associate the sender of the call to the DID that authorized this
call.

Emits `AssociationEstablished` and, optionally, `AssociationRemoved`
if there was a previous association for the account.

\# &lt;weight&gt;
Weight: O(1)
- Reads: ConnectedDids + ConnectedAccounts + DID Origin Check
- Writes: ConnectedDids + ConnectedAccounts
\# &lt;/weight&gt;
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
Changes the deposit owner.

The balance that is reserved by the current deposit owner will be
freed and balance of the new deposit owner will get reserved.

The subject of the call must be linked to the account.
The sender of the call will be the new deposit owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'change_deposit_owner', {'account': 'AccountId'}
)
```

---------
### reclaim_deposit
Remove the association of the provided account. This call can only
be called from the deposit owner. The reserved deposit will be
freed.

Emits `AssociationRemoved`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: ConnectedDids
- Writes: ConnectedDids
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'reclaim_deposit', {'account': 'AccountId'}
)
```

---------
### remove_account_association
Remove the association of the provided account ID. This call doesn&\#x27;t
require the authorization of the account ID, but the associated DID
needs to match the DID that authorized this call.

Emits `AssociationRemoved`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: ConnectedDids + ConnectedAccounts + DID Origin Check
- Writes: ConnectedDids + ConnectedAccounts
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'remove_account_association', {'account': 'AccountId'}
)
```

---------
### remove_sender_association
Remove the association of the sender account. This call doesn&\#x27;t
require the authorization of the DID, but requires a signed origin.

Emits `AssociationRemoved`.

\# &lt;weight&gt;
Weight: O(1)
- Reads: ConnectedDids + ConnectedAccounts + DID Origin Check
- Writes: ConnectedDids + ConnectedAccounts
\# &lt;/weight&gt;
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
Updates the deposit amount to the current deposit rate.

The sender must be the deposit owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'DidLookup', 'update_deposit', {'account': 'AccountId'}
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
| None | `AccountIdOf<T>` | ```AccountId```
| None | `DidIdentifierOf<T>` | ```AccountId```

---------
### AssociationRemoved
An association between a DID and an account ID was removed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `DidIdentifierOf<T>` | ```AccountId```

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
    'DidLookup', 'ConnectedAccounts', ['AccountId', 'AccountId']
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
    'DidLookup', 'ConnectedDids', ['AccountId']
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
### AssociationNotFound
The association does not exist.

---------
### InsufficientFunds
The account has insufficient funds and can&\#x27;t pay the fees or reserve
the deposit.

---------
### NotAuthorized
The origin was not allowed to manage the association between the DID
and the account ID.

---------
### OutdatedProof
The supplied proof of ownership was outdated.

---------
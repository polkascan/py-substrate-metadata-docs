
# Supersig

---------
## Calls

---------
### add_members
add members the supersig

`add members` will add a list of addesses to the members list of the supersig.
if an address is already present, it will be ignored.

The dispatch origin for this call must be `Signed` by the supersig

\# &lt;weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_members | `BoundedVec<(T::AccountId, Role), T::MaxAccountsPerTransaction>` | 

#### Python
```python
call = substrate.compose_call(
    'Supersig', 'add_members', {
    'new_members': [
        (
            'AccountId',
            (
                'Standard',
                'Master',
                'NotMember',
            ),
        ),
    ],
}
)
```

---------
### approve_call
vote for a call in the supersig

`approve_call` will add a positive, unique vote to the specified call proposal.
if the numbers of votes on this proposal = SimpleMajority (51%), then the call is
executed

The dispatch origin for this call must be `Signed`, and the origin must be a
supersig&\#x27;s member

\# &lt;weight&gt;

Related functions:
- `Currency::unreserve` will be called once IF SimpleMajority is reached
#### Attributes
| Name | Type |
| -------- | -------- | 
| supersig_account | `T::AccountId` | 
| call_id | `CallId` | 

#### Python
```python
call = substrate.compose_call(
    'Supersig', 'approve_call', {
    'call_id': 'u128',
    'supersig_account': 'AccountId',
}
)
```

---------
### create_supersig
create a supersig.

`create_supersig` will create a supersig with specified parameters, and transfer
currencies from the creator to the generated supersig:
    - the existencial deposit (minimum amount to make an account alive)
    - the price corresponding to the size (in bytes) of the members times the
      DepositPerByte

The dispatch origin for this call must be `Signed`.

\# &lt;weight&gt;

Related functions:
- `Currency::transfer` will be called once to deposit an existencial amount on supersig
- `frame_system::inc_consumers` will be called once to protect the supersig from
  deletion
#### Attributes
| Name | Type |
| -------- | -------- | 
| members | `BoundedVec<(T::AccountId, Role), T::MaxAccountsPerTransaction>` | 

#### Python
```python
call = substrate.compose_call(
    'Supersig', 'create_supersig', {
    'members': [
        (
            'AccountId',
            (
                'Standard',
                'Master',
                'NotMember',
            ),
        ),
    ],
}
)
```

---------
### delete_supersig
remove the supersig

`delete_supersig` will remove every members, transfer every remanent funds to the
target account, remove the supersig from storage, and set the consumers and providers
to 0

The dispatch origin for this call must be `Signed` by the supersig

\# &lt;weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiary | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Supersig', 'delete_supersig', {'beneficiary': 'AccountId'}
)
```

---------
### leave_supersig
leave a supersig

`leave_supersig` will remove caller from selected supersig

The dispatch origin for this call must be `Signed` by the user.

\# &lt;weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| supersig_account | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Supersig', 'leave_supersig', {'supersig_account': 'AccountId'}
)
```

---------
### remove_call
remove a call from the supersig

`remove_call` will remove a call from the poll.

The dispatch origin for this call must be `Signed` by either the supersig or the
account who submited the call

\# &lt;weight&gt;

Related functions:
- `Currency::unreserve` will be called once
#### Attributes
| Name | Type |
| -------- | -------- | 
| supersig_account | `T::AccountId` | 
| call_id | `CallId` | 

#### Python
```python
call = substrate.compose_call(
    'Supersig', 'remove_call', {
    'call_id': 'u128',
    'supersig_account': 'AccountId',
}
)
```

---------
### remove_members
remove members from the supersig

`remove_members` will remove a list of addesses from the members list of the supersig.
if an address is not present, it will be ignored.

The dispatch origin for this call must be `Signed` by the supersig

\# &lt;weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| members_to_remove | `BoundedVec<T::AccountId, T::MaxAccountsPerTransaction>` | 

#### Python
```python
call = substrate.compose_call(
    'Supersig', 'remove_members', {'members_to_remove': ['AccountId']}
)
```

---------
### submit_call
submit a call to a specific supersig.

`submit_call` will create a proposal on the supersig, that members can approve.
this will lock an amount that depend on the lenght of the encoded call, to prevent spam

The dispatch origin for this call must be `Signed`, and the origin must be a
supersig&\#x27;s member

\# &lt;weight&gt;

Related functions:
- `Currency::reserve` will be called once to lock the deposit amount
#### Attributes
| Name | Type |
| -------- | -------- | 
| supersig_account | `T::AccountId` | 
| call | `Box<<T as pallet::Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'Supersig', 'submit_call', {
    'call': 'Call',
    'supersig_account': 'AccountId',
}
)
```

---------
## Events

---------
### CallExecutionAttempted
a Call has been executed [supersig, call_nonce, result]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `CallId` | ```u128```
| None | `Result<DispatchResult, DispatchError>` | ```{'Ok': {'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}, 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### CallRemoved
a Call has been removed [supersig, call_nonce]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `CallId` | ```u128```

---------
### CallSubmitted
a Call has been submited [supersig, call_nonce, submiter]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `CallId` | ```u128```
| None | `T::AccountId` | ```AccountId```

---------
### CallVoted
a Call has been voted [supersig, call_nonce, voter]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `CallId` | ```u128```
| None | `T::AccountId` | ```AccountId```

---------
### MembersAdded
the list of users added to the supersig [supersig, [(user, role)]]
Users that were already in the supersig wont appear
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<(T::AccountId, Role)>` | ```[('AccountId', ('Standard', 'Master', 'NotMember'))]```

---------
### MembersRemoved
the list of users removed from the supersig [supersig, removed_users]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Vec<T::AccountId>` | ```['AccountId']```

---------
### SupersigCreated
Supersig has been created [supersig]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### SupersigLeaved
a member leaved the supersig [supersig, member]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```

---------
### SupersigRemoved
a supersig have been removed [supersig]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Calls

#### Python
```python
result = substrate.query(
    'Supersig', 'Calls', ['u128', 'u128']
)
```

#### Return value
```python
{'data': 'Bytes', 'deposit': 'u128', 'provider': 'AccountId'}
```
---------
### Members

#### Python
```python
result = substrate.query(
    'Supersig', 'Members', ['u128', 'AccountId']
)
```

#### Return value
```python
('Standard', 'Master', 'NotMember')
```
---------
### MembersVotes

#### Python
```python
result = substrate.query(
    'Supersig', 'MembersVotes', ['u128', 'u128', 'AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### NonceCall

#### Python
```python
result = substrate.query(
    'Supersig', 'NonceCall', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### NonceSupersig

#### Python
```python
result = substrate.query(
    'Supersig', 'NonceSupersig', []
)
```

#### Return value
```python
'u128'
```
---------
### TotalDeposit

#### Python
```python
result = substrate.query(
    'Supersig', 'TotalDeposit', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### TotalMembers

#### Python
```python
result = substrate.query(
    'Supersig', 'TotalMembers', ['u128']
)
```

#### Return value
```python
'u32'
```
---------
### Votes

#### Python
```python
result = substrate.query(
    'Supersig', 'Votes', ['u128', 'u128']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### DepositPerByte
 The amount of balance that must be deposited per bytes stored
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('Supersig', 'DepositPerByte')
```
---------
### MaxAccountsPerTransaction
 The maximum number of account that can added or removed in a single call
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Supersig', 'MaxAccountsPerTransaction')
```
---------
### PalletId
 The base id used for accountId calculation
#### Value
```python
'0x69642f7375736967'
```
#### Python
```python
constant = substrate.get_constant('Supersig', 'PalletId')
```
---------
## Errors

---------
### AlreadyVoted
the member already voted for the call

---------
### BadEncodedCall
could not execute the call because it was incorrectly encoded

---------
### CallNotFound
the call doesn&\#x27;t exist

---------
### Conversion
conversion

---------
### InvalidNonce
no more valid supersig nonce

---------
### InvalidNumberOfMembers
supersig must have at least one member

---------
### NotAllowed
the signatory is not allowed to perform this call

---------
### NotMember
the user is not a member of the supersig

---------
### NotSupersig
the call origin is not an existing supersig

---------
### Overflow
overflow

---------
### SupersigHaveLockedFunds
the supersig couldn&\#x27;t be deleted. This is due to the supersig having locked tokens

---------
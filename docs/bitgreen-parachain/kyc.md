
# KYC

---------
## Calls

---------
### add_member
Add a member `who` to the set.

May only be called from `T::AddOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'KYC', 'add_member', {
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
### change_key
Swap out the sending member for some other key `new`.

May only be called from `Signed` origin of a current member.

Prime membership is passed from the origin account to `new`, if extant.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'KYC', 'change_key', {
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
### force_add_authorized_account
Add a new account to the list of authorised Accounts
The caller must be from a permitted origin
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'KYC', 'force_add_authorized_account', {'account_id': 'AccountId'}
)
```

---------
### force_remove_authorized_account
Remove an account from the list of authorised accounts
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'KYC', 'force_remove_authorized_account', {'account_id': 'AccountId'}
)
```

---------
### force_set_kyc_airdrop
Set the airdrop amount for each successful kyc
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `Option<BalanceOf<T, I>>` | 

#### Python
```python
call = substrate.compose_call(
    'KYC', 'force_set_kyc_airdrop', {'amount': (None, 'u128')}
)
```

---------
### remove_member
Remove a member `who` from the set.

May only be called from `T::RemoveOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'KYC', 'remove_member', {
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
### reset_members
Change the membership to a new set, disregarding the existing membership. Be nice and
pass `members` pre-sorted.

May only be called from `T::ResetOrigin`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| members | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'KYC', 'reset_members', {'members': ['AccountId']}
)
```

---------
### swap_member
Swap out one member `remove` for another `add`.

May only be called from `T::SwapOrigin`.

Prime membership is *not* passed from `remove` to `add`, if extant.
#### Attributes
| Name | Type |
| -------- | -------- | 
| remove | `AccountIdLookupOf<T>` | 
| add | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'KYC', 'swap_member', {
    'add': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'remove': {
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
### AuthorizedAccountAdded
A new AuthorizedAccount has been added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### AuthorizedAccountRemoved
An AuthorizedAccount has been removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### Dummy
Phantom member, never used.
#### Attributes
No attributes

---------
### KYCAirdrop
User has received airdrop for kyc approval
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### KeyChanged
One of the members&\#x27; keys changed.
#### Attributes
No attributes

---------
### MemberAdded
The given member was added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### MemberRemoved
The given member was removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
### MembersReset
The membership was reset; see the transaction for who the new set is.
#### Attributes
No attributes

---------
### MembersSwapped
Two members were swapped; see the transaction for who.
#### Attributes
No attributes

---------
## Storage functions

---------
### AirdropAmount

#### Python
```python
result = substrate.query(
    'KYC', 'AirdropAmount', []
)
```

#### Return value
```python
'u128'
```
---------
### AuthorizedAccounts

#### Python
```python
result = substrate.query(
    'KYC', 'AuthorizedAccounts', []
)
```

#### Return value
```python
['AccountId']
```
---------
### Members
 The current membership, stored as an ordered Vec.

#### Python
```python
result = substrate.query(
    'KYC', 'Members', []
)
```

#### Return value
```python
['AccountId']
```
---------
## Constants

---------
### PalletId
 The KYC pallet id
#### Value
```python
'0x626974672f6b7963'
```
#### Python
```python
constant = substrate.get_constant('KYC', 'PalletId')
```
---------
## Errors

---------
### AlreadyMember
Already a member.

---------
### AuthorizedAccountAlreadyExists
Cannot add a duplicate authorised account

---------
### NotAuthorised
No authorization account

---------
### NotMember
Not a member.

---------
### TooManyAuthorizedAccounts
Adding a new authorized account failed

---------
### TooManyMembers
Too many members.

---------
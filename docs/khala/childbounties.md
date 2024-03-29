
# ChildBounties

---------
## Calls

---------
### accept_curator
See [`Pallet::accept_curator`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'accept_curator', {
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
### add_child_bounty
See [`Pallet::add_child_bounty`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| value | `BalanceOf<T>` | 
| description | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'add_child_bounty', {
    'description': 'Bytes',
    'parent_bounty_id': 'u32',
    'value': 'u128',
}
)
```

---------
### award_child_bounty
See [`Pallet::award_child_bounty`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 
| beneficiary | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'award_child_bounty', {
    'beneficiary': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
### claim_child_bounty
See [`Pallet::claim_child_bounty`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'claim_child_bounty', {
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
### close_child_bounty
See [`Pallet::close_child_bounty`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'close_child_bounty', {
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
### propose_curator
See [`Pallet::propose_curator`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 
| curator | `AccountIdLookupOf<T>` | 
| fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'propose_curator', {
    'child_bounty_id': 'u32',
    'curator': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'fee': 'u128',
    'parent_bounty_id': 'u32',
}
)
```

---------
### unassign_curator
See [`Pallet::unassign_curator`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_bounty_id | `BountyIndex` | 
| child_bounty_id | `BountyIndex` | 

#### Python
```python
call = substrate.compose_call(
    'ChildBounties', 'unassign_curator', {
    'child_bounty_id': 'u32',
    'parent_bounty_id': 'u32',
}
)
```

---------
## Events

---------
### Added
A child-bounty is added.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| child_index | `BountyIndex` | ```u32```

---------
### Awarded
A child-bounty is awarded to a beneficiary.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| child_index | `BountyIndex` | ```u32```
| beneficiary | `T::AccountId` | ```AccountId```

---------
### Canceled
A child-bounty is cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| child_index | `BountyIndex` | ```u32```

---------
### Claimed
A child-bounty is claimed by beneficiary.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `BountyIndex` | ```u32```
| child_index | `BountyIndex` | ```u32```
| payout | `BalanceOf<T>` | ```u128```
| beneficiary | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### ChildBounties
 Child bounties that have been added.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ChildBounties', ['u32', 'u32']
)
```

#### Return value
```python
{
    'curator_deposit': 'u128',
    'fee': 'u128',
    'parent_bounty': 'u32',
    'status': {
        'Active': {'curator': 'AccountId'},
        'Added': None,
        'CuratorProposed': {'curator': 'AccountId'},
        'PendingPayout': {
            'beneficiary': 'AccountId',
            'curator': 'AccountId',
            'unlock_at': 'u32',
        },
    },
    'value': 'u128',
}
```
---------
### ChildBountyCount
 Number of total child bounties.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ChildBountyCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ChildBountyDescriptions
 The description of each child-bounty.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ChildBountyDescriptions', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### ChildrenCuratorFees
 The cumulative child-bounty curator fee for each parent bounty.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ChildrenCuratorFees', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### ParentChildBounties
 Number of child bounties per parent bounty.
 Map of parent bounty index to number of child bounties.

#### Python
```python
result = substrate.query(
    'ChildBounties', 'ParentChildBounties', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### ChildBountyValueMinimum
 Minimum value for a child-bounty.
#### Value
```python
1000000000000
```
#### Python
```python
constant = substrate.get_constant('ChildBounties', 'ChildBountyValueMinimum')
```
---------
### MaxActiveChildBountyCount
 Maximum number of child bounties that can be added to a parent bounty.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('ChildBounties', 'MaxActiveChildBountyCount')
```
---------
## Errors

---------
### InsufficientBountyBalance
The bounty balance is not enough to add new child-bounty.

---------
### ParentBountyNotActive
The parent bounty is not in active state.

---------
### TooManyChildBounties
Number of child bounties exceeds limit `MaxActiveChildBountyCount`.

---------

# Delegation

---------
## Calls

---------
### add_delegation
See [`Pallet::add_delegation`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 
| parent_id | `DelegationNodeIdOf<T>` | 
| delegate | `DelegatorIdOf<T>` | 
| permissions | `Permissions` | 
| delegate_signature | `DelegateSignatureTypeOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'add_delegation', {
    'delegate': 'AccountId',
    'delegate_signature': {
        'Ecdsa': '[u8; 65]',
        'Ed25519': '[u8; 64]',
        'Sr25519': '[u8; 64]',
    },
    'delegation_id': 'scale_info::12',
    'parent_id': 'scale_info::12',
    'permissions': {'bits': 'u32'},
}
)
```

---------
### change_deposit_owner
See [`Pallet::change_deposit_owner`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'change_deposit_owner', {'delegation_id': 'scale_info::12'}
)
```

---------
### create_hierarchy
See [`Pallet::create_hierarchy`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| root_node_id | `DelegationNodeIdOf<T>` | 
| ctype_hash | `CtypeHashOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'create_hierarchy', {
    'ctype_hash': 'scale_info::12',
    'root_node_id': 'scale_info::12',
}
)
```

---------
### reclaim_deposit
See [`Pallet::reclaim_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 
| max_removals | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'reclaim_deposit', {
    'delegation_id': 'scale_info::12',
    'max_removals': 'u32',
}
)
```

---------
### remove_delegation
See [`Pallet::remove_delegation`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 
| max_removals | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'remove_delegation', {
    'delegation_id': 'scale_info::12',
    'max_removals': 'u32',
}
)
```

---------
### revoke_delegation
See [`Pallet::revoke_delegation`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 
| max_parent_checks | `u32` | 
| max_revocations | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'revoke_delegation', {
    'delegation_id': 'scale_info::12',
    'max_parent_checks': 'u32',
    'max_revocations': 'u32',
}
)
```

---------
### update_deposit
See [`Pallet::update_deposit`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegation_id | `DelegationNodeIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Delegation', 'update_deposit', {'delegation_id': 'scale_info::12'}
)
```

---------
## Events

---------
### DelegationCreated
A new delegation has been created.
\[creator ID, root node ID, delegation node ID, parent node ID,
delegate ID, permissions\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```scale_info::12```
| None | `DelegationNodeIdOf<T>` | ```scale_info::12```
| None | `DelegationNodeIdOf<T>` | ```scale_info::12```
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `Permissions` | ```{'bits': 'u32'}```

---------
### DelegationRemoved
A delegation has been removed.
\[remover ID, delegation node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```scale_info::12```

---------
### DelegationRevoked
A delegation has been revoked.
\[revoker ID, delegation node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```scale_info::12```

---------
### DepositReclaimed
The deposit owner reclaimed a deposit by removing a delegation
subtree. \[revoker ID, delegation node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```scale_info::12```

---------
### HierarchyCreated
A new hierarchy has been created.
\[creator ID, root node ID, CTYPE hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```scale_info::12```
| None | `CtypeHashOf<T>` | ```scale_info::12```

---------
### HierarchyRemoved
A hierarchy has been removed from the storage on chain.
\[remover ID, root node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```scale_info::12```

---------
### HierarchyRevoked
A hierarchy has been revoked.
\[revoker ID, root node ID\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `DelegatorIdOf<T>` | ```AccountId```
| None | `DelegationNodeIdOf<T>` | ```scale_info::12```

---------
## Storage functions

---------
### DelegationHierarchies
 Delegation hierarchies stored on chain.

 It maps for a (root) node ID to the hierarchy details.

#### Python
```python
result = substrate.query(
    'Delegation', 'DelegationHierarchies', ['scale_info::12']
)
```

#### Return value
```python
{'ctype_hash': 'scale_info::12'}
```
---------
### DelegationNodes
 Delegation nodes stored on chain.

 It maps from a node ID to the node details.

#### Python
```python
result = substrate.query(
    'Delegation', 'DelegationNodes', ['scale_info::12']
)
```

#### Return value
```python
{
    'children': 'scale_info::451',
    'deposit': {'amount': 'u128', 'owner': 'AccountId'},
    'details': {'owner': 'AccountId', 'permissions': {'bits': 'u32'}, 'revoked': 'bool'},
    'hierarchy_root_id': 'scale_info::12',
    'parent': (None, 'scale_info::12'),
}
```
---------
## Constants

---------
### Deposit
 The deposit that is required for storing a delegation.
#### Value
```python
1000000000000000
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'Deposit')
```
---------
### MaxChildren
 Maximum number of all children for a delegation node. For a binary
 tree, this should be twice the maximum depth of the tree, i.e.
 `2 ^ MaxParentChecks`.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxChildren')
```
---------
### MaxParentChecks
 Maximum number of upwards traversals of the delegation tree from a
 node to the root and thus the depth of the delegation tree.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxParentChecks')
```
---------
### MaxRemovals
 Maximum number of removals. Should be same as MaxRevocations
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxRemovals')
```
---------
### MaxRevocations
 Maximum number of revocations.
#### Value
```python
5
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxRevocations')
```
---------
### MaxSignatureByteLength
#### Value
```python
64
```
#### Python
```python
constant = substrate.get_constant('Delegation', 'MaxSignatureByteLength')
```
---------
## Errors

---------
### AccessDenied
The operation wasn&\#x27;t allowed because of insufficient rights.

---------
### DelegateNotFound
No delegate with the given ID stored on chain.

---------
### DelegationAlreadyExists
There is already a delegation node with the same ID stored on chain.

---------
### DelegationNotFound
No delegation with the given ID stored on chain.

---------
### ExceededRemovalBounds
Max number of removals for delegation nodes has been reached for the
operation.

---------
### ExceededRevocationBounds
Max number of revocations for delegation nodes has been reached for
the operation.

---------
### HierarchyAlreadyExists
There is already a hierarchy with the same ID stored on chain.

---------
### HierarchyNotFound
No hierarchy with the given ID stored on chain.

---------
### Internal
An error that is not supposed to take place, yet it happened.

---------
### InvalidDelegateSignature
The delegate&\#x27;s signature for the delegation creation operation is
invalid.

---------
### MaxChildrenExceeded
The max number of all children has been reached for the
corresponding delegation node.

---------
### MaxParentChecksTooLarge
The max number of parent checks exceeds the limit for the pallet.

---------
### MaxRemovalsTooLarge
The max number of removals exceeds the limit for the pallet.

---------
### MaxRevocationsTooLarge
The max number of revocation exceeds the limit for the pallet.

---------
### MaxSearchDepthReached
Max number of nodes checked without verifying the given condition.

---------
### NotOwnerOfDelegationHierarchy
The delegation creator is not allowed to write the delegation
because they are not the owner of the delegation root node.

---------
### NotOwnerOfParentDelegation
The delegation creator is not allowed to write the delegation
because they are not the owner of the delegation parent node.

---------
### ParentDelegationNotFound
No parent delegation with the given ID stored on chain.

---------
### ParentDelegationRevoked
The parent delegation has previously been revoked.

---------
### UnauthorizedDelegation
The delegation creator is not allowed to create the delegation.

---------
### UnauthorizedRemoval
The call origin is not authorized to remove the delegation.

---------
### UnauthorizedRevocation
The delegation revoker is not allowed to revoke the delegation.

---------
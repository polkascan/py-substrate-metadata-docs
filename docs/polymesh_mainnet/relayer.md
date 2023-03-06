
# Relayer

---------
## Calls

---------
### accept_paying_key
Accepts a `paying_key` authorization.

\# Arguments
- `auth_id` the authorization id to accept a `paying_key`.

\# Errors
- `AuthorizationError::Invalid` if `auth_id` does not exist for the given caller.
- `AuthorizationError::Expired` if `auth_id` the authorization has expired.
- `AuthorizationError::BadType` if `auth_id` was not a `AddRelayerPayingKey` authorization.
- `NotAuthorizedForUserKey` if `origin` is not authorized to accept the authorization for the `user_key`.
- `NotAuthorizedForPayingKey` if the authorization was created an identity different from the `paying_key`&\#x27;s identity.
- `UserKeyCddMissing` if the `user_key` is not attached to a CDD&\#x27;d identity.
- `PayingKeyCddMissing` if the `paying_key` is not attached to a CDD&\#x27;d identity.
- `UnauthorizedCaller` if `origin` is not authorized to call this extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Relayer', 'accept_paying_key', {'auth_id': 'u64'}
)
```

---------
### decrease_polyx_limit
Decrease the available POLYX for a `user_key`.

\# Arguments
- `user_key` the user key of the subsidy to update the available POLYX.
- `amount` the amount of POLYX to remove from the subsidy of `user_key`.

\# Errors
- `NoPayingKey` if the `user_key` doesn&\#x27;t have a `paying_key`.
- `NotPayingKey` if `origin` doesn&\#x27;t match the current `paying_key`.
- `UnauthorizedCaller` if `origin` is not authorized to call this extrinsic.
- `Overlow` if the subsidy has less then `amount` POLYX remaining.
#### Attributes
| Name | Type |
| -------- | -------- | 
| user_key | `T::AccountId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Relayer', 'decrease_polyx_limit', {
    'amount': 'u128',
    'user_key': 'AccountId',
}
)
```

---------
### increase_polyx_limit
Increase the available POLYX for a `user_key`.

\# Arguments
- `user_key` the user key of the subsidy to update the available POLYX.
- `amount` the amount of POLYX to add to the subsidy of `user_key`.

\# Errors
- `NoPayingKey` if the `user_key` doesn&\#x27;t have a `paying_key`.
- `NotPayingKey` if `origin` doesn&\#x27;t match the current `paying_key`.
- `UnauthorizedCaller` if `origin` is not authorized to call this extrinsic.
- `Overlow` if the subsidy&\#x27;s remaining POLYX would have overflowed `u128::MAX`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| user_key | `T::AccountId` | 
| amount | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Relayer', 'increase_polyx_limit', {
    'amount': 'u128',
    'user_key': 'AccountId',
}
)
```

---------
### remove_paying_key
Removes the `paying_key` from a `user_key`.

\# Arguments
- `user_key` the user key to remove the subsidy from.
- `paying_key` the paying key that was subsidising the `user_key`.

\# Errors
- `NotAuthorizedForUserKey` if `origin` is not authorized to remove the subsidy for the `user_key`.
- `NoPayingKey` if the `user_key` doesn&\#x27;t have a `paying_key`.
- `NotPayingKey` if the `paying_key` doesn&\#x27;t match the current `paying_key`.
- `UnauthorizedCaller` if `origin` is not authorized to call this extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| user_key | `T::AccountId` | 
| paying_key | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Relayer', 'remove_paying_key', {
    'paying_key': 'AccountId',
    'user_key': 'AccountId',
}
)
```

---------
### set_paying_key
Creates an authorization to allow `user_key` to accept the caller (`origin == paying_key`) as their subsidiser.

\# Arguments
- `user_key` the user key to subsidise.
- `polyx_limit` the initial POLYX limit for this subsidy.

\# Errors
- `UnauthorizedCaller` if `origin` is not authorized to call this extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| user_key | `T::AccountId` | 
| polyx_limit | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Relayer', 'set_paying_key', {
    'polyx_limit': 'u128',
    'user_key': 'AccountId',
}
)
```

---------
### update_polyx_limit
Updates the available POLYX for a `user_key`.

\# Arguments
- `user_key` the user key of the subsidy to update the available POLYX.
- `polyx_limit` the amount of POLYX available for subsidising the `user_key`.

\# Errors
- `NoPayingKey` if the `user_key` doesn&\#x27;t have a `paying_key`.
- `NotPayingKey` if `origin` doesn&\#x27;t match the current `paying_key`.
- `UnauthorizedCaller` if `origin` is not authorized to call this extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| user_key | `T::AccountId` | 
| polyx_limit | `Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Relayer', 'update_polyx_limit', {
    'polyx_limit': 'u128',
    'user_key': 'AccountId',
}
)
```

---------
## Events

---------
### AcceptedPayingKey
Accepted paying key.

(Caller DID, User Key, Paying Key)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `AccountId` | ```AccountId```

---------
### AuthorizedPayingKey
Authorization given for `paying_key` to `user_key`.

(Caller DID, User Key, Paying Key, Initial POLYX limit, Auth ID)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `u64` | ```u64```

---------
### RemovedPayingKey
Removed paying key.

(Caller DID, User Key, Paying Key)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `AccountId` | ```AccountId```

---------
### UpdatedPolyxLimit
Updated polyx limit.

(Caller DID, User Key, Paying Key, POLYX limit, old remaining POLYX)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### Subsidies
 The subsidy for a `user_key` if they are being subsidised,
 as a map `user_key` =&gt; `Subsidy`.

 A key can only have one subsidy at a time.  To change subsidisers
 a key needs to call `remove_paying_key` to remove the current subsidy,
 before they can accept a new subsidiser.

#### Python
```python
result = substrate.query(
    'Relayer', 'Subsidies', ['AccountId']
)
```

#### Return value
```python
{'paying_key': 'AccountId', 'remaining': 'u128'}
```
---------
## Errors

---------
### NoPayingKey
The `user_key` doesn&\#x27;t have a `paying_key`.

---------
### NotAuthorizedForPayingKey
The signer is not authorized for `paying_key`.

---------
### NotAuthorizedForUserKey
The signer is not authorized for `user_key`.

---------
### NotPayingKey
The `user_key` has a different `paying_key`.

---------
### Overflow
The remaining POLYX for `user_key` overflowed.

---------
### PayingKeyCddMissing
The `user_key` is not attached to a CDD&\#x27;d identity.

---------
### UserKeyCddMissing
The `user_key` is not attached to a CDD&\#x27;d identity.

---------
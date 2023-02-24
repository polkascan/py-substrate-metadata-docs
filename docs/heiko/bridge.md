
# Bridge

---------
## Calls

---------
### clean_cap_accumulated_value
Clean the accumulated cap value to make bridge work again
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_token_id | `CurrencyId` | 
| bridge_type | `BridgeType` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'clean_cap_accumulated_value', {
    'bridge_token_id': 'u32',
    'bridge_type': (
        'BridgeOut',
        'BridgeIn',
    ),
}
)
```

---------
### materialize
Materialize the bridge token to specified recipient in this chain

The first call to the same cross-chain transaction will create a proposal
And subsequent calls will update the existing state until completion

- `src_id`: chain_id of the source chain, should be registered.
- `src_nonce`: nonce of the source chain, should be unique to identify the cross-cahin tx.
- `bridge_token_id`: bridge_token_id of the bridge token to be materialized, should be registered.
- `to`: recipient of the bridge token of this chain
- `amount`: amount to be materialized, the decimal of bridge token may be different
- `favour`: whether to favour the cross-chain transaction or not, always be true for now.
#### Attributes
| Name | Type |
| -------- | -------- | 
| src_id | `ChainId` | 
| src_nonce | `ChainNonce` | 
| bridge_token_id | `CurrencyId` | 
| to | `T::AccountId` | 
| amount | `BalanceOf<T>` | 
| favour | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'materialize', {
    'amount': 'u128',
    'bridge_token_id': 'u32',
    'favour': 'bool',
    'src_id': 'u32',
    'src_nonce': 'u64',
    'to': 'AccountId',
}
)
```

---------
### register_bridge_token
Register the specified bridge_token_id

Only registered bridge_tokens are allowed to cross-chain

- `bridge_token`: bridge_token_id should be unique.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| bridge_token | `BridgeToken` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'register_bridge_token', {
    'asset_id': 'u32',
    'bridge_token': {
        'enable': 'bool',
        'external': 'bool',
        'fee': 'u128',
        'id': 'u32',
        'in_amount': 'u128',
        'in_cap': 'u128',
        'out_amount': 'u128',
        'out_cap': 'u128',
    },
}
)
```

---------
### register_chain
Register the specified chain_id

Only registered chains are allowed to do cross-chain

- `chain_id`: should be unique.
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain_id | `ChainId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'register_chain', {'chain_id': 'u32'}
)
```

---------
### set_bridge_token_cap
Set the cross-chain transaction cap for a registered bridge token
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_token_id | `CurrencyId` | 
| bridge_type | `BridgeType` | 
| new_cap | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'set_bridge_token_cap', {
    'bridge_token_id': 'u32',
    'bridge_type': (
        'BridgeOut',
        'BridgeIn',
    ),
    'new_cap': 'u128',
}
)
```

---------
### set_bridge_token_fee
Set the cross-chain transaction fee for a registered bridge token
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_token_id | `CurrencyId` | 
| new_fee | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'set_bridge_token_fee', {
    'bridge_token_id': 'u32',
    'new_fee': 'u128',
}
)
```

---------
### set_bridge_token_status
Set the cross-chain transaction fee for a registered bridge token
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_token_id | `CurrencyId` | 
| enable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'set_bridge_token_status', {
    'bridge_token_id': 'u32',
    'enable': 'bool',
}
)
```

---------
### teleport
Teleport the bridge token to specified recipient in the destination chain

Transfer funds from one account to an account in another registered chain.
Support for native token and tokens of Assets pallet
The caller&\#x27;s assets will be locked into palletId

- `dest_id`: chain_id of the destination chain, should be registered.
- `bridge_token_id`: bridge token should be registered before teleport.
- `to`: recipient of the bridge token of another chain
- `amount`: amount to be teleported, the decimal of bridge token may be different
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest_id | `ChainId` | 
| bridge_token_id | `CurrencyId` | 
| to | `TeleAccount` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'teleport', {
    'amount': 'u128',
    'bridge_token_id': 'u32',
    'dest_id': 'u32',
    'to': 'Bytes',
}
)
```

---------
### unregister_bridge_token
Unregister the specified bridge_token_id
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_token_id | `CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'unregister_bridge_token', {'bridge_token_id': 'u32'}
)
```

---------
### unregister_chain
Unregister the specified chain_id
#### Attributes
| Name | Type |
| -------- | -------- | 
| chain_id | `ChainId` | 

#### Python
```python
call = substrate.compose_call(
    'Bridge', 'unregister_chain', {'chain_id': 'u32'}
)
```

---------
## Events

---------
### BridgeTokenAccumulatedValueCleaned
The accumulated cap value cleaned
[bridge_token_id, bridge_type]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```
| None | `BridgeType` | ```('BridgeOut', 'BridgeIn')```

---------
### BridgeTokenCapUpdated
The status of the bridge token cap has updated
[bridge_token_id, bridge_type, new_cap]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```
| None | `BridgeType` | ```('BridgeOut', 'BridgeIn')```
| None | `BalanceOf<T>` | ```u128```

---------
### BridgeTokenFeeUpdated
Bridge token fee has updated
[bridge_token_id, fee]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### BridgeTokenRegistered
New bridge_token_id has been registered
[asset_id, bridge_token_id, external, fee, enable, out_cap, out_amount, in_cap, in_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `CurrencyId` | ```u32```
| None | `bool` | ```bool```
| None | `BalanceOf<T>` | ```u128```
| None | `bool` | ```bool```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### BridgeTokenRemoved
The bridge_token_id has been unregistered
[asset_id, bridge_token_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `CurrencyId` | ```u32```

---------
### BridgeTokenStatusUpdated
The status of the bridge token has updated
[bridge_token_id, enabled]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```
| None | `bool` | ```bool```

---------
### ChainRegistered
New chain_id has been registered
[chain_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```u32```

---------
### ChainRemoved
The chain_id has been unregistered
[chain_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```u32```

---------
### MaterializeInitialized
Event emitted when a proposal is initialized by materialization
[voter, src_id, src_nonce, bridge_token_id, dst_address, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ChainId` | ```u32```
| None | `ChainNonce` | ```u64```
| None | `CurrencyId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### MaterializeMinted
Event emitted when bridge token is issued by materialization
[src_id, chain_nonce, bridge_token_id, dst_address, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```u32```
| None | `ChainNonce` | ```u64```
| None | `CurrencyId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### MaterializeVoteAgainst
Vote against a proposal
[src_id, src_nonce, voter, bridge_token_id, dst_address, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```u32```
| None | `ChainNonce` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `CurrencyId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### MaterializeVoteFor
Vote for a proposal
[src_id, src_nonce, voter, bridge_token_id, dst_address, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```u32```
| None | `ChainNonce` | ```u64```
| None | `T::AccountId` | ```AccountId```
| None | `CurrencyId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### ProposalApproved
Proposal was approved successfully
[src_id, src_nonce]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```u32```
| None | `ChainNonce` | ```u64```

---------
### ProposalRejected
Proposal was rejected
[src_id, src_nonce]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```u32```
| None | `ChainNonce` | ```u64```

---------
### TeleportBurned
Event emitted when bridge token is destroyed by teleportation
[ori_address, dest_id, chain_nonce, bridge_token_id, dst_address, amount, fee]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `ChainId` | ```u32```
| None | `ChainNonce` | ```u64```
| None | `CurrencyId` | ```u32```
| None | `TeleAccount` | ```Bytes```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### VoteThresholdUpdated
Vote threshold has updated
[vote_threshold]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
## Storage functions

---------
### AssetIds

#### Python
```python
result = substrate.query(
    'Bridge', 'AssetIds', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### BridgeRegistry

#### Python
```python
result = substrate.query(
    'Bridge', 'BridgeRegistry', ['u32']
)
```

#### Return value
```python
[('u64', 'u64')]
```
---------
### BridgeTokens

#### Python
```python
result = substrate.query(
    'Bridge', 'BridgeTokens', ['u32']
)
```

#### Return value
```python
{
    'enable': 'bool',
    'external': 'bool',
    'fee': 'u128',
    'id': 'u32',
    'in_amount': 'u128',
    'in_cap': 'u128',
    'out_amount': 'u128',
    'out_cap': 'u128',
}
```
---------
### ChainNonces

#### Python
```python
result = substrate.query(
    'Bridge', 'ChainNonces', ['u32']
)
```

#### Return value
```python
'u64'
```
---------
### ProposalVotes
 Mapping of [chain_id -&gt; (nonce, call) -&gt; proposal]

#### Python
```python
result = substrate.query(
    'Bridge', 'ProposalVotes', [
    'u32',
    (
        'u64',
        {
            'amount': 'u128',
            'bridge_token_id': 'u32',
            'to': 'AccountId',
        },
    ),
]
)
```

#### Return value
```python
{
    'expiry': 'u32',
    'status': ('Initiated', 'Approved', 'Rejected'),
    'votes_against': ['AccountId'],
    'votes_for': ['AccountId'],
}
```
---------
### VoteThreshold

#### Python
```python
result = substrate.query(
    'Bridge', 'VoteThreshold', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### ChainId
 The identifier for this chain.
 This must be unique and must not collide with existing IDs within a set of bridged chains.
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'ChainId')
```
---------
### ExistentialDeposit
 The essential balance for an existed account
#### Value
```python
10000000000
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'ExistentialDeposit')
```
---------
### GiftAccount
 An account to pay the bonus
#### Value
```python
'hJHfe3mtq3Rx4gDKWqnFH5iEQ585zvDhET114G2CPeha2gcTp'
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'GiftAccount')
```
---------
### NativeCurrencyId
 Currency id of the native token
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'NativeCurrencyId')
```
---------
### PalletId
 The bridge&#x27;s pallet id, keep all teleported assets.
#### Value
```python
'0x7061722f62726964'
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'PalletId')
```
---------
### ProposalLifetime
 Each proposal can live up to [ProposalLifetime] blocks
#### Value
```python
2592000
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'ProposalLifetime')
```
---------
### RootOperatorAccountId
 The root operator account id
#### Value
```python
'hJFDU5ssbB3JU6PyvaS4DrdVosVZd4zqJcqSd4rJt1W2ekYfn'
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'RootOperatorAccountId')
```
---------
### ThresholdPercentage
 The threshold percentage of relayers required to approve a proposal
#### Value
```python
80
```
#### Python
```python
constant = substrate.get_constant('Bridge', 'ThresholdPercentage')
```
---------
## Errors

---------
### BridgeInCapExceeded
The bridging amount is exceed the capacity

---------
### BridgeOutCapExceeded
The bridging amount is exceed the capacity

---------
### BridgeTokenAlreadyRegistered
The bridge token is invalid, it cannot be a existed bridge_token_id

---------
### BridgeTokenDisabled
The bridge token is not available in cross-chain

---------
### BridgeTokenNotRegistered
The bridge token is not registered and the related operation will be invalid

---------
### BridgingAmountTooLow
The bridging amount is too low

---------
### ChainIdAlreadyRegistered
The chain_id is invalid, it cannot be a existed chain_id or this chain_id

---------
### ChainIdNotRegistered
The chain_id is not registered and the related operation will be invalid

---------
### InvalidVoteThreshold
The new threshold is invalid

---------
### MemberAlreadyVoted
The RelayMembers already vote for the proposal

---------
### OriginNoPermission
Origin has no permission to operate on the bridge

---------
### ProposalAlreadyComplete
Proposal has been finished

---------
### ProposalDoesNotExist
No proposal was found

---------
### ProposalExpired
The proposal has exceeded its life time.

---------
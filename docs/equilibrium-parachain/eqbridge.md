
# EqBridge

---------
## Calls

---------
### disable_withdrawals
Disable asset withdrawals to specific chain under an associated resource ID.
Sudo only.

\# &lt;weight&gt;
- O(1) write
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| resource_id | `chainbridge::ResourceId` | 
| chain_id | `chainbridge::ChainId` | 

#### Python
```python
call = substrate.compose_call(
    'EqBridge', 'disable_withdrawals', {
    'chain_id': 'u8',
    'resource_id': '[u8; 32]',
}
)
```

---------
### enable_withdrawals
Enable asset withdrawals to specific chain under an associated resource ID.
Sudo only.

\# &lt;weight&gt;
- O(1) write
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| resource_id | `chainbridge::ResourceId` | 
| chain_id | `chainbridge::ChainId` | 

#### Python
```python
call = substrate.compose_call(
    'EqBridge', 'enable_withdrawals', {
    'chain_id': 'u8',
    'resource_id': '[u8; 32]',
}
)
```

---------
### remark
This can be called by the bridge to demonstrate an arbitrary call from a proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| hash | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'EqBridge', 'remark', {'hash': '[u8; 32]'}
)
```

---------
### set_chain_address_type
Stores chain id relation to chain address type.
Sudo only.

\# &lt;weight&gt;
- O(1) write
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest_id | `chainbridge::ChainId` | 
| address_type | `Option<ChainAddressType>` | 

#### Python
```python
call = substrate.compose_call(
    'EqBridge', 'set_chain_address_type', {
    'address_type': (
        None,
        (
            'Ethereum',
            'Substrate',
            'SubstrateWithPrefix',
        ),
    ),
    'dest_id': 'u8',
}
)
```

---------
### set_minimum_transfer_amount
Stores minimum transfer amount for sending asset to external chain.
Sudo only.

\# &lt;weight&gt;
- O(1) write
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest_id | `chainbridge::ChainId` | 
| resource_id | `chainbridge::ResourceId` | 
| minimum_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'EqBridge', 'set_minimum_transfer_amount', {
    'dest_id': 'u8',
    'minimum_amount': 'u128',
    'resource_id': '[u8; 32]',
}
)
```

---------
### set_resource
Stores an asset on chain under an associated resource ID.
Sudo only.

\# &lt;weight&gt;
- O(1) write
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `chainbridge::ResourceId` | 
| asset | `Asset` | 

#### Python
```python
call = substrate.compose_call(
    'EqBridge', 'set_resource', {'asset': 'u64', 'id': '[u8; 32]'}
)
```

---------
### transfer
Deposits specified amount of Eq/Gens tokens to the user&\#x27;s account
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| amount | `T::Balance` | 
| resource_id | `chainbridge::ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'EqBridge', 'transfer', {
    'amount': 'u128',
    'resource_id': '[u8; 32]',
    'to': 'AccountId',
}
)
```

---------
### transfer_native
Transfers some amount of the native token to some recipient on a (whitelisted) destination chain.
Charges fee and accumulates it on the special account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `T::Balance` | 
| recipient | `Vec<u8>` | 
| dest_id | `chainbridge::ChainId` | 
| resource_id | `chainbridge::ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'EqBridge', 'transfer_native', {
    'amount': 'u128',
    'dest_id': 'u8',
    'recipient': 'Bytes',
    'resource_id': '[u8; 32]',
}
)
```

---------
### xcm_transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `Vec<u8>` | 
| amount | `T::Balance` | 
| resource_id | `chainbridge::ResourceId` | 

#### Python
```python
call = substrate.compose_call(
    'EqBridge', 'xcm_transfer', {
    'amount': 'u128',
    'resource_id': '[u8; 32]',
    'to': 'Bytes',
}
)
```

---------
## Events

---------
### ChainAddressTypeChanged
ChainAddressType has changed. \[chainId, Option&lt;ChainAddressType&gt;\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `chainbridge::ChainId` | ```u8```
| None | `Option<ChainAddressType>` | ```(None, ('Ethereum', 'Substrate', 'SubstrateWithPrefix'))```

---------
### FromBridgeTransfer
Transfers funds from the bridge into the network
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Asset` | ```u64```
| None | `T::Balance` | ```u128```

---------
### FromBridgeTransferNext
Transfers funds from the bridge into the network to transfer next
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```
| None | `Asset` | ```u64```
| None | `T::Balance` | ```u128```

---------
### MinimumTransferAmountChanged
Minimum transfer amount to out of the network has changed. \[chainId, resourceId, new_minimum_amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `chainbridge::ChainId` | ```u8```
| None | `chainbridge::ResourceId` | ```[u8; 32]```
| None | `T::Balance` | ```u128```

---------
### Remark
Demonstrate an arbitrary call from a proposal. \[hash\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Hash` | ```[u8; 32]```

---------
### ToBridgeTransfer
Transfers funds out of the network to the bridge
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `Asset` | ```u64```
| None | `T::Balance` | ```u128```

---------
### WithdrawalsToggled
Allowability withdrawals for the resource id to chain has changed. \[resource_id, chain_id, enabled\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `chainbridge::ResourceId` | ```[u8; 32]```
| None | `chainbridge::ChainId` | ```u8```
| None | `bool` | ```bool```

---------
## Storage functions

---------
### AssetResource

#### Python
```python
result = substrate.query(
    'EqBridge', 'AssetResource', ['u64']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### ChainAddressTypes

#### Python
```python
result = substrate.query(
    'EqBridge', 'ChainAddressTypes', ['u8']
)
```

#### Return value
```python
('Ethereum', 'Substrate', 'SubstrateWithPrefix')
```
---------
### EnabledWithdrawals

#### Python
```python
result = substrate.query(
    'EqBridge', 'EnabledWithdrawals', ['[u8; 32]']
)
```

#### Return value
```python
'Bytes'
```
---------
### MinimumTransferAmount

#### Python
```python
result = substrate.query(
    'EqBridge', 'MinimumTransferAmount', ['u8', '[u8; 32]']
)
```

#### Return value
```python
'u128'
```
---------
### Resources

#### Python
```python
result = substrate.query(
    'EqBridge', 'Resources', ['[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
## Errors

---------
### ChainAddressTypeEqual
Attempt to set ChainAddressType to current value

---------
### ChainNotWhitelisted
Interactions with this chain is not permitted

---------
### DisabledChain
Bridge transfers to this chain are disabled

---------
### DisabledWithdrawals
Asset withdrawals to this chain are disabled

---------
### InvalidAccount
Invalid destination Account for XCM transfer

---------
### InvalidAssetType
not allowed to bridge tokens of this type

---------
### InvalidResourceId
Resource id not mapped to `Asset`

---------
### InvalidTransfer

---------
### RecipientChainAddressTypeMismatch
wrong recipient address

---------
### TransferAmountLowerMinimum
Transfer amount is lower than a minimum for given `ChainId` and `ResourceId`

---------
### WithdrawalsAllowabilityEqual
Withdrawals to this resource id and chain id have equal allowability

---------
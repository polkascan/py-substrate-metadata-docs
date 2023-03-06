
# BridgeDarwiniaMessages

---------
## Calls

---------
### increase_message_fee
Pay additional fee for the message.
#### Attributes
| Name | Type |
| -------- | -------- | 
| lane_id | `LaneId` | 
| nonce | `MessageNonce` | 
| additional_fee | `T::OutboundMessageFee` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDarwiniaMessages', 'increase_message_fee', {
    'additional_fee': 'u128',
    'lane_id': '[u8; 4]',
    'nonce': 'u64',
}
)
```

---------
### receive_messages_delivery_proof
Receive messages delivery proof from bridged chain.
#### Attributes
| Name | Type |
| -------- | -------- | 
| proof | `MessagesDeliveryProofOf<T, I>` | 
| relayers_state | `UnrewardedRelayersState` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDarwiniaMessages', 'receive_messages_delivery_proof', {
    'proof': {
        'bridged_header_hash': '[u8; 32]',
        'lane': '[u8; 4]',
        'storage_proof': ['Bytes'],
    },
    'relayers_state': {
        'messages_in_oldest_entry': 'u64',
        'total_messages': 'u64',
        'unrewarded_relayer_entries': 'u64',
    },
}
)
```

---------
### receive_messages_proof
Receive messages proof from bridged chain.

The weight of the call assumes that the transaction always brings outbound lane
state update. Because of that, the submitter (relayer) has no benefit of not including
this data in the transaction, so reward confirmations lags should be minimal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| relayer_id_at_bridged_chain | `T::InboundRelayer` | 
| proof | `MessagesProofOf<T, I>` | 
| messages_count | `u32` | 
| dispatch_weight | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDarwiniaMessages', 'receive_messages_proof', {
    'dispatch_weight': 'u64',
    'messages_count': 'u32',
    'proof': {
        'bridged_header_hash': '[u8; 32]',
        'lane': '[u8; 4]',
        'nonces_end': 'u64',
        'nonces_start': 'u64',
        'storage_proof': ['Bytes'],
    },
    'relayer_id_at_bridged_chain': 'AccountId',
}
)
```

---------
### send_message
Send message over lane.
#### Attributes
| Name | Type |
| -------- | -------- | 
| lane_id | `LaneId` | 
| payload | `T::OutboundPayload` | 
| delivery_and_dispatch_fee | `T::OutboundMessageFee` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDarwiniaMessages', 'send_message', {
    'delivery_and_dispatch_fee': 'u128',
    'lane_id': '[u8; 4]',
    'payload': {
        'call': 'Bytes',
        'dispatch_fee_payment': (
            'AtSourceChain',
            'AtTargetChain',
        ),
        'origin': {
            'SourceAccount': 'AccountId',
            'SourceRoot': None,
            'TargetAccount': (
                'AccountId',
                {
                    'Ecdsa': '[u8; 33]',
                    'Ed25519': '[u8; 32]',
                    'Sr25519': '[u8; 32]',
                },
                {
                    'Ecdsa': '[u8; 65]',
                    'Ed25519': '[u8; 64]',
                    'Sr25519': '[u8; 64]',
                },
            ),
        },
        'spec_version': 'u32',
        'weight': 'u64',
    },
}
)
```

---------
### set_operating_mode
Halt or resume all/some pallet operations.

May only be called either by root, or by `PalletOwner`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| operating_mode | `OperatingMode` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDarwiniaMessages', 'set_operating_mode', {
    'operating_mode': (
        'Normal',
        'RejectingOutboundMessages',
        'Halted',
    ),
}
)
```

---------
### set_owner
Change `PalletOwner`.

May only be called either by root, or by `PalletOwner`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_owner | `Option<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDarwiniaMessages', 'set_owner', {'new_owner': (None, 'AccountId')}
)
```

---------
### update_pallet_parameter
Update pallet parameter.

May only be called either by root, or by `PalletOwner`.

The weight is: single read for permissions check + 2 writes for parameter value and
event.
#### Attributes
| Name | Type |
| -------- | -------- | 
| parameter | `T::Parameter` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeDarwiniaMessages', 'update_pallet_parameter', {
    'parameter': {
        'DarwiniaToCrabConversionRate': 'u128',
    },
}
)
```

---------
## Events

---------
### MessageAccepted
Message has been accepted and is waiting to be delivered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `LaneId` | ```[u8; 4]```
| None | `MessageNonce` | ```u64```

---------
### MessagesDelivered
Messages in the inclusive range have been delivered to the bridged chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `LaneId` | ```[u8; 4]```
| None | `DeliveredMessages` | ```{'begin': 'u64', 'end': 'u64', 'dispatch_results': 'BitVec'}```

---------
### ParameterUpdated
Pallet parameter has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::Parameter` | ```{'DarwiniaToCrabConversionRate': 'u128'}```

---------
## Storage functions

---------
### InboundLanes
 Map of lane id =&gt; inbound lane data.

#### Python
```python
result = substrate.query(
    'BridgeDarwiniaMessages', 'InboundLanes', ['[u8; 4]']
)
```

#### Return value
```python
{
    'last_confirmed_nonce': 'u64',
    'relayers': [
        {
            'messages': {
                'begin': 'u64',
                'dispatch_results': 'BitVec',
                'end': 'u64',
            },
            'relayer': 'AccountId',
        },
    ],
}
```
---------
### OutboundLanes
 Map of lane id =&gt; outbound lane data.

#### Python
```python
result = substrate.query(
    'BridgeDarwiniaMessages', 'OutboundLanes', ['[u8; 4]']
)
```

#### Return value
```python
{
    'latest_generated_nonce': 'u64',
    'latest_received_nonce': 'u64',
    'oldest_unpruned_nonce': 'u64',
}
```
---------
### OutboundMessages
 All queued outbound messages.

#### Python
```python
result = substrate.query(
    'BridgeDarwiniaMessages', 'OutboundMessages', [
    {
        'lane_id': '[u8; 4]',
        'nonce': 'u64',
    },
]
)
```

#### Return value
```python
{'fee': 'u128', 'payload': 'Bytes'}
```
---------
### PalletOperatingMode
 The current operating mode of the pallet.

 Depending on the mode either all, some, or no transactions will be allowed.

#### Python
```python
result = substrate.query(
    'BridgeDarwiniaMessages', 'PalletOperatingMode', []
)
```

#### Return value
```python
('Normal', 'RejectingOutboundMessages', 'Halted')
```
---------
### PalletOwner
 Optional pallet owner.

 Pallet owner has a right to halt all pallet operations and then resume it. If it is
 `None`, then there are no direct ways to halt/resume pallet operations, but other
 runtime methods may still be used to do that (i.e. democracy::referendum to update halt
 flag directly or call the `halt_operations`).

#### Python
```python
result = substrate.query(
    'BridgeDarwiniaMessages', 'PalletOwner', []
)
```

#### Return value
```python
'AccountId'
```
---------
## Constants

---------
### BridgedChainId
 Gets the chain id value from the instance.
#### Value
```python
'0x64617277'
```
#### Python
```python
constant = substrate.get_constant('BridgeDarwiniaMessages', 'BridgedChainId')
```
---------
## Errors

---------
### FailedToWithdrawMessageFee
Submitter has failed to pay fee for delivering and dispatching messages.

---------
### Halted
All pallet operations are halted.

---------
### InvalidMessagesDeliveryProof
Invalid messages delivery proof has been submitted.

---------
### InvalidMessagesProof
Invalid messages has been submitted.

---------
### InvalidUnrewardedRelayers
The bridged chain has invalid `UnrewardedRelayers` in its storage (fatal for the lane).

---------
### InvalidUnrewardedRelayersState
The relayer has declared invalid unrewarded relayers state in the
`receive_messages_delivery_proof` call.

---------
### MessageIsAlreadyDelivered
The message someone is trying to work with (i.e. increase fee) is already-delivered.

---------
### MessageIsNotYetSent
The message someone is trying to work with (i.e. increase fee) is not yet sent.

---------
### MessageRejectedByChainVerifier
Message has been treated as invalid by chain verifier.

---------
### MessageRejectedByLaneVerifier
Message has been treated as invalid by lane verifier.

---------
### TooManyMessagesInTheProof
The transaction brings too many messages.

---------
### TryingToConfirmMoreMessagesThanExpected
The number of actually confirmed messages is going to be larger than the number of
messages in the proof. This may mean that this or bridged chain storage is corrupted.

---------
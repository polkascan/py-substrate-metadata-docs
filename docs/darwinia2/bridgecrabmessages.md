
# BridgeCrabMessages

---------
## Calls

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
    'BridgeCrabMessages', 'receive_messages_delivery_proof', {
    'proof': {
        'bridged_header_hash': '[u8; 32]',
        'lane': '[u8; 4]',
        'storage_proof': ['Bytes'],
    },
    'relayers_state': {
        'last_delivered_nonce': 'u64',
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

Note: To maintain compatibility, the call index is 5 instead of 4 because the
call(increase_message_fee) with index 4 has been removed. https://github.com/darwinia-network/darwinia-messages-substrate/pull/207
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
    'BridgeCrabMessages', 'receive_messages_proof', {
    'dispatch_weight': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
    'messages_count': 'u32',
    'proof': {
        'bridged_header_hash': '[u8; 32]',
        'lane': '[u8; 4]',
        'nonces_end': 'u64',
        'nonces_start': 'u64',
        'storage_proof': ['Bytes'],
    },
    'relayer_id_at_bridged_chain': '[u8; 20]',
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
    'BridgeCrabMessages', 'send_message', {
    'delivery_and_dispatch_fee': 'u128',
    'lane_id': '[u8; 4]',
    'payload': {
        'call': 'Bytes',
        'dispatch_fee_payment': (
            'AtSourceChain',
            'AtTargetChain',
        ),
        'origin': {
            'SourceAccount': '[u8; 20]',
            'SourceRoot': None,
            'TargetAccount': (
                '[u8; 20]',
                '[u8; 20]',
                '[u8; 65]',
            ),
        },
        'spec_version': 'u32',
        'weight': {
            'proof_size': 'u64',
            'ref_time': 'u64',
        },
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
| operating_mode | `MessagesOperatingMode` | 

#### Python
```python
call = substrate.compose_call(
    'BridgeCrabMessages', 'set_operating_mode', {
    'operating_mode': {
        'Basic': ('Normal', 'Halted'),
        'RejectingOutboundMessages': None,
    },
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
    'BridgeCrabMessages', 'set_owner', {'new_owner': (None, '[u8; 20]')}
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
    'BridgeCrabMessages', 'update_pallet_parameter', {'parameter': ()}
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
| lane_id | `LaneId` | ```[u8; 4]```
| nonce | `MessageNonce` | ```u64```

---------
### MessagesDelivered
Messages in the inclusive range have been delivered to the bridged chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| lane_id | `LaneId` | ```[u8; 4]```
| messages | `DeliveredMessages` | ```{'begin': 'u64', 'end': 'u64', 'dispatch_results': 'BitVec'}```

---------
### MessagesReceived
Messages have been received from the bridged chain.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<ReceivedMessages<ReceivalResult>>` | ```[{'lane': '[u8; 4]', 'receive_results': [('u64', {'Dispatched': 'scale_info::158', 'InvalidNonce': None, 'TooManyUnrewardedRelayers': None, 'TooManyUnconfirmedMessages': None, 'PreDispatchValidateFailed': None})], 'skipped_for_not_enough_weight': ['u64']}]```

---------
### ParameterUpdated
Pallet parameter has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| parameter | `T::Parameter` | ```()```

---------
## Storage functions

---------
### InboundLanes
 Map of lane id =&gt; inbound lane data.

#### Python
```python
result = substrate.query(
    'BridgeCrabMessages', 'InboundLanes', ['[u8; 4]']
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
            'relayer': '[u8; 20]',
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
    'BridgeCrabMessages', 'OutboundLanes', ['[u8; 4]']
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
    'BridgeCrabMessages', 'OutboundMessages', [
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
    'BridgeCrabMessages', 'PalletOperatingMode', []
)
```

#### Return value
```python
{'Basic': ('Normal', 'Halted'), 'RejectingOutboundMessages': None}
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
    'BridgeCrabMessages', 'PalletOwner', []
)
```

#### Return value
```python
'[u8; 20]'
```
---------
## Constants

---------
### BridgedChainId
 Gets the chain id value from the instance.
#### Value
```python
'0x63726162'
```
#### Python
```python
constant = substrate.get_constant('BridgeCrabMessages', 'BridgedChainId')
```
---------
### MaximalOutboundPayloadSize
 Maximal size of the outbound payload.
#### Value
```python
2621440
```
#### Python
```python
constant = substrate.get_constant('BridgeCrabMessages', 'MaximalOutboundPayloadSize')
```
---------
## Errors

---------
### BridgeModule
Error generated by the `OwnedBridgeModule` trait.

---------
### FailedToWithdrawMessageFee
Submitter has failed to pay fee for delivering and dispatching messages.

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
### MessageIsTooLarge
The message is too large to be sent over the bridge.

---------
### MessageRejectedByChainVerifier
Message has been treated as invalid by chain verifier.

---------
### MessageRejectedByLaneVerifier
Message has been treated as invalid by lane verifier.

---------
### NotOperatingNormally
Pallet is not in Normal operating mode.

---------
### TooManyMessagesInTheProof
The transaction brings too many messages.

---------
### TryingToConfirmMoreMessagesThanExpected
The number of actually confirmed messages is going to be larger than the number of
messages in the proof. This may mean that this or bridged chain storage is corrupted.

---------
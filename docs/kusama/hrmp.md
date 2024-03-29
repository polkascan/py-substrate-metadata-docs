
# Hrmp

---------
## Calls

---------
### establish_system_channel
See [`Pallet::establish_system_channel`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| sender | `ParaId` | 
| recipient | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'establish_system_channel', {'recipient': 'u32', 'sender': 'u32'}
)
```

---------
### force_clean_hrmp
See [`Pallet::force_clean_hrmp`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| num_inbound | `u32` | 
| num_outbound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'force_clean_hrmp', {
    'num_inbound': 'u32',
    'num_outbound': 'u32',
    'para': 'u32',
}
)
```

---------
### force_open_hrmp_channel
See [`Pallet::force_open_hrmp_channel`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| sender | `ParaId` | 
| recipient | `ParaId` | 
| max_capacity | `u32` | 
| max_message_size | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'force_open_hrmp_channel', {
    'max_capacity': 'u32',
    'max_message_size': 'u32',
    'recipient': 'u32',
    'sender': 'u32',
}
)
```

---------
### force_process_hrmp_close
See [`Pallet::force_process_hrmp_close`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| channels | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'force_process_hrmp_close', {'channels': 'u32'}
)
```

---------
### force_process_hrmp_open
See [`Pallet::force_process_hrmp_open`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| channels | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'force_process_hrmp_open', {'channels': 'u32'}
)
```

---------
### hrmp_accept_open_channel
See [`Pallet::hrmp_accept_open_channel`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| sender | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'hrmp_accept_open_channel', {'sender': 'u32'}
)
```

---------
### hrmp_cancel_open_request
See [`Pallet::hrmp_cancel_open_request`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| channel_id | `HrmpChannelId` | 
| open_requests | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'hrmp_cancel_open_request', {
    'channel_id': {
        'recipient': 'u32',
        'sender': 'u32',
    },
    'open_requests': 'u32',
}
)
```

---------
### hrmp_close_channel
See [`Pallet::hrmp_close_channel`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| channel_id | `HrmpChannelId` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'hrmp_close_channel', {
    'channel_id': {
        'recipient': 'u32',
        'sender': 'u32',
    },
}
)
```

---------
### hrmp_init_open_channel
See [`Pallet::hrmp_init_open_channel`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `ParaId` | 
| proposed_max_capacity | `u32` | 
| proposed_max_message_size | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'hrmp_init_open_channel', {
    'proposed_max_capacity': 'u32',
    'proposed_max_message_size': 'u32',
    'recipient': 'u32',
}
)
```

---------
### poke_channel_deposits
See [`Pallet::poke_channel_deposits`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| sender | `ParaId` | 
| recipient | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'poke_channel_deposits', {'recipient': 'u32', 'sender': 'u32'}
)
```

---------
## Events

---------
### ChannelClosed
HRMP channel closed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| by_parachain | `ParaId` | ```u32```
| channel_id | `HrmpChannelId` | ```{'sender': 'u32', 'recipient': 'u32'}```

---------
### HrmpChannelForceOpened
An HRMP channel was opened via Root origin.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `ParaId` | ```u32```
| recipient | `ParaId` | ```u32```
| proposed_max_capacity | `u32` | ```u32```
| proposed_max_message_size | `u32` | ```u32```

---------
### HrmpSystemChannelOpened
An HRMP channel was opened between two system chains.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `ParaId` | ```u32```
| recipient | `ParaId` | ```u32```
| proposed_max_capacity | `u32` | ```u32```
| proposed_max_message_size | `u32` | ```u32```

---------
### OpenChannelAccepted
Open HRMP channel accepted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `ParaId` | ```u32```
| recipient | `ParaId` | ```u32```

---------
### OpenChannelCanceled
An HRMP channel request sent by the receiver was canceled by either party.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| by_parachain | `ParaId` | ```u32```
| channel_id | `HrmpChannelId` | ```{'sender': 'u32', 'recipient': 'u32'}```

---------
### OpenChannelDepositsUpdated
An HRMP channel&\#x27;s deposits were updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `ParaId` | ```u32```
| recipient | `ParaId` | ```u32```

---------
### OpenChannelRequested
Open HRMP channel requested.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `ParaId` | ```u32```
| recipient | `ParaId` | ```u32```
| proposed_max_capacity | `u32` | ```u32```
| proposed_max_message_size | `u32` | ```u32```

---------
## Storage functions

---------
### HrmpAcceptedChannelRequestCount
 This mapping tracks how many open channel requests were accepted by a given recipient para.
 Invariant: `HrmpOpenChannelRequests` should contain the same number of items `(_, X)` with
 `confirmed` set to true, as the number of `HrmpAcceptedChannelRequestCount` for `X`.

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpAcceptedChannelRequestCount', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### HrmpChannelContents
 Storage for the messages for each channel.
 Invariant: cannot be non-empty if the corresponding channel in `HrmpChannels` is `None`.

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpChannelContents', [{'recipient': 'u32', 'sender': 'u32'}]
)
```

#### Return value
```python
[{'data': 'Bytes', 'sent_at': 'u32'}]
```
---------
### HrmpChannelDigests
 Maintains a mapping that can be used to answer the question: What paras sent a message at
 the given block number for a given receiver. Invariants:
 - The inner `Vec&lt;ParaId&gt;` is never empty.
 - The inner `Vec&lt;ParaId&gt;` cannot store two same `ParaId`.
 - The outer vector is sorted ascending by block number and cannot store two items with the
   same block number.

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpChannelDigests', ['u32']
)
```

#### Return value
```python
[('u32', ['u32'])]
```
---------
### HrmpChannels
 HRMP channel data associated with each para.
 Invariant:
 - each participant in the channel should satisfy `Paras::is_valid_para(P)` within a session.

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpChannels', [{'recipient': 'u32', 'sender': 'u32'}]
)
```

#### Return value
```python
{
    'max_capacity': 'u32',
    'max_message_size': 'u32',
    'max_total_size': 'u32',
    'mqc_head': (None, 'scale_info::12'),
    'msg_count': 'u32',
    'recipient_deposit': 'u128',
    'sender_deposit': 'u128',
    'total_size': 'u32',
}
```
---------
### HrmpCloseChannelRequests
 A set of pending HRMP close channel requests that are going to be closed during the session
 change. Used for checking if a given channel is registered for closure.

 The set is accompanied by a list for iteration.

 Invariant:
 - There are no channels that exists in list but not in the set and vice versa.

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpCloseChannelRequests', [{'recipient': 'u32', 'sender': 'u32'}]
)
```

#### Return value
```python
()
```
---------
### HrmpCloseChannelRequestsList

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpCloseChannelRequestsList', []
)
```

#### Return value
```python
[{'recipient': 'u32', 'sender': 'u32'}]
```
---------
### HrmpEgressChannelsIndex

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpEgressChannelsIndex', ['u32']
)
```

#### Return value
```python
['u32']
```
---------
### HrmpIngressChannelsIndex
 Ingress/egress indexes allow to find all the senders and receivers given the opposite side.
 I.e.

 (a) ingress index allows to find all the senders for a given recipient.
 (b) egress index allows to find all the recipients for a given sender.

 Invariants:
 - for each ingress index entry for `P` each item `I` in the index should present in
   `HrmpChannels` as `(I, P)`.
 - for each egress index entry for `P` each item `E` in the index should present in
   `HrmpChannels` as `(P, E)`.
 - there should be no other dangling channels in `HrmpChannels`.
 - the vectors are sorted.

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpIngressChannelsIndex', ['u32']
)
```

#### Return value
```python
['u32']
```
---------
### HrmpOpenChannelRequestCount
 This mapping tracks how many open channel requests are initiated by a given sender para.
 Invariant: `HrmpOpenChannelRequests` should contain the same number of items that has
 `(X, _)` as the number of `HrmpOpenChannelRequestCount` for `X`.

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpOpenChannelRequestCount', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### HrmpOpenChannelRequests
 The set of pending HRMP open channel requests.

 The set is accompanied by a list for iteration.

 Invariant:
 - There are no channels that exists in list but not in the set and vice versa.

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpOpenChannelRequests', [{'recipient': 'u32', 'sender': 'u32'}]
)
```

#### Return value
```python
{
    '_age': 'u32',
    'confirmed': 'bool',
    'max_capacity': 'u32',
    'max_message_size': 'u32',
    'max_total_size': 'u32',
    'sender_deposit': 'u128',
}
```
---------
### HrmpOpenChannelRequestsList

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpOpenChannelRequestsList', []
)
```

#### Return value
```python
[{'recipient': 'u32', 'sender': 'u32'}]
```
---------
### HrmpWatermarks
 The HRMP watermark associated with each para.
 Invariant:
 - each para `P` used here as a key should satisfy `Paras::is_valid_para(P)` within a
   session.

#### Python
```python
result = substrate.query(
    'Hrmp', 'HrmpWatermarks', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### AcceptHrmpChannelAlreadyConfirmed
The channel is already confirmed.

---------
### AcceptHrmpChannelDoesntExist
The channel from the sender to the origin doesn&\#x27;t exist.

---------
### AcceptHrmpChannelLimitExceeded
The recipient already has the maximum number of allowed inbound channels.

---------
### CancelHrmpOpenChannelUnauthorized
Canceling is requested by neither the sender nor recipient of the open channel request.

---------
### ChannelCreationNotAuthorized
The channel between these two chains cannot be authorized.

---------
### CloseHrmpChannelAlreadyUnderway
The channel close request is already requested.

---------
### CloseHrmpChannelDoesntExist
The channel to be closed doesn&\#x27;t exist.

---------
### CloseHrmpChannelUnauthorized
The origin tries to close a channel where it is neither the sender nor the recipient.

---------
### OpenHrmpChannelAlreadyConfirmed
Cannot cancel an HRMP open channel request because it is already confirmed.

---------
### OpenHrmpChannelAlreadyExists
The channel already exists

---------
### OpenHrmpChannelAlreadyRequested
There is already a request to open the same channel.

---------
### OpenHrmpChannelCapacityExceedsLimit
The requested capacity exceeds the global limit.

---------
### OpenHrmpChannelDoesntExist
The open request doesn&\#x27;t exist.

---------
### OpenHrmpChannelInvalidRecipient
The recipient is not a valid para.

---------
### OpenHrmpChannelLimitExceeded
The sender already has the maximum number of allowed outbound channels.

---------
### OpenHrmpChannelMessageSizeExceedsLimit
The open request requested the message size that exceeds the global limit.

---------
### OpenHrmpChannelToSelf
The sender tried to open a channel to themselves.

---------
### OpenHrmpChannelZeroCapacity
The requested capacity is zero.

---------
### OpenHrmpChannelZeroMessageSize
The requested maximum message size is 0.

---------
### WrongWitness
The provided witness data is wrong.

---------
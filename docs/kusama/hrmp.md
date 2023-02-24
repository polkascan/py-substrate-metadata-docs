
# Hrmp

---------
## Calls

---------
### force_clean_hrmp
This extrinsic triggers the cleanup of all the HRMP storage items that
a para may have. Normally this happens once per session, but this allows
you to trigger the cleanup immediately for a specific parachain.

Origin must be Root.

Number of inbound and outbound channels for `para` must be provided as witness data of weighing.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| inbound | `u32` | 
| outbound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Hrmp', 'force_clean_hrmp', {
    'inbound': 'u32',
    'outbound': 'u32',
    'para': 'u32',
}
)
```

---------
### force_open_hrmp_channel
Open a channel from a `sender` to a `recipient` `ParaId` using the Root origin. Although
opened by Root, the `max_capacity` and `max_message_size` are still subject to the Relay
Chain&\#x27;s configured limits.

Expected use is when one of the `ParaId`s involved in the channel is governed by the
Relay Chain, e.g. a common good parachain.
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
Force process HRMP close channel requests.

If there are pending HRMP close channel requests, you can use this
function process all of those requests immediately.

Total number of closing channels must be provided as witness data of weighing.
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
Force process HRMP open channel requests.

If there are pending HRMP open channel requests, you can use this
function process all of those requests immediately.

Total number of opening channels must be provided as witness data of weighing.
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
Accept a pending open channel request from the given sender.

The channel will be opened only on the next session boundary.
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
This cancels a pending open channel request. It can be canceled by either of the sender
or the recipient for that request. The origin must be either of those.

The cancellation happens immediately. It is not possible to cancel the request if it is
already accepted.

Total number of open requests (i.e. `HrmpOpenChannelRequestsList`) must be provided as
witness data.
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
Initiate unilateral closing of a channel. The origin must be either the sender or the
recipient in the channel being closed.

The closure can only happen on a session change.
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
Initiate opening a channel from a parachain to a given recipient with given channel
parameters.

- `proposed_max_capacity` - specifies how many messages can be in the channel at once.
- `proposed_max_message_size` - specifies the maximum size of the messages.

These numbers are a subject to the relay-chain configuration limits.

The channel can be opened only after the recipient confirms it and only on a session
change.
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
## Events

---------
### ChannelClosed
HRMP channel closed. `[by_parachain, channel_id]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `HrmpChannelId` | ```{'sender': 'u32', 'recipient': 'u32'}```

---------
### HrmpChannelForceOpened
An HRMP channel was opened via Root origin.
`[sender, recipient, proposed_max_capacity, proposed_max_message_size]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `u32` | ```u32```

---------
### OpenChannelAccepted
Open HRMP channel accepted. `[sender, recipient]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `ParaId` | ```u32```

---------
### OpenChannelCanceled
An HRMP channel request sent by the receiver was canceled by either party.
`[by_parachain, channel_id]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `HrmpChannelId` | ```{'sender': 'u32', 'recipient': 'u32'}```

---------
### OpenChannelRequested
Open HRMP channel requested.
`[sender, recipient, proposed_max_capacity, proposed_max_message_size]`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `ParaId` | ```u32```
| None | `u32` | ```u32```
| None | `u32` | ```u32```

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
    'mqc_head': (None, '[u8; 32]'),
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
 - each para `P` used here as a key should satisfy `Paras::is_valid_para(P)` within a session.

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
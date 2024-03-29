
# Dmp

---------
## Storage functions

---------
### DeliveryFeeFactor
 The factor to multiply the base delivery fee by.

#### Python
```python
result = substrate.query(
    'Dmp', 'DeliveryFeeFactor', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### DownwardMessageQueueHeads
 A mapping that stores the downward message queue MQC head for each para.

 Each link in this chain has a form:
 `(prev_head, B, H(M))`, where
 - `prev_head`: is the previous head hash or zero if none.
 - `B`: is the relay-chain block number in which a message was appended.
 - `H(M)`: is the hash of the message being appended.

#### Python
```python
result = substrate.query(
    'Dmp', 'DownwardMessageQueueHeads', ['u32']
)
```

#### Return value
```python
'scale_info::12'
```
---------
### DownwardMessageQueues
 The downward messages addressed for a certain para.

#### Python
```python
result = substrate.query(
    'Dmp', 'DownwardMessageQueues', ['u32']
)
```

#### Return value
```python
[{'msg': 'Bytes', 'sent_at': 'u32'}]
```
---------
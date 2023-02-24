
# Dmp

---------
## Storage functions

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
'[u8; 32]'
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
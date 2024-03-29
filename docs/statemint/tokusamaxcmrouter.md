
# ToKusamaXcmRouter

---------
## Calls

---------
### report_bridge_status
See [`Pallet::report_bridge_status`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| bridge_id | `H256` | 
| is_congested | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'ToKusamaXcmRouter', 'report_bridge_status', {
    'bridge_id': 'scale_info::12',
    'is_congested': 'bool',
}
)
```

---------
## Storage functions

---------
### Bridge
 Bridge that we are using.

 **bridges-v1** assumptions: all outbound messages through this router are using single lane
 and to single remote consensus. If there is some other remote consensus that uses the same
 bridge hub, the separate pallet instance shall be used, In `v2` we&#x27;ll have all required
 primitives (lane-id aka bridge-id, derived from XCM locations) to support multiple  bridges
 by the same pallet instance.

#### Python
```python
result = substrate.query(
    'ToKusamaXcmRouter', 'Bridge', []
)
```

#### Return value
```python
{'delivery_fee_factor': 'u128', 'is_congested': 'bool'}
```
---------
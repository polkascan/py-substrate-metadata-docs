
# Swaps

---------
## Storage functions

---------
### OrderIdToSwapId
 Maps a `OrderId` to its corresponding `AccountId` and `SwapId`

 NOTE: The storage is killed when the swap order no longer exists

#### Python
```python
result = substrate.query(
    'Swaps', 'OrderIdToSwapId', ['u64']
)
```

#### Return value
```python
(
    'AccountId',
    (
        {'pool_id': 'u64', 'tranche_id': '[u8; 16]'},
        ('Investment', 'Redemption'),
    ),
)
```
---------
### SwapIdToOrderId
 Maps an `AccountId` and `SwapId` to its corresponding `OrderId`

 NOTE: The storage is killed when the swap order no longer exists

#### Python
```python
result = substrate.query(
    'Swaps', 'SwapIdToOrderId', [
    (
        'AccountId',
        (
            {
                'pool_id': 'u64',
                'tranche_id': '[u8; 16]',
            },
            (
                'Investment',
                'Redemption',
            ),
        ),
    ),
]
)
```

#### Return value
```python
'u64'
```
---------
## Errors

---------
### CancelMoreThanPending
Emitted when the cancelled amount is greater than the pending amount

---------
### OrderNotFound
Failed to retrieve the order.

---------
### SwapNotFound
Failed to retrieve the swap.

---------
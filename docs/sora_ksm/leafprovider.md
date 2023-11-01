
# LeafProvider

---------
## Storage functions

---------
### LatestDigest
 Latest digest

#### Python
```python
result = substrate.query(
    'LeafProvider', 'LatestDigest', []
)
```

#### Return value
```python
[
    {
        'Commitment': (
            {
                'EVM': '[u64; 4]',
                'EVMLegacy': 'u32',
                'Sub': {
                    'Custom': 'u32',
                    'Kusama': None,
                    'Mainnet': None,
                    'Polkadot': None,
                    'Rococo': None,
                },
            },
            '[u8; 32]',
        ),
    },
]
```
---------
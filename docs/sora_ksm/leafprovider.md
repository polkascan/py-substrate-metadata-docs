
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
                'EVM': 'scale_info::111',
                'EVMLegacy': 'u32',
                'Sub': (
                    'Mainnet',
                    'Kusama',
                    'Polkadot',
                    'Rococo',
                    'Alphanet',
                    'Liberland',
                ),
            },
            'scale_info::11',
        ),
    },
]
```
---------

# MerkleDistributor

---------
## Calls

---------
### add_to_create_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MerkleDistributor', 'add_to_create_whitelist', {'account': 'AccountId'}
)
```

---------
### charge
Charge currency to the account of merkle distributor

`merkle_distributor_id`: ID of a merkle distributor.
#### Attributes
| Name | Type |
| -------- | -------- | 
| merkle_distributor_id | `T::MerkleDistributorId` | 

#### Python
```python
call = substrate.compose_call(
    'MerkleDistributor', 'charge', {'merkle_distributor_id': 'u32'}
)
```

---------
### claim
`claim` Claim rewards through user information and merkle proof.

- `merkle_distributor_id`: ID of a merkle distributor.
- `index`: The index of the merkle tree leaf.
- `account`: The owner&\#x27;s account of merkle proof.
- `merkle_proof`: The hashes with merkle tree leaf can get merkle tree root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| merkle_distributor_id | `T::MerkleDistributorId` | 
| index | `u32` | 
| account | `<T::Lookup as StaticLookup>::Source` | 
| amount | `u128` | 
| merkle_proof | `Vec<H256>` | 

#### Python
```python
call = substrate.compose_call(
    'MerkleDistributor', 'claim', {
    'account': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'amount': 'u128',
    'index': 'u32',
    'merkle_distributor_id': 'u32',
    'merkle_proof': ['[u8; 32]'],
}
)
```

---------
### create_merkle_distributor
`create_merkle_distributor` will create a merkle distributor,
 which allow specified users claim asset.

The dispatch origin for this call must be `Signed` by root.

- `merkle_root`: The root of a merkle tree.
- `description`: About the purpose of this distribution.
- `distribute_currency`: The id of currency about this distribution.
- `distribute_amount`: The total currency amount of this distribution.
#### Attributes
| Name | Type |
| -------- | -------- | 
| merkle_root | `H256` | 
| description | `Vec<u8>` | 
| distribute_currency | `T::CurrencyId` | 
| distribute_amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'MerkleDistributor', 'create_merkle_distributor', {
    'description': 'Bytes',
    'distribute_amount': 'u128',
    'distribute_currency': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
    'merkle_root': '[u8; 32]',
}
)
```

---------
### emergency_withdraw
#### Attributes
| Name | Type |
| -------- | -------- | 
| merkle_distributor_id | `T::MerkleDistributorId` | 
| recipient | `<T::Lookup as StaticLookup>::Source` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'MerkleDistributor', 'emergency_withdraw', {
    'amount': 'u128',
    'merkle_distributor_id': 'u32',
    'recipient': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### remove_from_create_whitelist
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'MerkleDistributor', 'remove_from_create_whitelist', {'account': 'AccountId'}
)
```

---------
## Events

---------
### AddToWhiteList
add account who can create merkle distributor. \ [account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### Claim
claim reward. \[merkle distributor id, account, balance]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::MerkleDistributorId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `u128` | ```u128```

---------
### Create
create a merkle distributor. \ [merkle distributor id, merkle tree root, total reward balance]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::MerkleDistributorId` | ```u32```
| None | `H256` | ```[u8; 32]```
| None | `T::Balance` | ```u128```

---------
### RemoveFromWhiteList
remove account from the set who can create merkle distributor. \ [account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### Withdraw
withdraw reward. \ [merkle distributor id, account, balance]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::MerkleDistributorId` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `T::Balance` | ```u128```

---------
## Storage functions

---------
### ClaimedBitMap

#### Python
```python
result = substrate.query(
    'MerkleDistributor', 'ClaimedBitMap', ['u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
### CreateWhiteSet
 Accounts in the whitelist can create merkle distributor.

#### Python
```python
result = substrate.query(
    'MerkleDistributor', 'CreateWhiteSet', []
)
```

#### Return value
```python
'scale_info::631'
```
---------
### MerkleDistributorMetadata

#### Python
```python
result = substrate.query(
    'MerkleDistributor', 'MerkleDistributorMetadata', ['u32']
)
```

#### Return value
```python
{
    'charged': 'bool',
    'description': 'Bytes',
    'distribute_amount': 'u128',
    'distribute_currency': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': ('u8', 'u32', 'u32', 'u32'),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
    'distribute_holder': 'AccountId',
    'merkle_root': '[u8; 32]',
}
```
---------
### NextMerkleDistributorId

#### Python
```python
result = substrate.query(
    'MerkleDistributor', 'NextMerkleDistributorId', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### PalletId
#### Value
```python
'0x62662f6d6b6c6473'
```
#### Python
```python
constant = substrate.get_constant('MerkleDistributor', 'PalletId')
```
---------
### StringLimit
 The maximum length of a merkel description stored on-chain.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('MerkleDistributor', 'StringLimit')
```
---------
## Errors

---------
### AlreadyInWhiteList
Account has already in the set who can create merkle distributor

---------
### BadChargeAccount


---------
### BadDescription
Invalid metadata given.

---------
### Charged
The reward is already charged.

---------
### Claimed
The reward is already distributed.

---------
### InvalidMerkleDistributorId
The id is not exist.

---------
### MerkleVerifyFailed
The proof is invalid

---------
### NotInWhiteList
Account is no in the set who can create merkle distributor

---------
### WithdrawAmountExceed
Withdraw amount exceed charge amount.

---------
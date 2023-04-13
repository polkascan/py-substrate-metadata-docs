
# Portfolio

---------
## Calls

---------
### accept_portfolio_custody
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Portfolio', 'accept_portfolio_custody', {'auth_id': 'u64'}
)
```

---------
### create_portfolio
Creates a portfolio with the given `name`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| name | `PortfolioName` | 

#### Python
```python
call = substrate.compose_call(
    'Portfolio', 'create_portfolio', {'name': 'Bytes'}
)
```

---------
### delete_portfolio
Deletes a user portfolio. A portfolio can be deleted only if it has no funds.

\# Errors
* `PortfolioDoesNotExist` if `num` doesn&\#x27;t reference a valid portfolio.
* `PortfolioNotEmpty` if the portfolio still holds any asset

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| num | `PortfolioNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Portfolio', 'delete_portfolio', {'num': 'u64'}
)
```

---------
### move_portfolio_funds
Moves a token amount from one portfolio of an identity to another portfolio of the same
identity. Must be called by the custodian of the sender.
Funds from deleted portfolios can also be recovered via this method.

A short memo can be added to to each token amount moved.

\# Errors
* `PortfolioDoesNotExist` if one or both of the portfolios reference an invalid portfolio.
* `destination_is_same_portfolio` if both sender and receiver portfolio are the same
* `DifferentIdentityPortfolios` if the sender and receiver portfolios belong to different identities
* `UnauthorizedCustodian` if the caller is not the custodian of the from portfolio
* `InsufficientPortfolioBalance` if the sender does not have enough free balance
* `NoDuplicateAssetsAllowed` the same ticker can&\#x27;t be repeated in the items vector.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `PortfolioId` | 
| to | `PortfolioId` | 
| items | `Vec<MovePortfolioItem>` | 

#### Python
```python
call = substrate.compose_call(
    'Portfolio', 'move_portfolio_funds', {
    'from': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    'items': [
        {
            'amount': 'u128',
            'memo': (None, '[u8; 32]'),
            'ticker': '[u8; 12]',
        },
    ],
    'to': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
}
)
```

---------
### move_portfolio_funds_v2
Moves fungigle an non-fungible tokens from one portfolio of an identity to another portfolio of the same
identity. Must be called by the custodian of the sender.
Funds from deleted portfolios can also be recovered via this method.

A short memo can be added to to each token amount moved.

\# Errors
* `PortfolioDoesNotExist` if one or both of the portfolios reference an invalid portfolio.
* `destination_is_same_portfolio` if both sender and receiver portfolio are the same
* `DifferentIdentityPortfolios` if the sender and receiver portfolios belong to different identities
* `UnauthorizedCustodian` if the caller is not the custodian of the from portfolio
* `InsufficientPortfolioBalance` if the sender does not have enough free balance
* `NoDuplicateAssetsAllowed` the same ticker can&\#x27;t be repeated in the items vector.
* `InvalidTransferNFTNotOwned` if the caller is trying to move an NFT he doesn&\#x27;t own.
* `InvalidTransferNFTIsLocked` if the caller is trying to move a locked NFT.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `PortfolioId` | 
| to | `PortfolioId` | 
| funds | `Vec<Fund>` | 

#### Python
```python
call = substrate.compose_call(
    'Portfolio', 'move_portfolio_funds_v2', {
    'from': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    'funds': [
        {
            'description': {
                'Fungible': {
                    'amount': 'u128',
                    'ticker': '[u8; 12]',
                },
                'NonFungible': {
                    'ids': ['u64'],
                    'ticker': '[u8; 12]',
                },
            },
            'memo': (None, '[u8; 32]'),
        },
    ],
    'to': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
}
)
```

---------
### quit_portfolio_custody
When called by the custodian of `portfolio_id`,
allows returning the custody of the portfolio to the portfolio owner unilaterally.

\# Errors
* `UnauthorizedCustodian` if the caller is not the current custodian of `portfolio_id`.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| pid | `PortfolioId` | 

#### Python
```python
call = substrate.compose_call(
    'Portfolio', 'quit_portfolio_custody', {
    'pid': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
}
)
```

---------
### rename_portfolio
Renames a non-default portfolio.

\# Errors
* `PortfolioDoesNotExist` if `num` doesn&\#x27;t reference a valid portfolio.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| num | `PortfolioNumber` | 
| to_name | `PortfolioName` | 

#### Python
```python
call = substrate.compose_call(
    'Portfolio', 'rename_portfolio', {'num': 'u64', 'to_name': 'Bytes'}
)
```

---------
## Events

---------
### FungibleTokensMovedBetweenPortfolios
A token amount has been moved from one portfolio to another.

\# Parameters
* origin DID
* source portfolio
* destination portfolio
* asset ticker
* asset balance that was moved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `Ticker` | ```[u8; 12]```
| None | `Balance` | ```u128```
| None | `Option<PortfolioMemo>` | ```(None, '[u8; 32]')```

---------
### MovedBetweenPortfolios
A token amount has been moved from one portfolio to another.

\# Parameters
* origin DID
* source portfolio
* destination portfolio
* asset ticker
* asset balance that was moved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `Ticker` | ```[u8; 12]```
| None | `Balance` | ```u128```
| None | `Option<Memo>` | ```(None, '[u8; 32]')```

---------
### NFTsMovedBetweenPortfolios
NFTs have been moved from one portfolio to another.

\# Parameters
* origin DID
* source portfolio
* destination portfolio
* NFTs
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `NFTs` | ```{'ticker': '[u8; 12]', 'ids': ['u64']}```
| None | `Option<PortfolioMemo>` | ```(None, '[u8; 32]')```

---------
### PortfolioCreated
The portfolio has been successfully created.

\# Parameters
* origin DID
* portfolio number
* portfolio name
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PortfolioNumber` | ```u64```
| None | `PortfolioName` | ```Bytes```

---------
### PortfolioCustodianChanged
Custody of a portfolio has been given to a different identity

\# Parameters
* origin DID
* portfolio id
* portfolio custodian did
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PortfolioId` | ```{'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}```
| None | `IdentityId` | ```[u8; 32]```

---------
### PortfolioDeleted
The portfolio has been successfully removed.

\# Parameters
* origin DID
* portfolio number
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PortfolioNumber` | ```u64```

---------
### PortfolioRenamed
The portfolio identified with `num` has been renamed to `name`.

\# Parameters
* origin DID
* portfolio number
* portfolio name
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `PortfolioNumber` | ```u64```
| None | `PortfolioName` | ```Bytes```

---------
### UserPortfolios
All non-default portfolio numbers and names of a DID.

\# Parameters
* origin DID
* vector of number-name pairs
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Vec<(PortfolioNumber, PortfolioName)>` | ```[('u64', 'Bytes')]```

---------
## Storage functions

---------
### NameToNumber
 Inverse map of `Portfolios` used to ensure bijectivitiy,
 and uniqueness of names in `Portfolios`.

#### Python
```python
result = substrate.query(
    'Portfolio', 'NameToNumber', ['[u8; 32]', 'Bytes']
)
```

#### Return value
```python
'u64'
```
---------
### NextPortfolioNumber
 The next portfolio sequence number of an identity.

#### Python
```python
result = substrate.query(
    'Portfolio', 'NextPortfolioNumber', ['[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
### PortfolioAssetBalances
 The asset balances of portfolios.

#### Python
```python
result = substrate.query(
    'Portfolio', 'PortfolioAssetBalances', [
    {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    '[u8; 12]',
]
)
```

#### Return value
```python
'u128'
```
---------
### PortfolioAssetCount
 How many assets with non-zero balance this portfolio contains.

#### Python
```python
result = substrate.query(
    'Portfolio', 'PortfolioAssetCount', [
    {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
]
)
```

#### Return value
```python
'u64'
```
---------
### PortfolioCustodian
 The custodian of a particular portfolio. None implies that the identity owner is the custodian.

#### Python
```python
result = substrate.query(
    'Portfolio', 'PortfolioCustodian', [
    {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
]
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### PortfolioLockedAssets
 Amount of assets locked in a portfolio.
 These assets show up in portfolio balance but can not be transferred away.

#### Python
```python
result = substrate.query(
    'Portfolio', 'PortfolioLockedAssets', [
    {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    '[u8; 12]',
]
)
```

#### Return value
```python
'u128'
```
---------
### PortfolioLockedNFT
 All locked nft for a given portfolio.

#### Python
```python
result = substrate.query(
    'Portfolio', 'PortfolioLockedNFT', [
    {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    ('[u8; 12]', 'u64'),
]
)
```

#### Return value
```python
'bool'
```
---------
### PortfolioNFT
 The nft associated to the portfolio.

#### Python
```python
result = substrate.query(
    'Portfolio', 'PortfolioNFT', [
    {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    ('[u8; 12]', 'u64'),
]
)
```

#### Return value
```python
'bool'
```
---------
### Portfolios
 The set of existing portfolios with their names. If a certain pair of a DID and
 portfolio number maps to `None` then such a portfolio doesn&#x27;t exist. Conversely, if a
 pair maps to `Some(name)` then such a portfolio exists and is called `name`.

#### Python
```python
result = substrate.query(
    'Portfolio', 'Portfolios', ['[u8; 32]', 'u64']
)
```

#### Return value
```python
'Bytes'
```
---------
### PortfoliosInCustody
 Tracks all the portfolios in custody of a particular identity. Only used by the UIs.
 When `true` is stored as the value for a given `(did, pid)`, it means that `pid` is in custody of `did`.
 `false` values are never explicitly stored in the map, and are instead inferred by the absence of a key.

#### Python
```python
result = substrate.query(
    'Portfolio', 'PortfoliosInCustody', [
    '[u8; 32]',
    {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
]
)
```

#### Return value
```python
'bool'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'Portfolio', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
## Errors

---------
### DestinationIsSamePortfolio
The source and destination portfolios should be different.

---------
### DifferentIdentityPortfolios
The portfolios belong to different identities

---------
### InsufficientPortfolioBalance
Insufficient balance for a transaction.

---------
### InsufficientTokensLocked
Can not unlock more tokens than what are locked

---------
### InvalidTransferNFTIsLocked
Locked NFTs can not be moved between portfolios.

---------
### InvalidTransferNFTNotOwned
Only owned NFTs can be moved between portfolios.

---------
### NFTAlreadyLocked
The NFT is already locked.

---------
### NFTNotFoundInPortfolio
The NFT does not exist in the portfolio.

---------
### NFTNotLocked
The NFT has never been locked.

---------
### NoDuplicateAssetsAllowed
Duplicate asset among the items.

---------
### PortfolioDoesNotExist
The portfolio doesn&\#x27;t exist.

---------
### PortfolioNameAlreadyInUse
The portfolio couldn&\#x27;t be renamed because the chosen name is already in use.

---------
### PortfolioNotEmpty
The portfolio still has some asset balance left

---------
### SecondaryKeyNotAuthorizedForPortfolio
The secondary key is not authorized to access the portfolio(s).

---------
### UnauthorizedCustodian
The porfolio&\#x27;s custody is with someone other than the caller.

---------
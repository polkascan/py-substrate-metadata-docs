
# TransferAllowList

---------
## Calls

---------
### add_allowance_delay
Adds an account/currency delay
Calling on an account/currency with an existing delay will fail.
To update a delay the delay has to be set to future modifiable.
then an update delay extrinsic called
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'TransferAllowList', 'add_allowance_delay', {
    'currency_id': {
        'All': None,
        'Specific': {
            'Native': None,
            None: None,
            'AUSD': None,
            'ForeignAsset': 'u32',
            'LocalAsset': 'u32',
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
        },
    },
    'delay': 'u32',
}
)
```

---------
### add_transfer_allowance
Adds a transfer allowance for a sending Account/Currency.
Allowance either starts at the current block + the delay set for the
account, if a delay is present.
or block 0 if no delay is present.
Important! Account/Currency sets with an allowance set are
restricted to just the allowances added for the account -
to have unrestricted transfers allowed for the sending Account and
Currency, no allowances should be present.

Running this for an existing allowance generates a new allowance
based on the current delay, or lack thereof
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| receiver | `T::Location` | 

#### Python
```python
call = substrate.compose_call(
    'TransferAllowList', 'add_transfer_allowance', {
    'currency_id': {
        'All': None,
        'Specific': {
            'Native': None,
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
            'AUSD': None,
            'ForeignAsset': 'u32',
            'LocalAsset': 'u32',
            'Staking': (
                'BlockRewards',
            ),
        },
    },
    'receiver': {
        'Address': {
            'Centrifuge': '[u8; 32]',
            'EVM': ('u64', '[u8; 20]'),
        },
        'Local': 'AccountId',
        'XCM': 'scale_info::12',
    },
}
)
```

---------
### purge_allowance_delay
Removes an existing sending account/currency delay
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'TransferAllowList', 'purge_allowance_delay', {
    'currency_id': {
        'All': None,
        'Specific': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'LocalAsset': 'u32',
            'Native': None,
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
            'Staking': (
                'BlockRewards',
            ),
        },
    },
}
)
```

---------
### purge_transfer_allowance
Removes a transfer allowance for a sending account/currency and
receiving location Decrements or removes the sending
account/currency count.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| receiver | `T::Location` | 

#### Python
```python
call = substrate.compose_call(
    'TransferAllowList', 'purge_transfer_allowance', {
    'currency_id': {
        'All': None,
        'Specific': {
            'Native': None,
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
            'AUSD': None,
            'ForeignAsset': 'u32',
            'LocalAsset': 'u32',
            'Staking': (
                'BlockRewards',
            ),
        },
    },
    'receiver': {
        'Address': {
            'Centrifuge': '[u8; 32]',
            'EVM': ('u64', '[u8; 20]'),
        },
        'Local': 'AccountId',
        'XCM': 'scale_info::12',
    },
}
)
```

---------
### remove_transfer_allowance
Restricts a transfer allowance for a sending
account/currency/receiver location to:
- either the current block + delay if a delay is set
- or the current block if no delay is set
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| receiver | `T::Location` | 

#### Python
```python
call = substrate.compose_call(
    'TransferAllowList', 'remove_transfer_allowance', {
    'currency_id': {
        'All': None,
        'Specific': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'LocalAsset': 'u32',
            'Native': None,
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
        },
    },
    'receiver': {
        'Address': {
            'Centrifuge': '[u8; 32]',
            'EVM': ('u64', '[u8; 20]'),
        },
        'Local': 'AccountId',
        'XCM': 'scale_info::12',
    },
}
)
```

---------
### toggle_allowance_delay_once_future_modifiable
This allows the delay value to be modified after the current delay
has passed since the current block Or sets the delay value to be not
modifiable iff modifiable at has already passed
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'TransferAllowList', 'toggle_allowance_delay_once_future_modifiable', {
    'currency_id': {
        'All': None,
        'Specific': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'LocalAsset': 'u32',
            'Native': None,
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
        },
    },
}
)
```

---------
### update_allowance_delay
Updates an allowance delay, only callable if the delay has been set
to allow future modifications and the delay modifiable_at block has
been passed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `T::CurrencyId` | 
| delay | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'TransferAllowList', 'update_allowance_delay', {
    'currency_id': {
        'All': None,
        'Specific': {
            None: None,
            'AUSD': None,
            'ForeignAsset': 'u32',
            'LocalAsset': 'u32',
            'Native': None,
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
        },
    },
    'delay': 'u32',
}
)
```

---------
## Events

---------
### ToggleTransferAllowanceDelayFutureModifiable
Event for Allowance delay future modification allowed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender_account_id | `T::AccountId` | ```AccountId```
| currency_id | `T::CurrencyId` | ```{'All': None, 'Specific': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}}```
| modifiable_once_after | `Option<T::BlockNumber>` | ```(None, 'u32')```

---------
### TransferAllowanceCreated
Event for successful creation of a transfer allowance
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender_account_id | `T::AccountId` | ```AccountId```
| currency_id | `T::CurrencyId` | ```{'All': None, 'Specific': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}}```
| receiver | `T::Location` | ```{'Local': 'AccountId', 'XCM': 'scale_info::12', 'Address': {'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}}```
| allowed_at | `T::BlockNumber` | ```u32```
| blocked_at | `T::BlockNumber` | ```u32```

---------
### TransferAllowanceDelayAdd
Event for Allowance delay creation
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender_account_id | `T::AccountId` | ```AccountId```
| currency_id | `T::CurrencyId` | ```{'All': None, 'Specific': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}}```
| delay | `T::BlockNumber` | ```u32```

---------
### TransferAllowanceDelayPurge
Event for Allowance delay removal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender_account_id | `T::AccountId` | ```AccountId```
| currency_id | `T::CurrencyId` | ```{'All': None, 'Specific': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}}```

---------
### TransferAllowanceDelayUpdate
Event for Allowance delay update
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender_account_id | `T::AccountId` | ```AccountId```
| currency_id | `T::CurrencyId` | ```{'All': None, 'Specific': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}}```
| delay | `T::BlockNumber` | ```u32```

---------
### TransferAllowancePurged
Event for successful removal of transfer allowance perms
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender_account_id | `T::AccountId` | ```AccountId```
| currency_id | `T::CurrencyId` | ```{'All': None, 'Specific': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}}```
| receiver | `T::Location` | ```{'Local': 'AccountId', 'XCM': 'scale_info::12', 'Address': {'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}}```

---------
### TransferAllowanceRemoved
Event for successful removal of transfer allowance perms
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender_account_id | `T::AccountId` | ```AccountId```
| currency_id | `T::CurrencyId` | ```{'All': None, 'Specific': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',), 'LocalAsset': 'u32'}}```
| receiver | `T::Location` | ```{'Local': 'AccountId', 'XCM': 'scale_info::12', 'Address': {'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}}```
| allowed_at | `T::BlockNumber` | ```u32```
| blocked_at | `T::BlockNumber` | ```u32```

---------
## Storage functions

---------
### AccountCurrencyTransferAllowance
 Storage item for allowances specified for a sending account, currency
 type and receiving location

#### Python
```python
result = substrate.query(
    'TransferAllowList', 'AccountCurrencyTransferAllowance', [
    'AccountId',
    {
        'All': None,
        'Specific': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'LocalAsset': 'u32',
            'Native': None,
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
        },
    },
    {
        'Address': {
            'Centrifuge': '[u8; 32]',
            'EVM': ('u64', '[u8; 20]'),
        },
        'Local': 'AccountId',
        'XCM': 'scale_info::12',
    },
]
)
```

#### Return value
```python
{'allowed_at': 'u32', 'blocked_at': 'u32'}
```
---------
### AccountCurrencyTransferCountDelay
 Storage item containing number of allowances set, delay for sending
 account/currency, and block number delay is modifiable at. Contains an
 instance of AllowanceMetadata with allowance count as `u64`,
 current_delay as `Option&lt;T::BlockNumber&gt;`, and modifiable_at as
 `Option&lt;T::BlockNumber&gt;`. If a delay is set, but no allowances have been
 created, `allowance_count` will be set to `0`. A double map is used here
 as we need to know whether there is a restriction set for the account
 and currency in the case where there is no allowance for destination
 location. Using an StorageNMap would not allow us to look up whether
 there was a restriction for the sending account and currency, given
 that:
 - we&#x27;re checking whether there&#x27;s an allowance specified for the receiver
   location
   - we would only find whether a restriction was set for the account in
     this case if:
     - an allowance was specified for the receiving location, which would
       render blocked restrictions useless
 - we would otherwise need to store a vec of locations, which is
   problematic given that there isn&#x27;t a set limit on receivers
 If a transfer restriction is in place, then a second lookup is done on
 AccountCurrencyAllowances to see if there is an allowance for the
 receiver This allows us to keep storage map vals to known/bounded sizes.

#### Python
```python
result = substrate.query(
    'TransferAllowList', 'AccountCurrencyTransferCountDelay', [
    'AccountId',
    {
        'All': None,
        'Specific': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'LocalAsset': 'u32',
            'Native': None,
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
        },
    },
]
)
```

#### Return value
```python
{
    'allowance_count': 'u64',
    'current_delay': (None, 'u32'),
    'once_modifiable_after': (None, 'u32'),
}
```
---------
## Errors

---------
### AllowanceHasNotExpired
Attempted to clear active allowance

---------
### DelayUnmodifiable
Delay has not been set to modified, or delay at which modification
has been set has not been reached.

---------
### DuplicateAllowance
Attempted to create allowance for existing Sending Account,
Currency, and Receiver combination

---------
### DuplicateDelay
Delay already exists

---------
### NoAllowanceForDestination
Transfer from sending account and currency not allowed to
destination

---------
### NoAllowancesSet
An operation expecting one or more allowances for a sending
Account/Currency set, where none present

---------
### NoMatchingAllowance
No matching allowance for Location/Currency

---------
### NoMatchingDelay
No matching delay for the sending account and currency combination.
Cannot delete a non-existant entry

---------
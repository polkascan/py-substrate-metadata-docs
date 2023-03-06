
# CorporateAction

---------
## Calls

---------
### change_record_date
Changes the record date of the CA identified by `ca_id`.

\#\# Arguments
- `origin` which must be an external agent of `ca_id.ticker` with relevant permissions.
- `ca_id` of the CA to alter.
- `record_date`, if any, to calculate the impact of the CA.
   If provided, this results in a scheduled balance snapshot (&quot;checkpoint&quot;) at the date.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchCA` if `id` does not identify an existing CA.
- When `record_date.is_some()`, other errors due to checkpoint scheduling may occur.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 
| record_date | `Option<RecordDateSpec>` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateAction', 'change_record_date', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
    'record_date': (
        None,
        {
            'Existing': 'u64',
            'ExistingSchedule': 'u64',
            'Scheduled': 'u64',
        },
    ),
}
)
```

---------
### initiate_corporate_action
Initiates a CA for `ticker` of `kind` with `details` and other provided arguments.

\#\# Arguments
- `origin` which must be an external agent of `ticker` with relevant permissions.
- `ticker` that the CA is made for.
- `kind` of CA being initiated.
- `decl_date` of CA bring initialized.
- `record_date`, if any, to calculate the impact of this CA.
   If provided, this results in a scheduled balance snapshot (&quot;checkpoint&quot;) at the date.
- `details` of the CA in free-text form, up to a certain number of bytes in length.
- `targets`, if any, which this CA is relevant/irrelevant to.
   Overrides, if provided, the default at the asset level (`set_default_targets`).
- `default_withholding_tax`, if any, is the default withholding tax to use for this CA.
   Overrides, if provided, the default at the asset level (`set_default_withholding_tax`).
- `withholding_tax`, if any, provides per-DID withholding tax overrides.
   Overrides, if provided, the default at the asset level (`set_did_withholding_tax`).

\# Errors
- `DetailsTooLong` if `details.len()` goes beyond `max_details_length`.
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `CounterOverflow` in the unlikely event that so many CAs were created for this `ticker`,
  that integer overflow would have occured if instead allowed.
- `TooManyDidTaxes` if `withholding_tax.unwrap().len()` would go over the limit `MaxDidWhts`.
- `DuplicateDidTax` if a DID is included more than once in `wt`.
- `TooManyTargetIds` if `targets.unwrap().identities.len() &gt; T::MaxTargetIds::get()`.
- `DeclDateInFuture` if the declaration date is not in the past.
- When `record_date.is_some()`, other errors due to checkpoint scheduling may occur.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| kind | `CAKind` | 
| decl_date | `Moment` | 
| record_date | `Option<RecordDateSpec>` | 
| details | `CADetails` | 
| targets | `Option<TargetIdentities>` | 
| default_withholding_tax | `Option<Tax>` | 
| withholding_tax | `Option<Vec<(IdentityId, Tax)>>` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateAction', 'initiate_corporate_action', {
    'decl_date': 'u64',
    'default_withholding_tax': (
        None,
        'u32',
    ),
    'details': 'Bytes',
    'kind': (
        'PredictableBenefit',
        'UnpredictableBenefit',
        'IssuerNotice',
        'Reorganization',
        'Other',
    ),
    'record_date': (
        None,
        {
            'Existing': 'u64',
            'ExistingSchedule': 'u64',
            'Scheduled': 'u64',
        },
    ),
    'targets': (
        None,
        {
            'identities': ['[u8; 32]'],
            'treatment': (
                'Include',
                'Exclude',
            ),
        },
    ),
    'ticker': '[u8; 12]',
    'withholding_tax': (
        None,
        [('[u8; 32]', 'u32')],
    ),
}
)
```

---------
### initiate_corporate_action_and_distribute
Utility extrinsic to batch `initiate_corporate_action` and `distribute`
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_args | `InitiateCorporateActionArgs` | 
| portfolio | `Option<PortfolioNumber>` | 
| currency | `Ticker` | 
| per_share | `Balance` | 
| amount | `Balance` | 
| payment_at | `Moment` | 
| expires_at | `Option<Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateAction', 'initiate_corporate_action_and_distribute', {
    'amount': 'u128',
    'ca_args': {
        'decl_date': 'u64',
        'default_withholding_tax': (
            None,
            'u32',
        ),
        'details': 'Bytes',
        'kind': (
            'PredictableBenefit',
            'UnpredictableBenefit',
            'IssuerNotice',
            'Reorganization',
            'Other',
        ),
        'record_date': (
            None,
            {
                'Existing': 'u64',
                'ExistingSchedule': 'u64',
                'Scheduled': 'u64',
            },
        ),
        'targets': (
            None,
            {
                'identities': [
                    '[u8; 32]',
                ],
                'treatment': (
                    'Include',
                    'Exclude',
                ),
            },
        ),
        'ticker': '[u8; 12]',
        'withholding_tax': (
            None,
            [('[u8; 32]', 'u32')],
        ),
    },
    'currency': '[u8; 12]',
    'expires_at': (None, 'u64'),
    'payment_at': 'u64',
    'per_share': 'u128',
    'portfolio': (None, 'u64'),
}
)
```

---------
### link_ca_doc
Link the given CA `id` to the given `docs`.
Any previous links for the CA are removed in favor of `docs`.

The workflow here is to add the documents and initiating the CA in any order desired.
Once both exist, they can now be linked together.

\#\# Arguments
- `origin` which must be an external agent of `id.ticker` with relevant permissions.
- `id` of the CA to associate with `docs`.
- `docs` to associate with the CA with `id`.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchCA` if `id` does not identify an existing CA.
- `NoSuchDoc` if any of `docs` does not identify an existing document.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `CAId` | 
| docs | `Vec<DocumentId>` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateAction', 'link_ca_doc', {
    'docs': ['u32'],
    'id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
}
)
```

---------
### remove_ca
Removes the CA identified by `ca_id`.

Associated data, such as document links, ballots,
and capital distributions are also removed.

Any schedule associated with the record date will see
`strong_ref_count(schedule_id)` decremented.

\#\# Arguments
- `origin` which must be an external agent of `ca_id.ticker` with relevant permissions.
- `ca_id` of the CA to remove.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchCA` if `id` does not identify an existing CA.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateAction', 'remove_ca', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
}
)
```

---------
### set_default_targets
Set the default CA `TargetIdentities` to `targets`.

\#\# Arguments
- `origin` which must be an external agent of `ticker` with relevant permissions.
- `ticker` for which the default identities are changing.
- `targets` the default target identities for a CA.

\#\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `TooManyTargetIds` if `targets.identities.len() &gt; T::MaxTargetIds::get()`.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| targets | `TargetIdentities` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateAction', 'set_default_targets', {
    'targets': {
        'identities': ['[u8; 32]'],
        'treatment': (
            'Include',
            'Exclude',
        ),
    },
    'ticker': '[u8; 12]',
}
)
```

---------
### set_default_withholding_tax
Set the default withholding tax for all DIDs and CAs relevant to this `ticker`.

\#\# Arguments
- `origin` which must be an external agent of `ticker` with relevant permissions.
- `ticker` that the withholding tax will apply to.
- `tax` that should be withheld when distributing dividends, etc.

\#\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| tax | `Tax` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateAction', 'set_default_withholding_tax', {'tax': 'u32', 'ticker': '[u8; 12]'}
)
```

---------
### set_did_withholding_tax
Set the withholding tax of `ticker` for `taxed_did` to `tax`.
If `Some(tax)`, this overrides the default withholding tax of `ticker` to `tax` for `taxed_did`.
Otherwise, if `None`, the default withholding tax will be used.

\#\# Arguments
- `origin` which must be an external agent of `ticker` with relevant permissions.
- `ticker` that the withholding tax will apply to.
- `taxed_did` that will have its withholding tax updated.
- `tax` that should be withheld when distributing dividends, etc.

\#\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `TooManyDidTaxes` if `Some(tax)` and adding the override would go over the limit `MaxDidWhts`.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| ticker | `Ticker` | 
| taxed_did | `IdentityId` | 
| tax | `Option<Tax>` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateAction', 'set_did_withholding_tax', {
    'tax': (None, 'u32'),
    'taxed_did': '[u8; 32]',
    'ticker': '[u8; 12]',
}
)
```

---------
### set_max_details_length
Set the max `length` of `details` in terms of bytes.
May only be called via a PIP.
#### Attributes
| Name | Type |
| -------- | -------- | 
| length | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'CorporateAction', 'set_max_details_length', {'length': 'u32'}
)
```

---------
## Events

---------
### CAATransferred
A new DID was made the CAA.
(New CAA DID, Ticker, New CAA DID).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```

---------
### CAInitiated
A CA was initiated.
(Agent DID, CA id, the CA, the CA details)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `CorporateAction` | ```{'kind': ('PredictableBenefit', 'UnpredictableBenefit', 'IssuerNotice', 'Reorganization', 'Other'), 'decl_date': 'u64', 'record_date': (None, {'date': 'u64', 'checkpoint': {'Scheduled': ('u64', 'u64'), 'Existing': 'u64'}}), 'targets': {'identities': ['[u8; 32]'], 'treatment': ('Include', 'Exclude')}, 'default_withholding_tax': 'u32', 'withholding_tax': [('[u8; 32]', 'u32')]}```
| None | `CADetails` | ```Bytes```

---------
### CALinkedToDoc
A CA was linked to a set of docs.
(Agent DID, CA Id, List of doc identifiers)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `Vec<DocumentId>` | ```['u32']```

---------
### CARemoved
A CA was removed.
(Agent DID, CA Id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```

---------
### DefaultTargetIdentitiesChanged
The set of default `TargetIdentities` for a ticker changed.
(Agent DID, Ticker, New TargetIdentities)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `TargetIdentities` | ```{'identities': ['[u8; 32]'], 'treatment': ('Include', 'Exclude')}```

---------
### DefaultWithholdingTaxChanged
The default withholding tax for a ticker changed.
(Agent DID, Ticker, New Tax).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `Tax` | ```u32```

---------
### DidWithholdingTaxChanged
The withholding tax specific to a DID for a ticker changed.
(Agent DID, Ticker, Taxed DID, New Tax).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```
| None | `IdentityId` | ```[u8; 32]```
| None | `Option<Tax>` | ```(None, 'u32')```

---------
### MaxDetailsLengthChanged
The maximum length of `details` in bytes was changed.
(GC DID, new length)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `u32` | ```u32```

---------
### RecordDateChanged
A CA&\#x27;s record date changed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `CorporateAction` | ```{'kind': ('PredictableBenefit', 'UnpredictableBenefit', 'IssuerNotice', 'Reorganization', 'Other'), 'decl_date': 'u64', 'record_date': (None, {'date': 'u64', 'checkpoint': {'Scheduled': ('u64', 'u64'), 'Existing': 'u64'}}), 'targets': {'identities': ['[u8; 32]'], 'treatment': ('Include', 'Exclude')}, 'default_withholding_tax': 'u32', 'withholding_tax': [('[u8; 32]', 'u32')]}```

---------
## Storage functions

---------
### CADocLink
 Associations from CAs to `Document`s via their IDs.
 (CAId =&gt; [DocumentId])

 The `CorporateActions` map stores `Ticker =&gt; LocalId =&gt; The CA`,
 so we can infer `Ticker =&gt; CAId`. Therefore, we don&#x27;t need a double map.

#### Python
```python
result = substrate.query(
    'CorporateAction', 'CADocLink', [
    {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
]
)
```

#### Return value
```python
['u32']
```
---------
### CAIdSequence
 The next per-`Ticker` CA ID in the sequence.
 The full ID is defined as a combination of `Ticker` and a number in this sequence.

#### Python
```python
result = substrate.query(
    'CorporateAction', 'CAIdSequence', ['[u8; 12]']
)
```

#### Return value
```python
'u32'
```
---------
### CorporateActions
 All recorded CAs thus far.
 Only generic information is stored here.
 Specific `CAKind`s, e.g., benefits and corporate ballots, may use additional on-chain storage.

 (ticker =&gt; local ID =&gt; the corporate action)

#### Python
```python
result = substrate.query(
    'CorporateAction', 'CorporateActions', ['[u8; 12]', 'u32']
)
```

#### Return value
```python
{
    'decl_date': 'u64',
    'default_withholding_tax': 'u32',
    'kind': (
        'PredictableBenefit',
        'UnpredictableBenefit',
        'IssuerNotice',
        'Reorganization',
        'Other',
    ),
    'record_date': (
        None,
        {'checkpoint': {'Existing': 'u64', 'Scheduled': ('u64', 'u64')}, 'date': 'u64'},
    ),
    'targets': {
        'identities': ['[u8; 32]'],
        'treatment': ('Include', 'Exclude'),
    },
    'withholding_tax': [('[u8; 32]', 'u32')],
}
```
---------
### DefaultTargetIdentities
 The identities targeted by default for CAs for this ticker,
 either to be excluded or included.

 (ticker =&gt; target identities)

#### Python
```python
result = substrate.query(
    'CorporateAction', 'DefaultTargetIdentities', ['[u8; 12]']
)
```

#### Return value
```python
{'identities': ['[u8; 32]'], 'treatment': ('Include', 'Exclude')}
```
---------
### DefaultWithholdingTax
 The default amount of tax to withhold (&quot;withholding tax&quot;, WT) for this ticker when distributing dividends.

 To understand withholding tax, e.g., let&#x27;s assume that you hold ACME shares.
 ACME now decides to distribute 100 SEK to Alice.
 Alice lives in Sweden, so Skatteverket (the Swedish tax authority) wants 30% of that.
 Then those 100 * 30% are withheld from Alice, and ACME will send them to Skatteverket.

 (ticker =&gt; % to withhold)

#### Python
```python
result = substrate.query(
    'CorporateAction', 'DefaultWithholdingTax', ['[u8; 12]']
)
```

#### Return value
```python
'u32'
```
---------
### Details
 Associates details in free-form text with a CA by its ID.
 (CAId =&gt; CADetails)

#### Python
```python
result = substrate.query(
    'CorporateAction', 'Details', [
    {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
]
)
```

#### Return value
```python
'Bytes'
```
---------
### DidWithholdingTax
 The amount of tax to withhold (&quot;withholding tax&quot;, WT) for a certain ticker x DID.
 If an entry exists for a certain DID, it overrides the default in `DefaultWithholdingTax`.

 (ticker =&gt; [(did, % to withhold)]

#### Python
```python
result = substrate.query(
    'CorporateAction', 'DidWithholdingTax', ['[u8; 12]']
)
```

#### Return value
```python
[('[u8; 32]', 'u32')]
```
---------
### MaxDetailsLength
 Determines the maximum number of bytes that the free-form `details` of a CA can store.

 Note that this is not the number of `char`s or the number of [graphemes].
 While this may be unnatural in terms of human understanding of a text&#x27;s length,
 it more closely reflects actual storage costs (`&#x27;a&#x27;` is cheaper to store than an emoji).

 [graphemes]: https://en.wikipedia.org/wiki/Grapheme

#### Python
```python
result = substrate.query(
    'CorporateAction', 'MaxDetailsLength', []
)
```

#### Return value
```python
'u32'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'CorporateAction', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
## Constants

---------
### MaxDidWhts
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('CorporateAction', 'MaxDidWhts')
```
---------
### MaxTargetIds
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('CorporateAction', 'MaxTargetIds')
```
---------
## Errors

---------
### AuthNotCAATransfer
The authorization type is not to transfer the CAA to another DID.

---------
### DeclDateAfterRecordDate
A CA&\#x27;s declaration date was strictly after its record date.

---------
### DeclDateInFuture
A CA&\#x27;s declaration date occurs in the future.

---------
### DetailsTooLong
The `details` of a CA exceeded the max allowed length.

---------
### DuplicateDidTax
A withholding tax override for a given DID was specified more than once.
The chain refused to make a choice, and hence there was an error.

---------
### NoRecordDate
The CA did not have a record date.

---------
### NoSuchCA
A CA with the given `CAId` did not exist.

---------
### NoSuchCheckpointId
On CA creation, a checkpoint ID was provided which doesn&\#x27;t exist.

---------
### NotTargetedByCA
CA does not target the DID.

---------
### RecordDateAfterStart
A CA&\#x27;s record date was strictly after the &quot;start&quot; time,
where &quot;start&quot; is context dependent.
For example, it could be the start of a ballot, or the start-of-payment in capital distribution.

---------
### TooManyDidTaxes
Too many withholding tax overrides were specified.

---------
### TooManyTargetIds
Too many identities in `TargetIdentities` were specified.

---------
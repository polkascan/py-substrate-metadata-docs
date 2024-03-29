
# Forum

---------
## Calls

---------
### add_post
Add post

&lt;weight&gt;

\#\# Weight
`O (W + V)` where:
- `W` is the category depth,
- `V` is the size of the text in kilobytes
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| forum_user_id | `ForumUserId<T>` | 
| category_id | `T::CategoryId` | 
| thread_id | `T::ThreadId` | 
| text | `Vec<u8>` | 
| editable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'add_post', {
    'category_id': 'u64',
    'editable': 'bool',
    'forum_user_id': 'u64',
    'text': 'Bytes',
    'thread_id': 'u64',
}
)
```

---------
### create_category
Add a new category.

&lt;weight&gt;

\#\# Weight
`O (W + V + X)` where:
- `W` is the category depth
- `V` is the size of the category title in kilobytes.
- `X` is the size of the category description in kilobytes.
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| parent_category_id | `Option<T::CategoryId>` | 
| title | `Vec<u8>` | 
| description | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'create_category', {
    'description': 'Bytes',
    'parent_category_id': (
        None,
        'u64',
    ),
    'title': 'Bytes',
}
)
```

---------
### create_thread
Create new thread in category

&lt;weight&gt;

\#\# Weight
`O (W + V + X)` where:
- `W` is the category depth
- `V` is the size of the thread title in kilobytes.
- `X` is the size of the thread text in kilobytes.
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| forum_user_id | `ForumUserId<T>` | 
| category_id | `T::CategoryId` | 
| metadata | `Vec<u8>` | 
| text | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'create_thread', {
    'category_id': 'u64',
    'forum_user_id': 'u64',
    'metadata': 'Bytes',
    'text': 'Bytes',
}
)
```

---------
### delete_category
Delete category

&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is the category depth
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `PrivilegedActor<T>` | 
| category_id | `T::CategoryId` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'delete_category', {
    'actor': {
        'Lead': None,
        'Moderator': 'u64',
    },
    'category_id': 'u64',
}
)
```

---------
### delete_posts
Delete post from storage.
You need to provide a vector of posts to delete in the form
(T::CategoryId, T::ThreadId, T::PostId, bool)
where the last bool is whether you want to hide it apart from deleting it

\#\# Weight
`O (W + V + P)` where:
- `W` is the category depth,
- `V` is the size of the rationale in kilobytes
- `P` is the number of posts to delete
- DB:
   - O(W + P)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| forum_user_id | `ForumUserId<T>` | 
| posts | `BTreeMap<ExtendedPostId<T>, bool>` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'delete_posts', {
    'forum_user_id': 'u64',
    'posts': 'scale_info::87',
    'rationale': 'Bytes',
}
)
```

---------
### delete_thread
Delete thread

&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is the category depth
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| forum_user_id | `ForumUserId<T>` | 
| category_id | `T::CategoryId` | 
| thread_id | `T::ThreadId` | 
| hide | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'delete_thread', {
    'category_id': 'u64',
    'forum_user_id': 'u64',
    'hide': 'bool',
    'thread_id': 'u64',
}
)
```

---------
### edit_post_text
Edit post text

&lt;weight&gt;

\#\# Weight
`O (W + V)` where:
- `W` is the category depth,
- `V` is the size of the new text in kilobytes
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| forum_user_id | `ForumUserId<T>` | 
| category_id | `T::CategoryId` | 
| thread_id | `T::ThreadId` | 
| post_id | `T::PostId` | 
| new_text | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'edit_post_text', {
    'category_id': 'u64',
    'forum_user_id': 'u64',
    'new_text': 'Bytes',
    'post_id': 'u64',
    'thread_id': 'u64',
}
)
```

---------
### edit_thread_metadata
Edit thread metadata

&lt;weight&gt;

\#\# Weight
`O (W + V)` where:
- `W` is the category depth
- `V` is the size of the thread metadata in kilobytes.
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| forum_user_id | `ForumUserId<T>` | 
| category_id | `T::CategoryId` | 
| thread_id | `T::ThreadId` | 
| new_metadata | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'edit_thread_metadata', {
    'category_id': 'u64',
    'forum_user_id': 'u64',
    'new_metadata': 'Bytes',
    'thread_id': 'u64',
}
)
```

---------
### moderate_post
Moderate post

&lt;weight&gt;

\#\# Weight
`O (W + V)` where:
- `W` is the category depth,
- `V` is the size of the rationale in kilobytes
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `PrivilegedActor<T>` | 
| category_id | `T::CategoryId` | 
| thread_id | `T::ThreadId` | 
| post_id | `T::PostId` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'moderate_post', {
    'actor': {
        'Lead': None,
        'Moderator': 'u64',
    },
    'category_id': 'u64',
    'post_id': 'u64',
    'rationale': 'Bytes',
    'thread_id': 'u64',
}
)
```

---------
### moderate_thread
Moderate thread

&lt;weight&gt;

\#\# Weight
`O (W + V + X)` where:
- `W` is the category depth,
- `V` is the number of thread posts,
- `X` is the size of the rationale in kilobytes
- DB:
   - O(W + V)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `PrivilegedActor<T>` | 
| category_id | `T::CategoryId` | 
| thread_id | `T::ThreadId` | 
| rationale | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'moderate_thread', {
    'actor': {
        'Lead': None,
        'Moderator': 'u64',
    },
    'category_id': 'u64',
    'rationale': 'Bytes',
    'thread_id': 'u64',
}
)
```

---------
### move_thread_to_category
Move thread to another category

&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is the category depth
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `PrivilegedActor<T>` | 
| category_id | `T::CategoryId` | 
| thread_id | `T::ThreadId` | 
| new_category_id | `T::CategoryId` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'move_thread_to_category', {
    'actor': {
        'Lead': None,
        'Moderator': 'u64',
    },
    'category_id': 'u64',
    'new_category_id': 'u64',
    'thread_id': 'u64',
}
)
```

---------
### set_stickied_threads
Set stickied threads for category

&lt;weight&gt;

\#\# Weight
`O (W + V)` where:
- `W` is the category depth,
- `V` is the length of the stickied_ids
- DB:
   - O(W + V)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `PrivilegedActor<T>` | 
| category_id | `T::CategoryId` | 
| stickied_ids | `BTreeSet<T::ThreadId>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'set_stickied_threads', {
    'actor': {
        'Lead': None,
        'Moderator': 'u64',
    },
    'category_id': 'u64',
    'stickied_ids': 'scale_info::90',
}
)
```

---------
### update_category_archival_status
Update archival status

&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is the category depth
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `PrivilegedActor<T>` | 
| category_id | `T::CategoryId` | 
| new_archival_status | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'update_category_archival_status', {
    'actor': {
        'Lead': None,
        'Moderator': 'u64',
    },
    'category_id': 'u64',
    'new_archival_status': 'bool',
}
)
```

---------
### update_category_description
Update category description

&lt;weight&gt;

\#\# Weight
`O (W)` where:
- `W` is the category depth
- `V` is the size of the category description in kilobytes.
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `PrivilegedActor<T>` | 
| category_id | `T::CategoryId` | 
| description | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'update_category_description', {
    'actor': {
        'Lead': None,
        'Moderator': 'u64',
    },
    'category_id': 'u64',
    'description': 'Bytes',
}
)
```

---------
### update_category_membership_of_moderator
Enable a moderator can moderate a category and its sub categories.

&lt;weight&gt;

\#\# Weight
`O (1)`
- DB:
   - O(1) doesn&\#x27;t depend on the state or parameters
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| moderator_id | `ModeratorId<T>` | 
| category_id | `T::CategoryId` | 
| new_value | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'update_category_membership_of_moderator', {
    'category_id': 'u64',
    'moderator_id': 'u64',
    'new_value': 'bool',
}
)
```

---------
### update_category_title
Update category title

&lt;weight&gt;

\#\# Weight
`O (W + V)` where:
- `W` is the category depth
- `V` is the size of the category title in kilobytes.
- DB:
   - O(W)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| actor | `PrivilegedActor<T>` | 
| category_id | `T::CategoryId` | 
| title | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Forum', 'update_category_title', {
    'actor': {
        'Lead': None,
        'Moderator': 'u64',
    },
    'category_id': 'u64',
    'title': 'Bytes',
}
)
```

---------
## Events

---------
### CategoryArchivalStatusUpdated
An arhical status of category with given id was updated.
The second argument reflects the new archival status of the category.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CategoryId` | ```u64```
| None | `bool` | ```bool```
| None | `PrivilegedActor` | ```{'Lead': None, 'Moderator': 'u64'}```

---------
### CategoryCreated
A category was introduced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CategoryId` | ```u64```
| None | `Option<CategoryId>` | ```(None, 'u64')```
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```

---------
### CategoryDeleted
A category was deleted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CategoryId` | ```u64```
| None | `PrivilegedActor` | ```{'Lead': None, 'Moderator': 'u64'}```

---------
### CategoryDescriptionUpdated
A discription of category with given id was updated.
The second argument reflects the new description hash of the category.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CategoryId` | ```u64```
| None | `Hash` | ```scale_info::11```
| None | `PrivilegedActor` | ```{'Lead': None, 'Moderator': 'u64'}```

---------
### CategoryMembershipOfModeratorUpdated
An moderator ability to moderate a category and its subcategories updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ModeratorId` | ```u64```
| None | `CategoryId` | ```u64```
| None | `bool` | ```bool```

---------
### CategoryStickyThreadUpdate
Sticky thread updated for category
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CategoryId` | ```u64```
| None | `BTreeSet<ThreadId>` | ```scale_info::90```
| None | `PrivilegedActor` | ```{'Lead': None, 'Moderator': 'u64'}```

---------
### CategoryTitleUpdated
A title of category with given id was updated.
The second argument reflects the new title hash of the category.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CategoryId` | ```u64```
| None | `Hash` | ```scale_info::11```
| None | `PrivilegedActor` | ```{'Lead': None, 'Moderator': 'u64'}```

---------
### PostAdded
Post with given id was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PostId` | ```u64```
| None | `ForumUserId` | ```u64```
| None | `CategoryId` | ```u64```
| None | `ThreadId` | ```u64```
| None | `Vec<u8>` | ```Bytes```
| None | `bool` | ```bool```

---------
### PostDeleted
Post with givne id was deleted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```
| None | `ForumUserId` | ```u64```
| None | `BTreeMap<ExtendedPostId, bool>` | ```scale_info::87```

---------
### PostModerated
Post with givne id was moderated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PostId` | ```u64```
| None | `Vec<u8>` | ```Bytes```
| None | `PrivilegedActor` | ```{'Lead': None, 'Moderator': 'u64'}```
| None | `CategoryId` | ```u64```
| None | `ThreadId` | ```u64```

---------
### PostTextUpdated
Post with given id had its text updated.
The second argument reflects the number of total edits when the text update occurs.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `PostId` | ```u64```
| None | `ForumUserId` | ```u64```
| None | `CategoryId` | ```u64```
| None | `ThreadId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### ThreadCreated
A thread with given id was created.
A third argument reflects the initial post id of the thread.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CategoryId` | ```u64```
| None | `ThreadId` | ```u64```
| None | `PostId` | ```u64```
| None | `ForumUserId` | ```u64```
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```

---------
### ThreadDeleted
A thread was deleted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ThreadId` | ```u64```
| None | `ForumUserId` | ```u64```
| None | `CategoryId` | ```u64```
| None | `bool` | ```bool```

---------
### ThreadMetadataUpdated
A thread metadata given id was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ThreadId` | ```u64```
| None | `ForumUserId` | ```u64```
| None | `CategoryId` | ```u64```
| None | `Vec<u8>` | ```Bytes```

---------
### ThreadModerated
A thread with given id was moderated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ThreadId` | ```u64```
| None | `Vec<u8>` | ```Bytes```
| None | `PrivilegedActor` | ```{'Lead': None, 'Moderator': 'u64'}```
| None | `CategoryId` | ```u64```

---------
### ThreadMoved
A thread was moved to new category
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ThreadId` | ```u64```
| None | `CategoryId` | ```u64```
| None | `PrivilegedActor` | ```{'Lead': None, 'Moderator': 'u64'}```
| None | `CategoryId` | ```u64```

---------
### ThreadUpdated
A thread with given id was updated.
The second argument reflects the new archival status of the thread.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ThreadId` | ```u64```
| None | `bool` | ```bool```
| None | `PrivilegedActor` | ```{'Lead': None, 'Moderator': 'u64'}```
| None | `CategoryId` | ```u64```

---------
## Storage functions

---------
### CategoryById
 Map category identifier to corresponding category.

#### Python
```python
result = substrate.query(
    'Forum', 'CategoryById', ['u64']
)
```

#### Return value
```python
{
    'archived': 'bool',
    'description_hash': 'scale_info::11',
    'num_direct_moderators': 'u32',
    'num_direct_subcategories': 'u32',
    'num_direct_threads': 'u32',
    'parent_category_id': (None, 'u64'),
    'sticky_thread_ids': 'scale_info::90',
    'title_hash': 'scale_info::11',
}
```
---------
### CategoryByModerator
 Moderator set for each Category

#### Python
```python
result = substrate.query(
    'Forum', 'CategoryByModerator', ['u64', 'u64']
)
```

#### Return value
```python
()
```
---------
### CategoryCounter
 Counter for all existing categories.

#### Python
```python
result = substrate.query(
    'Forum', 'CategoryCounter', []
)
```

#### Return value
```python
'u64'
```
---------
### NextCategoryId
 Category identifier value to be used for the next Category created.

#### Python
```python
result = substrate.query(
    'Forum', 'NextCategoryId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextPostId
 Post identifier value to be used for for next post created.

#### Python
```python
result = substrate.query(
    'Forum', 'NextPostId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextThreadId
 Thread identifier value to be used for next Thread in threadById.

#### Python
```python
result = substrate.query(
    'Forum', 'NextThreadId', []
)
```

#### Return value
```python
'u64'
```
---------
### PostById
 Map post identifier to corresponding post.

#### Python
```python
result = substrate.query(
    'Forum', 'PostById', ['u64', 'u64']
)
```

#### Return value
```python
{
    'author_id': 'u64',
    'cleanup_pay_off': {
        'amount': 'u128',
        'repayment_restricted_to': (None, 'AccountId'),
    },
    'last_edited': 'u32',
    'text_hash': 'scale_info::11',
    'thread_id': 'u64',
}
```
---------
### ThreadById
 Map thread identifier to corresponding thread.

#### Python
```python
result = substrate.query(
    'Forum', 'ThreadById', ['u64', 'u64']
)
```

#### Return value
```python
{
    'author_id': 'u64',
    'category_id': 'u64',
    'cleanup_pay_off': {
        'amount': 'u128',
        'repayment_restricted_to': (None, 'AccountId'),
    },
    'number_of_editable_posts': 'u64',
}
```
---------
## Constants

---------
### MaxDirectSubcategoriesInCategory
 MaxDirectSubcategoriesInCategory
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Forum', 'MaxDirectSubcategoriesInCategory')
```
---------
### MaxTotalCategories
 MaxTotalCategories
#### Value
```python
40
```
#### Python
```python
constant = substrate.get_constant('Forum', 'MaxTotalCategories')
```
---------
### PostDeposit
 Exports const
 Deposit needed to create a post
#### Value
```python
1928887055
```
#### Python
```python
constant = substrate.get_constant('Forum', 'PostDeposit')
```
---------
### ThreadDeposit
 Deposit needed to create a thread
#### Value
```python
1864121502
```
#### Python
```python
constant = substrate.get_constant('Forum', 'ThreadDeposit')
```
---------
## Errors

---------
### AccountDoesNotMatchPostAuthor
Account does not match post author.

---------
### AccountDoesNotMatchThreadAuthor
Thread not authored by the given user.

---------
### AncestorCategoryImmutable
Ancestor category immutable, i.e. deleted or archived

---------
### ArithmeticError
Unexpected arithmetic error (overflow / underflow)

---------
### CannotDeleteThreadWithOutstandingPosts
A thread with outstanding posts cannot be removed

---------
### CategoryDoesNotExist
Category does not exist.

---------
### CategoryModeratorDoesNotExist
Provided moderator is not given category moderator

---------
### CategoryNotBeingUpdated
Category not being updated.

---------
### CategoryNotEmptyCategories
Category still contains some subcategories.

---------
### CategoryNotEmptyThreads
Category still contains some threads.

---------
### ForumUserIdNotMatchAccount
Forum user id not match its account.

---------
### InsufficientBalanceForPost
Not enough balance to post

---------
### InsufficientBalanceForThreadCreation
Not enough balance to create thread

---------
### MapSizeLimit
Maximum size of storage map exceeded

---------
### MaxNumberOfStickiedThreadsExceeded
Maximum number of stickied threads per category exceeded

---------
### MaxValidCategoryDepthExceeded
Maximum valid category depth exceeded.

---------
### ModeratorCantDeleteCategory
No permissions to delete category.

---------
### ModeratorCantUpdateCategory
No permissions to update category.

---------
### ModeratorIdNotMatchAccount
Moderator id not match its account.

---------
### ModeratorModerateDestinationCategory
Moderator can&\#x27;t moderate destination category.

---------
### ModeratorModerateOriginCategory
Moderator can&\#x27;t moderate category containing thread.

---------
### OriginNotForumLead
Origin doesn&\#x27;t correspond to any lead account

---------
### PathLengthShouldBeGreaterThanZero
Category path len should be greater than zero

---------
### PostDoesNotExist
Post does not exist.

---------
### ThreadDoesNotExist
Thread does not exist

---------
### ThreadMoveInvalid
Origin is the same as the destination.

---------
### ThreadNotBeingUpdated
Thread not being updated.

---------
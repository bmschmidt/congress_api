# Download the Data #

Simply run:

```python
python get_and_unzip_data.py
```

This will download all the data, make directories, unzip the data and remove the zip files when it is all done. It uses the multiprocessing module to do everything in parallel, so it is pretty quick.

# About the Data #

## Bill IDs ##

Bill IDs are a combination of the type of bill, the bill number, and the session of Congress a bill was introduced in. They are of the format:

[type][number]-[session]

For example, H.R. 4173 from the 111th Congress would be "hr4173-111".

## Guaranteed Fields ##

The only fields you can assume are present are:

* bill_id
* bill_type
* number
* code
* session
* chamber
* abbreviated

## Abbreviated bills ##

Since information on new votes is published much more quickly than information on new bills, it's possible that for bills quickly introduced and voted upon, we may encounter a vote on a bill whose full information is not available.

In this case, as a convenience, we will create an "abbreviated" bill document with as much information as can be gleaned from the vote, and will set the "abbreviated" field to true. If "abbreviated" is false, then you can expect much more information to be present, such as sponsorship, timeline information, and Congressional actions.

In practice, Senate vote information include the official and short titles of the bill being voted upon, so for some abbreviated bills, the "official_title" and "short_title" fields may also be present.

## Text Search Fields ##
If the "search" parameter is passed to the API, a case-insensitive pattern match of the given string is applied to the following fields:

* short_title
* official_title
* popular_title
* keywords
* summary

## Types of Bills ##

* **hr**: House bills ("H.R.")
* **hres**: House resolutions ("H.Res")
* **hjres**: House joint resolutions ("H.J.Res")
* **hcres**: House concurrent resolutions ("H.C.Res" or "H.Con.Res")
* **s**: Senate bills ("S.")
* **sres**: Senate resolutions ("S.Res")
* **sjres**: Senate joint resolutions ("S.J.Res")
* **scres**: Senate concurrent resolutions ("S.C.Res" or "S.Con.Res")

## Fields ##

* **bill_id**: Unique ID. (See above list for how to construct the ID.)
* **bill_type**: Type of bill. (See above list for what the types mean.)
* **number**: The number of the bill. (For example, HR 4173's number is 4173.)
* **session**: The session of Congress this bill was introduced in.
* **chamber**: The chamber of Congress this bill originated in.
* **short_title**: An officially designated "short title" of a bill. Not all bills have this. (e.g. "Truth in Fur Labeling Act of 2010")
* **official_title**: The official title of a bill. Almost all bills have one of these.
* **popular_title**: An officially designated "popular title" (i.e. "Health care reform bill") for a bill. Very uncommon (there were 4 in the 111th Congress).
* **titles**: An array of objects containing all short, official, and popular titles to the bill, and when the titles were made.
* **summary**: An official summary of the bill, if the Congressional Research Service has written one.
* **sponsor_id**: Bioguide ID for the legislator sponsoring the bill.
* **sponsor**: Object containing basic data about the legislator sponsoring the bill.
* **cosponsor_ids**: An array of bioguide IDs for the legislators cosponsoring the bill.
* **cosponsors**: An array of objects containing basic data about the legislators cosponsoring the bill.
* **committee_ids**: An array of committee IDs for committees which have some relation to this bill.
* **committees**: An array of objects, keyed by committee ID, which give basic details about each committee that has some relation to this bill, and what kind of role the committee has in regards to it.
* **amendment_ids**: An array of IDs of introduced amendments to this bill, that refer to documents in the amendments collection.
* **amendments**: An array of basic information about introduced amendments to this bill.
* **amendments_count**: The number of amendments to this bill that have been introduced.
* **keywords**: An array of official keywords and phrases that categorize the bill.
* **actions**: An array of all actions upon a bill, in sequence. Fields described below.
* **last_action**: The last action to happen to a bill.
* **last_action_at**: (timestamp) The time of the last action to happen to a bill.
* **passage_votes**: An array of objects containing details on passage votes taken on the bill. Fields described below.
* **passage_votes_count**: The number of passage votes taken on this bill.
* **last_passage_vote_at**: (timestamp) Last time a passage vote was taken on a bill.
* **related_bills**: A hash where the keys are the type of relation, and the values are arrays of bill IDs.
* **introduced_at**: (timestamp) When a bill was introduced. **Default order for this collection.**
* **senate_passage_result**: The result of a Senate passage vote on the bill, if one was taken. "pass", "fail", or null.
* **senate_passage_result_at**: (timestamp) When the Senate last voted on passage of the bill, if it did.
* **house_passage_result**: The result of a House passage vote on the bill, if one was taken. "pass", "fail", or null.
* **house_passage_result_at**: (timestamp) When the House last voted on passage of the bill, if it did.
* **awaiting_signature**: (boolean) Whether a bill is **currently** awaiting the president's signature. Becomes false once the bill is vetoed or enacted.
* **awaiting_signature_since**: (timestamp) When a bill began awaiting the president's signature, if it has been. Unset once the bill is enacted or vetoed.
* **vetoed**: (boolean) Whether a bill has been vetoed.
* **vetoed_at**: (timestamp) When a bill was vetoed, if it was.
* **senate_override_result**: The result of a Senate veto override vote, if one was taken. "pass", "fail", or null.
* **senate_override_result_at**: (timestamp) When the Senate last voted to override a veto of the bill, if it did.
* **house_override_result**: The result of a House veto override vote, if one was taken. "pass", "fail", or null.
* **house_override_result_at**: (timestamp) When the House last voted to override a veto of the bill, if it did.
* **enacted**: (boolean) Whether a bill has been enacted as law, through signature or a veto override.
* **enacted_at**: (timestamp) When a bill was enacted, if it was.

## actions ##

* **text**: Text describing the action that occurred to the bill.
* **acted_at**: (timestamp) Date or time the action occurred.
* **type**: Type of action that occurred. Usually this is "action", but can be "vote", "vote2", "vote-aux", "signed", "topresident", "enacted", and potentially other unforeseen values.

## passage_votes ##

* **result**: Result of the vote. Either "pass" or "fail".
* **voted_at**: (timestamp) When the vote occurred.
* **passage_type**: What this vote signifies. Can be "vote", "vote2", "vote-aux", or "pingpong".
* **text**: Text describing the vote.
* **how**: How the vote was taken. Can be "roll" if it was a roll call vote, or one of several forms indicating a voice vote or unanimous consent.
* **roll_id**: If the vote was a roll call vote, the associated roll call ID.
* **chamber**: Chamber the vote took place in. Either "house" or "senate".

## committees ##

A hash, keyed by committee ID, relating some basic information about the committee to what roles the committee had in relation to the bill.

* **activity**: An array of activities this committee has in relation to this bill.
* **committee**: Basic information about the committee.

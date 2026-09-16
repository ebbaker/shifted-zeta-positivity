# Check replay

[drafts.py](drafts.py) runs every programme registered in its `CHECKS`
dictionary and requires the output to equal the preserved record in
[`../numerics/records/`](../numerics/README.md).

```sh
python3 validation/drafts.py check --replay
```

It does not update the records, prove any mathematical claim, or say anything
about Weil positivity. This investigation has no manuscript yet, so the
`record` and `save` commands of the sibling investigations are absent; they
will be added with the same interface when there is a manuscript to record.

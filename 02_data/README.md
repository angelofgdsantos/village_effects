# 02_data

All project data. **Mostly gitignored** — only codebooks and small reference files are committed.

## Structure

| Subfolder | Contents | Committed? |
|-----------|---------|-----------|
| `raw/` | Unmodified source data as received | No |
| `processed/` | Cleaned / merged data ready for analysis | No |
| `codebooks/` | Data documentation, variable labels, source descriptions | Yes |

## Rule

Never modify raw data files. All processing goes in `03_analysis/scripts/` and writes to `processed/`.

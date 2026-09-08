# Public release checklist

Use this checklist before a repository is promoted as reusable.

## Automated scan

The featured public repositories were searched on 2026-09-08 for:

- Personal Microsoft email addresses.
- Private SharePoint URLs.
- Microsoft tenant and subscription identifiers.
- Local `C:\Users\...` paths.
- Common credential field names.
- `CONFIDENTIAL` and `NDA` markers.

No direct matches were found in the featured public repositories.

This is a first-pass scan, not a legal or security review.

The repository includes a weekly GitHub Actions audit in `.github/workflows/public-repo-audit.yml`. It clones every promoted public repository, checks for a root license, and fails on common private-path, tenant, email, and credential patterns.

## Required before calling a repository open source

- Add an explicit license appropriate to the asset.
- Remove private data, customer material, tenant configuration, and credentials.
- Replace personal machine paths with variables or documented placeholders.
- Use synthetic examples.
- Confirm that Microsoft logos, templates, and third-party content can be redistributed.
- Test the setup from a clean environment.

## Licensing guidance

- Code, scripts, and templates: consider MIT.
- Original learning material and presentations: consider Creative Commons.
- Microsoft or third-party material: do not relicense without confirmed rights.

## Current boundary

Microsoft products can appear as public examples and supported platforms. Microsoft-internal data, tenant-specific configuration, private links, and non-public product information cannot.

## Withheld projects

Agent Otto is not promoted publicly. Its original working repository contained internal program transcripts and tenant-specific configuration. A sanitized copy also inherited deprecated Teams AI dependencies with unresolved high-severity advisories. It remains private until it is migrated to the current Teams SDK and passes the public audit.

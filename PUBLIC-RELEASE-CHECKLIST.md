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

The audit reads text files only. Word, Excel, PowerPoint and PDF files, including their author metadata and rights protection, need a manual check before they are published.

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

The Copilot executive simulation stays internal until it passes a public release review: no Microsoft branding or internal labels, only publicly announced product surfaces, and a reviewed build published without its source.

The retail kiosk avatar repositories (`caip-demo-kiosk-avatar` and `druid-avatar-prototype`) stay private: they come from a customer engagement. The public version is `avatar-kiosk-starter`, a fresh repository with a single commit, a fictional brand and catalogue, and no engagement documents, subscription IDs or endpoints.

Agent Otto is not promoted publicly. Its original working repository contained internal program transcripts and tenant-specific configuration. A sanitized copy also inherited deprecated Teams AI dependencies with unresolved high-severity advisories. It remains private until it is migrated to the current Teams SDK and passes the public audit.

The former Frontier Consultancy repository history is private. A clean compatibility repository keeps existing `frontier-consultancy-public` Pages links working and redirects them to the sanitized `frontier-consultancy-kit`.

Frontier Consultancy is intentionally view-only. The public repository supports workshop discovery, participant preparation, and reference after a facilitated session. It does not grant permission for independent delivery, adaptation, or redistribution.

Frontier Consultancy is Microsoft-led for partners. Microsoft track-lead email addresses are published on the approved public contact pages under `partners/`. The AIBS and Business Transformation track pages (`aibs/` and `business/`) may link to the same people: the track leads added those links themselves in October 2026. Any other Microsoft address in the kit fails the audit.

The Capgemini audience deck deliberately retains Johan's visible speaker contact.
Its exception is limited to his exact address in the published deck and its v4
archive. The Enter the Agentic Enterprise Era audience deck
(`talks/agentic-enterprise-era-2026/deck.html`) has the same exception for the
contact slide. The speaker page (`speaker/index.html` in this repository) shows
the same address as the booking contact for event organisers, with an exception
limited to that file. Other Microsoft work email addresses and other file paths
remain subject to the audit.

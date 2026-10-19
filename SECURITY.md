# Security Policy

## Supported Versions

Only the default branch and the latest release are maintained. Older snapshots are not patched.

## Reporting a Vulnerability

Please **do not** open a public issue for a security problem.

Use GitHub's private vulnerability reporting instead:

https://github.com/rngfbbbffhjgggd-commits/Photo-PDF-Bidirectional-Converter-zh/security/advisories/new

The report stays private between you and the maintainer until a fix is published. This is a personal project, so there is no SLA and no paid support — expect a first reply within roughly a week, and please include a repro so the fix can be verified.

## Scope

This tool converts images to PDF and PDFs back to images using local libraries.

In scope:
- writes outside the output directory you selected
- code execution triggered by a maliciously crafted image or PDF
- unintended network access

Out of scope:
- defects in the upstream libraries (report those upstream)
- files that are corrupt beyond parsing

## What helps a report

- the version or commit you tested
- steps to reproduce, or a minimal proof of concept
- the impact you believe it has (local file write, credential leak, code execution, ...)

## Out of scope

- issues that only reproduce with an unsupported Python / OS / dependency version
- findings from automated scanners with no demonstrated impact
- bugs in third-party services this project merely talks to

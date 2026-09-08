"""Clone promoted public repositories and check basic release hygiene."""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


OWNER = "JW-Sthlm"
REPOSITORIES = [
    "JW-Sthlm.github.io",
    "signal-engine-oss",
    "frontier-consultancy-public",
    "frontier-consultancy-kit",
    "talks",
    "build-2026-gold",
    "copilot-overview",
    "ai-operator-intro",
    "partner-library-starter",
    "slidemaster-framework",
    "executive-assistant-blueprint",
    "podcast-prep-skill",
    "content-humanizer",
    "visual-sidekick",
]

LICENSE_FILES = {
    "LICENSE",
    "LICENSE.md",
    "LICENSE.txt",
    "COPYING",
    "COPYING.md",
}

TEXT_SUFFIXES = {
    ".css",
    ".env",
    ".example",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".sh",
    ".template",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}

PATTERNS = {
    "Microsoft work email": re.compile(r"\b[A-Z0-9._%+-]+@microsoft\.com\b", re.I),
    "tenant domain": re.compile(r"\b[A-Z0-9._-]+\.onmicrosoft\.com\b", re.I),
    "private SharePoint URL": re.compile(r"https?://[^\s]+sharepoint\.com/personal/", re.I),
    "Windows home path": re.compile(r"C:\\Users\\(?!<|%|your)[^\\\s]+\\", re.I),
    "file URL to home path": re.compile(r"file:///C:/Users/", re.I),
    "Azure tenant UUID": re.compile(
        r"az\s+login\s+--tenant\s+[0-9a-f]{8}-[0-9a-f]{4}-"
        r"[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        re.I,
    ),
    "GitHub token": re.compile(r"\bgh[opurs]_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}


def clone(repo: str, destination: Path) -> None:
    subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            "--quiet",
            f"https://github.com/{OWNER}/{repo}.git",
            str(destination),
        ],
        check=True,
    )


def text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.as_posix().endswith("/scripts/audit_public_repos.py"):
            continue
        if path.stat().st_size > 2_000_000:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name.startswith(".env"):
            yield path


def audit(repo: str, root: Path) -> list[str]:
    findings: list[str] = []
    if not any((root / name).exists() for name in LICENSE_FILES):
        findings.append("missing root license file")

    for path in text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(root)
        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{relative}:{line}: {label}")
    return findings


def main() -> int:
    all_findings: dict[str, list[str]] = {}
    with tempfile.TemporaryDirectory(prefix="public-repo-audit-") as tmp:
        base = Path(tmp)
        for repo in REPOSITORIES:
            destination = base / repo
            print(f"Auditing {OWNER}/{repo}")
            try:
                clone(repo, destination)
            except subprocess.CalledProcessError:
                all_findings[repo] = ["repository could not be cloned as public"]
                continue
            findings = audit(repo, destination)
            if findings:
                all_findings[repo] = findings

    if all_findings:
        print("\nPublic release audit failed:")
        for repo, findings in all_findings.items():
            print(f"\n{OWNER}/{repo}")
            for finding in findings:
                print(f"  - {finding}")
        return 1

    print(f"\nPublic release audit passed for {len(REPOSITORIES)} repositories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

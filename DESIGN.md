# Design

## Theme

Clawpilot light and dark themes. The light theme uses a warm off-white canvas, white working surfaces, charcoal text, and one deep rose accent. Dark mode uses charcoal surfaces with a pale rose accent. Theme follows system preference and can be overridden with `?scoutTheme=light` or `?scoutTheme=dark`.

## Typography

- Primary: Segoe UI, with Aptos and Calibri fallbacks.
- Monospace: Consolas, used only for repository names, commands, and small technical metadata.
- Display copy is large, direct, and tightly grouped. Body copy stays below 72 characters per line.

## Layout

- A compact sticky navigation.
- An asymmetric hero with the main statement and Johan's portrait.
- A short "start here" sequence using varied editorial blocks.
- A filterable project library presented as horizontal records rather than an identical card grid.
- A candid licensing note before the footer.

## Components

- Status pill: live demo, MIT licensed, source available, or reference.
- Project record: name, plain-language value, audience, metadata, and actions.
- Filter controls: accessible buttons with visible selected state.
- Copy command: copies a GitHub clone command and confirms success.

## Motion

One restrained load sequence for the hero and featured projects. Hover motion is limited to small translations and border changes. Reduced-motion users receive immediate states.

## Imagery

Use Johan's real reference portrait only. No generated or stock people.

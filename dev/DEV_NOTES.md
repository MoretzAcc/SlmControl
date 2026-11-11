# Development notes

## Development commands

```bash
uv run slmcontrol
uv run ruff check .
uv run python -m unittest discover -s tests
```

## Versioning policy

- Starting with 3.7.0, versions use `major.minor.patch`.
- Major is 3 and is expected to remain constant.
- Increment minor for new features or drastic changes, resetting patch to 0 (for example, 3.7.2 to 3.8.0).
- Increment patch for small changes, bug fixes, and typo corrections (for example, 3.7.0 to 3.7.1).
- This is a project-specific policy; a minor release may include breaking changes.
- Historical changelog versions, Git tags, and commits retain their original version numbers.

## To implement
- Warning when a monitor reports more than 8 bits per channel. The value is displayed, but the software output remains 8-bit and currently has no such warning.
- Make refresh button mostly irrelevant by including hotplug detection.
- Detect identical monitor names in the sidebar and add find some additional information that is not identical and add this to the sidebar.

## Open tasks

- Improve the current overlap between the Enable SLM output button and the output preview. Scaling down the preview is undesirable here, so an overlap can be a reasonable solution; the current implementation of that overlap needs improvement. Leave the UI unchanged until this design is revisited.
- Stabilize the HEROS connection toggle before exposing it in the user interface again.
- Add more end-to-end usage examples; existing client examples are in [client/src/examples](../client/src/examples).


## Known limitations and validation needs

- Native dimensions are derived from Qt geometry multiplied by device pixel ratio. Geometry/DPI signals and refresh trigger rescans, but aggressive or fractional OS scaling can still produce platform-specific problems. Verify both resolution changes and the resulting pattern reset on real hardware.
- Linux EDID-to-screen mapping depends on the desktop/compositor and needs further testing with multiple and mirrored monitors. Missing or duplicate metadata can prevent reliable identification.
- Screen IDs include host and monitor/connector information. They are intended to remain stable for an unchanged setup, but are not guaranteed hardware identifiers; moving ports or changing available metadata can change them.
- Verify output focus prevention on Linux and Windows and Aero Peek exclusions on Windows. These require a native desktop session.

## Future ideas

- Support output precision above 8 bits per channel.
- Optional REST API access.
- Decouple the logic completely from the UI, add argument uv run slmcontrol --headless

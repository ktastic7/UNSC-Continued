ST-12 MARKET ID PREFLIGHT VALIDATOR
===================================

Purpose
-------
Build-time/preflight validation for authored UNSC market condition, submarket,
and industry IDs. This tool is development-only and is not packaged into the
runtime mod.

It validates:
- the five normal authored markets created through UNSC_AddMarketplace;
- six uncolonized authored condition markets created through
  addUncolonizedConditions;
- direct Vanilla industry additions outside the helper (currently Reach Orbital
  Works);
- the optional Industrial Evolution Reach railgun industry against exact IndEvo
  industry data;
- literal true/false use for the two hardened addMarketplace boolean arguments.

Evidence requirements
---------------------
Run against the exact target Starsector API source and data registries plus the
exact supported Industrial Evolution industry registry. Do not substitute
hand-written constants or guessed registry files.

Use `python tools/validate_market_ids.py --help` for required arguments.

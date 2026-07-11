"""Streamlit Community Cloud entry point for the AquaScope dashboard.

Community Cloud builds from a script at the repo root, so this shim just
delegates to the real implementation in aquascope/dashboard/app.py --
there's a single source of truth for the dashboard logic.

Local usage:
    streamlit run streamlit_app.py

Equivalent CLI usage (launches the same app.py):
    aquascope dashboard
"""

from aquascope.dashboard.app import main

main()

# Copilot / AI Assistant Instructions

Purpose: concise, repo-specific guidance so an AI can be immediately productive working in this repository.

- **Big picture**: This repo contains small Python demos and Streamlit apps plus an ML notebook that trains an XGBoost model on a cars dataset. Primary artifacts:
  - `demo_app.py` and `finance_app.py` — interactive Streamlit apps (UI + light business logic)
  - `demo.ipynb` — Jupyter notebook that downloads `cars24-car-price-cleaned-new.csv`, prepares features, and trains an `XGBRegressor` using scikit-learn APIs
  - miscellaneous small modules (`calculator.py`, `widgets.py`, `hello.py`) used for demos/examples

- **Data & integrations**:
  - The notebook uses `gdown` to fetch a Google Drive file and saves it as `cars24-car-price-cleaned-new.csv` in the repo root. Keep that filename when referencing the dataset.
  - `finance_app.py` uses `yfinance` to fetch market data at runtime (network access required).

- **Dependencies** (explicit imports discovered):
  - `pandas`, `scikit-learn`, `xgboost`, `gdown`, `streamlit`, `yfinance` (install via `pip`)

- **Developer workflows / commands** (how to run things locally):
  - Run demo Streamlit app: `streamlit run demo_app.py`
  - Run finance app: `streamlit run finance_app.py`
  - Open and run the notebook: `jupyter lab` or `jupyter notebook` then open `demo.ipynb`
  - Run small scripts: `python hello.py` or `python calculator.py` as needed

- **Project-specific conventions & patterns** (use these when modifying or generating code):
  - Streamlit UIs are implemented in top-level `*_app.py` files and rely on immediate-execution script structure (no separate CLI entrypoint). Avoid refactoring them into hidden modules unless you also update the run instructions.
  - Notebooks are used for ML experiments; they download external data during execution (`gdown.download(...)`) and expect the CSV in repo root afterwards. When producing code that refers to training data, reference the existing filename.
  - Minimal module style: helper functions (e.g., `sqr()` in `demo_app.py`, math functions in `calculator.py`) are defined inline and used directly by the apps — follow this pattern for small demos.

- **Integration & cross-component notes**:
  - Network I/O: both `gdown` (Google Drive) and `yfinance` (Yahoo) are used — CI or running environments must allow outbound HTTP(S).
  - No packaging / tests / CI files detected — changes that add runtime dependencies should include an updated `requirements.txt` (project currently does not include one).

- **Editing guidance for AI agents** (concise actionable rules):
  - Preserve Streamlit app structure and direct execution flow; if you extract functionality into modules, also update `streamlit run` instructions.
  - When modifying `demo.ipynb`, keep data-download cell intact or update README/instructions to explain the new data location.
  - When adding dependencies, provide `requirements.txt` with pinned versions and include a short run example.
  - Prefer minimal, non-invasive edits: these demos are educational; avoid large refactors without the user's approval.

- **Key files to inspect for context**:
  - `demo.ipynb` — ML experiment and data download
  - `demo_app.py` — simple Streamlit demo (widgets and helper `sqr()`)
  - `finance_app.py` — Streamlit app using `yfinance`
  - `calculator.py`, `widgets.py` — small helper/demo modules

If anything here is unclear or you want the instructions expanded (for example: adding a `requirements.txt`, pinning dependency versions, or adding CI/test commands), tell me which part to expand and I'll update the file.

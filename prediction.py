import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.inspection import permutation_importance

# Optional: use these only if you want to save artifacts locally
# import joblib

st.set_page_config(page_title="F1 Prediction", page_icon="🏎️", layout="wide")

# -------------------------------------------------------------------
# File paths
# -------------------------------------------------------------------
DRIVER_CSV = "DriverPrediction.csv"
CONSTRUCTOR_CSV = "ConstructorPrediction.csv"
COMPARISON_CSV = "regression_comparison.csv"


# -------------------------------------------------------------------
# Data loading
# -------------------------------------------------------------------
@st.cache_data
def load_data():
    driver_df = pd.read_csv(DRIVER_CSV)
    constructor_df = pd.read_csv(CONSTRUCTOR_CSV)
    comparison_df = pd.read_csv(COMPARISON_CSV)
    return driver_df, constructor_df, comparison_df


# -------------------------------------------------------------------
# Driver-to-constructor mapping
# IMPORTANT: keys must match driverRef values exactly
# -------------------------------------------------------------------
DRIVER_TO_CONSTRUCTOR = {
    "hamilton": "Mercedes",
    "russell": "Mercedes",
    "max_verstappen": "Red Bull",
    "perez": "Red Bull",
    "leclerc": "Ferrari",
    "sainz": "Ferrari",
    "norris": "McLaren",
    "piastri": "McLaren",
    "alonso": "Aston Martin",
    "stroll": "Aston Martin",
    "ocon": "Alpine",
    "gasly": "Alpine",
    "hulkenberg": "Haas",
    "kevin_magnussen": "Haas",
    "ricciardo": "Racing Bulls",
    "tsunoda": "Racing Bulls",
    "bottas": "Kick Sauber",
    "zhou": "Kick Sauber",
    "albon": "Williams",
    "sargeant": "Williams",
}


# -------------------------------------------------------------------
# Feature engineering
# -------------------------------------------------------------------
def engineer_features(df: pd.DataFrame, constructor_map: dict) -> pd.DataFrame:
    df = df.copy()

    # Recency-weighted average points
    w21, w22, w23 = 1, 2, 4
    total_w = w21 + w22 + w23
    df["weighted_avg_points"] = (
        df["2021_points"] * w21
        + df["2022_points"] * w22
        + df["2023_points"] * w23
    ) / total_w

    # Points vs teammate
    driver_key = df["driverRef"].astype(str).str.lower().str.strip()
    df["_constructor"] = driver_key.map(constructor_map)

    for yr in ["2021", "2022", "2023"]:
        col = f"{yr}_points"
        team_mean = df.groupby("_constructor")[col].transform("mean")
        df[f"pts_vs_teammate_{yr}"] = df[col] - team_mean

    df.drop(columns=["_constructor"], inplace=True)

    # Driver-to-car ratio
    df["driver_to_car_ratio"] = df["driverRating"] / df["carRating"].replace(0, np.nan)

    return df


# -------------------------------------------------------------------
# Feature columns and target
# -------------------------------------------------------------------
FEATURE_COLS = [
    "driverRating",
    "carRating",
    "constructorStrategy",
    "2021_points",
    "2022_points",
    "2023_points",
    "weighted_avg_points",
    "pts_vs_teammate_2021",
    "pts_vs_teammate_2022",
    "pts_vs_teammate_2023",
    "driver_to_car_ratio",
]
TARGET_COL = "2024_points"


# -------------------------------------------------------------------
# Models
# -------------------------------------------------------------------
def make_models():
    return {
        "Ridge": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("model", Ridge(alpha=1.0)),
        ]),
        "Lasso": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("model", Lasso(alpha=0.05, max_iter=10000)),
        ]),
        "ElasticNet": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("model", ElasticNet(alpha=0.05, l1_ratio=0.5, max_iter=10000)),
        ]),
        "RandomForest": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("model", RandomForestRegressor(
                n_estimators=500,
                random_state=42,
                max_depth=4,
                min_samples_leaf=2,
            )),
        ]),
        "GradientBoosting": Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("model", GradientBoostingRegressor(
                n_estimators=200,
                learning_rate=0.05,
                max_depth=2,
                random_state=42,
            )),
        ]),
    }


# -------------------------------------------------------------------
# Evaluation helpers
# -------------------------------------------------------------------
def evaluate_models(df: pd.DataFrame, feature_cols: list, target_col: str):
    work_df = df.dropna(subset=[target_col]).copy()
    X = work_df[feature_cols]
    y = work_df[target_col]

    loo = LeaveOneOut()
    results, pred_store = [], {}

    for name, model in make_models().items():
        preds = cross_val_predict(model, X, y, cv=loo)
        results.append({
            "Model": name,
            "MAE": mean_absolute_error(y, preds),
            "RMSE": np.sqrt(mean_squared_error(y, preds)),
            "R2": r2_score(y, preds),
        })
        pred_store[name] = preds

    results_df = pd.DataFrame(results).sort_values("MAE").reset_index(drop=True)
    return results_df, pred_store, work_df


def build_constructor_table(driver_df_with_preds: pd.DataFrame, pred_col: str, constructor_map: dict):
    df = driver_df_with_preds.copy()
    df["driver_key"] = df["driverRef"].astype(str).str.lower().str.strip()
    df["Constructor"] = df["driver_key"].map(constructor_map)

    constructor_df = (
        df.dropna(subset=["Constructor"])
        .groupby("Constructor", as_index=False)
        .agg({
            "2021_points": "sum",
            "2022_points": "sum",
            "2023_points": "sum",
            pred_col: "sum",
        })
        .rename(columns={
            "2021_points": "2021_Points",
            "2022_points": "2022_Points",
            "2023_points": "2023_Points",
            pred_col: "Predicted_2024_Points",
        })
    )

    for col in ["2021_Points", "2022_Points", "2023_Points", "Predicted_2024_Points"]:
        constructor_df[col] = constructor_df[col].round().clip(lower=0).astype(int)

    return constructor_df.sort_values("Predicted_2024_Points", ascending=False).reset_index(drop=True)


def plot_actual_vs_predicted(y_true, y_pred, title):
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.scatter(y_true, y_pred, zorder=3)
    lo = min(np.min(y_true), np.min(y_pred))
    hi = max(np.max(y_true), np.max(y_pred))
    ax.plot([lo, hi], [lo, hi], linestyle="--", color="grey")
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig


def plot_bar(df, x_col, y_col, title, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(11, 4))
    bars = ax.bar(df[x_col], df[y_col])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=90)
    plt.tight_layout()

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, f"{int(round(yval))}",
                ha="center", va="bottom", fontsize=8)
    return fig


# -------------------------------------------------------------------
# Main app
# -------------------------------------------------------------------
def main():
    st.title("Formula 1 Prediction Dashboard")
    st.caption("Driver and constructor predictions with a clean, reusable Streamlit workflow.")

    try:
        driver_df, constructor_df, comparison_df = load_data()
    except Exception as e:
        st.error(f"Could not load CSV files: {e}")
        st.stop()

    driver_df = engineer_features(driver_df, DRIVER_TO_CONSTRUCTOR)

    missing_cols = [c for c in FEATURE_COLS + [TARGET_COL] if c not in driver_df.columns]
    if missing_cols:
        st.error(f"Missing columns in driver data: {missing_cols}")
        st.stop()

    results_df, pred_store, work_df = evaluate_models(driver_df, FEATURE_COLS, TARGET_COL)
    best_model_name = results_df.iloc[0]["Model"]
    cv_preds = pred_store[best_model_name]

    driver_cv_df = work_df.copy()
    driver_cv_df["cv_predicted_2024_points"] = (
        pd.Series(cv_preds, index=work_df.index)
        .round()
        .clip(lower=0)
        .astype(int)
    )
    driver_cv_df = driver_cv_df.sort_values("cv_predicted_2024_points", ascending=False)

    constructor_cv_df = build_constructor_table(
        driver_cv_df,
        "cv_predicted_2024_points",
        DRIVER_TO_CONSTRUCTOR,
    )

    # -------- Driver section --------
    st.header("Prediction: F1 Driver Points for 2024 Season")

    col1, col2 = st.columns([1.3, 1])
    with col1:
        st.subheader("Model comparison")
        st.dataframe(results_df.style.format({"MAE": "{:.2f}", "RMSE": "{:.2f}", "R2": "{:.3f}"}),
                     use_container_width=True)
        st.info(f"Best model by MAE: **{best_model_name}**")

    with col2:
        st.subheader("Feature engineering")
        st.write("The notebook adds:")
        st.write("- weighted average points")
        st.write("- points vs teammate")
        st.write("- driver-to-car ratio")

    st.subheader("Driver predictions")
    driver_table = driver_cv_df[[
        "driverRef",
        "2021_points",
        "2022_points",
        "2023_points",
        "2024_points",
        "cv_predicted_2024_points",
    ]].copy()
    st.dataframe(driver_table, use_container_width=True)

    fig1 = plot_actual_vs_predicted(
        driver_cv_df["2024_points"],
        driver_cv_df["cv_predicted_2024_points"],
        title=f"Driver CV — Actual vs Predicted ({best_model_name})",
    )
    st.pyplot(fig1, clear_figure=True)

    fig2 = plot_bar(
        driver_cv_df.sort_values("cv_predicted_2024_points", ascending=True),
        "driverRef",
        "cv_predicted_2024_points",
        "Predicted 2024 Points for Each Driver",
        "Driver",
        "Predicted 2024 Points",
    )
    st.pyplot(fig2, clear_figure=True)

    st.markdown(
        """
        <div style="background-color:black; padding:10px; border-radius:8px;">
            <span style="color:white;">
            Note: sports predictions are not always accurate. This page uses a Lasso/linear-model style workflow
            with recent points, driver skill rating, car rating, and constructor context.
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="background-color:black; padding:10px; border-radius:8px; margin-top:10px;">
            <span style="color:white;">
            This was a retrospective prediction exercise, not a real pre-season forecast.
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -------- Constructor section --------
    st.write("---------------------------------------------------------------------------------------")
    st.header("Prediction: F1 Constructor Points for 2024 Season")

    constructor_table = constructor_cv_df[[
        "Constructor",
        "2021_Points",
        "2022_Points",
        "2023_Points",
        "Predicted_2024_Points",
    ]]
    st.dataframe(constructor_table, use_container_width=True)

    fig3 = plot_bar(
        constructor_cv_df.sort_values("Predicted_2024_Points", ascending=True),
        "Constructor",
        "Predicted_2024_Points",
        "Predicted 2024 Points for Constructor",
        "Constructor",
        "Predicted 2024 Points",
    )
    st.pyplot(fig3, clear_figure=True)

    st.markdown(
        """
        <div style="background-color:black; padding:10px; border-radius:8px;">
            <span style="color:white;">
            Note: constructor totals are built from the driver predictions.
            AlphaTauri is renamed as Racing Bulls.
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -------- Comparison section --------
    st.subheader("Why linear regression")
    if {"Model", "R2 Value"}.issubset(comparison_df.columns):
        st.dataframe(comparison_df[["Model", "R2 Value"]], use_container_width=True)
    else:
        st.dataframe(comparison_df, use_container_width=True)

    # -------- Feature importance --------
    st.subheader("Feature importance")
    final_model = make_models()[best_model_name]
    X_all = work_df[FEATURE_COLS]
    y_all = work_df[TARGET_COL]
    final_model.fit(X_all, y_all)

    perm = permutation_importance(
        final_model,
        X_all,
        y_all,
        scoring="neg_mean_absolute_error",
        n_repeats=50,
        random_state=42,
    )

    perm_df = (
        pd.DataFrame({
            "Feature": FEATURE_COLS,
            "Importance_Mean": perm.importances_mean,
            "Importance_Std": perm.importances_std,
        })
        .sort_values("Importance_Mean", ascending=False)
        .reset_index(drop=True)
    )

    st.dataframe(perm_df, use_container_width=True)

    fig4, ax = plt.subplots(figsize=(9, 5))
    ax.barh(
        perm_df["Feature"][::-1],
        perm_df["Importance_Mean"][::-1],
        xerr=perm_df["Importance_Std"][::-1],
        capsize=4,
    )
    ax.set_title("Permutation Feature Importance (final model, in-sample)")
    ax.set_xlabel("Mean decrease in MAE score when feature is shuffled")
    plt.tight_layout()
    st.pyplot(fig4, clear_figure=True)


if __name__ == "__main__":
    main()

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


# -------------------------------------------------------------------
# Driver-to-constructor mapping
# IMPORTANT: keys must match DriverPrediction.csv driverRef values exactly
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

BASE_FEATURE_COLS = [
    "driverRating",
    "carRating",
    "constructorStrategy",
    "2021_points",
    "2022_points",
    "2023_points",
]

ENGINEERED_FEATURE_COLS = [
    "weighted_avg_points",
    "pts_vs_teammate_2021",
    "pts_vs_teammate_2022",
    "pts_vs_teammate_2023",
    "driver_to_car_ratio",
]

FEATURE_COLS = BASE_FEATURE_COLS + ENGINEERED_FEATURE_COLS
TARGET_COL = "2024_points"


# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def _style_table(df: pd.DataFrame) -> str:
    table_html = df.to_html(index=False, classes="dataframe", border=0)
    return f"""
    <style>
    table.dataframe {{
        background-color: black;
        color: white;
        padding: 10px;
        border-collapse: collapse;
        width: 100%;
    }}
    table.dataframe th, table.dataframe td {{
        padding: 8px;
        border: 1px solid #444;
        text-align: center;
    }}
    table.dataframe th {{
        background-color: #E11433;
        color: white;
    }}
    </style>
    {table_html}
    """


def _make_numeric(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    df = df.copy()
    for col in cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def _validate_columns(df: pd.DataFrame, required_cols: list[str]) -> list[str]:
    return [col for col in required_cols if col not in df.columns]


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = _make_numeric(df, BASE_FEATURE_COLS + [TARGET_COL])

    # Recency-weighted points: 2023 matters most, then 2022, then 2021.
    df["weighted_avg_points"] = (
        df["2021_points"] * 1
        + df["2022_points"] * 2
        + df["2023_points"] * 4
    ) / 7

    # Teammate-relative points by constructor.
    df["driver_key"] = df["driverRef"].astype(str).str.lower().str.strip()
    df["Constructor"] = df["driver_key"].map(DRIVER_TO_CONSTRUCTOR)

    for year in ["2021", "2022", "2023"]:
        points_col = f"{year}_points"
        teammate_mean = df.groupby("Constructor")[points_col].transform("mean")
        df[f"pts_vs_teammate_{year}"] = df[points_col] - teammate_mean

    # How much driver rating exceeds or trails car rating.
    df["driver_to_car_ratio"] = df["driverRating"] / df["carRating"].replace(0, np.nan)

    return df


def make_models() -> dict[str, Pipeline]:
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
                max_depth=4,
                min_samples_leaf=2,
                random_state=42,
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


def evaluate_models(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, np.ndarray], pd.DataFrame]:
    work_df = df.dropna(subset=[TARGET_COL]).copy()
    X = work_df[FEATURE_COLS]
    y = work_df[TARGET_COL]

    loo = LeaveOneOut()
    rows = []
    predictions_by_model = {}

    for model_name, model in make_models().items():
        cv_predictions = cross_val_predict(model, X, y, cv=loo)
        predictions_by_model[model_name] = cv_predictions
        rows.append({
            "Model": model_name,
            "MAE": mean_absolute_error(y, cv_predictions),
            "RMSE": np.sqrt(mean_squared_error(y, cv_predictions)),
            "R2": r2_score(y, cv_predictions),
        })

    results_df = pd.DataFrame(rows).sort_values("MAE").reset_index(drop=True)
    return results_df, predictions_by_model, work_df


def build_constructor_table(driver_df: pd.DataFrame, prediction_col: str) -> pd.DataFrame:
    constructor_df = (
        driver_df.dropna(subset=["Constructor"])
        .groupby("Constructor", as_index=False)
        .agg({
            "2021_points": "sum",
            "2022_points": "sum",
            "2023_points": "sum",
            prediction_col: "sum",
        })
        .rename(columns={
            "2021_points": "2021_Points",
            "2022_points": "2022_Points",
            "2023_points": "2023_Points",
            prediction_col: "Predicted_2024_Points",
        })
    )

    for col in ["2021_Points", "2022_Points", "2023_Points", "Predicted_2024_Points"]:
        constructor_df[col] = constructor_df[col].round().clip(lower=0).astype(int)

    return constructor_df.sort_values("Predicted_2024_Points", ascending=False).reset_index(drop=True)


def plot_bar(df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str):
    fig, ax = plt.subplots(figsize=(10, 4), facecolor="#463F41")
    ax.set_facecolor("#463F41")

    bars = ax.bar(df[x_col], df[y_col], color="#E11433")
    ax.set_xlabel(xlabel, color="white")
    ax.set_ylabel(ylabel, color="white")
    ax.set_title(title, color="white")
    ax.tick_params(axis="x", colors="white", rotation=90)
    ax.tick_params(axis="y", colors="white")

    for spine in ax.spines.values():
        spine.set_color("white")

    for bar in bars:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            f"{int(round(yval))}",
            ha="center",
            va="bottom",
            color="white",
            fontsize=8,
        )

    plt.tight_layout()
    return fig


def plot_actual_vs_predicted(df: pd.DataFrame, prediction_col: str, model_name: str):
    fig, ax = plt.subplots(figsize=(7, 5), facecolor="#463F41")
    ax.set_facecolor("#463F41")

    ax.scatter(df[TARGET_COL], df[prediction_col], color="#E11433")
    low = min(df[TARGET_COL].min(), df[prediction_col].min())
    high = max(df[TARGET_COL].max(), df[prediction_col].max())
    ax.plot([low, high], [low, high], linestyle="--", color="white")

    ax.set_xlabel("Actual 2024 Points", color="white")
    ax.set_ylabel("Predicted 2024 Points", color="white")
    ax.set_title(f"Actual vs Predicted 2024 Points ({model_name})", color="white")
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")

    for spine in ax.spines.values():
        spine.set_color("white")

    plt.tight_layout()
    return fig


def show_note(text: str):
    st.write(
        f"""
        <div style="background-color: black; padding: 10px; border-radius: 8px; margin-top: 8px;">
            <span style="color: white;">{text}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------------------
# Function used by your main app:
# from prediction import predict_points
# predict_points(data)
# -------------------------------------------------------------------
def predict_points(data: pd.DataFrame):
    st.header("Prediction: F1 Driver Points for 2024 Season")

    required_cols = ["driverRef"] + BASE_FEATURE_COLS + [TARGET_COL]
    missing_cols = _validate_columns(data, required_cols)
    if missing_cols:
        st.error(f"DriverPrediction.csv is missing these columns: {missing_cols}")
        return

    driver_df = engineer_features(data)

    # Warn if any drivers are not in the constructor map.
    unmapped = driver_df.loc[driver_df["Constructor"].isna(), "driverRef"].dropna().unique().tolist()
    if unmapped:
        st.warning(
            "These driverRef values are not mapped to a constructor, so constructor totals may be incomplete: "
            + ", ".join(map(str, unmapped))
        )

    results_df, predictions_by_model, work_df = evaluate_models(driver_df)
    best_model_name = results_df.iloc[0]["Model"]

    # Honest leave-one-out predictions.
    driver_results = work_df.copy()
    driver_results["cv_predicted_2024_points"] = (
        pd.Series(predictions_by_model[best_model_name], index=work_df.index)
        .round()
        .clip(lower=0)
        .astype(int)
    )

    # Training-fit predictions. These usually look much better, but they are not real out-of-sample predictions.
    final_model = make_models()[best_model_name]
    X_all = work_df[FEATURE_COLS]
    y_all = work_df[TARGET_COL]
    final_model.fit(X_all, y_all)
    driver_results["training_fit_2024_points"] = (
        pd.Series(final_model.predict(X_all), index=work_df.index)
        .round()
        .clip(lower=0)
        .astype(int)
    )

    st.subheader("Model comparison")
    formatted_results = results_df.copy()
    formatted_results["MAE"] = formatted_results["MAE"].round(2)
    formatted_results["RMSE"] = formatted_results["RMSE"].round(2)
    formatted_results["R2"] = formatted_results["R2"].round(3)
    st.write(_style_table(formatted_results), unsafe_allow_html=True)
    st.info(f"Best validation model by MAE: {best_model_name}")

    prediction_view = st.radio(
        "Choose prediction output to display",
        [
            "Honest CV predictions",
            "Training-fit predictions only",
        ],
        horizontal=True,
    )

    if prediction_view == "Honest CV predictions":
        prediction_col = "cv_predicted_2024_points"
        show_note(
            "Honest CV predictions are out-of-sample validation estimates. They are more trustworthy for model evaluation, but they can look strange with only about 20 drivers."
        )
    else:
        prediction_col = "training_fit_2024_points"
        show_note(
            "Training-fit predictions are fitted on the same data being predicted. They are useful for demos, but they should not be presented as real forecasts."
        )

    driver_results = driver_results.sort_values(prediction_col, ascending=False)

    driver_display = driver_results[[
        "driverRef",
        "2021_points",
        "2022_points",
        "2023_points",
        "2024_points",
        prediction_col,
    ]].rename(columns={
        prediction_col: "predicted_2024_points",
    })

    driver_display["predicted_2024_points"] = driver_display["predicted_2024_points"].round().clip(lower=0).astype(int)
    st.write(_style_table(driver_display), unsafe_allow_html=True)

    fig1 = plot_bar(
        driver_display,
        "driverRef",
        "predicted_2024_points",
        "Predicted 2024 Points for Each Driver",
        "Driver",
        "Predicted 2024 Points",
    )
    st.pyplot(fig1, clear_figure=True)

    fig2 = plot_actual_vs_predicted(driver_results, prediction_col, best_model_name)
    st.pyplot(fig2, clear_figure=True)

    show_note(
        "Predicting sports results is difficult. This model uses recent points, driver skill rating, car rating, constructor strategy, teammate-relative points, and a few engineered features."
    )
    show_note(
        "This page is best understood as a retrospective model evaluation for the 2024 season, not a perfect pre-season forecast."
    )

    st.write("---------------------------------------------------------------------------------------")
    st.header("Prediction: F1 Constructor Points for 2024 Season")

    constructor_df = build_constructor_table(driver_results, prediction_col)
    st.write(_style_table(constructor_df), unsafe_allow_html=True)

    fig3 = plot_bar(
        constructor_df,
        "Constructor",
        "Predicted_2024_Points",
        "Predicted 2024 Points for Constructor",
        "Constructor",
        "Predicted 2024 Points",
    )
    st.pyplot(fig3, clear_figure=True)

    show_note(
        "Constructor totals are generated by summing the two driver predictions for each constructor. There is no separate constructor ML model. AlphaTauri is treated as Racing Bulls."
    )

    st.subheader("Feature importance")
    st.caption("Permutation importance is calculated on the fitted final model, so use it as a model explanation, not as separate validation.")

    perm = permutation_importance(
        final_model,
        X_all,
        y_all,
        scoring="neg_mean_absolute_error",
        n_repeats=50,
        random_state=42,
    )

    importance_df = (
        pd.DataFrame({
            "Feature": FEATURE_COLS,
            "Importance_Mean": perm.importances_mean,
            "Importance_Std": perm.importances_std,
        })
        .sort_values("Importance_Mean", ascending=False)
        .reset_index(drop=True)
    )
    importance_df["Importance_Mean"] = importance_df["Importance_Mean"].round(3)
    importance_df["Importance_Std"] = importance_df["Importance_Std"].round(3)
    st.write(_style_table(importance_df), unsafe_allow_html=True)

    fig4, ax = plt.subplots(figsize=(9, 5), facecolor="#463F41")
    ax.set_facecolor("#463F41")
    ax.barh(importance_df["Feature"][::-1], importance_df["Importance_Mean"][::-1], color="#E11433")
    ax.set_xlabel("Permutation Importance", color="white")
    ax.set_title("Feature Importance", color="white")
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")

    for spine in ax.spines.values():
        spine.set_color("white")

    plt.tight_layout()
    st.pyplot(fig4, clear_figure=True)

    st.subheader("Why this approach")
    st.write(
        """
        This version compares multiple regularized and tree-based regression models using leave-one-out cross-validation. 
        That is more honest than only showing predictions from a model fitted on all drivers, especially because the dataset is very small.
        """
    )

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


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


def _add_prediction_table_css():
    st.markdown(
        """
        <style>
        div[data-testid="stTable"] table {
            background-color: black !important;
            color: white !important;
        }
        div[data-testid="stTable"] th {
            background-color: black !important;
            color: white !important;
            border-bottom: 1px solid #555 !important;
        }
        div[data-testid="stTable"] td {
            background-color: black !important;
            color: white !important;
            border-bottom: 1px solid #333 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _show_table(df):
    """Show a clean table. No df.to_html and no raw <table> text."""
    display_df = df.copy().reset_index(drop=True)
    styled = (
        display_df.style.hide(axis="index")
        .set_properties(**{"background-color": "black", "color": "white"})
        .set_table_styles(
            [
                {
                    "selector": "th",
                    "props": [
                        ("background-color", "black"),
                        ("color", "white"),
                        ("border-bottom", "1px solid #555"),
                    ],
                },
                {
                    "selector": "td",
                    "props": [
                        ("background-color", "black"),
                        ("color", "white"),
                        ("border-bottom", "1px solid #333"),
                    ],
                },
            ]
        )
    )
    st.table(styled)


def _black_note(text):
    st.markdown(
        f"""
        <div style="background-color: black; padding: 10px; margin-bottom: 8px;">
            <span style="color: white;">{text}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _make_numeric(df, columns):
    df = df.copy()
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def _prepare_features(raw_data):
    df = raw_data.copy()
    df = _make_numeric(df, BASE_FEATURE_COLS + [TARGET_COL])

    df["driver_key"] = df["driverRef"].astype(str).str.lower().str.strip()
    df["Constructor"] = df["driver_key"].map(DRIVER_TO_CONSTRUCTOR)

    df["weighted_avg_points"] = (
        df["2021_points"] * 1 + df["2022_points"] * 2 + df["2023_points"] * 4
    ) / 7

    for year in ["2021", "2022", "2023"]:
        points_col = f"{year}_points"
        teammate_mean = df.groupby("Constructor")[points_col].transform("mean")
        df[f"pts_vs_teammate_{year}"] = df[points_col] - teammate_mean

    df["driver_to_car_ratio"] = df["driverRating"] / df["carRating"].replace(0, np.nan)
    return df


def _make_model():
    return Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("model", ElasticNet(alpha=0.05, l1_ratio=0.5, max_iter=10000, random_state=42)),
        ]
    )


@st.cache_data(show_spinner=False)
def _get_prediction_outputs(raw_data):
    df = _prepare_features(raw_data)
    model_df = df.dropna(subset=[TARGET_COL]).copy()

    X = model_df[FEATURE_COLS]
    y = model_df[TARGET_COL]

    # Honest validation output. Cached so it does not rerun every click.
    cv_model = _make_model()
    cv_pred = cross_val_predict(cv_model, X, y, cv=LeaveOneOut())

    # Training-fit output. This is fast and useful for showing model fit.
    final_model = _make_model()
    final_model.fit(X, y)
    training_pred = final_model.predict(X)

    cv_df = model_df.copy()
    train_df = model_df.copy()

    cv_df["predicted_2024_points"] = np.round(np.clip(cv_pred, 0, None)).astype(int)
    train_df["predicted_2024_points"] = np.round(np.clip(training_pred, 0, None)).astype(int)

    cv_df = cv_df.sort_values("predicted_2024_points", ascending=False).reset_index(drop=True)
    train_df = train_df.sort_values("predicted_2024_points", ascending=False).reset_index(drop=True)

    return cv_df, train_df


def _constructor_predictions(driver_df):
    constructor_df = (
        driver_df.dropna(subset=["Constructor"])
        .groupby("Constructor", as_index=False)
        .agg(
            {
                "2021_points": "sum",
                "2022_points": "sum",
                "2023_points": "sum",
                "predicted_2024_points": "sum",
            }
        )
        .rename(
            columns={
                "2021_points": "2021_Points",
                "2022_points": "2022_Points",
                "2023_points": "2023_Points",
                "predicted_2024_points": "Predicted_2024_Points",
            }
        )
    )

    for col in ["2021_Points", "2022_Points", "2023_Points", "Predicted_2024_Points"]:
        constructor_df[col] = constructor_df[col].round().clip(lower=0).astype(int)

    return constructor_df.sort_values("Predicted_2024_Points", ascending=False).reset_index(drop=True)


def _plot_driver_bar(driver_table):
    fig, ax = plt.subplots(figsize=(10, 4), facecolor="#463F41")
    ax.set_facecolor("#463F41")

    bars = ax.bar(driver_table["driverRef"], driver_table["predicted_2024_points"], color="#E11433")

    ax.set_xlabel("Driver", color="white")
    ax.set_ylabel("Predicted 2024 Points", color="white")
    ax.set_title("Predicted 2024 Points for Each Driver", color="white")
    ax.tick_params(axis="x", colors="white", rotation=90)
    ax.tick_params(axis="y", colors="white")

    for spine in ax.spines.values():
        spine.set_color("white")

    for bar in bars:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            int(round(yval)),
            ha="center",
            va="bottom",
            color="white",
            fontsize=8,
        )

    fig.tight_layout()
    return fig


def _plot_elasticnet_line(driver_df):
    plot_df = driver_df.sort_values("2024_points", ascending=False).reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(10, 4), facecolor="#463F41")
    ax.set_facecolor("#463F41")

    ax.plot(
        plot_df["driverRef"],
        plot_df["2024_points"],
        marker="o",
        linewidth=2,
        color="white",
        label="Actual 2024 Points",
    )
    ax.plot(
        plot_df["driverRef"],
        plot_df["predicted_2024_points"],
        marker="o",
        linewidth=2,
        color="#E11433",
        label="ElasticNet Predicted Points",
    )

    ax.set_xlabel("Driver", color="white")
    ax.set_ylabel("Points", color="white")
    ax.set_title("ElasticNet: Actual vs Predicted 2024 Driver Points", color="white")
    ax.tick_params(axis="x", colors="white", rotation=90)
    ax.tick_params(axis="y", colors="white")

    for spine in ax.spines.values():
        spine.set_color("white")

    legend = ax.legend()
    legend.get_frame().set_facecolor("#463F41")
    legend.get_frame().set_edgecolor("white")
    for text in legend.get_texts():
        text.set_color("white")

    fig.tight_layout()
    return fig


def _plot_constructor_bar(constructor_table):
    fig, ax = plt.subplots(figsize=(10, 4), facecolor="#463F41")
    ax.set_facecolor("#463F41")

    bars = ax.bar(constructor_table["Constructor"], constructor_table["Predicted_2024_Points"], color="#E11433")

    ax.set_xlabel("Constructor", color="white")
    ax.set_ylabel("Predicted 2024 Points", color="white")
    ax.set_title("Predicted 2024 Points for Constructor", color="white")
    ax.tick_params(axis="x", colors="white", rotation=90)
    ax.tick_params(axis="y", colors="white")

    for spine in ax.spines.values():
        spine.set_color("white")

    for bar in bars:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            int(round(yval)),
            ha="center",
            va="bottom",
            color="white",
            fontsize=8,
        )

    fig.tight_layout()
    return fig


def predict_points(data):
    st.header("Prediction: F1 Driver Points for 2024 Season")
    _add_prediction_table_css()

    required_cols = ["driverRef"] + BASE_FEATURE_COLS + [TARGET_COL]
    missing_cols = [col for col in required_cols if col not in data.columns]
    if missing_cols:
        st.error(f"DriverPrediction.csv is missing these columns: {missing_cols}")
        return

    cv_df, train_df = _get_prediction_outputs(data.copy())

    prediction_mode = st.radio(
        "Choose prediction output",
        ["Honest CV predictions", "Training-fit predictions"],
        horizontal=True,
        key="prediction_output_mode",
    )

    if prediction_mode == "Training-fit predictions":
        display_df = train_df.copy()
        _black_note("Showing ElasticNet training-fit predictions. These are model-fit values, not true out-of-sample forecasts.")
    else:
        display_df = cv_df.copy()
        _black_note("Showing ElasticNet honest CV predictions. These are out-of-sample validation estimates.")

    driver_table = display_df[
        [
            "driverRef",
            "2021_points",
            "2022_points",
            "2023_points",
            "2024_points",
            "predicted_2024_points",
        ]
    ].copy()

    _show_table(driver_table)

    fig = _plot_driver_bar(driver_table)
    st.pyplot(fig)
    plt.close(fig)

    fig_line = _plot_elasticnet_line(display_df)
    st.pyplot(fig_line)
    plt.close(fig_line)

    st.markdown(
        '<img src="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/rockcms/2022-10/221010-Max-Verstappen-ew-1132a-276412.jpg" width="700" height="400"/>',
        unsafe_allow_html=True,
    )

    _black_note(
        "Note: Predicting sports results is not always accurate. This model uses the last three years of points data, driver skill rating, car rating, constructor strategy, and engineered teammate features."
    )

    st.write("---------------------------------------------------------------------------------------")
    st.header("Prediction: F1 Constructor Points for 2024 Season")

    constructor_table = _constructor_predictions(display_df)[
        [
            "Constructor",
            "2021_Points",
            "2022_Points",
            "2023_Points",
            "Predicted_2024_Points",
        ]
    ].copy()

    _show_table(constructor_table)

    fig_constructor = _plot_constructor_bar(constructor_table)
    st.pyplot(fig_constructor)
    plt.close(fig_constructor)

    st.markdown(
        '<img src="https://mclaren.bloomreach.io/cdn-cgi/image/width=680,height=460,fit=crop,quality=80,format=webp/delivery/resources/content/gallery/mclaren-racing/formula-1/2024/schedule/abu-dhabi-grand-prix/race/report/report_0010_gp2424_193025_67a4774.jpg" width="700" height="400"/>',
        unsafe_allow_html=True,
    )

    _black_note("Note: This data is based on driver predictions. AlphaTauri is renamed as Racing Bulls.")

    st.subheader("Why ElasticNet")
    _black_note("ElasticNet was kept because it gives a more stable prediction line than the old Lasso-only version on this very small dataset.")

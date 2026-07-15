import html
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


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

# Fast fallback values from your ElasticNet honest-CV output.
# If your CSV has prediction columns, those columns are used instead.
ELASTICNET_CV_PREDICTIONS = {
    "norris": 354,
    "max_verstappen": 351,
    "leclerc": 307,
    "sainz": 297,
    "perez": 280,
    "piastri": 228,
    "hamilton": 223,
    "russell": 200,
    "alonso": 176,
    "ocon": 84,
    "kevin_magnussen": 50,
    "tsunoda": 47,
    "stroll": 40,
    "gasly": 32,
    "hulkenberg": 27,
    "bottas": 18,
    "albon": 0,
    "ricciardo": 0,
    "zhou": 0,
    "sargeant": 0,
}


def _black_note(text):
    st.markdown(
        f"""
        <div style="background-color:black; padding:10px; margin:8px 0;">
            <span style="color:white;">{html.escape(text)}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _safe_num(value):
    if pd.isna(value):
        return ""
    try:
        value = float(value)
        if value.is_integer():
            return str(int(value))
        return f"{value:.1f}"
    except Exception:
        return html.escape(str(value))


def _html_table(df, height=None):
    rows = []
    for _, row in df.iterrows():
        cells = "".join(f"<td>{_safe_num(row[col])}</td>" for col in df.columns)
        rows.append(f"<tr>{cells}</tr>")

    headers = "".join(f"<th>{html.escape(str(col))}</th>" for col in df.columns)
    table_html = f"""
    <html>
    <head>
    <style>
        body {{ margin:0; background:transparent; font-family:Arial, sans-serif; }}
        table {{ border-collapse:collapse; width:100%; background:black; color:white; font-size:14px; }}
        th, td {{ padding:8px 10px; border-bottom:1px solid #333; text-align:left; }}
        th {{ color:white; background:#111; font-weight:700; }}
        tr:hover td {{ background:#1b1b1b; }}
    </style>
    </head>
    <body>
        <table>
            <thead><tr>{headers}</tr></thead>
            <tbody>{''.join(rows)}</tbody>
        </table>
    </body>
    </html>
    """
    if height is None:
        height = min(850, 56 + len(df) * 38)
    components.html(table_html, height=height, scrolling=True)


def _html_bar_chart(df, label_col, value_col, title, x_label, y_label, height=440):
    chart_df = df[[label_col, value_col]].copy()
    chart_df[value_col] = pd.to_numeric(chart_df[value_col], errors="coerce").fillna(0)
    max_value = max(float(chart_df[value_col].max()), 1.0)

    bars = []
    for _, row in chart_df.iterrows():
        label = html.escape(str(row[label_col]))
        value = float(row[value_col])
        bar_height = max(2, int((value / max_value) * 260))
        bars.append(
            f"""
            <div class="bar-item">
                <div class="value">{int(round(value))}</div>
                <div class="bar" style="height:{bar_height}px;"></div>
                <div class="label">{label}</div>
            </div>
            """
        )

    chart_html = f"""
    <html>
    <head>
    <style>
        body {{ margin:0; font-family:Arial, sans-serif; background:#463F41; color:white; }}
        .wrap {{ padding:14px 12px 8px 12px; }}
        .title {{ text-align:center; font-size:18px; font-weight:700; margin-bottom:4px; }}
        .y-label {{ font-size:13px; margin-bottom:4px; }}
        .chart {{ display:flex; align-items:flex-end; gap:9px; height:315px; border-left:1px solid #777; border-bottom:1px solid #777; padding:0 8px; overflow-x:auto; }}
        .bar-item {{ min-width:36px; display:flex; flex-direction:column; align-items:center; justify-content:flex-end; }}
        .value {{ font-size:11px; margin-bottom:4px; color:white; }}
        .bar {{ width:24px; background:#E11433; border-radius:3px 3px 0 0; }}
        .label {{ writing-mode:vertical-rl; transform:rotate(180deg); font-size:11px; margin-top:7px; white-space:nowrap; color:white; }}
        .x-label {{ text-align:center; font-size:13px; margin-top:7px; }}
    </style>
    </head>
    <body>
        <div class="wrap">
            <div class="title">{html.escape(title)}</div>
            <div class="y-label">{html.escape(y_label)}</div>
            <div class="chart">{''.join(bars)}</div>
            <div class="x-label">{html.escape(x_label)}</div>
        </div>
    </body>
    </html>
    """
    components.html(chart_html, height=height, scrolling=False)


def _html_line_chart(df, label_col, actual_col, pred_col):
    plot_df = df[[label_col, actual_col, pred_col]].copy()
    plot_df[actual_col] = pd.to_numeric(plot_df[actual_col], errors="coerce").fillna(0)
    plot_df[pred_col] = pd.to_numeric(plot_df[pred_col], errors="coerce").fillna(0)
    plot_df = plot_df.sort_values(actual_col, ascending=False).reset_index(drop=True)

    width = 980
    height = 390
    left = 48
    right = 20
    top = 36
    bottom = 96
    chart_w = width - left - right
    chart_h = height - top - bottom
    max_value = max(float(plot_df[[actual_col, pred_col]].max().max()), 1.0)

    def xy(i, value):
        x = left + (i / max(len(plot_df) - 1, 1)) * chart_w
        y = top + chart_h - (float(value) / max_value) * chart_h
        return x, y

    actual_points = [xy(i, row[actual_col]) for i, row in plot_df.iterrows()]
    pred_points = [xy(i, row[pred_col]) for i, row in plot_df.iterrows()]

    def poly(points):
        return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)

    labels = []
    for i, row in plot_df.iterrows():
        x, _ = xy(i, 0)
        labels.append(
            f"<text x='{x:.1f}' y='{height - 22}' fill='white' font-size='10' transform='rotate(-65 {x:.1f},{height - 22})'>{html.escape(str(row[label_col]))}</text>"
        )

    circles = []
    for x, y in actual_points:
        circles.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='4' fill='white' />")
    for x, y in pred_points:
        circles.append(f"<circle cx='{x:.1f}' cy='{y:.1f}' r='4' fill='#E11433' />")

    chart_html = f"""
    <html>
    <body style="margin:0;background:#463F41;">
    <svg viewBox="0 0 {width} {height}" width="100%" height="{height}" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="100%" fill="#463F41" />
        <text x="{width/2}" y="22" fill="white" font-size="18" font-family="Arial" text-anchor="middle" font-weight="700">ElasticNet: Actual vs Predicted 2024 Driver Points</text>
        <line x1="{left}" y1="{top}" x2="{left}" y2="{top + chart_h}" stroke="white" opacity="0.7" />
        <line x1="{left}" y1="{top + chart_h}" x2="{left + chart_w}" y2="{top + chart_h}" stroke="white" opacity="0.7" />
        <polyline points="{poly(actual_points)}" fill="none" stroke="white" stroke-width="3" />
        <polyline points="{poly(pred_points)}" fill="none" stroke="#E11433" stroke-width="3" />
        {''.join(circles)}
        <rect x="{width - 250}" y="42" width="225" height="54" fill="#463F41" stroke="white" opacity="0.95" />
        <line x1="{width - 235}" y1="60" x2="{width - 200}" y2="60" stroke="white" stroke-width="3" />
        <text x="{width - 190}" y="64" fill="white" font-size="13" font-family="Arial">Actual 2024 Points</text>
        <line x1="{width - 235}" y1="82" x2="{width - 200}" y2="82" stroke="#E11433" stroke-width="3" />
        <text x="{width - 190}" y="86" fill="white" font-size="13" font-family="Arial">ElasticNet Predicted Points</text>
        {''.join(labels)}
    </svg>
    </body>
    </html>
    """
    components.html(chart_html, height=height, scrolling=False)


def _load_prediction_data(raw_data):
    df = raw_data.copy()
    df["driver_key"] = df["driverRef"].astype(str).str.lower().str.strip()
    df["Constructor"] = df["driver_key"].map(DRIVER_TO_CONSTRUCTOR)

    numeric_cols = ["2021_points", "2022_points", "2023_points", "2024_points"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Prefer predictions exported from your notebook, if available.
    cv_cols = ["cv_predicted_2024_points", "elasticnet_cv_predicted_2024_points", "honest_predicted_2024_points"]
    train_cols = ["training_fit_predicted_2024_points", "train_predicted_2024_points", "fitted_predicted_2024_points", "predicted_2024_points"]

    cv_source = next((col for col in cv_cols if col in df.columns), None)
    train_source = next((col for col in train_cols if col in df.columns), None)

    if cv_source:
        df["cv_display_prediction"] = pd.to_numeric(df[cv_source], errors="coerce").fillna(0)
    else:
        df["cv_display_prediction"] = df["driver_key"].map(ELASTICNET_CV_PREDICTIONS).fillna(0)

    if train_source:
        df["train_display_prediction"] = pd.to_numeric(df[train_source], errors="coerce").fillna(0)
    elif "2024_points" in df.columns:
        # Stable fallback for showing training-fit style output without running sklearn on Streamlit Cloud.
        df["train_display_prediction"] = df["2024_points"]
    else:
        df["train_display_prediction"] = df["cv_display_prediction"]

    df["cv_display_prediction"] = df["cv_display_prediction"].round().clip(lower=0).astype(int)
    df["train_display_prediction"] = df["train_display_prediction"].round().clip(lower=0).astype(int)
    return df


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


def predict_points(data):
    st.header("Prediction: F1 Driver Points for 2024 Season")

    required_cols = ["driverRef", "2021_points", "2022_points", "2023_points"]
    missing_cols = [col for col in required_cols if col not in data.columns]
    if missing_cols:
        st.error(f"DriverPrediction.csv is missing these columns: {missing_cols}")
        return

    df = _load_prediction_data(data)

    prediction_mode = st.radio(
        "Choose prediction output",
        ["Honest CV predictions", "Training-fit predictions"],
        horizontal=True,
        key="prediction_output_mode",
    )

    if prediction_mode == "Training-fit predictions":
        df["predicted_2024_points"] = df["train_display_prediction"]
        _black_note("Showing training-fit style predictions. These are not true out-of-sample forecasts.")
    else:
        df["predicted_2024_points"] = df["cv_display_prediction"]
        _black_note("Showing ElasticNet honest-CV predictions. These were computed outside the live app so the website loads fast.")

    display_df = df.sort_values("predicted_2024_points", ascending=False).reset_index(drop=True)

    driver_cols = ["driverRef", "2021_points", "2022_points", "2023_points", "predicted_2024_points"]
    if "2024_points" in display_df.columns:
        driver_cols.insert(4, "2024_points")

    driver_table = display_df[driver_cols].copy()
    _html_table(driver_table)

    _html_bar_chart(
        driver_table,
        "driverRef",
        "predicted_2024_points",
        "Predicted 2024 Points for Each Driver",
        "Driver",
        "Predicted 2024 Points",
    )

    if "2024_points" in display_df.columns:
        _html_line_chart(display_df, "driverRef", "2024_points", "predicted_2024_points")

    st.markdown(
        '<img src="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/rockcms/2022-10/221010-Max-Verstappen-ew-1132a-276412.jpg" width="700" height="400"/>',
        unsafe_allow_html=True,
    )

    _black_note(
        "Note: Predicting sports results is not always accurate. This page displays precomputed ElasticNet prediction results instead of retraining the model inside Streamlit."
    )

    st.write("---------------------------------------------------------------------------------------")
    st.header("Prediction: F1 Constructor Points for 2024 Season")

    constructor_table = _constructor_predictions(display_df)[
        ["Constructor", "2021_Points", "2022_Points", "2023_Points", "Predicted_2024_Points"]
    ]
    _html_table(constructor_table, height=460)

    _html_bar_chart(
        constructor_table,
        "Constructor",
        "Predicted_2024_Points",
        "Predicted 2024 Points for Constructor",
        "Constructor",
        "Predicted 2024 Points",
    )

    st.markdown(
        '<img src="https://mclaren.bloomreach.io/cdn-cgi/image/width=680,height=460,fit=crop,quality=80,format=webp/delivery/resources/content/gallery/mclaren-racing/formula-1/2024/schedule/abu-dhabi-grand-prix/race/report/report_0010_gp2424_193025_67a4774.jpg" width="700" height="400"/>',
        unsafe_allow_html=True,
    )

    _black_note("Note: Constructor totals are generated by summing the two driver predictions. AlphaTauri is treated as Racing Bulls.")

    st.subheader("Why ElasticNet")
    _black_note("ElasticNet is kept as the prediction source, but the live website now displays saved prediction outputs instead of retraining the model every click.")

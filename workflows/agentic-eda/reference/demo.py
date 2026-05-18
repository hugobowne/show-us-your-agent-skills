# /// script
# dependencies = [
#     "anywidget==0.11.0",
#     "marimo",
#     "plotly==6.7.0",
#     "polars==1.40.1",
#     "scipy==1.17.1",
# ]
# requires-python = ">=3.13"
# ///

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def imports():
    import marimo as mo
    import polars as pl
    import plotly.graph_objects as go
    import anywidget
    import traitlets
    from pathlib import Path

    return Path, anywidget, go, mo, pl, traitlets


@app.cell(hide_code=True)
def header(mo):
    mo.md("""
    # Protein Engineering Data Analysis

    This notebook analyzes an imine reductase (IRED) enzyme engineering dataset from Novartis.
    We load two datasets:

    - **Activity data** (`002.csv`) — enzyme activity measurements for single-site mutations
    - **Chirality data** (`003.csv`) — enantiomeric excess (stereoselectivity) for combinatorial variants
    """)
    return


@app.cell(hide_code=True)
def load_data(Path, mo, pl):
    data_dir = Path("data/ired-novartis")

    activity_df = pl.read_csv(data_dir / "cs1c02786_si_002.csv")
    chirality_df = pl.read_csv(data_dir / "cs1c02786_si_003.csv")

    mo.md(f"""## Data loaded

    - **Activity**: {activity_df.shape[0]:,} rows x {activity_df.shape[1]} columns
    - **Chirality**: {chirality_df.shape[0]:,} rows x {chirality_df.shape[1]} columns""")
    return activity_df, chirality_df


@app.cell(hide_code=True)
def activity_label(mo):
    mo.md("""
    ### Activity Data (enzyme activity measurements)
    """)
    return


@app.cell(hide_code=True)
def show_activity(activity_df):
    activity_df
    return


@app.cell(hide_code=True)
def chirality_label(mo):
    mo.md("""
    ### Chirality Data (enantiomeric excess)
    """)
    return


@app.cell(hide_code=True)
def show_chirality(chirality_df):
    chirality_df
    return


@app.cell(hide_code=True)
def heatmap_header(mo):
    mo.md("""
    ## Single-Point Mutation Heatmap
    """)
    return


@app.cell(hide_code=True)
def heatmap_dropdown(mo):
    dataset_dropdown = mo.ui.dropdown(
        options={
            "Activity (mean)": "activity",
            "Chirality (enantiomeric excess)": "chirality",
        },
        value="Activity (mean)",
        label="Select dataset",
    )
    dataset_dropdown
    return (dataset_dropdown,)


@app.cell(hide_code=True)
def colormap_note(mo):
    mo.md("""
    **Colormap choices:**

    - **Activity** uses the *Viridis* sequential colormap — activity values are non-negative, so a sequential scale faithfully represents magnitude.
    - **Chirality** uses a *RdBu* diverging colormap centered at 0 — enantiomeric excess ranges from −1 to +1, where sign indicates which enantiomer dominates.
    """)
    return


@app.cell(hide_code=True)
def heatmap_plot(activity_df, chirality_df, dataset_dropdown, go, mo, pl):
    import re


    def parse_single_mutations(df, value_col):
        single = df.filter(~pl.col("mutation").str.contains(";"))

        parsed = single.with_columns(
            [
                pl.col("mutation")
                .str.extract(r"([A-Z])(\d+)([A-Z])", 1)
                .alias("original_aa"),
                pl.col("mutation")
                .str.extract(r"([A-Z])(\d+)([A-Z])", 2)
                .cast(pl.Int64)
                .alias("position"),
                pl.col("mutation")
                .str.extract(r"([A-Z])(\d+)([A-Z])", 3)
                .alias("mutant_aa"),
            ]
        ).select(["position", "mutant_aa", "original_aa", value_col])

        return parsed


    choice = dataset_dropdown.value

    if choice == "activity":
        parsed = parse_single_mutations(activity_df, "mean")
        value_col = "mean"
        title = "Enzyme Activity (mean)"
        colorbar_title = "Mean Activity"
        colorscale = "Viridis"
        zmid = None
    else:
        parsed = parse_single_mutations(chirality_df, "r_enantiomeric_excess")
        value_col = "r_enantiomeric_excess"
        title = "Enzyme Chirality (R enantiomeric excess)"
        colorbar_title = "R ee"
        colorscale = "RdBu"
        zmid = 0

    aa_order = list("ACDEFGHIKLMNPQRSTVWY")

    pivot = parsed.pivot(
        on="mutant_aa",
        index="position",
        values=value_col,
        aggregate_function="mean",
    ).sort("position")

    positions = pivot["position"].to_list()
    present_aas = [c for c in aa_order if c in pivot.columns]
    z = []
    for aa in present_aas:
        z.append(pivot[aa].to_list())

    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=[str(p) for p in positions],
            y=present_aas,
            colorscale=colorscale,
            zmid=zmid,
            colorbar=dict(title=colorbar_title),
            hovertemplate="Position: %{x}<br>Amino Acid: %{y}<br>Value: %{z:.4f}<extra></extra>",
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title="Position",
        yaxis_title="Mutant Amino Acid",
        height=500,
        xaxis=dict(dtick=5),
    )

    mo.ui.plotly(fig)
    return


@app.cell(hide_code=True)
def scatter_header(mo):
    mo.md("""
    ## Activity vs Chirality Correlation

    Scatter plot of single-point mutants measured in **both** assays, showing whether higher activity tends to coincide with a particular stereochemical preference.
    """)
    return


@app.cell(hide_code=True)
def scatter_plot(activity_df, chirality_df, go, mo, pl):
    activity_single = activity_df.filter(
        ~pl.col("mutation").str.contains(";")
    ).select(["mutation", "mean"])

    chirality_single = chirality_df.filter(
        ~pl.col("mutation").str.contains(";")
    ).select(["mutation", "r_enantiomeric_excess"])

    joined_df = activity_single.join(chirality_single, on="mutation", how="inner")

    scatter_fig = go.Figure(
        data=go.Scatter(
            x=joined_df["mean"].to_list(),
            y=joined_df["r_enantiomeric_excess"].to_list(),
            mode="markers",
            text=joined_df["mutation"].to_list(),
            hovertemplate="Mutation: %{text}<br>Activity: %{x:.4f}<br>R ee: %{y:.4f}<extra></extra>",
            marker=dict(size=8, opacity=0.7),
        )
    )

    scatter_fig.update_layout(
        title=f"Activity vs Chirality ({joined_df.shape[0]} shared single-point mutants)",
        xaxis_title="Activity (mean)",
        yaxis_title="R Enantiomeric Excess",
        height=500,
    )

    mo.ui.plotly(scatter_fig)
    return (joined_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Noting that there's not a big correlation between chirality and activity. NTS: what's the correlation?
    """)
    return


@app.cell(hide_code=True)
def lineplot_header(mo):
    mo.md("""
    ## Per-Position Mutational Effect

    Summarize the mutational landscape by position: which residue positions are most amenable to mutation? Toggle between mean and maximum effect, and between the activity and chirality assays.
    """)
    return


@app.cell(hide_code=True)
def lineplot_controls(mo):
    line_dataset_dropdown = mo.ui.dropdown(
        options={
            "Activity (mean)": "activity",
            "Chirality (enantiomeric excess)": "chirality",
        },
        value="Activity (mean)",
        label="Dataset",
    )
    line_agg_dropdown = mo.ui.dropdown(
        options={
            "Mean across mutations": "mean",
            "Maximum across mutations": "max",
        },
        value="Mean across mutations",
        label="Aggregation",
    )
    mo.hstack([line_dataset_dropdown, line_agg_dropdown])
    return line_agg_dropdown, line_dataset_dropdown


@app.cell(hide_code=True)
def lineplot(
    activity_df,
    chirality_df,
    go,
    line_agg_dropdown,
    line_dataset_dropdown,
    mo,
    pl,
):
    line_choice = line_dataset_dropdown.value
    line_agg = line_agg_dropdown.value

    if line_choice == "activity":
        line_source_df = activity_df
        line_value_col = "mean"
        line_ylabel = "Activity (mean)"
    else:
        line_source_df = chirality_df
        line_value_col = "r_enantiomeric_excess"
        line_ylabel = "R Enantiomeric Excess"

    line_single = line_source_df.filter(~pl.col("mutation").str.contains(";"))
    line_parsed = line_single.with_columns(
        [
            pl.col("mutation")
            .str.extract(r"([A-Z])(\d+)([A-Z])", 2)
            .cast(pl.Int64)
            .alias("position"),
        ]
    )

    if line_agg == "mean":
        pos_summary = (
            line_parsed.group_by("position")
            .agg(pl.col(line_value_col).mean().alias("value"))
            .sort("position")
        )
        agg_label = "Mean"
    else:
        pos_summary = (
            line_parsed.group_by("position")
            .agg(pl.col(line_value_col).max().alias("value"))
            .sort("position")
        )
        agg_label = "Max"

    line_fig = go.Figure(
        data=go.Scatter(
            x=pos_summary["position"].to_list(),
            y=pos_summary["value"].to_list(),
            mode="lines+markers",
            marker=dict(size=5),
            hovertemplate="Position: %{x}<br>"
            + agg_label
            + " "
            + line_ylabel
            + ": %{y:.4f}<extra></extra>",
        )
    )

    line_fig.update_layout(
        title=f"{agg_label} Mutational Effect per Position — {line_ylabel}",
        xaxis_title="Position",
        yaxis_title=f"{agg_label} {line_ylabel}",
        height=450,
    )

    mo.ui.plotly(line_fig)
    return


@app.cell(hide_code=True)
def structure_header(mo):
    mo.md("""
    ## Protein Structure Viewer

    Co-crystal structure of the IRED enzyme (PDB: 7OG3) with the NDP cofactor. Protein chains A and B shown as ribbon; substrate/cofactor shown as ball-and-stick. Waters are hidden.
    """)
    return


@app.cell(hide_code=True)
def viewer_widget_class(anywidget, traitlets):
    _VIEWER_ESM = """
    import $3Dmol from "https://esm.sh/3dmol@2?bundle";

    function render({ model, el }) {
      const container = document.createElement("div");
      container.style.cssText = "width:100%;height:500px;position:relative;";
      el.appendChild(container);

      const viewer = $3Dmol.createViewer(container, {
        backgroundColor: "white",
      });

      const pdbData = model.get("pdb_data");
      const residueColors = model.get("residue_colors");
      const unmappedColor = 0xb0b0b0;

      viewer.addModel(pdbData, "pdb");

      viewer.setStyle({}, {});

      const hasColors = residueColors && Object.keys(residueColors).length > 0;

      if (hasColors) {
        viewer.setStyle(
          { hetflag: false },
          {
            cartoon: {
              colorfunc: (atom) => {
                const hex = residueColors[String(atom.resi)];
                if (hex) return parseInt(hex.replace("#", ""), 16);
                return unmappedColor;
              },
            },
          }
        );
      } else {
        viewer.setStyle({ hetflag: false }, { cartoon: { color: "spectrum" } });
      }

      viewer.setStyle(
        { hetflag: true, resn: ["NDP", "NA"] },
        { stick: { radius: 0.2 }, sphere: { scale: 0.3 } }
      );

      viewer.zoomTo();
      viewer.render();

      return () => {
        viewer.clear();
        container.remove();
      };
    }

    export default { render };
    """


    class ProteinViewer(anywidget.AnyWidget):
        pdb_data = traitlets.Unicode("").tag(sync=True)
        residue_colors = traitlets.Dict({}).tag(sync=True)
        _esm = _VIEWER_ESM

    return (ProteinViewer,)


@app.cell(hide_code=True)
def show_structure(
    Path,
    ProteinViewer,
    activity_df,
    chirality_df,
    line_agg_dropdown,
    line_dataset_dropdown,
    pl,
):
    import plotly.colors as pc
    import re as _re

    struct_choice = line_dataset_dropdown.value
    struct_agg = line_agg_dropdown.value

    if struct_choice == "activity":
        struct_src = activity_df
        struct_vcol = "mean"
        struct_cscale = "Viridis"
    else:
        struct_src = chirality_df
        struct_vcol = "r_enantiomeric_excess"
        struct_cscale = "RdBu"

    struct_single = struct_src.filter(~pl.col("mutation").str.contains(";"))
    struct_parsed = struct_single.with_columns(
        pl.col("mutation")
        .str.extract(r"([A-Z])(\d+)([A-Z])", 2)
        .cast(pl.Int64)
        .alias("position"),
    )

    if struct_agg == "mean":
        struct_pos = (
            struct_parsed.group_by("position")
            .agg(pl.col(struct_vcol).mean().alias("value"))
            .sort("position")
        )
    else:
        struct_pos = (
            struct_parsed.group_by("position")
            .agg(pl.col(struct_vcol).max().alias("value"))
            .sort("position")
        )

    positions_list = struct_pos["position"].to_list()
    values_list = struct_pos["value"].to_list()

    if struct_cscale == "RdBu":
        vabs = max(abs(min(values_list)), abs(max(values_list)))
        vmin, vmax = -vabs, vabs
    else:
        vmin, vmax = min(values_list), max(values_list)

    normed = [
        (v - vmin) / (vmax - vmin) if vmax > vmin else 0.5 for v in values_list
    ]
    rgb_strings = pc.sample_colorscale(struct_cscale, normed)


    def rgb_to_hex(rgb_str):
        nums = [int(x) for x in _re.findall(r"\d+", rgb_str)]
        return f"#{nums[0]:02x}{nums[1]:02x}{nums[2]:02x}"


    color_map = {
        str(p): rgb_to_hex(c) for p, c in zip(positions_list, rgb_strings)
    }

    pdb_text = Path("data/ired-novartis/7OG3.pdb").read_text()
    structure_viewer = ProteinViewer(pdb_data=pdb_text, residue_colors=color_map)
    structure_viewer
    return


@app.cell(hide_code=True)
def compute_correlation(joined_df):
    from scipy import stats as _stats

    _corr_result = _stats.pearsonr(
        joined_df["mean"].to_list(),
        joined_df["r_enantiomeric_excess"].to_list(),
    )
    _spearman_result = _stats.spearmanr(
        joined_df["mean"].to_list(),
        joined_df["r_enantiomeric_excess"].to_list(),
    )
    correlation_pearson_r = _corr_result.statistic
    correlation_pearson_p = _corr_result.pvalue
    correlation_spearman_rho = _spearman_result.statistic
    correlation_spearman_p = _spearman_result.pvalue
    n_shared = joined_df.shape[0]
    return (
        correlation_pearson_p,
        correlation_pearson_r,
        correlation_spearman_p,
        correlation_spearman_rho,
        n_shared,
    )


@app.cell(hide_code=True)
def summary(
    correlation_pearson_p,
    correlation_pearson_r,
    correlation_spearman_p,
    correlation_spearman_rho,
    mo,
    n_shared,
):
    mo.md(f"""
    ## Summary

    ### Structural observations

    Mutated positions cluster at the **interface between the two protein chains** (A and B).
    This is consistent with the dimer interface playing a functional role
    in shaping the active-site geometry — mutations here can modulate
    both catalytic activity and stereoselectivity without directly contacting the substrate.

    ### Correlation between activity and chirality

    Among the **{n_shared} single-point mutants** measured in both assays,
    enzyme activity and enantiomeric excess show **weak and largely non-significant linear correlation**:

    | Metric | Value | *p*-value |
    |--------|-------|-----------|
    | Pearson *r* | {correlation_pearson_r:.3f} | {correlation_pearson_p:.3e} |
    | Spearman *ρ* | {correlation_spearman_rho:.3f} | {correlation_spearman_p:.3e} |

    The Pearson correlation (*r* = {correlation_pearson_r:.3f}, *p* = {correlation_pearson_p:.2f})
    is not statistically significant at the 0.05 level,
    indicating that a mutation's effect on **how much** product is formed
    is largely independent of **which enantiomer** it favors.
    The Spearman rank correlation is modest (*ρ* = {correlation_spearman_rho:.3f})
    and reaches significance, suggesting a weak monotonic trend,
    but the effect size remains small.

    **Practical implication:** activity and chirality can, to a first approximation,
    be engineered independently — a useful property for multi-objective protein engineering campaigns.
    """)
    return


if __name__ == "__main__":
    app.run()

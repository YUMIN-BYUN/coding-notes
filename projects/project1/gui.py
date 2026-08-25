import ctypes
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from src.analysis import run_fit

from src.result_formatter import (
    format_quick_result,
    format_detail_result,
)

from src.plotting import (
    plot_raw_data,
    plot_fit,
    plot_residuals,
)

from src.models import (
    linear_model,
    polynomial_model,
    exponential_model,
    sinusoidal_model,
    gaussian_model,
)

from src.fitting import create_custom_model

from src.result_io import (
    save_result_csv,
    save_result_json,
    save_figure,
)


# =========================================================
# Windows High-DPI Support
# =========================================================

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass


class FittingApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Experimental Data Fitting Tool"
        )

        self.root.geometry(
            "1400x900"
        )

        self.root.minsize(
            1100,
            700
        )

        # Loaded data
        self.data = None
        self.file_path = None

        # Latest fitting result
        self.result = None

        # Figures
        self.raw_figure = None
        self.fit_figure = None
        self.residual_figure = None

        # Canvases
        self.raw_canvas = None
        self.fit_canvas = None
        self.residual_canvas = None

        self.create_widgets()


    # =====================================================
    # GUI Construction
    # =====================================================

    def create_widgets(self):

        main_frame = ttk.Frame(
            self.root
        )

        main_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        main_frame.columnconfigure(
            0,
            weight=1
        )

        main_frame.columnconfigure(
            1,
            weight=2
        )

        main_frame.rowconfigure(
            0,
            weight=1
        )


        # =================================================
        # LEFT PANEL
        # =================================================

        left_frame = ttk.Frame(
            main_frame
        )

        left_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 5)
        )


        # =================================================
        # Data File
        # =================================================

        file_frame = ttk.LabelFrame(
            left_frame,
            text="Data File"
        )

        file_frame.pack(
            fill="x",
            pady=5
        )

        self.file_path_var = tk.StringVar()

        ttk.Entry(
            file_frame,
            textvariable=self.file_path_var
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=5,
            pady=5
        )

        ttk.Button(
            file_frame,
            text="Browse",
            command=self.browse_csv
        ).pack(
            side="right",
            padx=5,
            pady=5
        )


        # =================================================
        # Columns
        # =================================================

        column_frame = ttk.LabelFrame(
            left_frame,
            text="Columns"
        )

        column_frame.pack(
            fill="x",
            pady=5
        )

        column_frame.columnconfigure(
            1,
            weight=1
        )


        ttk.Label(
            column_frame,
            text="X Column"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.x_column_var = tk.StringVar()

        self.x_column_combo = ttk.Combobox(
            column_frame,
            textvariable=self.x_column_var,
            state="readonly"
        )

        self.x_column_combo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        ttk.Label(
            column_frame,
            text="Y Column"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.y_column_var = tk.StringVar()

        self.y_column_combo = ttk.Combobox(
            column_frame,
            textvariable=self.y_column_var,
            state="readonly"
        )

        self.y_column_combo.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        ttk.Label(
            column_frame,
            text="Y Uncertainty"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.yerr_column_var = tk.StringVar(
            value="None"
        )

        self.yerr_column_combo = ttk.Combobox(
            column_frame,
            textvariable=self.yerr_column_var,
            state="readonly"
        )

        self.yerr_column_combo.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        # =================================================
        # Axis Settings
        # =================================================

        axis_frame = ttk.LabelFrame(
            left_frame,
            text="Axis Settings"
        )

        axis_frame.pack(
            fill="x",
            pady=5
        )

        axis_frame.columnconfigure(
            1,
            weight=1
        )

        axis_frame.columnconfigure(
            3,
            weight=1
        )


        self.x_label_var = tk.StringVar(
            value="x"
        )

        self.x_unit_var = tk.StringVar()

        self.y_label_var = tk.StringVar(
            value="y"
        )

        self.y_unit_var = tk.StringVar()

        self.x_scale_var = tk.StringVar(
            value="linear"
        )

        self.y_scale_var = tk.StringVar(
            value="linear"
        )


        ttk.Label(
            axis_frame,
            text="X Label"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        ttk.Entry(
            axis_frame,
            textvariable=self.x_label_var
        ).grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        ttk.Label(
            axis_frame,
            text="Unit"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        ttk.Entry(
            axis_frame,
            textvariable=self.x_unit_var
        ).grid(
            row=0,
            column=3,
            padx=5,
            pady=5,
            sticky="ew"
        )


        ttk.Label(
            axis_frame,
            text="Y Label"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        ttk.Entry(
            axis_frame,
            textvariable=self.y_label_var
        ).grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        ttk.Label(
            axis_frame,
            text="Unit"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        ttk.Entry(
            axis_frame,
            textvariable=self.y_unit_var
        ).grid(
            row=1,
            column=3,
            padx=5,
            pady=5,
            sticky="ew"
        )


        ttk.Label(
            axis_frame,
            text="X Scale"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        ttk.Combobox(
            axis_frame,
            textvariable=self.x_scale_var,
            values=[
                "linear",
                "log"
            ],
            state="readonly"
        ).grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        ttk.Label(
            axis_frame,
            text="Y Scale"
        ).grid(
            row=2,
            column=2,
            padx=5,
            pady=5
        )

        ttk.Combobox(
            axis_frame,
            textvariable=self.y_scale_var,
            values=[
                "linear",
                "log"
            ],
            state="readonly"
        ).grid(
            row=2,
            column=3,
            padx=5,
            pady=5,
            sticky="ew"
        )


        ttk.Button(
            axis_frame,
            text="Preview Raw Data",
            command=self.preview_raw_data
        ).grid(
            row=3,
            column=0,
            columnspan=4,
            padx=5,
            pady=8
        )


        # =================================================
        # Model Settings
        # =================================================

        model_frame = ttk.LabelFrame(
            left_frame,
            text="Model Settings"
        )

        model_frame.pack(
            fill="x",
            pady=5
        )

        model_frame.columnconfigure(
            1,
            weight=1
        )


        self.model_var = tk.StringVar(
            value="Linear"
        )

        ttk.Label(
            model_frame,
            text="Model"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.model_combo = ttk.Combobox(
            model_frame,
            textvariable=self.model_var,
            values=[
                "Linear",
                "Polynomial",
                "Exponential",
                "Sinusoidal",
                "Gaussian",
                "Custom"
            ],
            state="readonly"
        )

        self.model_combo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )

        self.model_combo.bind(
            "<<ComboboxSelected>>",
            self.update_model_inputs
        )


        # Polynomial degree
        self.degree_var = tk.StringVar(
            value="2"
        )

        ttk.Label(
            model_frame,
            text="Degree"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.degree_entry = ttk.Entry(
            model_frame,
            textvariable=self.degree_var
        )

        self.degree_entry.grid(
            row=1,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        # Initial guess mode
        self.initial_guess_mode_var = tk.StringVar(
            value="Auto"
        )

        ttk.Label(
            model_frame,
            text="Initial Guess"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.initial_guess_mode_combo = ttk.Combobox(
            model_frame,
            textvariable=self.initial_guess_mode_var,
            values=[
                "Auto",
                "Manual"
            ],
            state="readonly"
        )

        self.initial_guess_mode_combo.grid(
            row=2,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )

        self.initial_guess_mode_combo.bind(
            "<<ComboboxSelected>>",
            self.update_model_inputs
        )


        # Guess values
        self.initial_guess_var = tk.StringVar()

        ttk.Label(
            model_frame,
            text="Guess Values"
        ).grid(
            row=3,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.initial_guess_entry = ttk.Entry(
            model_frame,
            textvariable=self.initial_guess_var
        )

        self.initial_guess_entry.grid(
            row=3,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        # Custom expression
        self.custom_expression_var = tk.StringVar()

        ttk.Label(
            model_frame,
            text="Expression"
        ).grid(
            row=4,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.custom_expression_entry = ttk.Entry(
            model_frame,
            textvariable=self.custom_expression_var
        )

        self.custom_expression_entry.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        # Custom parameter names
        self.custom_parameter_names_var = tk.StringVar()

        ttk.Label(
            model_frame,
            text="Parameters"
        ).grid(
            row=5,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )

        self.custom_parameter_names_entry = ttk.Entry(
            model_frame,
            textvariable=self.custom_parameter_names_var
        )

        self.custom_parameter_names_entry.grid(
            row=5,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        # Result mode
        self.result_mode_var = tk.StringVar(
            value="Quick"
        )

        ttk.Label(
            model_frame,
            text="Result Mode"
        ).grid(
            row=6,
            column=0,
            padx=5,
            pady=5
        )

        ttk.Combobox(
            model_frame,
            textvariable=self.result_mode_var,
            values=[
                "Quick",
                "Detail"
            ],
            state="readonly"
        ).grid(
            row=6,
            column=1,
            padx=5,
            pady=5,
            sticky="ew"
        )


        # =================================================
        # FIT / SAVE BUTTONS
        # =================================================

        button_frame = ttk.Frame(
            left_frame
        )

        button_frame.pack(
            fill="x",
            pady=8
        )

        button_frame.columnconfigure(
            0,
            weight=1
        )

        button_frame.columnconfigure(
            1,
            weight=1
        )


        ttk.Button(
            button_frame,
            text="FIT",
            command=self.run_analysis
        ).grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 3),
            ipady=6
        )


        ttk.Button(
            button_frame,
            text="Save Results",
            command=self.save_results
        ).grid(
            row=0,
            column=1,
            sticky="ew",
            padx=(3, 0),
            ipady=6
        )


        # =================================================
        # Results
        # =================================================

        result_frame = ttk.LabelFrame(
            left_frame,
            text="Results"
        )

        result_frame.pack(
            fill="both",
            expand=True,
            pady=5
        )

        self.result_text = tk.Text(
            result_frame,
            height=12,
            wrap="word"
        )

        self.result_text.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )


        # =================================================
        # RIGHT PANEL
        # =================================================

        right_frame = ttk.Frame(
            main_frame
        )

        right_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(5, 0)
        )


        self.plot_notebook = ttk.Notebook(
            right_frame
        )

        self.plot_notebook.pack(
            fill="both",
            expand=True
        )


        self.raw_tab = ttk.Frame(
            self.plot_notebook
        )

        self.plot_notebook.add(
            self.raw_tab,
            text="Raw Data"
        )


        self.fit_tab = ttk.Frame(
            self.plot_notebook
        )

        self.plot_notebook.add(
            self.fit_tab,
            text="Fit"
        )


        self.residual_tab = ttk.Frame(
            self.plot_notebook
        )

        self.plot_notebook.add(
            self.residual_tab,
            text="Residual"
        )


        self.update_model_inputs()


    # =====================================================
    # Model UI State
    # =====================================================

    def update_model_inputs(self, event=None):

        model = self.model_var.get()

        self.degree_entry.configure(
            state="disabled"
        )

        self.initial_guess_mode_combo.configure(
            state="disabled"
        )

        self.initial_guess_entry.configure(
            state="disabled"
        )

        self.custom_expression_entry.configure(
            state="disabled"
        )

        self.custom_parameter_names_entry.configure(
            state="disabled"
        )


        if model == "Polynomial":

            self.degree_entry.configure(
                state="normal"
            )


        elif model in (
            "Exponential",
            "Sinusoidal",
            "Gaussian"
        ):

            self.initial_guess_mode_combo.configure(
                state="readonly"
            )

            if (
                self.initial_guess_mode_var.get()
                == "Manual"
            ):

                self.initial_guess_entry.configure(
                    state="normal"
                )


        elif model == "Custom":

            self.initial_guess_mode_var.set(
                "Manual"
            )

            self.initial_guess_entry.configure(
                state="normal"
            )

            self.custom_expression_entry.configure(
                state="normal"
            )

            self.custom_parameter_names_entry.configure(
                state="normal"
            )


    # =====================================================
    # CSV Loading
    # =====================================================

    def browse_csv(self):

        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ]
        )

        if not file_path:
            return

        try:

            self.data = pd.read_csv(
                file_path
            )

        except Exception as error:

            messagebox.showerror(
                "CSV Error",
                str(error)
            )

            return


        self.file_path = file_path

        self.file_path_var.set(
            file_path
        )

        columns = list(
            self.data.columns
        )

        self.x_column_combo["values"] = columns

        self.y_column_combo["values"] = columns

        self.yerr_column_combo["values"] = [
            "None",
            *columns
        ]


        if len(columns) >= 1:
            self.x_column_var.set(
                columns[0]
            )

        if len(columns) >= 2:
            self.y_column_var.set(
                columns[1]
            )

        self.yerr_column_var.set(
            "None"
        )


    # =====================================================
    # Read Selected Data
    # =====================================================

    def get_selected_data(self):

        if self.data is None:
            raise ValueError(
                "Please load a CSV file first."
            )

        x_column = self.x_column_var.get()
        y_column = self.y_column_var.get()
        yerr_column = self.yerr_column_var.get()


        x = self.data[
            x_column
        ].to_numpy(
            dtype=float
        )

        y = self.data[
            y_column
        ].to_numpy(
            dtype=float
        )


        if yerr_column == "None":
            yerr = None

        else:
            yerr = self.data[
                yerr_column
            ].to_numpy(
                dtype=float
            )


        return x, y, yerr


    # =====================================================
    # Raw Preview
    # =====================================================

    def preview_raw_data(self):

        try:

            x, y, yerr = self.get_selected_data()

            figure = plot_raw_data(
                x=x,
                y=y,
                x_label=self.x_label_var.get(),
                x_unit=self.x_unit_var.get(),
                y_label=self.y_label_var.get(),
                y_unit=self.y_unit_var.get(),
                yerr=yerr,
                x_scale=self.x_scale_var.get(),
                y_scale=self.y_scale_var.get()
            )

            self.raw_figure = figure

            self.raw_canvas = self.display_figure(
                figure,
                self.raw_tab,
                self.raw_canvas
            )

            self.plot_notebook.select(
                self.raw_tab
            )

        except Exception as error:

            messagebox.showerror(
                "Preview Error",
                str(error)
            )


    # =====================================================
    # Run Fit
    # =====================================================

    def run_analysis(self):

        try:

            x, y, yerr = self.get_selected_data()

            model = self.model_var.get().lower()

            degree = None
            initial_guess = None
            custom_expression = None
            custom_parameter_names = None


            if model == "polynomial":

                degree = int(
                    self.degree_var.get()
                )


            elif model in (
                "exponential",
                "sinusoidal",
                "gaussian"
            ):

                if (
                    self.initial_guess_mode_var.get()
                    == "Manual"
                ):

                    initial_guess = [
                        float(value.strip())
                        for value
                        in self.initial_guess_var.get().split(",")
                    ]


            elif model == "custom":

                custom_expression = (
                    self.custom_expression_var.get()
                )

                custom_parameter_names = [
                    name.strip()
                    for name
                    in self.custom_parameter_names_var.get().split(",")
                    if name.strip()
                ]

                initial_guess = [
                    float(value.strip())
                    for value
                    in self.initial_guess_var.get().split(",")
                ]


            # ---------------------------------------------
            # Core analysis
            # ---------------------------------------------

            self.result = run_fit(
                x=x,
                y=y,
                yerr=yerr,
                model=model,
                degree=degree,
                initial_guess=initial_guess,
                custom_expression=custom_expression,
                custom_parameter_names=custom_parameter_names
            )


            # Save a few GUI metadata fields
            self.result["input_file"] = self.file_path

            self.result["x_column"] = (
                self.x_column_var.get()
            )

            self.result["y_column"] = (
                self.y_column_var.get()
            )

            self.result["yerr_column"] = (
                self.yerr_column_var.get()
            )

            self.result["x_label"] = (
                self.x_label_var.get()
            )

            self.result["x_unit"] = (
                self.x_unit_var.get()
            )

            self.result["y_label"] = (
                self.y_label_var.get()
            )

            self.result["y_unit"] = (
                self.y_unit_var.get()
            )


            # ---------------------------------------------
            # Result formatter
            # ---------------------------------------------

            if self.result_mode_var.get() == "Quick":

                result_string = format_quick_result(
                    self.result
                )

            else:

                result_string = format_detail_result(
                    self.result
                )


            self.result_text.delete(
                "1.0",
                tk.END
            )

            self.result_text.insert(
                tk.END,
                result_string
            )


            # ---------------------------------------------
            # Dense fit curve
            # ---------------------------------------------

            x_fit = np.linspace(
                np.min(x),
                np.max(x),
                500
            )

            parameters = self.result[
                "parameters"
            ]


            if model == "linear":

                y_fit = linear_model(
                    x_fit,
                    *parameters
                )


            elif model == "polynomial":

                y_fit = polynomial_model(
                    x_fit,
                    parameters
                )


            elif model == "exponential":

                y_fit = exponential_model(
                    x_fit,
                    *parameters
                )


            elif model == "sinusoidal":

                y_fit = sinusoidal_model(
                    x_fit,
                    *parameters
                )


            elif model == "gaussian":

                y_fit = gaussian_model(
                    x_fit,
                    *parameters
                )


            elif model == "custom":

                custom_model = create_custom_model(
                    custom_expression,
                    custom_parameter_names
                )

                y_fit = custom_model(
                    x_fit,
                    *parameters
                )


            # ---------------------------------------------
            # Fit Plot
            # ---------------------------------------------

            fit_figure = plot_fit(
                x=x,
                y=y,
                x_fit=x_fit,
                y_fit=y_fit,
                xlabel=self.x_label_var.get(),
                xunit=self.x_unit_var.get(),
                ylabel=self.y_label_var.get(),
                yunit=self.y_unit_var.get(),
                title=f"{self.model_var.get()} Fit",
                yerr=yerr,
                x_scale=self.x_scale_var.get(),
                y_scale=self.y_scale_var.get()
            )

            self.fit_figure = fit_figure

            self.fit_canvas = self.display_figure(
                fit_figure,
                self.fit_tab,
                self.fit_canvas
            )


            # ---------------------------------------------
            # Residual Plot
            # ---------------------------------------------

            residual_figure = plot_residuals(
                x=x,
                residuals=self.result["residuals"],
                xlabel=self.x_label_var.get(),
                xunit=self.x_unit_var.get(),
                yunit=self.y_unit_var.get(),
                x_scale=self.x_scale_var.get()
            )

            self.residual_figure = residual_figure

            self.residual_canvas = self.display_figure(
                residual_figure,
                self.residual_tab,
                self.residual_canvas
            )


            self.plot_notebook.select(
                self.fit_tab
            )


        except Exception as error:

            messagebox.showerror(
                "Fit Error",
                str(error)
            )


    # =====================================================
    # Save Results
    # =====================================================

    def save_results(self):

        if self.result is None:

            messagebox.showerror(
                "Save Error",
                "Please run a fit before saving results."
            )

            return


        if (
            self.fit_figure is None
            or self.residual_figure is None
        ):

            messagebox.showerror(
                "Save Error",
                "Fit plots are not available."
            )

            return


        save_directory = filedialog.askdirectory(
            title="Select Save Directory"
        )


        if not save_directory:
            return


        try:

            csv_path = os.path.join(
                save_directory,
                "fit_result.csv"
            )

            json_path = os.path.join(
                save_directory,
                "fit_result.json"
            )

            fit_plot_path = os.path.join(
                save_directory,
                "fit_plot.png"
            )

            residual_plot_path = os.path.join(
                save_directory,
                "residual_plot.png"
            )


            save_result_csv(
                self.result,
                csv_path
            )

            save_result_json(
                self.result,
                json_path
            )

            save_figure(
                self.fit_figure,
                fit_plot_path
            )

            save_figure(
                self.residual_figure,
                residual_plot_path
            )


            messagebox.showinfo(
                "Save Complete",
                "Results saved successfully.\n\n"
                f"{save_directory}"
            )


        except Exception as error:

            messagebox.showerror(
                "Save Error",
                str(error)
            )


    # =====================================================
    # Display Figure
    # =====================================================

    def display_figure(
        self,
        figure,
        tab,
        old_canvas
    ):

        if old_canvas is not None:

            old_canvas.get_tk_widget().destroy()


        canvas = FigureCanvasTkAgg(
            figure,
            master=tab
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )

        return canvas


# =========================================================
# Main
# =========================================================

def main():

    root = tk.Tk()

    app = FittingApp(
        root
    )

    root.mainloop()


if __name__ == "__main__":
    main()
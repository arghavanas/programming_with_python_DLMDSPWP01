# ** Ideal Function Mapping with Python**
This project is a Python application designed to determine the best-fitting ideal functions for training data, map test points, and visualize the results using SQLite, Pandas, NumPy, and Bokeh. 

## **Overview**
This project follows an **object-oriented** approach to:
1. Data Loading: Reads training, ideal, and test datasets from CSV files and imports them into an SQLite database.
2. Ideal Function Determination: For each column in the training dataset, the code computes the Sum of SquaredErrors (SSE) with respect to each of the ideal function       columns and selects the ideal function with the lowest SSE.
3. Test Data Mapping: Maps each test data point to the closest ideal function based on an acceptable deviation threshold (calculated as √2 times the maximum deviation).
4. Visualization: Uses Bokeh to generate an interactive visualization that displays the ideal function curves and the corresponding test data points.

---

## ** Project Structure**
```
/project_root
│── app/                       # Application source code
│   │── main.py                # Main execution script
│   │── config.py              # Configuration settings
│   │── database.py            # SQLite database handling
│   │── datasets.py            # Training, Ideal, and Test dataset classes
│   │── visualizer.py          # Bokeh visualization module
│── data/                      # CSV files (must be present before running)
│   │── train.csv
│   │── ideal.csv
│   │── test.csv
│── output/                    # Stores the generated Bokeh visualization
│── requirements.txt           # Python dependencies
│── Dockerfile                 # Docker configuration
│── docker-compose.yml         # Docker Compose configuration
│── .dockerignore              # Files to be ignored in the Docker container
│── README.md                  # This documentation file
```

---

## ** Installation**
### **1. Clone the Repository**
```bash```
Clone the repository using the following commands:

git clone https://github.com/arghavanas/programming_with_python_DLMDSPWP01.git

cd programming_with_python_DLMDSPWP01/coding_assignment_finding_ideal_functions


### **2. Verify CSV Files**
Before running the application, make sure the CSV files are inside the **`data/`** folder:
```bash```
ls data/
```
Expected output:
```bash```
train.csv  ideal.csv  test.csv
```
If the files are missing, **add them before proceeding**.

---

## ** Running the Application**
### **Using Docker**
This application is fully containerized with **Docker**. It runs in an isolated environment where dependencies and execution are managed inside a container.

#### ** Building the Docker Image**
```bash
docker-compose build
```
This builds the container image and ensures all dependencies are installed.

#### ** Running the Application**
```bash
docker-compose up
```
This:
- Starts the container.
- Loads **training, ideal, and test datasets** into SQLite.
- Finds the **best-fitting ideal functions**.
- Maps test data points to ideal functions.
- Generates a **Bokeh visualization**.

Once the process is complete, the **output visualization** is saved in the `output/` folder.

---

## ** Accessing the Output**
### **1.Checking the Logs**
Review the logs to ensure the application is running correctly:
```bash
docker-compose logs
```

### **2.Viewing the Output File**
The visualization is saved as:
```
output/bokeh_visualization.html
```
To open it:
- **Mac:** `open output/bokeh_visualization.html`
- **Linux:** `xdg-open output/bokeh_visualization.html`
- **Windows:** `start output/bokeh_visualization.html`

---

## ** Stopping the Application**
To **stop the running container**, press:
```bash
CTRL + C
```
Or run:
```bash
docker-compose down
```

---


## **Detailed Code Explanation**
- The application loads **training, ideal, and test datasets** into an **SQLite database**.
- It finds the **best-fit ideal functions** for training columns using **Sum of Squared Errors (SSE)**.
- Test data points are mapped to their closest **ideal function** within an **acceptable deviation (√2 × max deviation)**.
- The **Bokeh visualization** is saved as `bokeh_visualization.html` and automatically opened in the browser.

---

## ** Methodology**


### **Determining the Best-Fitting Ideal Functions**
- **Approach:**  
  For each training column (e.g., \( y_1, y_2, \ldots \)), the application calculates the **Sum of Squared Errors (SSE)** with every corresponding ideal function column:
  \[
    \text{SSE} = \sum (y_{\text{train}} - y_{\text{ideal}})^2
  \]
- **Selection:**  
  The ideal function with the smallest SSE value is chosen as the best fit.

### **Mapping Test Data Points**
- **Criteria:**  
  A test point \((x, y)\) is considered a match for an ideal function if it lies within \(\sqrt{2} \times \max(\text{deviation})\).  
- **Resolution:**  
  If multiple ideal functions meet this condition, the one with the smallest deviation is selected.

### **Visualization**
- **Implementation:**  
  The application uses Bokeh to generate an interactive plot.  
  - **Ideal Functions:** Rendered as colored lines.  
  - **Test Points:** Plotted as scatter points, color-coded to match the assigned ideal function.  
- **Output:**  
  The final visualization is saved as an HTML file (`bokeh_visualization.html`) in the `output/` folder.

---

## **Detailed Code Explanation**
### ** `config.py`**
- **Purpose:**  
  Contains global configuration settings such as database connection details and threshold parameters.

- **Key Components:**  
  - **Database Connection String:** Specifies the path or URI for the SQLite database.  
  - **Deviation Thresholds:** Determines the acceptable range for mapping test data points to an ideal function.

---

### ** `database.py`**

- **Purpose:**  
  Manages interactions with the SQLite database, ensuring that CSV data is properly loaded and accessed.

- **Key Methods:**  
  - **`load_csv_to_db`**  
    Reads data from CSV files and inserts it into the SQLite database.  
  - **`fetch_data`**  
    Retrieves data from the database and converts it into a Pandas DataFrame for further processing.

- **Implementation Notes:**  
  - Uses the Python **sqlite3** module for database operations.  
  - Organizes each CSV into its own table, maintaining a clear separation of training, ideal, and test data.

---

### ** `datasets.py`**

- **Purpose:**  
  Defines classes responsible for handling the training, ideal, and test datasets.

- **Classes and Methods:**  
  1. **`TrainingDataSet`**  
     - **`find_best_fit`**:  
       Calculates the Sum of Squared Errors (SSE) between the training data and each candidate ideal function. The function with the lowest SSE is selected.  
  2. **`IdealDataSet`**  
     - Stores the collection of ideal function columns for comparison.  
  3. **`TestDataSet`**  
     - **`map_test_points`**:  
       Maps each test point to the ideal function that lies within an acceptable deviation threshold, selecting the function with the smallest error if multiple functions qualify.

- **Implementation Details:**  
  - Relies on **NumPy** for vectorized computations of SSE.  
  - Integrates closely with **database.py** to retrieve data.  
  - Keeps logic for each dataset type separate, promoting clarity and maintainability.

---

### ** `visualizer.py`**

- **Purpose:**  
  Generates visualizations using **Bokeh**, providing an interactive interface to explore ideal function curves and mapped test points.

- **Key Methods:**  
  - **`plot_ideal_functions`**  
    Plots each ideal function as a distinct line, using different colors for easy differentiation.  
  - **`plot_test_points`**  
    Displays the test data points, color-coded by the ideal function they have been mapped to.  
  - **`save_visualization`**  
    Saves the final Bokeh figure as an HTML file (`bokeh_visualization.html`) in the `output/` directory.
    
### ** `main.py`**

- **Purpose:**  
  Serves as the central entry point for the application.

- **Workflow:**  
  1. **Data Loading:**  
     Invokes methods in `database.py` to read CSV files and store them in the SQLite database.  
  2. **Best-Fit Calculation:**  
     Calls `find_best_fit` from `TrainingDataSet` to identify which ideal function aligns best with each training column.  
  3. **Test Point Mapping:**  
     Uses `map_test_points` from `TestDataSet` to link each test data point to its ideal function.  
  4. **Visualization Generation:**  
     Triggers `visualizer.py` to plot the ideal functions and the mapped test data points, saving the result to an HTML file.

- **Implementation Notes:**  
  - Coordinates the execution order of all major functions.  
  - Handles logging or console output to track the progress of each step.

---

## ** Sample Output**
After running the application, a **Bokeh plot** is generated, displaying:

✅ Ideal function lines.  
✅ Test data points mapped to their closest ideal function.

 Open `bokeh_visualization.html` in your browser to see the **visual representation**.

---

## ** License**
This project is open-source under the **MIT License**.

---

## **📧 Contact**
For any questions, feel free to reach out! 
📩 **Arghavanas89@gmail.com**  
🔗 *https://github.com/Arghavanas*






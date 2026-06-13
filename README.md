
## ✅ **README.md**

````markdown
# folder-tree

`folder-tree` is a Python CLI tool that generates a clean, tree-like visualization of any project's folder and file structure — similar to the Unix `tree` command, but with modern features and Markdown output.

It recursively scans your directory, applies exclusion or collapsing rules, and saves the output to a Markdown file.

---

## Features

- Recursively lists all folders and files
- Shows folder hierarchy using `├──`, `└──`, and `│`
- Sorts folders before files (alphabetically)
- Supports folder collapsing (`--collapse`)
- Supports hiding folders completely (`--hide`)
- Allows depth-limited traversal (`--depth`)
- Displays per-folder file/folder counts (`--show-counts`)
- Outputs both to console and a Markdown file (`structure.md` by default)

---

## Installation

### Local (development)

```bash
pip install -e .
```
````

### Once published (example)

```bash
pip install folder-tree
```

---

## Basic Usage

```bash
folder-tree
```

### Example Output

```
aws-todo/
├── backend/
│   ├── src/
│   ├── package.json
│   └── README.md
├── frontend/
│   ├── src/
│   ├── public/
│   └── README.md
└── package.json
```

The output is also saved automatically to:

```
structure.md
```

---

## Command Options

| Flag            | Description                                     | Example                        |
| --------------- | ----------------------------------------------- | ------------------------------ |
| `--collapse`    | Show folder name but don’t expand contents      | `--collapse node_modules dist` |
| `--hide`        | Completely exclude certain folders              | `--hide public cypress`        |
| `--show-counts` | Show folder/file counts beside each folder name | `--show-counts`                |
| `--depth`       | Limit how deep the recursion goes               | `--depth 2`                    |
| `--output`      | Specify output file name                        | `--output project_tree.md`     |

---

## Examples

### 1. Default run

```bash
folder-tree
```

**Output:**

```
project/
├── src/
│   ├── index.js
│   ├── utils/
│   └── App.jsx
├── package.json
└── README.md
```

---

### 2. Collapse large folders

```bash
folder-tree --collapse node_modules dist
```

**Output:**

```
project/
├── src/
│   ├── index.js
│   └── App.jsx
├── node_modules/
│   (2450 files hidden)
├── dist/
│   (132 files hidden)
└── package.json
```

---

### 3. Hide unwanted folders

```bash
folder-tree --hide public cypress
```

**Output:**

```
project/
├── src/
├── package.json
└── README.md
```

---

### 4. Show per-folder counts

```bash
folder-tree --show-counts
```

**Output:**

```
project/ (4 folders, 3 files)
├── src/ (2 folders, 5 files)
│   ├── components/ (2 folders, 3 files)
│   └── utils/ (0 folders, 2 files)
└── README.md
```

---

### 5. Limit tree depth

```bash
folder-tree --depth 2
```

**Output:**

```
project/
├── src/
│   ├── components/
│   ├── utils/
│   └── index.js
└── package.json
```

---

### 6. Combine multiple options

```bash
folder-tree --collapse node_modules dist --hide public --show-counts --depth 3 --output project_tree.md
```

**Output:**

```
project/ (5 folders, 3 files)
├── backend/ (3 folders, 4 files)
│   ├── src/ (2 folders, 3 files)
│   └── package.json
├── frontend/ (4 folders, 6 files)
├── node_modules/
│   (2450 files hidden)
└── README.md

Folder structure generated successfully!
Saved to: project_tree.md
```

---

## Example Markdown Output (structure.md)

```markdown
# Project Folder Structure

project/
├── src/
│ ├── pages/
│ ├── utils/
│ │ ├── constants.js
│ │ └── helpers.js
│ ├── App.jsx
│ └── index.js
├── package.json
└── README.md
```




## Uninstall

```bash
pip uninstall folder-tree
```

---

## License

MIT © 2025 Abhishek Hegde

---

## Contributing

Pull requests and suggestions are welcome.
If you find a bug or have a feature idea, feel free to open an issue or PR.

---

## Quick Reference

| Use Case           | Command                                    | Description                   |
| ------------------ | ------------------------------------------ | ----------------------------- |
| Generate full tree | `folder-tree`                              | Full scan, default behavior   |
| Limited depth      | `folder-tree --depth 2`                    | Show only top 2 levels        |
| Exclude folders    | `folder-tree --hide public .next`          | Hide specific folders         |
| Collapse folders   | `folder-tree --collapse node_modules dist` | Summarize bulky folders       |
| Show folder counts | `folder-tree --show-counts`                | Display subfolder/file counts |
| Custom output file | `folder-tree --output structure.md`        | Save under custom name        |

```


Got it 👍 — here’s a **clean, minimal version** you can share directly in your README or with teammates.
It only includes **installation** and **usage** — no extra text, perfectly formatted for Markdown.

---

## Installation

### From PyPI

```bash
pip install folder-tree
```

### From GitHub (latest version)

```bash
pip install git+https://github.com/abhishekHegde2000/folder-tree-tool.git
```

---

## Usage

### Basic

```bash
folder-tree
```

### With options

```bash
folder-tree --show-counts --depth 2
folder-tree --collapse node_modules dist
folder-tree --hide public cypress
folder-tree --collapse node_modules --hide public --depth 3 --output project_structure.md
```

**Output example:**

```
project/ (4 folders, 3 files)
├── src/ (2 folders, 5 files)
│   ├── components/ (2 folders, 3 files)
│   └── utils/ (0 folders, 2 files)
├── node_modules/
│   (2450 files hidden)
└── README.md
```


Local Installation :

Here is the complete, unbroken, step-by-step guide from the moment you clone the repository all the way to running the tool globally.

---

### Step 1: Clone the Repository

Open your terminal (PowerShell or Command Prompt) and run the following commands to clone the code and move into the project directory:

```powershell
cd C:\code
git clone https://github.com/abhishekHegde2000/folder-tree-tool.git
cd folder-tree-tool

```

---

### Step 2: Install Locally in Editable Mode

While inside the `C:\code\folder-tree-tool` directory, run this command to install the package to your system:

```powershell
pip install -e .

```

*Note down the installation log. It will show a warning stating that `folder-tree.exe` is installed in a specific directory (like `C:\Users\abhih\AppData\Local\Python\pythoncore-3.14-64\Scripts`) which is not on your PATH.*

---

### Step 3: Copy your Scripts Path

Based on your Python version, copy the exact path where the executable was sent. For your system, it is:

```text
C:\Users\abhih\AppData\Local\Python\pythoncore-3.14-64\Scripts

```

---

### Step 4: Add the Path to Windows Environment Variables

1. Press the **Windows Key** on your keyboard, type **`env`**, and select **Edit the system environment variables**.
2. Click the **Environment Variables...** button at the bottom right of the window.
3. Look at the top section labeled **User variables for abhih** and click on the variable named **`Path`** to highlight it.
4. Click the **Edit...** button right below that section.
5. Click **New** on the right side of the popup window, and paste your path:
`C:\Users\abhih\AppData\Local\Python\pythoncore-3.14-64\Scripts`
6. Click **OK** on all three open windows to save your changes.

---

### Step 5: Restart the Terminal

1. **Close** your current PowerShell window completely.
2. Open a **brand new** PowerShell window (this forces Windows to load your updated PATH settings).

---

### Step 6: Verify and Run

Navigate to any folder on your computer that you want to visualize, and run the command:

```powershell
folder-tree

```

The tool will now execute properly and generate your Markdown directory tree structure!

The structure is printed in the terminal and saved as `structure.md` in the current directory.

---




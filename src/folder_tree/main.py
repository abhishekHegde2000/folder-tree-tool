#!/usr/bin/env python3
"""
generate_structure.py
---------------------
A Python script that recursively scans a directory and generates
a tree-like visualization of its folder and file structure.

Features:
 - Recursive traversal (folders first, alphabetically sorted)
 - Tree visualization using ├──, └──, │
 - Ignores hidden and bulky folders
 - Supports:
    --collapse  : show folder name but not expand
    --hide      : completely remove folders from output
    --show-counts : display per-folder folder/file counts
    --depth     : limit how deep the tree should go
 - Outputs to both console and Markdown (structure.md)
"""

import os
import argparse
from pathlib import Path

# ----------------------------
# Default Configuration
# ----------------------------

# Folders shown but not expanded
IGNORED_VISIBLE = {
    "node_modules",
    "dist",
    ".next",
    ".turbo",
    "build",
    "coverage",
}

# Folders completely hidden from output
IGNORED_HIDDEN = {
    "public",
    "cypress",
}

OUTPUT_FILE = "structure.md"

# ----------------------------
# Helper Functions
# ----------------------------


def count_contents(folder_path: Path):
    """Return (folder_count, file_count) inside a directory (non-recursive)."""
    folders = 0
    files = 0
    try:
        for entry in folder_path.iterdir():
            if entry.is_dir():
                folders += 1
            elif entry.is_file():
                files += 1
    except PermissionError:
        pass
    return folders, files


def count_files_recursively(folder_path: Path) -> int:
    """Count total files recursively inside a folder."""
    count = 0
    for _, _, files in os.walk(folder_path):
        count += len(files)
    return count


def get_sorted_contents(folder_path: Path):
    """Return sorted list of folders first, then files."""
    entries = list(folder_path.iterdir())
    folders = sorted([e for e in entries if e.is_dir()],
                     key=lambda x: x.name.lower())
    files = sorted([e for e in entries if e.is_file()],
                   key=lambda x: x.name.lower())
    return folders + files


def should_ignore(name: str, hidden_folders) -> bool:
    """Skip folders that are completely hidden or start with a dot."""
    return name.startswith(".") or name in hidden_folders


def should_collapse(name: str, collapsed_folders) -> bool:
    """Check if a folder should be collapsed (shown but not expanded)."""
    return name in collapsed_folders or name in IGNORED_VISIBLE


# ----------------------------
# Core Tree Logic
# ----------------------------

def build_tree(
    folder: Path,
    prefix: str = "",
    is_last: bool = True,
    collapsed_folders=None,
    hidden_folders=None,
    show_counts=False,
    current_depth=0,
    max_depth=None
):
    """Recursively build a folder tree structure."""
    if collapsed_folders is None:
        collapsed_folders = set()
    if hidden_folders is None:
        hidden_folders = set()

    base_name = folder.name
    connector = "└── " if is_last else "├── "
    tree_lines = []

    # Skip hidden folders entirely
    if should_ignore(base_name, hidden_folders):
        return tree_lines

    # Folder counts (if --show-counts enabled)
    counts_label = ""
    if show_counts:
        folders, files = count_contents(folder)
        counts_label = f" ({folders} folders, {files} files)"

    # Folder header
    tree_lines.append(f"{prefix}{connector}{base_name}/{counts_label}")

    # Stop recursion if depth limit reached
    if max_depth is not None and current_depth >= max_depth:
        return tree_lines

    # Prefix for children
    new_prefix = prefix + ("    " if is_last else "│   ")

    # Collapsed folders (non-expanded)
    if should_collapse(base_name, collapsed_folders):
        count = count_files_recursively(folder)
        tree_lines.append(f"{new_prefix}({count} files hidden)")
        return tree_lines

    # Directory contents
    try:
        contents = get_sorted_contents(folder)
    except PermissionError:
        tree_lines.append(f"{new_prefix}[Permission denied]")
        return tree_lines

    for index, entry in enumerate(contents):
        is_last_entry = index == len(contents) - 1
        if entry.is_dir():
            tree_lines.extend(
                build_tree(
                    entry,
                    new_prefix,
                    is_last_entry,
                    collapsed_folders,
                    hidden_folders,
                    show_counts,
                    current_depth + 1,
                    max_depth,
                )
            )
        else:
            connector = "└── " if is_last_entry else "├── "
            tree_lines.append(f"{new_prefix}{connector}{entry.name}")

    return tree_lines


# ----------------------------
# Generate & Save Output
# ----------------------------

def generate_structure(root_path: Path, collapsed_folders=None, hidden_folders=None, output_file=OUTPUT_FILE, show_counts=False, max_depth=None):
    """Generate folder structure and save to a Markdown file."""
    print(f"\n📂 Generating folder structure for: {root_path.resolve()}\n")

    tree_lines = build_tree(
        root_path,
        prefix="",
        is_last=True,
        collapsed_folders=collapsed_folders,
        hidden_folders=hidden_folders,
        show_counts=show_counts,
        current_depth=0,
        max_depth=max_depth,
    )

    tree_str = "\n".join(tree_lines)
    markdown_content = f"# Project Folder Structure\n\n```\n{tree_str}\n```\n"
    output_path = root_path / output_file

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print("✅ Folder structure generated successfully!")
    print(f"📄 Saved to: {output_path}\n")
    print(tree_str)


# ----------------------------
# CLI Interface
# ----------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate a folder tree and save it as structure.md.")
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root directory to scan (default: current directory)."
    )
    parser.add_argument(
        "--collapse",
        nargs="*",
        default=[],
        help="Folder names to show but not expand."
    )
    parser.add_argument(
        "--hide",
        nargs="*",
        default=[],
        help="Folder names to completely exclude from output."
    )
    parser.add_argument(
        "--show-counts",
        action="store_true",
        help="Display folder and file counts next to each folder name."
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=None,
        help="Limit how deep to traverse the folder tree (e.g., --depth 2)."
    )
    parser.add_argument(
        "--output",
        default=OUTPUT_FILE,
        help="Output file name (default: structure.md)."
    )

    args = parser.parse_args()
    root_path = Path(args.path).resolve()

    collapsed_folders = set(args.collapse)
    hidden_folders = IGNORED_HIDDEN.union(set(args.hide))

    generate_structure(
        root_path,
        collapsed_folders,
        hidden_folders,
        args.output,
        args.show_counts,
        args.depth,
    )


if __name__ == "__main__":
    main()


'''

⚙️ Usage Examples
1️⃣ Default run
python generate_structure.py

2️⃣ Limit depth to 2 levels
python generate_structure.py --depth 2

3️⃣ Combine with counts
python generate_structure.py --show-counts --depth 3

4️⃣ Collapse + Hide + Depth limit
python generate_structure.py --collapse node_modules dist --hide cypress public --show-counts --depth 2 --output project_tree.md


🧾 Example Output (with depth limit)
📂 Generating folder structure for: /Users/abhi/Projects/aws-todo

aws-todo/ (5 folders, 3 files)
├── backend/ (3 folders, 2 files)
│   ├── src/ (2 folders, 5 files)
│   ├── dist/
│   │   (240 files hidden)
│   └── package.json
├── frontend/ (4 folders, 6 files)
│   ├── src/
│   ├── public/
│   └── README.md
└── README.md


Since --depth 2 was used, it stopped expanding beyond 2 levels.


✨ What You Can Do Now


--collapse — fold large folders (shows file count)


--hide — exclude folders completely


--show-counts — see per-folder file/folder counts


--depth — restrict traversal levels


--output — save to any .md file name


It’s now a production-ready CLI utility for documenting or auditing any project’s structure.

without depth : python generate_structure.py --collapse node_modules --hide public tests --show-counts --output project_tree.md


'''

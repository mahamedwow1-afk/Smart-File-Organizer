from pathlib import Path
from core.scanner import scan_files
from core.organizer import build_organization_plan, execute_organization, undo_last

def main():
    print("--- Smart File Organizer ---")
    path_input = input("Enter folder path: ").strip()
    base_folder = Path(path_input)

    undo = input("Undo last operation? (y/n): ").lower()
    if undo == "y":
        undo_last(base_folder)
        print("Undo complete.")
        return

    files = scan_files(path_input)
    if not files:
        print("No files found.")
        return

    plan = build_organization_plan(files, path_input)
    print("\nPreview:")
    for folder, items in plan.items():
        print(f"Folder: {folder.name} ({len(items)} files)")

    confirm = input("\nExecute? (y/n): ").lower()
    if confirm == "y":
        execute_organization(plan, base_folder)
        print("Success!")

if __name__ == "__main__":
    main()
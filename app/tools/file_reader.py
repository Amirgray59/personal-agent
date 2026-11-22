from pathlib import Path
WORKSPACE_DIR = (
    Path(__file__).resolve().parents[2] / "workspace"
)

# Allowed file formats
ALLOWED_EXTENSIONS = {
    ".txt",
    ".md",
    ".csv",
    ".json",
    ".py"
}




# Maximum file size
MAX_FILE_BYTES = 50_000

# Maximum returned text
MAX_CONTENT_CHARS = 20_000


def read_file(path: str) -> dict:

    # 1. Validate input
    if not isinstance(path, str):
        raise ValueError("Path must be a string")

    path = path.strip()

    if not path:
        raise ValueError("Path cannot be empty")

    # 2. Prevent absolute paths and traversal
    relative_path = Path(path)

    if relative_path.is_absolute():
        raise ValueError("Absolute paths are not allowed")

    if ".." in relative_path.parts:
        raise ValueError("Path traversal is not allowed")

    try:

        workspace = WORKSPACE_DIR.resolve()

        target = (
            workspace / relative_path
        ).resolve(strict=True)

    except FileNotFoundError:
        raise ValueError("File not found")

    except OSError:
        raise ValueError("Unable to resolve file path")

    # 3. Verify that target stays inside workspace
    try:
        target.relative_to(workspace)

    except ValueError:
        raise ValueError("Access outside workspace is forbidden")

    # 4. Ensure target is a regular file
    if not target.is_file():
        raise ValueError("Target is not a regular file")

    # 5. Validate extension
    if target.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError("Unsupported file format")

    # 6. Read a limited amount of data
    with target.open("rb") as file:
        raw_content = file.read(MAX_FILE_BYTES + 1)

    size_truncated = len(raw_content) > MAX_FILE_BYTES

    if size_truncated:
        raw_content = raw_content[:MAX_FILE_BYTES]

    # 7. Decode UTF-8
    try:
        content = raw_content.decode("utf-8-sig")

    except UnicodeDecodeError:
        raise ValueError("File must use UTF-8 encoding")

    # 8. Limit returned characters
    content_truncated = (
        size_truncated
        or len(content) > MAX_CONTENT_CHARS
    )

    content = content[:MAX_CONTENT_CHARS]

    # 9. Return structured result
    return {
        "success": True,
        "file_name": target.name,
        "file_type": target.suffix.lower(),
        "size_bytes_read": len(raw_content),
        "content": content,
        "truncated": content_truncated
    }
import os
import re
import subprocess
import tempfile
from pathlib import Path


def format_markdown_files():
    md_files = list(Path("docs").glob("**/*.md"))

    excluded_path = Path("docs/models")
    md_files = [
        file for file in md_files if not str(file).startswith(str(excluded_path))
    ]

    additional_files = [Path("./README.md"), Path("./USAGE.md")]
    md_files.extend(additional_files)

    if not md_files:
        print("No .md files found in the current directory.")
        return

    python_codeblock_pattern = r"(```python\n)(.*?)(```)"

    def process_code_block(match):
        prefix = match.group(1)  # ```python\n
        code = match.group(2)  # code
        suffix = match.group(3)  # ```

        if "Optional" in code:
            code = re.sub(
                "import httpx",
                "from typing import Any, Optional, Union\n\nimport httpx",
                code,
            )
        code = re.sub(
            "from friendli_core",
            "\nfrom friendli",
            code,
        )

        code = re.sub(r",\s+(RetryConfig\(.*?\))", r", retries=\1", code)
        code = re.sub("fc_client", "friendli", code)

        if "await" in code:
            code = re.sub(
                "import FriendliCore",
                "import AsyncFriendli",
                code,
            )
            code = re.sub(r"with FriendliCore\(", "with AsyncFriendli(", code)
            code = re.sub(r"= FriendliCore\(", "= AsyncFriendli(", code)
        else:
            code = re.sub(
                "import FriendliCore",
                "import SyncFriendli",
                code,
            )
            code = re.sub(r"with FriendliCore\(", "with SyncFriendli(", code)
            code = re.sub(r"= FriendliCore\(", "= SyncFriendli(", code)

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False
        ) as temp_file:
            temp_file.write(code)
            temp_path = temp_file.name

        try:
            subprocess.run(
                ["ruff", "check", "--select", "I", "--fix", "-q", temp_path],
                check=True,
            )
            subprocess.run(["ruff", "format", "-q", temp_path], check=True)

            with open(temp_path, "r") as formatted_file:
                formatted_code = formatted_file.read()

            formatted_code = formatted_code.rstrip()

            if not formatted_code.endswith("\n"):
                formatted_code += "\n"

        except subprocess.CalledProcessError as e:
            print(f"Error formatting code block: {e}")
            formatted_code = code
        finally:
            os.unlink(temp_path)

        return prefix + formatted_code + suffix

    for md_file in md_files:
        try:
            with open(md_file, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Error: {md_file} not found.")
            continue
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue

        updated_content = re.sub(
            python_codeblock_pattern, process_code_block, content, flags=re.DOTALL
        )
        updated_content = re.sub(
            r"(?<=```python)\n(?=import httpx\n\nfrom friendli import AsyncFriendli\nfrom friendli\.httpclient import AsyncHttpClient)",
            r"\nfrom typing import Any, Optional, Union\n\n",
            updated_content,
        )
        updated_content = re.sub("_async", "", updated_content)
        updated_content = re.sub('"friendli_core"', '"friendli"', updated_content)
        updated_content = re.sub(r"git\+\<UNSET\>.git", "friendli", updated_content)
        updated_content = re.sub(
            "uvx --from friendli_core python",
            "uvx --from friendli python",
            updated_content,
        )

        if content != updated_content:
            try:
                with open(md_file, "w", encoding="utf-8") as file:
                    file.write(updated_content)
                print(f"Successfully processed Python code blocks in {md_file}")
            except Exception as e:
                print(f"Error writing to {md_file}: {e}")
        else:
            print(f"No changes were needed in {md_file}")


def replace_github_repository_name():
    target_files = [Path("./pyproject.toml"), Path("./.speakeasy/gen.lock")]

    for target_file in target_files:
        try:
            with open(target_file, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Error: {target_file} not found.")
            continue
        except Exception as e:
            print(f"Error reading {target_file}: {e}")
            continue

        updated_content = re.sub(
            r"friendli-python-internal", r"friendli-python", content
        )

        if content != updated_content:
            try:
                with open(target_file, "w", encoding="utf-8") as file:
                    file.write(updated_content)
                print(f"Successfully replaced GitHub repository name in {target_file}")
            except Exception as e:
                print(f"Error writing to {target_file}: {e}")
        else:
            print(f"No changes were needed in {target_file}")


if __name__ == "__main__":
    format_markdown_files()
    replace_github_repository_name()

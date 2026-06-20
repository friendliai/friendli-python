from __future__ import annotations

import os
import re
import subprocess
import tempfile
from pathlib import Path


def format_markdown_files():
    # Only the Speakeasy-generated SDK docs plus the top-level READMEs need the
    # public-API rewrite. `docs/models` (pure model reference) and any other docs
    # (e.g. design specs) are intentionally left untouched.
    md_files = list(Path("docs/sdks").glob("**/*.md"))
    md_files.extend([Path("./README.md"), Path("./USAGE.md")])

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
            # Import sorting is best-effort: a non-zero exit (e.g. unsortable
            # snippet) must not stop `ruff format`, which is what normalizes the
            # snippet (including stripping the blank line Speakeasy emits right
            # after `async def main():`).
            _ = subprocess.run(
                ["ruff", "check", "--select", "I", "--fix", "-q", temp_path],
                check=False,
            )
            _ = subprocess.run(["ruff", "format", "-q", temp_path], check=False)

            with open(temp_path, "r") as formatted_file:
                formatted_code = formatted_file.read()

            formatted_code = formatted_code.rstrip()

            if not formatted_code.endswith("\n"):
                formatted_code += "\n"

        except OSError as e:
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
        updated_content = re.sub("friendli_core", "friendli", updated_content)
        updated_content = re.sub("friendli-core", "friendli", updated_content)
        updated_content = re.sub(r"git\+\<UNSET\>.git", "friendli", updated_content)
        # Speakeasy emits a blank line right after `async def main():`, which
        # `ruff format` keeps. Drop it so the body starts under the signature.
        updated_content = re.sub(
            r"(async def main\(\):)\n\n", r"\1\n", updated_content
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


if __name__ == "__main__":
    format_markdown_files()

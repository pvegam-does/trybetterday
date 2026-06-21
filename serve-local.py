#!/usr/bin/env python3
"""Serve the static site locally with Vercel-style clean URLs."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
import os


class CleanUrlHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        parsed_path = urlsplit(path).path
        translated = super().translate_path(path)

        if Path(translated).exists() or Path(parsed_path).suffix:
            return translated

        clean_path = unquote(parsed_path).lstrip("/")
        html_path = Path(os.getcwd(), f"{clean_path}.html")

        if clean_path and html_path.is_file():
            return str(html_path)

        return translated


def main():
    parser = argparse.ArgumentParser(description="Serve public/ with clean URL support.")
    parser.add_argument("--port", type=int, default=4174)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--directory", default="public")
    args = parser.parse_args()

    os.chdir(args.directory)
    server = ThreadingHTTPServer((args.host, args.port), CleanUrlHandler)
    print(f"Serving {args.directory}/ at http://{args.host}:{args.port}/")
    server.serve_forever()


if __name__ == "__main__":
    main()

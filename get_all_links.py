import re
import json


def read_markdown_file(file_path):
    """
    マークダウンファイルを読み込みます。

    Parameters:
        file_path (str): ファイルのパス。

    Returns:
        str: 読み込まれたマークダウンテキスト。
    """
    with open(file_path, "r", encoding="utf-8") as f:
        markdown_text = f.read()
    return markdown_text


def extract_links_and_titles(markdown_text):
    """
    マークダウン形式のリンクテキストとURLを抽出し、タイトルとリンクの組み合わせを配列で返します。

    Parameters:
        markdown_text (str): 入力のマークダウンテキスト。

    Returns:
        list of dict: 各リンクを{'title': タイトル, 'url': リンク}の辞書形式で返すリスト。
    """
    # 正規表現パターン
    pattern = r"\[(.*?)\]\((https?://[^\)]+)\)"
    # タイトルとURLを抽出
    matches = re.findall(pattern, markdown_text)
    # 辞書形式でリストを作成
    result = [{"title": title, "url": url} for title, url in matches]
    return result


file_content = read_markdown_file("./original/text.md")
extracted_links_and_titles = extract_links_and_titles(file_content)

all_papers = []
for link in extracted_links_and_titles:
    url = link["url"]
    if "https://arxiv.org/abs/" in url:
        all_papers.append(link)


with open("all_links.json", "w", encoding="utf-8") as f:
    json.dump(all_papers, f, indent=4)

with open("all_links.json", "r", encoding="utf-8") as f:
    content = json.load(f)

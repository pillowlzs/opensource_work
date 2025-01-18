import re
import plotly.graph_objects as go
from datetime import datetime


def extract_fix_count(text):
    fix_pattern = re.compile(r"### Fixed(.*?)(?=(###|$))", re.DOTALL)
    fixes = fix_pattern.findall(text)
    fix_count = 0
    for fix_section in fixes:
        if isinstance(fix_section, tuple):
            fix_section = fix_section[0]  # 确保 fix_section 是字符串
        fix_count += len(re.findall(r"^-", fix_section, re.MULTILINE))
    return fix_count


def extract_date(text):
    date_pattern = re.compile(r"Published at: (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)")
    date_str = date_pattern.search(text).group(1)
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")


def main():
    # 读取文件内容
    with open('releases_info.txt', 'r') as file:
        content = file.read()
    # 按 'Release Name' 分割内容
    releases = content.split('Release Name:')
    dates = []
    fix_counts = []
    for release in releases[1:]:
        date = extract_date(release)
        fix_count = extract_fix_count(release)
        dates.append(date)
        fix_counts.append(fix_count)
    dates_str = [date.strftime("%Y-%m-%d") for date in dates]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates_str, y=fix_counts, mode='lines+markers', name='Fixes')),
    fig.update_layout(
        title="Number of Fixes over Time",
        xaxis_title="Date",
        yaxis_title="Number of Fixes",
    )
    fig.show()


if __name__ == "__main__":
    main()
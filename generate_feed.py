import datetime
import xml.etree.ElementTree as ET
from pathlib import Path

NEWS_FILE = Path("NEWS")
FEED_FILE = Path("feed.xml")

content = NEWS_FILE.read_text()
preview = content[:2000]

now = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

if FEED_FILE.exists():
    tree = ET.parse(FEED_FILE)
    root = tree.getroot()
    channel = root.find("channel")
else:
    root = ET.Element("rss", version="2.0")
    channel = ET.SubElement(root, "channel")

    ET.SubElement(channel, "title").text = "IANA tz NEWS Monitor"
    ET.SubElement(channel, "link").text = "https://ftp.iana.org/tz/code/NEWS"
    ET.SubElement(channel, "description").text = "Updates to the IANA tz NEWS file"

item = ET.SubElement(channel, "item")

ET.SubElement(item, "title").text = "NEWS updated"
ET.SubElement(item, "link").text = "https://ftp.iana.org/tz/code/NEWS"
ET.SubElement(item, "pubDate").text = now
ET.SubElement(item, "description").text = preview

tree = ET.ElementTree(root)
tree.write(FEED_FILE, encoding="utf-8", xml_declaration=True)

# import boilerpipe extractor
from boilerpipe.extract import Extractor

src_url = "https://www.anandabazar.com/sport/bwf-world-championships-final-pv-sindhu-vs-nozomi-okuhara-dgtl-1.1036258"
# src_url = "https://www.anandabazar.com/"

# initiate extractor
extractor = Extractor(extractor='ArticleExtractor', url=src_url)

# get the text/html using extractor
extracted_text = extractor.getText()
extracted_html = extractor.getHTML()

# print ourput
print(extracted_text);